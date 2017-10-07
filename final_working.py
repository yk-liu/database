from lxml import etree
import os
import pymongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from pymatgen import MPRester
from pymatgen.phasediagram.maker import PhaseDiagram
import pymatgen.phasediagram.analyzer as pda
import pprint
from pymatgen import Structure
import pymatgen.analysis.structure_matcher as sm
import pygal

class CEMD:
    def __init__(self, mongo_string='mongodb://localhost:27017/'):
        self.Mongo_connect(mongo_string)
        pass

    def Mongo_connect(self, mongo_string='mongodb://localhost:27017/'):
        self.client = pymongo.MongoClient(mongo_string)
        self.db = self.client.test_db
        self.collection = self.db.test_c
        self.posts = self.db.posts

    class BasicParseFunctions:
        @staticmethod
        def parse_i_tag_collection(itags_collection):
            d = {}
            for info in itags_collection.findall("i"):
                name = info.attrib.get("name")
                type = info.attrib.get("type")
                content = info.text
                d[name] = CEMD.BasicParseFunctions.assign_type(type, content)
            return d

        @staticmethod
        def parse_varray(varray):
            if varray.get("type") == 'int':
                m = [[int(number) for number in v.text.split()] for v in varray.findall("v")]
            else:
                m = [[float(number) for number in v.text.split()] for v in varray.findall("v")]
            return m

        @staticmethod
        def parse_array(array):
            array_dictionary = {}
            values = []
            dimension_list = {}
            field_list = []

            for dimension in array.findall("dimension"):
                dimension_list[dimension.attrib.get("dim")] = dimension.text

            for field in array.findall("field"):
                field_list.append(field.text)

            for r in array.iter("r"):
                values.append([float(number) for number in r.text.split()])

            array_dictionary["value"] = values
            array_dictionary['dimensions'] = dimension_list
            array_dictionary['fileds'] = field_list

            return array_dictionary

        @staticmethod
        def assign_type(type, content):
            if type == "logical":
                if type in ('T', 'True', 'true'):
                    return True
                elif type in ('F', 'False', 'false'):
                    return False
                else:
                    Warning("logical text " + content + " not T, True, true, F, False, false, set to False")
                return False
            elif type == "int":
                return int(content) if len(content.split()) == 1 else [int(number) for number in content.split()]
            elif type == "string":
                return content
            elif type == None:
                return float(content) if len(content.split()) == 1 else [float(number) for number in content.split()]
            else:
                Warning("New type: " + type + ", set to string")
            return content

    class AdvancedParseFunctions:
        @staticmethod
        def parse_finalpos(finalpos):
            d = {}
            for i in finalpos.iter("varray"):
                name = i.attrib.get("name")
                d[name] = CEMD.BasicParseFunctions.parse_varray(i)

            return d

        @staticmethod
        def parse_composition(atom_info):
            atom_names = {}
            for set in atom_info.findall("array"):

                if set.attrib.get("name") == "atoms":
                    for rc in set.iter("rc"):
                        atom_name = rc.find("c").text.replace(" ", '')
                        if atom_name in atom_names:
                            atom_names[atom_name] += 1
                        else:
                            atom_names[atom_name] = 1

                    break
            return atom_names

        @staticmethod
        def get_element(atom_names_dictionary):
            elements = []
            for atom_name in atom_names_dictionary:
                elements.append(atom_name.replace(" ", ""))
            return elements

        @staticmethod
        def get_formula(atom_names_dictionary):
            formula = ''
            for atom_name in atom_names_dictionary:
                formula += atom_name.replace(' ', '') + str(atom_names_dictionary[atom_name])
            return formula

        @staticmethod
        def parse_name_array(atominfo):
            atom_names = []
            for array in atominfo.findall("array"):
                if array.attrib["name"] == "atoms":
                    atom_names = [rc.find("c").text.strip()
                                  for rc in array.find("set")]

            if atom_names == []:
                ValueError("No atomname found in file")

            return atom_names

        @staticmethod
        def parse_eigenvalue(eigenvalue):
            eigenvalue = eigenvalue.find("array")
            eigenvalues = CEMD.BasicParseFunctions.parse_array(eigenvalue)
            return eigenvalues

        @staticmethod
        def parse_calculation(calculation):
            stress = []
            force = []
            efermi = 0.0
            eigenvalues = []
            energy = 0.0
            for i in calculation.iterchildren():
                if i.attrib.get("name") == "stress":
                    stress = CEMD.BasicParseFunctions.parse_varray(i)
                elif i.attrib.get("name") == "forces":
                    force = CEMD.BasicParseFunctions.parse_varray(i)
                elif i.tag == "dos":
                    for j in i.findall("i"):
                        if j.attrib.get("name") == "efermi":
                            efermi = float(j.text)
                            break
                elif i.tag == "eigenvalues":
                    eigenvalues = CEMD.AdvancedParseFunctions.parse_eigenvalue(i)
                elif i.tag == "energy":
                    for e in i.findall("i"):
                        if e.attrib.get("name") == "e_fr_energy":
                            energy = float(e.text)
                        else:
                            Warning("No e_fr_energy found in <calculation><energy> tag, energy set to 0.0")

            calculation = {}
            calculation["stress"] = stress
            calculation["efermi"] = efermi
            calculation["force"] = force
            calculation["eigenvalues"] = eigenvalues
            calculation["energy"] = energy
            return calculation

        @staticmethod
        def parse_kpoints(kpoints):
            for va in kpoints.findall("varray"):
                name = va.attrib["name"]
                if name == "kpointlist":
                    kpoints_matrix = CEMD.BasicParseFunctions.parse_varray(va)
            return kpoints_matrix

    @staticmethod
    def parse_single_file(xml_object):
        t = {}
        for child in xml_object.iterchildren():
            t.setdefault(child.tag, {})
            if child.tag == "incar":
                t[child.tag] = CEMD.BasicParseFunctions.parse_i_tag_collection(child)
            elif child.tag == "kpoints":
                t[child.tag] = CEMD.AdvancedParseFunctions.parse_kpoints(child)
            elif child.tag == "atominfo":
                t["name_array"] = CEMD.AdvancedParseFunctions.parse_name_array(child)
                t["composition"] = CEMD.AdvancedParseFunctions.parse_composition(child)
                t["elements"] = CEMD.AdvancedParseFunctions.get_element(t["composition"])
                t["formula"] = CEMD.AdvancedParseFunctions.get_formula(t["composition"])
            elif child.tag == "calculation":
                t["calculation"] = CEMD.AdvancedParseFunctions.parse_calculation(child)
            elif child.tag == "structure" and child.attrib.get("name") == "finalpos":
                t["finalpos"] = CEMD.AdvancedParseFunctions.parse_finalpos(child)
            elif child.tag not in ("i", "r", "v", "incar", "kpoints", "atominfo", "calculation"):
                t[child.tag] = CEMD.parse_single_file(child)
            else:
                return None

        # TODO: clean up all the NONE and {} keys in dictionary

        return t

    @staticmethod
    def costom_parse_single_file(xml_object):
        t = {}
        for child in xml_object.iterchildren():
            t.setdefault(child.tag, {})
            if child.tag == "incar":
                t[child.tag] = CEMD.BasicParseFunctions.parse_i_tag_collection(child)
            elif child.tag == "kpoints":
                t[child.tag] = CEMD.AdvancedParseFunctions.parse_kpoints(child)
            elif child.tag == "atominfo":
                t["name_array"] = CEMD.AdvancedParseFunctions.parse_name_array(child)
                t["composition"] = CEMD.AdvancedParseFunctions.parse_composition(child)
                t["elements"] = CEMD.AdvancedParseFunctions.get_element(t["composition"])
                t["formula"] = CEMD.AdvancedParseFunctions.get_formula(t["composition"])
            elif child.tag == "calculation":
                t["calculation"] = CEMD.AdvancedParseFunctions.parse_calculation(child)
            elif child.tag == "structure" and child.attrib.get("name") == "finalpos":
                t["finalpos"] = CEMD.AdvancedParseFunctions.parse_finalpos(child)
            elif child.tag not in ("i", "r", "v", "incar", "kpoints", "atominfo", "calculation"):
                t[child.tag] = CEMD.parse_single_file(child)
            else:
                return None

        # TODO: clean up all the NONE and {} keys in dictionary

        return t

    @staticmethod
    def parse_all(self, root="."):
        parsed = []
        visited_dir = []

        for dir_Name, subdir_List, _ in os.walk(root):
            if not subdir_List:
                if os.path.dirname(dir_Name) not in visited_dir:
                    print('\nProcessing directory: %s' % os.path.dirname(dir_Name))
                    success_count = 0
                    fail = []
                    visited_dir.append(os.path.dirname(dir_Name))
                    compond_elements = ''
                    # here we begin to draw convex hull
                    # we are now at the dir that contains all calculations for a system,
                    # for example, we are at dir [SrF] [SrF]/[Sr4F],[Sr3F],[Sr5F15]
                    # i = 0
                    for dirName, subdirList, fileList in os.walk(os.path.dirname(dir_Name)):
                        if not subdirList:
                            if "static-vasprun.xml" not in fileList:
                                print("failed to find vasprun file in ", dirName)
                                continue

                            file = dirName + '\\' + str(fileList[-1])
                            # looks like .\1-Sr1F2\static-vasprun.xml

                            try:
                                doc = etree.parse(file)
                                doc = doc.getroot()
                                dictionary = CEMD.parse_single_file(doc)

                                parsed.append(dictionary)
                                success_count += 1

                            except etree.XMLSyntaxError:
                                Warning('corrupted file found ' + file + "\n\n")
                                fail.append(file)

                    print(
                        "\nSuccessfully parsed " + str(success_count) + " structures in " + os.path.dirname(dir_Name))

                    if len(fail) != 0:
                        print("Failed : " + str(len(fail)) + " file(s) at " + ' '.join(fail))
                        print("Refused by lxml parse, might be corrupted")

        return parsed

    def parse_and_insert_all_files(self, root='.'):

        visited_dir = []
        for dir_Name, subdir_List, _ in os.walk(root):
            if not subdir_List:
                if os.path.dirname(dir_Name) not in visited_dir:
                    print('\nProcessing directory: %s' % os.path.dirname(dir_Name))
                    success_count = 0
                    fail = []
                    visited_dir.append(os.path.dirname(dir_Name))
                    compond_elements = ''
                    # here we begin to draw convex hull
                    # we are now at the dir that contains all calculations for a system,
                    # for example, we are at dir [SrF] [SrF]/[Sr4F],[Sr3F],[Sr5F15]
                    # i = 0
                    for dirName, subdirList, fileList in os.walk(os.path.dirname(dir_Name)):
                        if not subdirList:
                            if "static-vasprun.xml" not in fileList:
                                print("failed to find vasprun file in ", dirName)
                                continue

                            file = dirName + '\\' + str(fileList[-1])
                            # looks like .\1-Sr1F2\static-vasprun.xml

                            try:
                                doc = etree.parse(file)
                                doc = doc.getroot()
                                dictionary = CEMD.parse_single_file(doc)
                                # try:
                                # pprint.pprint(dictionary)
                                self.posts.insert_one(dictionary)
                                success_count += 1
                                # except:

                                    # exit("fail to insert to database")
                            except etree.XMLSyntaxError:
                                Warning('corrupted file found ' + file + "\n\n")
                                fail.append(file)

                    print(
                        "\nSuccessfully imported " + str(success_count) + " structures in " + os.path.dirname(dir_Name))

                    if len(fail) != 0:
                        print("Failed : " + str(len(fail)) + " file(s) at " + ' '.join(fail))
                        print("Refused by lxml parse, might be corrupted")

    def find(self, dictionary={'elements': ['Sr', 'N']}):
        result = []
        for post in self.posts.find(dictionary):
            result.append(post)
        return result

    @staticmethod
    def mpr_find_most_stable(elements, MPResterstring='ycLfD8pXz91gk6x3'):

        results = {}
        for xco, element in enumerate(elements):
            mpr = MPRester(MPResterstring)

            mp_entries = mpr.get_data(element)

            energy = min([i.get('energy_per_atom') for i in mp_entries])

            results[element] = energy

        return results

    @staticmethod
    def generate_structure_object(data):

        atomNames = data["name_array"]

        latt = data["finalpos"]["basis"]
        pos = data["finalpos"]["positions"]

        # print(type(data),type(latt),type(pos),type(atomNames))
        # print(latt,pos,atomNames)



        # try :

        # print("no problem!")
        # except TypeError:
        #     print("no!")

        return Structure(latt, atomNames, pos)

    @staticmethod
    def parse_and_update_one(xml_object):

        # costomize your own parse function
        t = CEMD.costom_parse_single_file(xml_object)

        # TODO: clean up all the NONE and {} keys in dictionary

        def is_duplicate(data_A, data_B):
            strucure_A = CEMD.generate_structure_object(data_A)
            strucure_B = CEMD.generate_structure_object(data_B)

            dist = sm.StructureMatcher().fit(strucure_A, strucure_B)
            if dist:
                return True
            else:
                return False

        result = self.find({"$and": [{"elements": t["elements"]}, {"composition": t["composition"]}]})

        for ref in result:
            if is_duplicate(struc, ref):
                try:
                    self.posts.find_and_update_one({"_id": struc["_id"]})
                    break
                except:
                    Warning("update operation failed!")
                    break

    # def parse_and_update_all(self, root='.'):
    #     visited_dir = []
    #     for dir_Name, subdir_List, _ in os.walk(root):
    #         if not subdir_List:
    #             if os.path.dirname(dir_Name) not in visited_dir:
    #                 print('\nProcessing directory: %s' % os.path.dirname(dir_Name))
    #                 success_count = 0
    #                 fail = []
    #                 visited_dir.append(os.path.dirname(dir_Name))
    #                 compond_elements = ''
    #                 # here we begin to draw convex hull
    #                 # we are now at the dir that contains all calculations for a system,
    #                 # for example, we are at dir [SrF] [SrF]/[Sr4F],[Sr3F],[Sr5F15]
    #                 # i = 0
    #                 for dirName, subdirList, fileList in os.walk(os.path.dirname(dir_Name)):
    #                     if not subdirList:
    #                         if "static-vasprun.xml" not in fileList:
    #                             print("failed to find vasprun file in ", dirName)
    #                             continue
    #
    #                         file = dirName + '\\' + str(fileList[-1])
    #                         # looks like .\1-Sr1F2\static-vasprun.xml
    #
    #                         try:
    #                             doc = etree.parse(file)
    #                             doc = doc.getroot()
    #                             dictionary = CEMD.costom_parse_single_file(doc)
    #                             try:
    #
    #                                 self.posts.insert_one(dictionary)
    #                                 success_count += 1
    #                             except Exception as e:
    #
    #                                 exit("fail to insert to database")
    #                         except etree.XMLSyntaxError:
    #                             Warning('corrupted file found ' + file + "\n\n")
    #                             fail.append(file)
    #
    #                 print(
    #                     "\nSuccessfully imported " + str(success_count) + " structures in " + os.path.dirname(dir_Name))
    #
    #                 if len(fail) != 0:
    #                     print("Failed : " + str(len(fail)) + " file(s) at " + ' '.join(fail))
    #                     print("Refused by lxml parse, might be corrupted")

    def range_cleanup_duplicate(self, search_dictionary={'elements': ['Sr', 'N']}):
        def is_duplicate(data_A, data_B):
            strucure_A = CEMD.generate_structure_object(data_A)
            strucure_B = CEMD.generate_structure_object(data_B)

            dist = sm.StructureMatcher().fit(strucure_A, strucure_B)
            if dist:
                return True
            else:
                return False

        result = self.find(search_dictionary)

        print("found result of"+str(len(result)))


        # for data in result:
        #     print(data["name_array"])

        cleaned = [result[0]]

        delete_count = 0
        for struc in result[1:]:
            duplicate_flag = False
            for ref in cleaned:
                if is_duplicate(struc, ref):
                    duplicate_flag = True
                    break
            if duplicate_flag:
                print("duplicate found!")
                # print(self.posts.find_one({"_id": struc["_id"]}))
                try:
                    self.posts.delete_one({"_id": struc["_id"]})
                    delete_count += 1
                except:
                    Warning("delete operation failed!")
            else:
                cleaned.append(struc)
                print("cleaned" + str(len(cleaned)))


        print("deleted" + str(delete_count) + "data, remaining :"+str(len(result)))


class CEMDP:
    def __init__(self, data_list):
        self.data_list = data_list
        self.elements = self._get_elements()

    def _get_elements(self, do_consistency_check=False):
        elements = self.data_list[0]["elements"]
        if do_consistency_check:
            for dictionary in self.data_list:
                if elements != dictionary["elements"]:
                    raise ValueError("inconsistency found in your data")

            print("No inconsistency found in your data")

        return elements

    def draw_convex(self, save_dir="."):

        def to_convex_point(dictionary=None):
            if dictionary is None:
                Warning("skiped drawing convext hull")
                pass

            energy = dictionary["calculation"]["energy"]

            name = ''
            atom_component = []

            total_atom = 0

            for atom_name in dictionary["composition"]:
                atom_count = dictionary["composition"][atom_name]
                name += str(atom_name.replace(" ", '')) + str(atom_count)
                total_atom += atom_count
                atom_component.append(dictionary["composition"][atom_name])

            point = [i / sum(atom_component) for i in atom_component[1:]]
            point.append(energy / total_atom)

            # print(name, energy, str(point))
            return name, point

        def level_convex(endpoints, points):
            left = [end for end in endpoints if end[0] == 0]
            right = [end for end in endpoints if end[0] == 1]

            left = left[left.index(min(left))]
            right = right[right.index(min(right))]
            # print(left,right)

            points.extend((left, right))
            # for point in points:
            #     print((point[0], point[-1]))

            for point in points:
                point[-1] = point[-1] - point[0] * right[-1] - (1 - point[0]) * left[-1]

            return points

        def to_endpoints(ends_dictionary):
            endpoints = []
            for i, end in enumerate(ends_dictionary):
                endpoints.append([i, ends_dictionary[end]])
            return endpoints

        ends = CEMD.mpr_find_most_stable(self.elements, MPResterstring='ycLfD8pXz91gk6x3')
        endpoints = to_endpoints(ends)

        convex_plot = []
        label = []
        name = ''.join(self.elements)

        for dictionary in self.data_list:
            convex_label, convex_point = to_convex_point(dictionary)
            convex_plot.append(convex_point)
            label.append(convex_label)

        label.extend(self.elements)

        convex_plot = level_convex(endpoints, convex_plot)

        points = np.array(convex_plot)

        hull = ConvexHull(points)
        fig, ax = plt.subplots()

        for i in range(len(points)):
            plt.plot(points[i, 0], points[i, 1], 'ko')
            ax.annotate(label[i], (points[i, 0], points[i, 1]))

        outer_x = []
        outer_y = []
        outer_points = []
        for vertex in hull.vertices:
            outer_points.append((points[vertex, 0], points[vertex, 1]))
        outer_points.sort(key=lambda p: p[0])
        for p in outer_points:
            outer_x.append(p[0])
            outer_y.append(p[1])

        print("convex plotted")

        plt.plot(outer_x, outer_y, "r*-")

        plt.savefig(save_dir + "/" + name + "_convexhull.png", dpi=300)
        plt.close()

    @staticmethod
    def show_radar(entry_label,data_label_list,data_list,title, save_dir='.', rect=None):
        radar_chart = pygal.Radar()
        radar_chart.x_labels = entry_label
        for data_label, data in zip(data_label_list, data_list):
            radar_chart.add(data_label,data)

        radar_chart.render_to_file(save_dir+"\\"+title+'radar12121_chart.svg')

    def show_radar_individual(self, data_list, save_dir='.', rect=None):
        if rect is None:
            rect = [0, 0, 1, 1]

        naxis = len(data_list[0])

        fig = pl.figure()

        angles = np.linspace(90., 90 + 360., naxis + 1)[0:-1]
        axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) for i in range(naxis)]
        ax = axes[0]
        ax.set_thetagrids(angles)

        for ax in axes:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)
            ax.yaxis.set_ticklabels([])  # hide the numbers of each radar line, took me so long

        for i, ax in enumerate(axes):
            ax.set_rgrids(range(1, len(self.gene_set[i])), angle=angles[i], labels=None)
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, len(self.gene_set[i]))
            # due to matplot lib, it requires lim to be positive.
            # for the sake of beauty, I here change it to 0-numberofsites, so the picture looks more 'full'

        for data in data_list:
            angle = np.deg2rad(np.r_[angles, angles[0]])
            data = np.r_[data, data[0]]
            ax.plot(angle, data, "-", lw=1, alpha=0.3)

        fig.savefig(save_dir + 'radar.png')
        pl.close(fig)


testdatabase = CEMD()
testdatabase.parse_and_insert_all_files()
testdatabase.parse_and_insert_all_files()
testdatabase.parse_and_insert_all_files()
#
print(len(testdatabase.find({'elements': ["Hf", "N"]})))
# tttt.draw_convex('.')
testdatabase.range_cleanup_duplicate({'elements': ["Hf", "N"]})

print(len(testdatabase.find({'elements': ["Hf", "N"]})))
