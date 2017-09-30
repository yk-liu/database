# Import the os module, for the os.walk function
from lxml import etree
import os
import pymongo
import pprint

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.test_db

cllection = db.test_c

posts = db.posts


def get_vasprunxml(set):
    def parse_i_tags(itags_collection):
        d = {}
        for info in itags_collection.findall("i"):
            name = info.attrib.get("name")
            type = info.attrib.get("type")
            content = info.text
            d[name] = assign_type(type, content)
        return d

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

    def parse_kpoints(elem):
        e = elem
        for va in elem.findall("varray"):
            name = va.attrib["name"]
            if name == "kpointlist":
                kpoints = parse_varray(va)
        return kpoints

    def parse_varray(elem):
        if elem.get("type") == 'int':
            m = [[int(number) for number in v.text.split()] for v in elem.findall("v")]
        else:
            m = [[float(number) for number in v.text.split()] for v in elem.findall("v")]
        return m

    def parse_eigenvalue(elem):
        elem = elem.find("array")
        eigenvalues = parse_array(elem)
        return eigenvalues

    def parse_calculation(calculation):
        stress = []
        force = []
        efermi = 0.0
        eigenvalues = []
        energy = 0.0
        for i in calculation.iterchildren():
            if i.attrib.get("name") == "stress":
                stress = parse_varray(i)
            elif i.attrib.get("name") == "forces":
                force = parse_varray(i)
            elif i.tag == "dos":
                for j in i.findall("i"):
                    if j.attrib.get("name") == "efermi":
                        efermi = float(j.text)
                        break
            elif i.tag == "eigenvalues":
                eigenvalues = parse_eigenvalue(i)
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

    def parse_composition(atom_info):
        atom_names = {}
        for set in atom_info.findall("array"):

            if set.attrib.get("name") == "atoms":
                for rc in set.iter("rc"):
                    atom_name = rc.find("c").text
                    if atom_name in atom_names:
                        atom_names[atom_name] += 1
                    else:
                        atom_names[atom_name] = 1

                break
        return atom_names

    def parse_finalpos(finalpos):
        d = {}
        for i in finalpos.iter("varray"):
            name = i.attrib.get("name")
            d[name] = parse_varray(i)

        return d

    t = {}
    for child in set.iterchildren():
        t.setdefault(child.tag, {})
        if child.tag == "incar":
            t[child.tag] = parse_i_tags(child)
        elif child.tag == "kpoints":
            t[child.tag] = parse_kpoints(child)
        elif child.tag == "atominfo":
            t["atominfo"] = None
            t["composition"] = parse_composition(child)
        elif child.tag == "calculation":
            t["calculation"] = parse_calculation(child)
        elif child.tag == "structure" and child.attrib.get("name") == "finalpos":
            t["finalpos"] = parse_finalpos(child)
        elif child.tag not in ("v", "i", "r", "incar", "kpoints", "atominfo", "calculation"):
            t[child.tag] = get_vasprunxml(child)
        else:
            return None

    return t


def to_convex_point(dictionary = None):
    if dictionary is None:
        Warning("skiped drawing convext hull")
        pass

    energy = dictionary["calculation"]["energy"]

    name = ''
    atom_component = []
    for atom_name in dictionary["composition"]:
        atom_count = dictionary["composition"][atom_name]
        name += str(atom_name.replace(" ",'')) + str(atom_count)

        atom_component.append(dictionary["composition"][atom_name])
    point = [i/sum(atom_component) for i in atom_component[:-1]]
    point.append(energy)
    print(name, energy, str(point))
    return name, point


def draw_convex(convex_plot,path,name):
    convex_plot = np.array(convex_plot)

    hull = ConvexHull(convex_plot)

    for i in range(len(convex_plot)):
        print(convex_plot[i, 0], convex_plot[i, 1], label[i])
        # plt.scatter(convex_plot[i,0], convex_plot[i,1], 'o',label=label[i])

    for simplex in hull.simplices:
        plt.plot(convex_plot[simplex, 0], convex_plot[simplex, 1], 'k-')

    # plt.plot(convex_plot[hull.vertices,0], convex_plot[hull.vertices,1], 'r--', lw=2)
    # plt.plot(convex_plot[hull.vertices[0],0], convex_plot[hull.vertices[0],1], 'r*')
    plt.show()
    plt.savefig(path+"/"+name+".pdf")
    plt.close()
    pass

# Set the directory you want to start from

visited_dir = []
# iterate to find the dir that has no sub dirs
for dir_Name, subdir_List, _ in os.walk("."):
    if not subdir_List:
        if os.path.dirname(dir_Name) not in visited_dir:
            success_count = 0
            fail = []
            convex_plot = []
            label = []
            visited_dir.append(os.path.dirname(dir_Name))
            # here we begin to draw convex hull
            # we are now at the dir that contains all calculations for a system,
            # for example, we are at dir [SrF] [SrF]/[Sr4F],[Sr3F],[Sr5F15]
            for dirName, subdirList, fileList in os.walk(os.path.dirname(dir_Name)):
                if not subdirList:
                    # print('Processing directory: %s' % dirName)
                    # if "static-vasprun.xml" in fileList:
                    #     print('found vasprun file, name = ', "static-vasprun.xml" if "static-vasprun.xml" in fileList else None)
                    # else:
                    #     print("failed to find vasprun file, ", fileList)

                    file = dirName + '\\' + str(fileList[-1])

                    # looks like .\1-Sr1F2\static-vasprun.xml

                    try:
                        doc = etree.parse(file)
                        doc = doc.getroot()
                        dictionary = get_vasprunxml(doc)
                        # print('parsing completed, now connecting database')

                        convex_label, convex_point =to_convex_point(dictionary)
                        convex_plot.append(convex_point)
                        label.append(convex_label)


                        try:
                            id = posts.insert_one(dictionary).inserted_id
                            # print("inserted data, id:", id)
                            # print("testing reading")
                            # pprint.pprint(posts.find_one({"_id": id}))
                            success_count += 1
                        except Exception as e:
                            exit("fail to load to database")
                    except etree.XMLSyntaxError:
                        Warning('corrupted file found ' + file + "\n\n")
                        fail.append(file)

            print(label)
            print(success_count)

            if len(fail) != 0:
                print("\nfailed : " + str(len(fail)) + " file(s) at " + ' '.join(fail))
                print("they are refused by lxml parse")
            else:
                print("\nsuccessfully imported data!")


