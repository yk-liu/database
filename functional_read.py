s = \
    """<modeling>
 <generator>
  <i name="program" type="string">vasp </i>
  <i name="version" type="string">5.4.1  </i>
  <i name="subversion" type="string">24Jun15 (build Jan 18 2016 15:29:17) complex                          parallel </i>
  <i name="platform" type="string">IFC91_ompi </i>
  <i name="date" type="string">2017 08 27 </i>
  <i name="time" type="string">04:44:09 </i>
 </generator>
 <incar>
  <i type="string" name="PREC">accurate</i>
  <i type="string" name="ALGO"> Normal</i>
  <i type="int" name="ISPIN">     1</i>
  <i type="int" name="ICHARG">     0</i>
  <i type="int" name="NELM">   100</i>
  <i type="int" name="IBRION">    -1</i>
  <i name="EDIFF">      0.00015000</i>
  <i type="int" name="NSW">     0</i>
  <i type="int" name="ISIF">     3</i>
  <i name="ENCUT">    520.00000000</i>
  <v name="MAGMOM">      0.60000000      0.60000000      0.60000000</v>
  <i type="string" name="LREAL"> Auto</i>
  <i type="int" name="ISMEAR">    -5</i>
  <i name="SIGMA">      0.05000000</i>
  <i type="logical" name="LWAVE"> T  </i>
  <i type="logical" name="LCHARG"> T  </i>
  <i type="logical" name="LVHAR"> F  </i>
  <i type="logical" name="LORBIT"> F  </i>
  <i type="logical" name="LELF"> T  </i>
  <i type="logical" name="LAECHG"> F  </i>
  <v type="int" name="KPOINT_BSE">    -1     0     0     0</v>
  <i type="int" name="NELM">   100</i>
 </incar>
 <kpoints>
  <generation param="Gamma">
   <v type="int" name="divisions">       7        7        7 </v>
   <v name="usershift">      0.00000000       0.00000000       0.00000000 </v>
   <v name="genvec1">      0.14285714       0.00000000       0.00000000 </v>
   <v name="genvec2">      0.00000000       0.14285714       0.00000000 </v>
   <v name="genvec3">      0.00000000       0.00000000       0.14285714 </v>
   <v name="shift">      0.00000000       0.00000000       0.00000000 </v>
  </generation>
  <varray name="kpointlist" >
   <v>       0.00000000       0.00000000       0.00000000 </v>
   <v>       0.14285714       0.00000000       0.00000000 </v>
   <v>       0.28571429       0.00000000       0.00000000 </v>
   <v>       0.42857143       0.00000000       0.00000000 </v>
   <v>       0.14285714       0.14285714       0.00000000 </v>
   <v>       0.28571429       0.14285714       0.00000000 </v>
   <v>       0.42857143       0.14285714       0.00000000 </v>
   <v>      -0.42857143       0.14285714       0.00000000 </v>
   <v>      -0.28571429       0.14285714       0.00000000 </v>
   <v>      -0.14285714       0.14285714       0.00000000 </v>
   <v>       0.28571429       0.28571429       0.00000000 </v>
   <v>       0.42857143       0.28571429       0.00000000 </v>
   <v>      -0.42857143       0.28571429       0.00000000 </v>
   <v>      -0.28571429       0.28571429       0.00000000 </v>
   <v>       0.42857143       0.42857143       0.00000000 </v>
   <v>      -0.42857143       0.42857143       0.00000000 </v>
   <v>       0.42857143       0.28571429       0.14285714 </v>
   <v>      -0.42857143       0.28571429       0.14285714 </v>
   <v>      -0.42857143       0.42857143       0.14285714 </v>
   <v>      -0.28571429       0.42857143       0.14285714 </v>
  </varray>
  <varray name="weights" >
   <v>       0.00291545 </v>
   <v>       0.02332362 </v>
   <v>       0.02332362 </v>
   <v>       0.02332362 </v>
   <v>       0.01749271 </v>
   <v>       0.06997085 </v>
   <v>       0.06997085 </v>
   <v>       0.06997085 </v>
   <v>       0.06997085 </v>
   <v>       0.03498542 </v>
   <v>       0.01749271 </v>
   <v>       0.06997085 </v>
   <v>       0.06997085 </v>
   <v>       0.03498542 </v>
   <v>       0.01749271 </v>
   <v>       0.03498542 </v>
   <v>       0.06997085 </v>
   <v>       0.13994169 </v>
   <v>       0.06997085 </v>
   <v>       0.06997085 </v>
  </varray>
  <varray name="tetrahedronlist"  type="int" >
   <v type="int" >       24        1        2        2        5 </v>
   <v type="int" >       48        2        5        6       10 </v>
   <v type="int" >       48        2        3        6       10 </v>
   <v type="int" >       24        2        2        5       10 </v>
   <v type="int" >       48        3        6        7        9 </v>
   <v type="int" >       48        3        4        7        9 </v>
   <v type="int" >       48        3        6        9       10 </v>
   <v type="int" >       48        4        7        8        8 </v>
   <v type="int" >       24        4        4        8        8 </v>
   <v type="int" >       48        4        7        8        9 </v>
   <v type="int" >       24        5        6        6       11 </v>
   <v type="int" >       24        5        6        6       10 </v>
   <v type="int" >       48        6       11       12       17 </v>
   <v type="int" >       48        6        7       12       17 </v>
   <v type="int" >       48        6        7        9       17 </v>
   <v type="int" >       24        6        6       11       17 </v>
   <v type="int" >       24        6        6       10       17 </v>
   <v type="int" >       48        6        9       10       17 </v>
   <v type="int" >       48        7       12       13       18 </v>
   <v type="int" >       48        7        8       13       18 </v>
   <v type="int" >       48        7        8        8       18 </v>
   <v type="int" >       48        7       12       17       18 </v>
   <v type="int" >       48        7        9       17       18 </v>
   <v type="int" >       48        7        8        9       18 </v>
   <v type="int" >       48        8       13       14       18 </v>
   <v type="int" >       48        8        9       14       18 </v>
   <v type="int" >       48        8       13       18       18 </v>
   <v type="int" >       24        8        8       18       18 </v>
   <v type="int" >       24        9        9       14       17 </v>
   <v type="int" >       24        9        9       10       17 </v>
   <v type="int" >       48        9       14       17       18 </v>
   <v type="int" >       24       11       12       12       15 </v>
   <v type="int" >       24       11       12       12       17 </v>
   <v type="int" >       48       12       15       16       19 </v>
   <v type="int" >       48       12       13       16       19 </v>
   <v type="int" >       48       12       13       18       19 </v>
   <v type="int" >       24       12       12       15       19 </v>
   <v type="int" >       24       12       12       17       19 </v>
   <v type="int" >       48       12       17       18       19 </v>
   <v type="int" >       24       13       13       16       20 </v>
   <v type="int" >       24       13       13       14       20 </v>
   <v type="int" >       48       13       14       18       20 </v>
   <v type="int" >       48       13       16       19       20 </v>
   <v type="int" >       48       13       18       19       20 </v>
   <v type="int" >       48       13       18       18       20 </v>
   <v type="int" >       24       14       18       18       20 </v>
   <v type="int" >       24       14       17       18       18 </v>
   <v type="int" >       12       15       15       16       16 </v>
   <v type="int" >       24       15       16       16       19 </v>
   <v type="int" >       12       16       16       19       19 </v>
   <v type="int" >       24       16       19       19       20 </v>
   <v type="int" >       24       17       18       18       19 </v>
   <v type="int" >       48       18       19       20       20 </v>
   <v type="int" >       24       18       18       20       20 </v>
   <v type="int" >       24       18       18       19       20 </v>
   <v type="int" >       12       19       19       20       20 </v>
   <v type="int" >       24       19       20       20       20 </v>
   <v type="int" >        6       20       20       20       20 </v>
  </varray>
  <i name="volumeweight">      0.00048591 </i>
 </kpoints>
 <parameters>
  <separator name="general" >
   <i type="string" name="SYSTEM">unknown system</i>
   <i type="logical" name="LCOMPAT"> F  </i>
  </separator>
  <separator name="electronic" >
   <i type="string" name="PREC">accura</i>
   <i name="ENMAX">    520.00000000</i>
   <i name="ENAUG">    613.61400000</i>
   <i name="EDIFF">      0.00015000</i>
   <i type="int" name="IALGO">    38</i>
   <i type="int" name="IWAVPR">    10</i>
   <i type="int" name="NBANDS">    16</i>
   <i name="NELECT">     24.00000000</i>
   <i type="int" name="TURBO">     0</i>
   <i type="int" name="IRESTART">     0</i>
   <i type="int" name="NREBOOT">     0</i>
   <i type="int" name="NMIN">     0</i>
   <i name="EREF">      0.00000000</i>
   <separator name="electronic smearing" >
    <i type="int" name="ISMEAR">    -5</i>
    <i name="SIGMA">      0.05000000</i>
    <i name="KSPACING">      0.50000000</i>
    <i type="logical" name="KGAMMA"> T  </i>
   </separator>
   <separator name="electronic projectors" >
    <i type="logical" name="LREAL"> T  </i>
    <v name="ROPT">     -0.00025000     -0.00025000</v>
    <i type="int" name="LMAXPAW">  -100</i>
    <i type="int" name="LMAXMIX">     2</i>
    <i type="logical" name="NLSPLINE"> F  </i>
   </separator>
   <separator name="electronic startup" >
    <i type="int" name="ISTART">     0</i>
    <i type="int" name="ICHARG">     0</i>
    <i type="int" name="INIWAV">     1</i>
   </separator>
   <separator name="electronic spin" >
    <i type="int" name="ISPIN">     1</i>
    <i type="logical" name="LNONCOLLINEAR"> F  </i>
    <v name="MAGMOM">      0.60000000      0.60000000      0.60000000</v>
    <i name="NUPDOWN">     -1.00000000</i>
    <i type="logical" name="LSORBIT"> F  </i>
    <v name="SAXIS">      0.00000000      0.00000000      1.00000000</v>
    <i type="logical" name="LSPIRAL"> F  </i>
    <v name="QSPIRAL">      0.00000000      0.00000000      0.00000000</v>
    <i type="logical" name="LZEROZ"> F  </i>
   </separator>
   <separator name="electronic exchange-correlation" >
    <i type="logical" name="LASPH"> F  </i>
    <i type="logical" name="LMETAGGA"> F  </i>
   </separator>
   <separator name="electronic convergence" >
    <i type="int" name="NELM">   100</i>
    <i type="int" name="NELMDL">    -5</i>
    <i type="int" name="NELMIN">     2</i>
    <i name="ENINI">    520.00000000</i>
    <separator name="electronic convergence detail" >
     <i type="logical" name="LDIAG"> T  </i>
     <i type="logical" name="LSUBROT"> F  </i>
     <i name="WEIMIN">      0.00000000</i>
     <i name="EBREAK">      0.00000234</i>
     <i name="DEPER">      0.30000000</i>
     <i type="int" name="NRMM">     4</i>
     <i name="TIME">      0.40000000</i>
    </separator>
   </separator>
   <separator name="electronic mixer" >
    <i name="AMIX">      0.40000000</i>
    <i name="BMIX">      1.00000000</i>
    <i name="AMIN">      0.10000000</i>
    <i name="AMIX_MAG">      1.60000000</i>
    <i name="BMIX_MAG">      1.00000000</i>
    <separator name="electronic mixer details" >
     <i type="int" name="IMIX">     4</i>
     <i type="logical" name="MIXFIRST"> F  </i>
     <i type="int" name="MAXMIX">   -45</i>
     <i name="WC">    100.00000000</i>
     <i type="int" name="INIMIX">     1</i>
     <i type="int" name="MIXPRE">     1</i>
     <i type="int" name="MREMOVE">     5</i>
    </separator>
   </separator>
   <separator name="electronic dipolcorrection" >
    <i type="logical" name="LDIPOL"> F  </i>
    <i type="logical" name="LMONO"> F  </i>
    <i type="int" name="IDIPOL">     0</i>
    <i name="EPSILON">      1.00000000</i>
    <v name="DIPOL">   -100.00000000   -100.00000000   -100.00000000</v>
    <i name="EFIELD">      0.00000000</i>
   </separator>
  </separator>
  <separator name="grids" >
   <i type="int" name="NGX">    32</i>
   <i type="int" name="NGY">    32</i>
   <i type="int" name="NGZ">    32</i>
   <i type="int" name="NGXF">    64</i>
   <i type="int" name="NGYF">    64</i>
   <i type="int" name="NGZF">    64</i>
   <i type="logical" name="ADDGRID"> F  </i>
  </separator>
  <separator name="ionic" >
   <i type="int" name="NSW">     0</i>
   <i type="int" name="IBRION">    -1</i>
   <i type="int" name="ISIF">     3</i>
   <i name="PSTRESS">      0.00000000</i>
   <i name="EDIFFG">      0.00150000</i>
   <i type="int" name="NFREE">     0</i>
   <i name="POTIM">      0.50000000</i>
   <i name="SMASS">     -3.00000000</i>
   <i name="SCALEE">      1.00000000</i>
  </separator>
  <separator name="ionic md" >
   <i name="TEBEG">      0.00010000</i>
   <i name="TEEND">      0.00010000</i>
   <i type="int" name="NBLOCK">     1</i>
   <i type="int" name="KBLOCK">     1</i>
   <i type="int" name="NPACO">   256</i>
   <i name="APACO">     16.00000000</i>
  </separator>
  <separator name="symmetry" >
   <i type="int" name="ISYM">     2</i>
   <i name="SYMPREC">      0.00001000</i>
  </separator>
  <separator name="dos" >
   <i type="logical" name="LORBIT"> F  </i>
   <v name="RWIGS">     -1.00000000     -1.00000000</v>
   <i type="int" name="NEDOS">   301</i>
   <i name="EMIN">     10.00000000</i>
   <i name="EMAX">    -10.00000000</i>
   <i name="EFERMI">      0.00000000</i>
  </separator>
  <separator name="writing" >
   <i type="int" name="NWRITE">     2</i>
   <i type="logical" name="LWAVE"> T  </i>
   <i type="logical" name="LCHARG"> T  </i>
   <i type="logical" name="LPARD"> F  </i>
   <i type="logical" name="LVTOT"> F  </i>
   <i type="logical" name="LVHAR"> F  </i>
   <i type="logical" name="LELF"> T  </i>
   <i type="logical" name="LOPTICS"> F  </i>
   <v name="STM">      0.00000000      0.00000000      0.00000000      0.00000000      0.00000000      0.00000000      0.00000000</v>
  </separator>
  <separator name="performance" >
   <i type="int" name="NPAR">     8</i>
   <i type="int" name="NSIM">     4</i>
   <i type="int" name="NBLK">    -1</i>
   <i type="logical" name="LPLANE"> T  </i>
   <i type="logical" name="LSCALAPACK"> T  </i>
   <i type="logical" name="LSCAAWARE"> F  </i>
   <i type="logical" name="LSCALU"> F  </i>
   <i type="logical" name="LASYNC"> F  </i>
   <i type="logical" name="LORBITALREAL"> F  </i>
  </separator>
  <separator name="miscellaneous" >
   <i type="int" name="IDIOT">     3</i>
   <i type="logical" name="LMUSIC"> F  </i>
   <v name="POMASS">     87.62000000     18.99800000</v>
   <v name="DARWINR">      0.00000000      0.00000000</v>
   <v name="DARWINV">      1.00000000      1.00000000</v>
   <i type="logical" name="LCORR"> T  </i>
  </separator>
  <i type="logical" name="GGA_COMPAT"> T  </i>
  <i type="logical" name="LBERRY"> F  </i>
  <i type="int" name="ICORELEVEL">     0</i>
  <i type="logical" name="LDAU"> F  </i>
  <i type="int" name="I_CONSTRAINED_M">     0</i>
  <separator name="electronic exchange-correlation" >
   <i type="string" name="GGA">--</i>
   <i type="int" name="VOSKOWN">     0</i>
   <i type="logical" name="LHFCALC"> F  </i>
   <i type="string" name="PRECFOCK"></i>
   <i type="logical" name="LSYMGRAD"> F  </i>
   <i type="logical" name="LHFONE"> F  </i>
   <i type="logical" name="LRHFCALC"> F  </i>
   <i type="logical" name="LTHOMAS"> F  </i>
   <i type="logical" name="LMODELHF"> F  </i>
   <i name="ENCUT4O">     -1.00000000</i>
   <i type="int" name="EXXOEP">     0</i>
   <i type="int" name="FOURORBIT">     0</i>
   <i name="AEXX">      0.00000000</i>
   <i name="HFALPHA">      0.00000000</i>
   <i name="MCALPHA">      0.00000000</i>
   <i name="ALDAX">      1.00000000</i>
   <i name="AGGAX">      1.00000000</i>
   <i name="ALDAC">      1.00000000</i>
   <i name="AGGAC">      1.00000000</i>
   <i type="int" name="NKREDX">     1</i>
   <i type="int" name="NKREDY">     1</i>
   <i type="int" name="NKREDZ">     1</i>
   <i type="logical" name="SHIFTRED"> F  </i>
   <i type="logical" name="ODDONLY"> F  </i>
   <i type="logical" name="EVENONLY"> F  </i>
   <i type="int" name="LMAXFOCK">     0</i>
   <i type="int" name="NMAXFOCKAE">     0</i>
   <i type="logical" name="LFOCKAEDFT"> F  </i>
   <i name="HFSCREEN">      0.00000000</i>
   <i name="HFSCREENC">      0.00000000</i>
   <i type="int" name="NBANDSGWLOW">     0</i>
  </separator>
  <separator name="vdW DFT" >
   <i type="logical" name="LUSE_VDW"> F  </i>
   <i name="Zab_VDW">     -0.84910000</i>
   <i name="PARAM1">      0.12340000</i>
   <i name="PARAM2">      1.00000000</i>
   <i name="PARAM3">      0.00000000</i>
  </separator>
  <separator name="model GW" >
   <i type="int" name="MODEL_GW">     0</i>
   <i name="MODEL_EPS0">     10.09958529</i>
   <i name="MODEL_ALPHA">      1.00000000</i>
  </separator>
  <separator name="linear response parameters" >
   <i type="logical" name="LEPSILON"> F  </i>
   <i type="logical" name="LRPA"> F  </i>
   <i type="logical" name="LNABLA"> F  </i>
   <i type="logical" name="LVEL"> F  </i>
   <i type="int" name="KINTER">     0</i>
   <i name="CSHIFT">      0.10000000</i>
   <i name="OMEGAMAX">     -1.00000000</i>
   <i name="DEG_THRESHOLD">      0.00200000</i>
  </separator>
  <separator name="orbital magnetization" >
   <i type="logical" name="NUCIND"> F  </i>
   <v name="MAGPOS">      0.00000000      0.00000000      0.00000000</v>
   <i type="logical" name="LNICSALL"> T  </i>
   <i type="logical" name="ORBITALMAG"> F  </i>
   <i type="logical" name="LMAGBLOCH"> F  </i>
   <i type="logical" name="LCHIMAG"> F  </i>
   <i type="logical" name="LGAUGE"> T  </i>
   <i type="int" name="MAGATOM">     0</i>
   <v name="MAGDIPOL">      0.00000000      0.00000000      0.00000000</v>
   <v name="AVECCONST">      0.00000000      0.00000000      0.00000000</v>
  </separator>
  <separator name="response functions" >
   <i type="logical" name="LADDER"> F  </i>
   <i type="logical" name="LFXC"> F  </i>
   <i type="logical" name="LHARTREE"> T  </i>
   <i type="int" name="IBSE">     0</i>
   <v type="int" name="KPOINT">    -1     0     0     0</v>
   <i type="logical" name="LTCTE"> F  </i>
   <i type="logical" name="LTETE"> F  </i>
   <i type="logical" name="LTRIPLET"> F  </i>
   <i type="logical" name="LFXCEPS"> F  </i>
   <i type="logical" name="LFXHEG"> F  </i>
   <i type="int" name="NATURALO">     0</i>
   <i type="logical" name="L2ORDER"> F  </i>
   <i type="logical" name="LUSEW"> F  </i>
   <i name="ENCUTGW">     -2.00000000</i>
   <i name="ENCUTGWSOFT">     -2.00000000</i>
   <i name="ENCUTLF">     -1.00000000</i>
   <i type="int" name="LMAXMP2">    -1</i>
   <i name="SCISSOR">      0.00000000</i>
   <i type="int" name="NOMEGA">     0</i>
   <i type="int" name="NOMEGAR">     0</i>
   <i type="int" name="NBANDSGW">    -1</i>
   <i type="int" name="NBANDSO">    -1</i>
   <i type="int" name="NBANDSV">    -1</i>
   <i type="int" name="NELM">   100</i>
   <i type="int" name="NELMHF">     1</i>
   <i type="int" name="DIM">     3</i>
   <i type="int" name="ANTIRES">     0</i>
   <i name="OMEGAMAX">    -30.00000000</i>
   <i name="OMEGAMIN">    -30.00000000</i>
   <i name="OMEGATL">   -200.00000000</i>
   <i type="int" name="OMEGAGRID">     0</i>
   <i name="CSHIFT">     -0.10000000</i>
   <i type="logical" name="SELFENERGY"> F  </i>
   <i type="logical" name="LSPECTRAL"> F  </i>
   <i type="logical" name="LSPECTRALGW"> F  </i>
   <i type="logical" name="LSINGLES"> F  </i>
   <i type="logical" name="LFERMIGW"> F  </i>
   <i type="logical" name="ODDONLYGW"> F  </i>
   <i type="logical" name="EVENONLYGW"> F  </i>
   <i type="int" name="NKREDLFX">     1</i>
   <i type="int" name="NKREDLFY">     1</i>
   <i type="int" name="NKREDLFZ">     1</i>
   <i type="int" name="MAXMEM">  1800</i>
   <i type="int" name="TELESCOPE">     0</i>
   <i type="int" name="TAUPAR">     1</i>
   <i type="int" name="OMEGAPAR">    -1</i>
   <i name="LAMBDA">      1.00000000</i>
  </separator>
  <separator name="External order field" >
   <i name="OFIELD_KAPPA">      0.00000000</i>
   <v name="OFIELD_K">      0.00000000      0.00000000      0.00000000</v>
   <i name="OFIELD_Q6_NEAR">      0.00000000</i>
   <i name="OFIELD_Q6_FAR">      0.00000000</i>
   <i name="OFIELD_A">      0.00000000</i>
  </separator>
 </parameters>
 <atominfo>
  <atoms>       3 </atoms>
  <types>       2 </types>
  <array name="atoms" >
   <dimension dim="1">ion</dimension>
   <field type="string">element</field>
   <field type="int">atomtype</field>
   <set>
    <rc><c>Sr</c><c>   1</c></rc>
    <rc><c>F </c><c>   2</c></rc>
    <rc><c>F </c><c>   2</c></rc>
   </set>
  </array>
  <array name="atomtypes" >
   <dimension dim="1">type</dimension>
   <field type="int">atomspertype</field>
   <field type="string">element</field>
   <field>mass</field>
   <field>valence</field>
   <field type="string">pseudopotential</field>
   <set>
    <rc><c>   1</c><c>Sr</c><c>     87.62000000</c><c>     10.00000000</c><c> PAW_PBE Sr_sv 07Sep2000                </c></rc>
    <rc><c>   2</c><c>F </c><c>     18.99800000</c><c>      7.00000000</c><c> PAW_PBE F 08Apr2002                    </c></rc>
   </set>
  </array>
 </atominfo>
 <structure name="initialpos" >
  <crystal>
   <varray name="basis" >
    <v>       0.00000000       2.93369200       2.93369200 </v>
    <v>       2.93369200       0.00000000       2.93369200 </v>
    <v>       2.93369200       2.93369200       0.00000000 </v>
   </varray>
   <i name="volume">     50.49792644 </i>
   <varray name="rec_basis" >
    <v>      -0.17043371       0.17043371       0.17043371 </v>
    <v>       0.17043371      -0.17043371       0.17043371 </v>
    <v>       0.17043371       0.17043371      -0.17043371 </v>
   </varray>
  </crystal>
  <varray name="positions" >
   <v>       0.00000000       0.00000000       0.00000000 </v>
   <v>       0.75000000       0.75000000       0.75000000 </v>
   <v>       0.25000000       0.25000000       0.25000000 </v>
  </varray>
 </structure>
 <calculation>
  <scstep>
   <time name="dav">    0.30    0.30</time>
   <time name="total">    0.32    0.32</time>
   <energy>
    <i name="alphaZ">    112.94592587 </i>
    <i name="ewald">  -1520.55261951 </i>
    <i name="hartreedc">    -66.06424216 </i>
    <i name="XCdc">     78.96546425 </i>
    <i name="pawpsdc">    251.82784968 </i>
    <i name="pawaedc">   -241.99717097 </i>
    <i name="eentropy">      0.00000000 </i>
    <i name="bandstr">  -1388.16635648 </i>
    <i name="atom">   2161.37896191 </i>
    <i name="e_fr_energy">   -611.66218740 </i>
    <i name="e_wo_entrp">   -611.66218740 </i>
    <i name="e_0_energy">   -611.66218740 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.24    0.24</time>
   <time name="total">    0.24    0.24</time>
   <energy>
    <i name="e_fr_energy">   -773.01797427 </i>
    <i name="e_wo_entrp">   -773.01797427 </i>
    <i name="e_0_energy">   -773.01797427 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.29    0.29</time>
   <time name="total">    0.29    0.29</time>
   <energy>
    <i name="e_fr_energy">   -778.50814968 </i>
    <i name="e_wo_entrp">   -778.50814968 </i>
    <i name="e_0_energy">   -778.50814968 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.29    0.29</time>
   <time name="total">    0.29    0.29</time>
   <energy>
    <i name="e_fr_energy">   -778.65831805 </i>
    <i name="e_wo_entrp">   -778.65831805 </i>
    <i name="e_0_energy">   -778.65831805 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.29    0.29</time>
   <time name="total">    0.32    0.32</time>
   <energy>
    <i name="e_fr_energy">   -778.66301156 </i>
    <i name="e_wo_entrp">   -778.66301156 </i>
    <i name="e_0_energy">   -778.66301156 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.22    0.22</time>
   <time name="total">    0.26    0.26</time>
   <energy>
    <i name="e_fr_energy">   -203.94924452 </i>
    <i name="e_wo_entrp">   -203.94924452 </i>
    <i name="e_0_energy">   -203.94924452 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.23    0.23</time>
   <time name="total">    0.28    0.28</time>
   <energy>
    <i name="e_fr_energy">    -67.36139137 </i>
    <i name="e_wo_entrp">    -67.36139137 </i>
    <i name="e_0_energy">    -67.36139137 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.22    0.22</time>
   <time name="total">    0.26    0.26</time>
   <energy>
    <i name="e_fr_energy">    -27.63102858 </i>
    <i name="e_wo_entrp">    -27.63102858 </i>
    <i name="e_0_energy">    -27.63102858 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.27    0.27</time>
   <time name="total">    0.31    0.31</time>
   <energy>
    <i name="e_fr_energy">    -39.26959956 </i>
    <i name="e_wo_entrp">    -39.26959956 </i>
    <i name="e_0_energy">    -39.26959956 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.25    0.25</time>
   <time name="total">    0.29    0.29</time>
   <energy>
    <i name="e_fr_energy">    -16.95747446 </i>
    <i name="e_wo_entrp">    -16.95747446 </i>
    <i name="e_0_energy">    -16.95747446 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.26    0.26</time>
   <time name="total">    0.30    0.30</time>
   <energy>
    <i name="e_fr_energy">    -17.47925038 </i>
    <i name="e_wo_entrp">    -17.47925038 </i>
    <i name="e_0_energy">    -17.47925038 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.23    0.23</time>
   <time name="total">    0.27    0.27</time>
   <energy>
    <i name="e_fr_energy">    -17.32712459 </i>
    <i name="e_wo_entrp">    -17.32712459 </i>
    <i name="e_0_energy">    -17.32712459 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.28    0.28</time>
   <time name="total">    0.32    0.32</time>
   <energy>
    <i name="e_fr_energy">    -17.30262078 </i>
    <i name="e_wo_entrp">    -17.30262078 </i>
    <i name="e_0_energy">    -17.30262078 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.23    0.23</time>
   <time name="total">    0.27    0.27</time>
   <energy>
    <i name="e_fr_energy">    -17.29157132 </i>
    <i name="e_wo_entrp">    -17.29157132 </i>
    <i name="e_0_energy">    -17.29157132 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.28    0.28</time>
   <time name="total">    0.33    0.33</time>
   <energy>
    <i name="e_fr_energy">    -17.28722793 </i>
    <i name="e_wo_entrp">    -17.28722793 </i>
    <i name="e_0_energy">    -17.28722793 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.27    0.27</time>
   <time name="total">    0.31    0.31</time>
   <energy>
    <i name="e_fr_energy">    -17.28601241 </i>
    <i name="e_wo_entrp">    -17.28601241 </i>
    <i name="e_0_energy">    -17.28601241 </i>
   </energy>
  </scstep>
  <scstep>
   <time name="dav">    0.22    0.22</time>
   <time name="total">    0.24    0.24</time>
   <energy>
    <i name="alphaZ">    112.94592587 </i>
    <i name="ewald">  -1520.55261951 </i>
    <i name="hartreedc">   -613.27649286 </i>
    <i name="XCdc">    111.47194100 </i>
    <i name="pawpsdc">   1467.92743491 </i>
    <i name="pawaedc">  -1470.28250813 </i>
    <i name="eentropy">      0.00000000 </i>
    <i name="bandstr">   -266.89863088 </i>
    <i name="atom">   2161.37896191 </i>
    <i name="e_fr_energy">    -17.28598769 </i>
    <i name="e_wo_entrp">    -17.28598769 </i>
    <i name="e_0_energy">    -17.28598769 </i>
   </energy>
  </scstep>
  <structure>
   <crystal>
    <varray name="basis" >
     <v>       0.00000000       2.93369200       2.93369200 </v>
     <v>       2.93369200       0.00000000       2.93369200 </v>
     <v>       2.93369200       2.93369200       0.00000000 </v>
    </varray>
    <i name="volume">     50.49792644 </i>
    <varray name="rec_basis" >
     <v>      -0.17043371       0.17043371       0.17043371 </v>
     <v>       0.17043371      -0.17043371       0.17043371 </v>
     <v>       0.17043371       0.17043371      -0.17043371 </v>
    </varray>
   </crystal>
   <varray name="positions" >
    <v>       0.00000000       0.00000000       0.00000000 </v>
    <v>       0.75000000       0.75000000       0.75000000 </v>
    <v>       0.25000000       0.25000000       0.25000000 </v>
   </varray>
  </structure>
  <varray name="forces" >
   <v>       0.00000000      -0.00000000       0.00000000 </v>
   <v>       0.00000000       0.00000000      -0.00000000 </v>
   <v>      -0.00000000      -0.00000000       0.00000000 </v>
  </varray>
  <varray name="stress" >
   <v>       4.68456642       0.00000000      -0.00000000 </v>
   <v>      -0.00000000       4.68456642      -0.00000000 </v>
   <v>      -0.00000000       0.00000000       4.68456642 </v>
  </varray>
  <energy>
   <i name="e_fr_energy">    -17.28598769 </i>
   <i name="e_wo_entrp">    -17.28598769 </i>
   <i name="e_0_energy">      0.00000000 </i>
  </energy>
  <time name="totalsc">    5.68    5.71</time>
  <eigenvalues>
   <array>
    <dimension dim="1">band</dimension>
    <dimension dim="2">kpoint</dimension>
    <dimension dim="3">spin</dimension>
    <field>eigene</field>
    <field>occ</field>
    <set>
     <set comment="spin 1">
      <set comment="kpoint 1">
       <r>  -32.1868    1.0000 </r>
       <r>  -21.2679    1.0000 </r>
       <r>  -20.8827    1.0000 </r>
       <r>  -14.1647    1.0000 </r>
       <r>  -14.1647    1.0000 </r>
       <r>  -14.1647    1.0000 </r>
       <r>   -3.5680    1.0000 </r>
       <r>   -3.5680    1.0000 </r>
       <r>   -3.5680    1.0000 </r>
       <r>   -2.0575    1.0000 </r>
       <r>   -2.0575    1.0000 </r>
       <r>   -2.0575    1.0000 </r>
       <r>    4.8047    0.0000 </r>
       <r>    7.9756    0.0000 </r>
       <r>    7.9756    0.0000 </r>
       <r>   10.2700    0.0000 </r>
      </set>
      <set comment="kpoint 2">
       <r>  -32.1777    1.0000 </r>
       <r>  -21.2851    1.0000 </r>
       <r>  -20.9117    1.0000 </r>
       <r>  -14.1781    1.0000 </r>
       <r>  -14.1781    1.0000 </r>
       <r>  -14.1489    1.0000 </r>
       <r>   -3.4863    1.0000 </r>
       <r>   -3.4863    1.0000 </r>
       <r>   -3.3995    1.0000 </r>
       <r>   -2.2376    1.0000 </r>
       <r>   -2.1158    1.0000 </r>
       <r>   -2.1158    1.0000 </r>
       <r>    5.2843    0.0000 </r>
       <r>    7.9822    0.0000 </r>
       <r>    7.9822    0.0000 </r>
       <r>   10.0479    0.0000 </r>
      </set>
      <set comment="kpoint 3">
       <r>  -32.1572    1.0000 </r>
       <r>  -21.3043    1.0000 </r>
       <r>  -20.9970    1.0000 </r>
       <r>  -14.2078    1.0000 </r>
       <r>  -14.2078    1.0000 </r>
       <r>  -14.1075    1.0000 </r>
       <r>   -3.2930    1.0000 </r>
       <r>   -3.2930    1.0000 </r>
       <r>   -3.0220    1.0000 </r>
       <r>   -2.5753    1.0000 </r>
       <r>   -2.2511    1.0000 </r>
       <r>   -2.2511    1.0000 </r>
       <r>    6.3644    0.0000 </r>
       <r>    8.0146    0.0000 </r>
       <r>    8.0146    0.0000 </r>
       <r>    9.5517    0.0000 </r>
      </set>
      <set comment="kpoint 4">
       <r>  -32.1407    1.0000 </r>
       <r>  -21.2895    1.0000 </r>
       <r>  -21.0980    1.0000 </r>
       <r>  -14.2313    1.0000 </r>
       <r>  -14.2313    1.0000 </r>
       <r>  -14.0688    1.0000 </r>
       <r>   -3.1213    1.0000 </r>
       <r>   -3.1213    1.0000 </r>
       <r>   -2.8111    1.0000 </r>
       <r>   -2.7072    1.0000 </r>
       <r>   -2.3709    1.0000 </r>
       <r>   -2.3709    1.0000 </r>
       <r>    7.4953    0.0000 </r>
       <r>    8.0564    0.0000 </r>
       <r>    8.0564    0.0000 </r>
       <r>    8.6482    0.0000 </r>
      </set>
      <set comment="kpoint 5">
       <r>  -32.1747    1.0000 </r>
       <r>  -21.2932    1.0000 </r>
       <r>  -20.9179    1.0000 </r>
       <r>  -14.1982    1.0000 </r>
       <r>  -14.1982    1.0000 </r>
       <r>  -14.1129    1.0000 </r>
       <r>   -3.4748    1.0000 </r>
       <r>   -3.4748    1.0000 </r>
       <r>   -3.2995    1.0000 </r>
       <r>   -2.4727    1.0000 </r>
       <r>   -2.0472    1.0000 </r>
       <r>   -2.0472    1.0000 </r>
       <r>    5.4424    0.0000 </r>
       <r>    7.7724    0.0000 </r>
       <r>    8.1854    0.0000 </r>
       <r>    9.8833    0.0000 </r>
      </set>
      <set comment="kpoint 6">
       <r>  -32.1580    1.0000 </r>
       <r>  -21.3155    1.0000 </r>
       <r>  -20.9797    1.0000 </r>
       <r>  -14.2321    1.0000 </r>
       <r>  -14.2178    1.0000 </r>
       <r>  -14.0757    1.0000 </r>
       <r>   -3.3282    1.0000 </r>
       <r>   -3.3180    1.0000 </r>
       <r>   -2.9515    1.0000 </r>
       <r>   -2.8343    1.0000 </r>
       <r>   -2.1310    1.0000 </r>
       <r>   -2.1049    1.0000 </r>
       <r>    6.2593    0.0000 </r>
       <r>    7.7099    0.0000 </r>
       <r>    8.3333    0.0000 </r>
       <r>    9.4387    0.0000 </r>
      </set>
      <set comment="kpoint 7">
       <r>  -32.1401    1.0000 </r>
       <r>  -21.3032    1.0000 </r>
       <r>  -21.0849    1.0000 </r>
       <r>  -14.2541    1.0000 </r>
       <r>  -14.2137    1.0000 </r>
       <r>  -14.0676    1.0000 </r>
       <r>   -3.1795    1.0000 </r>
       <r>   -3.1351    1.0000 </r>
       <r>   -3.0386    1.0000 </r>
       <r>   -2.5856    1.0000 </r>
       <r>   -2.2620    1.0000 </r>
       <r>   -2.2560    1.0000 </r>
       <r>    6.9333    0.0000 </r>
       <r>    8.0192    0.0000 </r>
       <r>    8.3193    0.0000 </r>
       <r>    9.0227    0.0000 </r>
      </set>
      <set comment="kpoint 8">
       <r>  -32.1346    1.0000 </r>
       <r>  -21.2710    1.0000 </r>
       <r>  -21.1468    1.0000 </r>
       <r>  -14.2481    1.0000 </r>
       <r>  -14.2059    1.0000 </r>
       <r>  -14.0824    1.0000 </r>
       <r>   -3.2111    1.0000 </r>
       <r>   -3.0194    1.0000 </r>
       <r>   -2.9960    1.0000 </r>
       <r>   -2.4895    1.0000 </r>
       <r>   -2.4490    1.0000 </r>
       <r>   -2.2202    1.0000 </r>
       <r>    7.1649    0.0000 </r>
       <r>    8.1319    0.0000 </r>
       <r>    8.1592    0.0000 </r>
       <r>    8.9692    0.0000 </r>
      </set>
      <set comment="kpoint 9">
       <r>  -32.1456    1.0000 </r>
       <r>  -21.3015    1.0000 </r>
       <r>  -21.0589    1.0000 </r>
       <r>  -14.2185    1.0000 </r>
       <r>  -14.2085    1.0000 </r>
       <r>  -14.1046    1.0000 </r>
       <r>   -3.3006    1.0000 </r>
       <r>   -3.0869    1.0000 </r>
       <r>   -2.8666    1.0000 </r>
       <r>   -2.7314    1.0000 </r>
       <r>   -2.4572    1.0000 </r>
       <r>   -2.0923    1.0000 </r>
       <r>    6.7929    0.0000 </r>
       <r>    7.9674    0.0000 </r>
       <r>    8.1153    0.0000 </r>
       <r>    9.2616    0.0000 </r>
      </set>
      <set comment="kpoint 10">
       <r>  -32.1648    1.0000 </r>
       <r>  -21.3023    1.0000 </r>
       <r>  -20.9597    1.0000 </r>
       <r>  -14.2063    1.0000 </r>
       <r>  -14.1873    1.0000 </r>
       <r>  -14.1247    1.0000 </r>
       <r>   -3.4228    1.0000 </r>
       <r>   -3.3305    1.0000 </r>
       <r>   -3.1287    1.0000 </r>
       <r>   -2.5434    1.0000 </r>
       <r>   -2.2840    1.0000 </r>
       <r>   -2.0358    1.0000 </r>
       <r>    5.9387    0.0000 </r>
       <r>    7.8865    0.0000 </r>
       <r>    8.0850    0.0000 </r>
       <r>    9.7029    0.0000 </r>
      </set>
      <set comment="kpoint 11">
       <r>  -32.1474    1.0000 </r>
       <r>  -21.3485    1.0000 </r>
       <r>  -20.9964    1.0000 </r>
       <r>  -14.2725    1.0000 </r>
       <r>  -14.2725    1.0000 </r>
       <r>  -13.9937    1.0000 </r>
       <r>   -3.2686    1.0000 </r>
       <r>   -3.2218    1.0000 </r>
       <r>   -3.2218    1.0000 </r>
       <r>   -2.6426    1.0000 </r>
       <r>   -2.0743    1.0000 </r>
       <r>   -2.0743    1.0000 </r>
       <r>    6.4645    0.0000 </r>
       <r>    7.8560    0.0000 </r>
       <r>    8.7273    0.0000 </r>
       <r>    8.9553    0.0000 </r>
      </set>
      <set comment="kpoint 12">
       <r>  -32.1334    1.0000 </r>
       <r>  -21.3523    1.0000 </r>
       <r>  -21.0634    1.0000 </r>
       <r>  -14.2986    1.0000 </r>
       <r>  -14.2786    1.0000 </r>
       <r>  -13.9703    1.0000 </r>
       <r>   -3.5306    1.0000 </r>
       <r>   -3.0696    1.0000 </r>
       <r>   -3.0491    1.0000 </r>
       <r>   -2.2982    1.0000 </r>
       <r>   -2.1838    1.0000 </r>
       <r>   -2.1546    1.0000 </r>
       <r>    6.4571    0.0000 </r>
       <r>    8.4875    0.0000 </r>
       <r>    8.7554    0.0000 </r>
       <r>    8.8458    0.0000 </r>
      </set>
      <set comment="kpoint 13">
       <r>  -32.1265    1.0000 </r>
       <r>  -21.2892    1.0000 </r>
       <r>  -21.1660    1.0000 </r>
       <r>  -14.2911    1.0000 </r>
       <r>  -14.2260    1.0000 </r>
       <r>  -14.0290    1.0000 </r>
       <r>   -3.5282    1.0000 </r>
       <r>   -3.0505    1.0000 </r>
       <r>   -2.8650    1.0000 </r>
       <r>   -2.4261    1.0000 </r>
       <r>   -2.2162    1.0000 </r>
       <r>   -2.1019    1.0000 </r>
       <r>    6.5485    0.0000 </r>
       <r>    8.3239    0.0000 </r>
       <r>    8.5849    0.0000 </r>
       <r>    9.0540    0.0000 </r>
      </set>
      <set comment="kpoint 14">
       <r>  -32.1320    1.0000 </r>
       <r>  -21.2605    1.0000 </r>
       <r>  -21.1698    1.0000 </r>
       <r>  -14.2557    1.0000 </r>
       <r>  -14.1532    1.0000 </r>
       <r>  -14.1314    1.0000 </r>
       <r>   -3.3622    1.0000 </r>
       <r>   -3.0883    1.0000 </r>
       <r>   -2.7706    1.0000 </r>
       <r>   -2.6599    1.0000 </r>
       <r>   -2.3734    1.0000 </r>
       <r>   -2.0512    1.0000 </r>
       <r>    6.7470    0.0000 </r>
       <r>    8.2018    0.0000 </r>
       <r>    8.3340    0.0000 </r>
       <r>    9.0226    0.0000 </r>
      </set>
      <set comment="kpoint 15">
       <r>  -32.1254    1.0000 </r>
       <r>  -21.3922    1.0000 </r>
       <r>  -21.0574    1.0000 </r>
       <r>  -14.3311    1.0000 </r>
       <r>  -14.3311    1.0000 </r>
       <r>  -13.8951    1.0000 </r>
       <r>   -3.8191    1.0000 </r>
       <r>   -2.9334    1.0000 </r>
       <r>   -2.9334    1.0000 </r>
       <r>   -2.1890    1.0000 </r>
       <r>   -2.1890    1.0000 </r>
       <r>   -2.0433    1.0000 </r>
       <r>    6.1881    0.0000 </r>
       <r>    8.1365    0.0000 </r>
       <r>    9.2681    0.0000 </r>
       <r>   10.0125    0.0000 </r>
      </set>
      <set comment="kpoint 16">
       <r>  -32.1224    1.0000 </r>
       <r>  -21.3679    1.0000 </r>
       <r>  -21.1003    1.0000 </r>
       <r>  -14.3278    1.0000 </r>
       <r>  -14.3063    1.0000 </r>
       <r>  -13.9217    1.0000 </r>
       <r>   -3.8077    1.0000 </r>
       <r>   -2.9296    1.0000 </r>
       <r>   -2.8544    1.0000 </r>
       <r>   -2.2934    1.0000 </r>
       <r>   -2.2052    1.0000 </r>
       <r>   -1.9710    1.0000 </r>
       <r>    6.2203    0.0000 </r>
       <r>    8.0973    0.0000 </r>
       <r>    9.1132    0.0000 </r>
       <r>    9.6793    0.0000 </r>
      </set>
      <set comment="kpoint 17">
       <r>  -32.1426    1.0000 </r>
       <r>  -21.3222    1.0000 </r>
       <r>  -21.0510    1.0000 </r>
       <r>  -14.2609    1.0000 </r>
       <r>  -14.2269    1.0000 </r>
       <r>  -14.0496    1.0000 </r>
       <r>   -3.2711    1.0000 </r>
       <r>   -3.1642    1.0000 </r>
       <r>   -3.0779    1.0000 </r>
       <r>   -2.5844    1.0000 </r>
       <r>   -2.3078    1.0000 </r>
       <r>   -2.0570    1.0000 </r>
       <r>    6.6456    0.0000 </r>
       <r>    7.9961    0.0000 </r>
       <r>    8.4666    0.0000 </r>
       <r>    9.0021    0.0000 </r>
      </set>
      <set comment="kpoint 18">
       <r>  -32.1303    1.0000 </r>
       <r>  -21.2790    1.0000 </r>
       <r>  -21.1587    1.0000 </r>
       <r>  -14.2891    1.0000 </r>
       <r>  -14.1732    1.0000 </r>
       <r>  -14.0801    1.0000 </r>
       <r>   -3.3236    1.0000 </r>
       <r>   -3.2255    1.0000 </r>
       <r>   -2.8389    1.0000 </r>
       <r>   -2.4755    1.0000 </r>
       <r>   -2.2836    1.0000 </r>
       <r>   -2.1243    1.0000 </r>
       <r>    6.7068    0.0000 </r>
       <r>    8.3620    0.0000 </r>
       <r>    8.4234    0.0000 </r>
       <r>    8.8673    0.0000 </r>
      </set>
      <set comment="kpoint 19">
       <r>  -32.1248    1.0000 </r>
       <r>  -21.3370    1.0000 </r>
       <r>  -21.1223    1.0000 </r>
       <r>  -14.3321    1.0000 </r>
       <r>  -14.2455    1.0000 </r>
       <r>  -13.9738    1.0000 </r>
       <r>   -3.6607    1.0000 </r>
       <r>   -3.0836    1.0000 </r>
       <r>   -2.8156    1.0000 </r>
       <r>   -2.3430    1.0000 </r>
       <r>   -2.1591    1.0000 </r>
       <r>   -2.0660    1.0000 </r>
       <r>    6.3618    0.0000 </r>
       <r>    8.3089    0.0000 </r>
       <r>    8.8585    0.0000 </r>
       <r>    9.1262    0.0000 </r>
      </set>
      <set comment="kpoint 20">
       <r>  -32.1234    1.0000 </r>
       <r>  -21.2618    1.0000 </r>
       <r>  -21.2088    1.0000 </r>
       <r>  -14.3295    1.0000 </r>
       <r>  -14.1573    1.0000 </r>
       <r>  -14.0615    1.0000 </r>
       <r>   -3.5427    1.0000 </r>
       <r>   -3.1881    1.0000 </r>
       <r>   -2.6522    1.0000 </r>
       <r>   -2.5342    1.0000 </r>
       <r>   -2.1600    1.0000 </r>
       <r>   -2.0432    1.0000 </r>
       <r>    6.4691    0.0000 </r>
       <r>    8.4327    0.0000 </r>
       <r>    8.6083    0.0000 </r>
       <r>    8.8510    0.0000 </r>
      </set>
     </set>
    </set>
   </array>
  </eigenvalues>
  <separator name="orbital magnetization" >
   <v name="MAGDIPOLOUT">      0.00000000      0.00000000      0.00000000</v>
  </separator>
  <dos>
   <i name="efermi">     -1.89034527 </i>
   <total>
    <array>
     <dimension dim="1">gridpoints</dimension>
     <dimension dim="2">spin</dimension>
     <field>energy</field>
     <field>total</field>
     <field>integrated</field>
     <set>
      <set comment="spin 1">
       <r>   -34.3096     0.0000     0.0000 </r>
       <r>   -34.1539     0.0000     0.0000 </r>
       <r>   -33.9983     0.0000     0.0000 </r>
       <r>   -33.8426     0.0000     0.0000 </r>
       <r>   -33.6869     0.0000     0.0000 </r>
       <r>   -33.5312     0.0000     0.0000 </r>
       <r>   -33.3756     0.0000     0.0000 </r>
       <r>   -33.2199     0.0000     0.0000 </r>
       <r>   -33.0642     0.0000     0.0000 </r>
       <r>   -32.9085     0.0000     0.0000 </r>
       <r>   -32.7529     0.0000     0.0000 </r>
       <r>   -32.5972     0.0000     0.0000 </r>
       <r>   -32.4415     0.0000     0.0000 </r>
       <r>   -32.2858     0.0000     0.0000 </r>
       <r>   -32.1302    80.8935     1.3407 </r>
       <r>   -31.9745     0.0000     2.0000 </r>
       <r>   -31.8188     0.0000     2.0000 </r>
       <r>   -31.6631     0.0000     2.0000 </r>
       <r>   -31.5075     0.0000     2.0000 </r>
       <r>   -31.3518     0.0000     2.0000 </r>
       <r>   -31.1961     0.0000     2.0000 </r>
       <r>   -31.0404     0.0000     2.0000 </r>
       <r>   -30.8848     0.0000     2.0000 </r>
       <r>   -30.7291     0.0000     2.0000 </r>
       <r>   -30.5734     0.0000     2.0000 </r>
       <r>   -30.4177     0.0000     2.0000 </r>
       <r>   -30.2621     0.0000     2.0000 </r>
       <r>   -30.1064     0.0000     2.0000 </r>
       <r>   -29.9507     0.0000     2.0000 </r>
       <r>   -29.7950     0.0000     2.0000 </r>
       <r>   -29.6394     0.0000     2.0000 </r>
       <r>   -29.4837     0.0000     2.0000 </r>
       <r>   -29.3280     0.0000     2.0000 </r>
       <r>   -29.1723     0.0000     2.0000 </r>
       <r>   -29.0167     0.0000     2.0000 </r>
       <r>   -28.8610     0.0000     2.0000 </r>
       <r>   -28.7053     0.0000     2.0000 </r>
       <r>   -28.5496     0.0000     2.0000 </r>
       <r>   -28.3940     0.0000     2.0000 </r>
       <r>   -28.2383     0.0000     2.0000 </r>
       <r>   -28.0826     0.0000     2.0000 </r>
       <r>   -27.9269     0.0000     2.0000 </r>
       <r>   -27.7713     0.0000     2.0000 </r>
       <r>   -27.6156     0.0000     2.0000 </r>
       <r>   -27.4599     0.0000     2.0000 </r>
       <r>   -27.3042     0.0000     2.0000 </r>
       <r>   -27.1486     0.0000     2.0000 </r>
       <r>   -26.9929     0.0000     2.0000 </r>
       <r>   -26.8372     0.0000     2.0000 </r>
       <r>   -26.6815     0.0000     2.0000 </r>
       <r>   -26.5259     0.0000     2.0000 </r>
       <r>   -26.3702     0.0000     2.0000 </r>
       <r>   -26.2145     0.0000     2.0000 </r>
       <r>   -26.0588     0.0000     2.0000 </r>
       <r>   -25.9032     0.0000     2.0000 </r>
       <r>   -25.7475     0.0000     2.0000 </r>
       <r>   -25.5918     0.0000     2.0000 </r>
       <r>   -25.4361     0.0000     2.0000 </r>
       <r>   -25.2805     0.0000     2.0000 </r>
       <r>   -25.1248     0.0000     2.0000 </r>
       <r>   -24.9691     0.0000     2.0000 </r>
       <r>   -24.8134     0.0000     2.0000 </r>
       <r>   -24.6578     0.0000     2.0000 </r>
       <r>   -24.5021     0.0000     2.0000 </r>
       <r>   -24.3464     0.0000     2.0000 </r>
       <r>   -24.1907     0.0000     2.0000 </r>
       <r>   -24.0351     0.0000     2.0000 </r>
       <r>   -23.8794     0.0000     2.0000 </r>
       <r>   -23.7237     0.0000     2.0000 </r>
       <r>   -23.5680     0.0000     2.0000 </r>
       <r>   -23.4124     0.0000     2.0000 </r>
       <r>   -23.2567     0.0000     2.0000 </r>
       <r>   -23.1010     0.0000     2.0000 </r>
       <r>   -22.9454     0.0000     2.0000 </r>
       <r>   -22.7897     0.0000     2.0000 </r>
       <r>   -22.6340     0.0000     2.0000 </r>
       <r>   -22.4783     0.0000     2.0000 </r>
       <r>   -22.3227     0.0000     2.0000 </r>
       <r>   -22.1670     0.0000     2.0000 </r>
       <r>   -22.0113     0.0000     2.0000 </r>
       <r>   -21.8556     0.0000     2.0000 </r>
       <r>   -21.7000     0.0000     2.0000 </r>
       <r>   -21.5443     0.0000     2.0000 </r>
       <r>   -21.3886     0.4461     2.0008 </r>
       <r>   -21.2329     0.0000     4.0000 </r>
       <r>   -21.0773     8.9473     5.2718 </r>
       <r>   -20.9216     1.6711     5.9645 </r>
       <r>   -20.7659     0.0000     6.0000 </r>
       <r>   -20.6102     0.0000     6.0000 </r>
       <r>   -20.4546     0.0000     6.0000 </r>
       <r>   -20.2989     0.0000     6.0000 </r>
       <r>   -20.1432     0.0000     6.0000 </r>
       <r>   -19.9875     0.0000     6.0000 </r>
       <r>   -19.8319     0.0000     6.0000 </r>
       <r>   -19.6762     0.0000     6.0000 </r>
       <r>   -19.5205     0.0000     6.0000 </r>
       <r>   -19.3648     0.0000     6.0000 </r>
       <r>   -19.2092     0.0000     6.0000 </r>
       <r>   -19.0535     0.0000     6.0000 </r>
       <r>   -18.8978     0.0000     6.0000 </r>
       <r>   -18.7421     0.0000     6.0000 </r>
       <r>   -18.5865     0.0000     6.0000 </r>
       <r>   -18.4308     0.0000     6.0000 </r>
       <r>   -18.2751     0.0000     6.0000 </r>
       <r>   -18.1194     0.0000     6.0000 </r>
       <r>   -17.9638     0.0000     6.0000 </r>
       <r>   -17.8081     0.0000     6.0000 </r>
       <r>   -17.6524     0.0000     6.0000 </r>
       <r>   -17.4967     0.0000     6.0000 </r>
       <r>   -17.3411     0.0000     6.0000 </r>
       <r>   -17.1854     0.0000     6.0000 </r>
       <r>   -17.0297     0.0000     6.0000 </r>
       <r>   -16.8740     0.0000     6.0000 </r>
       <r>   -16.7184     0.0000     6.0000 </r>
       <r>   -16.5627     0.0000     6.0000 </r>
       <r>   -16.4070     0.0000     6.0000 </r>
       <r>   -16.2513     0.0000     6.0000 </r>
       <r>   -16.0957     0.0000     6.0000 </r>
       <r>   -15.9400     0.0000     6.0000 </r>
       <r>   -15.7843     0.0000     6.0000 </r>
       <r>   -15.6286     0.0000     6.0000 </r>
       <r>   -15.4730     0.0000     6.0000 </r>
       <r>   -15.3173     0.0000     6.0000 </r>
       <r>   -15.1616     0.0000     6.0000 </r>
       <r>   -15.0059     0.0000     6.0000 </r>
       <r>   -14.8503     0.0000     6.0000 </r>
       <r>   -14.6946     0.0000     6.0000 </r>
       <r>   -14.5389     0.0000     6.0000 </r>
       <r>   -14.3832     0.0000     6.0000 </r>
       <r>   -14.2276    24.3757     8.1775 </r>
       <r>   -14.0719    28.6976    10.9443 </r>
       <r>   -13.9162     1.5132    11.9820 </r>
       <r>   -13.7605     0.0000    12.0000 </r>
       <r>   -13.6049     0.0000    12.0000 </r>
       <r>   -13.4492     0.0000    12.0000 </r>
       <r>   -13.2935     0.0000    12.0000 </r>
       <r>   -13.1378     0.0000    12.0000 </r>
       <r>   -12.9822     0.0000    12.0000 </r>
       <r>   -12.8265     0.0000    12.0000 </r>
       <r>   -12.6708     0.0000    12.0000 </r>
       <r>   -12.5151     0.0000    12.0000 </r>
       <r>   -12.3595     0.0000    12.0000 </r>
       <r>   -12.2038     0.0000    12.0000 </r>
       <r>   -12.0481     0.0000    12.0000 </r>
       <r>   -11.8924     0.0000    12.0000 </r>
       <r>   -11.7368     0.0000    12.0000 </r>
       <r>   -11.5811     0.0000    12.0000 </r>
       <r>   -11.4254     0.0000    12.0000 </r>
       <r>   -11.2697     0.0000    12.0000 </r>
       <r>   -11.1141     0.0000    12.0000 </r>
       <r>   -10.9584     0.0000    12.0000 </r>
       <r>   -10.8027     0.0000    12.0000 </r>
       <r>   -10.6470     0.0000    12.0000 </r>
       <r>   -10.4914     0.0000    12.0000 </r>
       <r>   -10.3357     0.0000    12.0000 </r>
       <r>   -10.1800     0.0000    12.0000 </r>
       <r>   -10.0243     0.0000    12.0000 </r>
       <r>    -9.8687     0.0000    12.0000 </r>
       <r>    -9.7130     0.0000    12.0000 </r>
       <r>    -9.5573     0.0000    12.0000 </r>
       <r>    -9.4017     0.0000    12.0000 </r>
       <r>    -9.2460     0.0000    12.0000 </r>
       <r>    -9.0903     0.0000    12.0000 </r>
       <r>    -8.9346     0.0000    12.0000 </r>
       <r>    -8.7790     0.0000    12.0000 </r>
       <r>    -8.6233     0.0000    12.0000 </r>
       <r>    -8.4676     0.0000    12.0000 </r>
       <r>    -8.3119     0.0000    12.0000 </r>
       <r>    -8.1563     0.0000    12.0000 </r>
       <r>    -8.0006     0.0000    12.0000 </r>
       <r>    -7.8449     0.0000    12.0000 </r>
       <r>    -7.6892     0.0000    12.0000 </r>
       <r>    -7.5336     0.0000    12.0000 </r>
       <r>    -7.3779     0.0000    12.0000 </r>
       <r>    -7.2222     0.0000    12.0000 </r>
       <r>    -7.0665     0.0000    12.0000 </r>
       <r>    -6.9109     0.0000    12.0000 </r>
       <r>    -6.7552     0.0000    12.0000 </r>
       <r>    -6.5995     0.0000    12.0000 </r>
       <r>    -6.4438     0.0000    12.0000 </r>
       <r>    -6.2882     0.0000    12.0000 </r>
       <r>    -6.1325     0.0000    12.0000 </r>
       <r>    -5.9768     0.0000    12.0000 </r>
       <r>    -5.8211     0.0000    12.0000 </r>
       <r>    -5.6655     0.0000    12.0000 </r>
       <r>    -5.5098     0.0000    12.0000 </r>
       <r>    -5.3541     0.0000    12.0000 </r>
       <r>    -5.1984     0.0000    12.0000 </r>
       <r>    -5.0428     0.0000    12.0000 </r>
       <r>    -4.8871     0.0000    12.0000 </r>
       <r>    -4.7314     0.0000    12.0000 </r>
       <r>    -4.5757     0.0000    12.0000 </r>
       <r>    -4.4201     0.0000    12.0000 </r>
       <r>    -4.2644     0.0000    12.0000 </r>
       <r>    -4.1087     0.0000    12.0000 </r>
       <r>    -3.9530     0.0000    12.0000 </r>
       <r>    -3.7974     0.5154    12.0186 </r>
       <r>    -3.6417     1.4358    12.1614 </r>
       <r>    -3.4860     4.0826    12.5370 </r>
       <r>    -3.3303     8.9632    13.3887 </r>
       <r>    -3.1747    11.5071    14.7073 </r>
       <r>    -3.0190     6.8085    16.3145 </r>
       <r>    -2.8633     6.0802    17.4132 </r>
       <r>    -2.7076     3.8120    18.0633 </r>
       <r>    -2.5520     4.3628    18.7615 </r>
       <r>    -2.3963     7.3786    19.7872 </r>
       <r>    -2.2406    10.5964    21.0962 </r>
       <r>    -2.0849    22.1081    23.2729 </r>
       <r>    -1.9293     0.0000    24.0000 </r>
       <r>    -1.7736     0.0000    24.0000 </r>
       <r>    -1.6179     0.0000    24.0000 </r>
       <r>    -1.4622     0.0000    24.0000 </r>
       <r>    -1.3066     0.0000    24.0000 </r>
       <r>    -1.1509     0.0000    24.0000 </r>
       <r>    -0.9952     0.0000    24.0000 </r>
       <r>    -0.8395     0.0000    24.0000 </r>
       <r>    -0.6839     0.0000    24.0000 </r>
       <r>    -0.5282     0.0000    24.0000 </r>
       <r>    -0.3725     0.0000    24.0000 </r>
       <r>    -0.2168     0.0000    24.0000 </r>
       <r>    -0.0612     0.0000    24.0000 </r>
       <r>     0.0945     0.0000    24.0000 </r>
       <r>     0.2502     0.0000    24.0000 </r>
       <r>     0.4059     0.0000    24.0000 </r>
       <r>     0.5615     0.0000    24.0000 </r>
       <r>     0.7172     0.0000    24.0000 </r>
       <r>     0.8729     0.0000    24.0000 </r>
       <r>     1.0286     0.0000    24.0000 </r>
       <r>     1.1842     0.0000    24.0000 </r>
       <r>     1.3399     0.0000    24.0000 </r>
       <r>     1.4956     0.0000    24.0000 </r>
       <r>     1.6513     0.0000    24.0000 </r>
       <r>     1.8069     0.0000    24.0000 </r>
       <r>     1.9626     0.0000    24.0000 </r>
       <r>     2.1183     0.0000    24.0000 </r>
       <r>     2.2740     0.0000    24.0000 </r>
       <r>     2.4296     0.0000    24.0000 </r>
       <r>     2.5853     0.0000    24.0000 </r>
       <r>     2.7410     0.0000    24.0000 </r>
       <r>     2.8967     0.0000    24.0000 </r>
       <r>     3.0523     0.0000    24.0000 </r>
       <r>     3.2080     0.0000    24.0000 </r>
       <r>     3.3637     0.0000    24.0000 </r>
       <r>     3.5194     0.0000    24.0000 </r>
       <r>     3.6750     0.0000    24.0000 </r>
       <r>     3.8307     0.0000    24.0000 </r>
       <r>     3.9864     0.0000    24.0000 </r>
       <r>     4.1421     0.0000    24.0000 </r>
       <r>     4.2977     0.0000    24.0000 </r>
       <r>     4.4534     0.0000    24.0000 </r>
       <r>     4.6091     0.0000    24.0000 </r>
       <r>     4.7647     0.0000    24.0000 </r>
       <r>     4.9204     0.0064    24.0002 </r>
       <r>     5.0761     0.0351    24.0032 </r>
       <r>     5.2318     0.0870    24.0124 </r>
       <r>     5.3874     0.1132    24.0289 </r>
       <r>     5.5431     0.1391    24.0484 </r>
       <r>     5.6988     0.1693    24.0724 </r>
       <r>     5.8545     0.2019    24.1012 </r>
       <r>     6.0101     0.2426    24.1355 </r>
       <r>     6.1658     0.3311    24.1794 </r>
       <r>     6.3215     1.5658    24.3368 </r>
       <r>     6.4772     3.0890    24.7325 </r>
       <r>     6.6328     2.6510    25.1847 </r>
       <r>     6.7885     1.7885    25.5991 </r>
       <r>     6.9442     0.9061    25.7902 </r>
       <r>     7.0999     0.5393    25.9021 </r>
       <r>     7.2555     0.2952    25.9641 </r>
       <r>     7.4112     0.1063    25.9955 </r>
       <r>     7.5669     0.0000    26.0000 </r>
       <r>     7.7226     0.3917    26.0026 </r>
       <r>     7.8782     2.0829    26.2087 </r>
       <r>     8.0339     3.2481    26.6218 </r>
       <r>     8.1896     5.7443    27.3928 </r>
       <r>     8.3453     8.5463    28.4353 </r>
       <r>     8.5009     2.6937    29.2261 </r>
       <r>     8.6566     1.8704    29.5887 </r>
       <r>     8.8123     1.1858    29.8243 </r>
       <r>     8.9680     8.1131    30.5933 </r>
       <r>     9.1236     2.1888    31.2719 </r>
       <r>     9.2793     1.1847    31.5263 </r>
       <r>     9.4350     0.9035    31.6882 </r>
       <r>     9.5907     0.6429    31.8085 </r>
       <r>     9.7463     0.4616    31.8931 </r>
       <r>     9.9020     0.3026    31.9528 </r>
       <r>    10.0577     0.1653    31.9883 </r>
       <r>    10.2134     0.0118    31.9998 </r>
       <r>    10.3690     0.0000    32.0000 </r>
       <r>    10.5247     0.0000    32.0000 </r>
       <r>    10.6804     0.0000    32.0000 </r>
       <r>    10.8361     0.0000    32.0000 </r>
       <r>    10.9917     0.0000    32.0000 </r>
       <r>    11.1474     0.0000    32.0000 </r>
       <r>    11.3031     0.0000    32.0000 </r>
       <r>    11.4588     0.0000    32.0000 </r>
       <r>    11.6144     0.0000    32.0000 </r>
       <r>    11.7701     0.0000    32.0000 </r>
       <r>    11.9258     0.0000    32.0000 </r>
       <r>    12.0815     0.0000    32.0000 </r>
       <r>    12.2371     0.0000    32.0000 </r>
       <r>    12.3928     0.0000    32.0000 </r>
      </set>
     </set>
    </array>
   </total>
   <partial>
    <array>
     <dimension dim="1">gridpoints</dimension>
     <dimension dim="2">spin</dimension>
     <dimension dim="3">ion</dimension>
     <field>energy</field>
     <field>  s</field>
     <field> py</field>
     <field> pz</field>
     <field> px</field>
     <field>dxy</field>
     <field>dyz</field>
     <field>dz2</field>
     <field>dxz</field>
     <field>dx2</field>
     <set>
      <set comment="ion 1">
       <set comment="spin 1">
        <r>   -34.3096     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -34.1539     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.9983     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.8426     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.6869     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.5312     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.3756     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.2199     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.0642     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.9085     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.7529     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.5972     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.4415     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.2858     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.1302    79.0387     0.0000     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.9745     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.8188     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.6631     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.5075     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.3518     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.1961     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.0404     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.8848     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.7291     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.5734     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.4177     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.2621     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.1064     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.9507     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.7950     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.6394     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.4837     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.3280     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.1723     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.0167     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.8610     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.7053     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.5496     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.3940     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.2383     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.0826     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.9269     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.7713     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.6156     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.4599     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.3042     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.1486     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.9929     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.8372     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.6815     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.5259     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.3702     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.2145     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.0588     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.9032     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.7475     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.5918     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.4361     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.2805     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.1248     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.9691     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.8134     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.6578     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.5021     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.3464     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.1907     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.0351     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.8794     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.7237     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.5680     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.4124     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.2567     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.1010     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.9454     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.7897     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.6340     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.4783     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.3227     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.1670     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.0113     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.8556     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.7000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.5443     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.3886     0.0002     0.0000     0.0127     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.2329     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.0773     0.0036     0.0064     0.0091     0.0253     0.0188     0.0024     0.0000     0.0030     0.0000 </r>
        <r>   -20.9216     0.0000     0.0002     0.0006     0.0002     0.0007     0.0004     0.0000     0.0004     0.0000 </r>
        <r>   -20.7659     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.6102     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.4546     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.2989     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.1432     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.9875     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.8319     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.6762     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.5205     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.3648     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.2092     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.0535     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.8978     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.7421     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.5865     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.4308     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.2751     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.1194     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.9638     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.8081     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.6524     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.4967     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.3411     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.1854     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.0297     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.8740     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.7184     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.5627     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.4070     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.2513     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.0957     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.9400     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.7843     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.6286     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.4730     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.3173     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.1616     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.0059     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.8503     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.6946     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.5389     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.3832     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.2276     0.0000     8.4636     2.5119    11.8474     0.0005     0.0001     0.0001     0.0001     0.0000 </r>
        <r>   -14.0719     0.0011     3.7652    18.8484     3.7878     0.0005     0.0012     0.0001     0.0003     0.0000 </r>
        <r>   -13.9162     0.0000     0.0010     1.3935     0.0005     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.7605     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.6049     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.4492     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.2935     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.1378     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.9822     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.8265     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.6708     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.5151     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.3595     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.2038     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.0481     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.8924     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.7368     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.5811     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.4254     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.2697     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.1141     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.9584     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.8027     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.6470     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.4914     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.3357     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.1800     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.0243     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.8687     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.7130     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.5573     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.4017     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.2460     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.0903     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.9346     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.7790     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.6233     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.4676     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.3119     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.1563     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.0006     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.8449     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.6892     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.5336     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.3779     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.2222     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.0665     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.9109     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.7552     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.5995     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.4438     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.2882     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.1325     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.9768     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.8211     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.6655     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.5098     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.3541     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.1984     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.0428     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.8871     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.7314     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.5757     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.4201     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.2644     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.1087     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.9530     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.7974     0.0102     0.0008     0.0001     0.0003     0.0000     0.0000     0.0065     0.0000     0.0000 </r>
        <r>    -3.6417     0.0272     0.0037     0.0006     0.0019     0.0003     0.0001     0.0146     0.0001     0.0001 </r>
        <r>    -3.4860     0.0420     0.0119     0.0027     0.0073     0.0225     0.0268     0.0166     0.0259     0.0009 </r>
        <r>    -3.3303     0.0471     0.0623     0.0092     0.0385     0.0707     0.0737     0.0277     0.0524     0.0036 </r>
        <r>    -3.1747     0.0348     0.1825     0.0170     0.0414     0.0509     0.0831     0.0362     0.0560     0.0175 </r>
        <r>    -3.0190     0.0220     0.0648     0.0099     0.0604     0.0386     0.0235     0.0040     0.0450     0.0034 </r>
        <r>    -2.8633     0.0144     0.0364     0.0019     0.0749     0.0143     0.0276     0.0009     0.0538     0.0084 </r>
        <r>    -2.7076     0.0134     0.0079     0.0137     0.0364     0.0179     0.0054     0.0038     0.0101     0.0016 </r>
        <r>    -2.5520     0.0063     0.0197     0.0300     0.0196     0.0169     0.0102     0.0026     0.0057     0.0025 </r>
        <r>    -2.3963     0.0031     0.0430     0.0263     0.0481     0.0133     0.0256     0.0019     0.0119     0.0060 </r>
        <r>    -2.2406     0.0036     0.0438     0.0525     0.0413     0.0113     0.0199     0.0039     0.0336     0.0040 </r>
        <r>    -2.0849     0.0025     0.0503     0.0738     0.0988     0.0106     0.0286     0.0032     0.0659     0.0025 </r>
        <r>    -1.9293     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.7736     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.6179     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.4622     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.3066     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.1509     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.9952     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.8395     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.6839     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.5282     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.3725     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.2168     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.0612     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.0945     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.2502     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.4059     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.5615     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.7172     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.8729     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.0286     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.1842     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.3399     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.4956     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.6513     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.8069     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.9626     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.1183     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.2740     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.4296     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.5853     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.7410     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.8967     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.0523     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.2080     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.3637     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.5194     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.6750     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.8307     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.9864     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.1421     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.2977     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.4534     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.6091     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.7647     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.9204     0.0007     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.0761     0.0039     0.0001     0.0002     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.2318     0.0097     0.0002     0.0005     0.0002     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.3874     0.0117     0.0005     0.0007     0.0005     0.0003     0.0001     0.0003     0.0001     0.0000 </r>
        <r>     5.5431     0.0136     0.0007     0.0012     0.0007     0.0004     0.0002     0.0008     0.0002     0.0000 </r>
        <r>     5.6988     0.0157     0.0008     0.0019     0.0008     0.0005     0.0003     0.0017     0.0003     0.0000 </r>
        <r>     5.8545     0.0180     0.0010     0.0026     0.0010     0.0006     0.0005     0.0027     0.0005     0.0000 </r>
        <r>     6.0101     0.0205     0.0013     0.0033     0.0013     0.0009     0.0007     0.0046     0.0007     0.0000 </r>
        <r>     6.1658     0.0243     0.0021     0.0047     0.0020     0.0022     0.0014     0.0117     0.0010     0.0002 </r>
        <r>     6.3215     0.0307     0.0039     0.0108     0.0035     0.0056     0.0038     0.3278     0.0019     0.0055 </r>
        <r>     6.4772     0.0427     0.0072     0.0269     0.0051     0.0102     0.0152     0.6577     0.0040     0.0344 </r>
        <r>     6.6328     0.0299     0.0091     0.0190     0.0070     0.0170     0.0184     0.5570     0.0055     0.0471 </r>
        <r>     6.7885     0.0278     0.0111     0.0142     0.0098     0.0236     0.0143     0.3349     0.0065     0.0199 </r>
        <r>     6.9442     0.0118     0.0060     0.0061     0.0056     0.0136     0.0076     0.1779     0.0051     0.0097 </r>
        <r>     7.0999     0.0090     0.0040     0.0045     0.0039     0.0100     0.0067     0.0951     0.0059     0.0029 </r>
        <r>     7.2555     0.0063     0.0025     0.0026     0.0025     0.0076     0.0055     0.0438     0.0055     0.0000 </r>
        <r>     7.4112     0.0024     0.0010     0.0009     0.0010     0.0032     0.0024     0.0147     0.0024     0.0000 </r>
        <r>     7.5669     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.7226     0.0094     0.0001     0.0019     0.0001     0.0002     0.0013     0.1487     0.0003     0.0271 </r>
        <r>     7.8782     0.0309     0.0013     0.0073     0.0004     0.0235     0.0174     0.4578     0.0071     0.5087 </r>
        <r>     8.0339     0.0529     0.0025     0.0150     0.0015     0.1264     0.0869     0.5550     0.0599     0.7371 </r>
        <r>     8.1896     0.0742     0.0067     0.0197     0.0085     0.6555     0.1593     0.7657     0.0869     1.1830 </r>
        <r>     8.3453     0.0864     0.0147     0.0335     0.0387     1.9803     0.2731     0.5193     0.1083     1.3688 </r>
        <r>     8.5009     0.0260     0.0024     0.0162     0.0036     0.1264     0.0817     0.0834     0.0259     1.0797 </r>
        <r>     8.6566     0.0182     0.0010     0.0154     0.0014     0.0530     0.0380     0.0664     0.0171     0.8175 </r>
        <r>     8.8123     0.0107     0.0038     0.0132     0.0037     0.0519     0.0306     0.0529     0.0291     0.4252 </r>
        <r>     8.9680     0.0240     0.0361     0.1374     0.0512     1.3012     1.0119     0.3365     0.5036     0.6852 </r>
        <r>     9.1236     0.0070     0.0051     0.0345     0.0067     0.3533     0.2711     0.0422     0.1861     0.2644 </r>
        <r>     9.2793     0.0042     0.0021     0.0208     0.0025     0.2407     0.1705     0.0145     0.1201     0.0517 </r>
        <r>     9.4350     0.0034     0.0011     0.0151     0.0013     0.1821     0.1374     0.0083     0.1072     0.0288 </r>
        <r>     9.5907     0.0029     0.0004     0.0108     0.0004     0.1379     0.0971     0.0036     0.0798     0.0170 </r>
        <r>     9.7463     0.0028     0.0002     0.0092     0.0002     0.1028     0.0669     0.0025     0.0590     0.0070 </r>
        <r>     9.9020     0.0018     0.0001     0.0055     0.0000     0.0655     0.0462     0.0015     0.0449     0.0012 </r>
        <r>    10.0577     0.0000     0.0000     0.0000     0.0000     0.0461     0.0265     0.0000     0.0256     0.0000 </r>
        <r>    10.2134     0.0000     0.0000     0.0000     0.0000     0.0033     0.0019     0.0000     0.0018     0.0000 </r>
        <r>    10.3690     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.5247     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.6804     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.8361     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.9917     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.1474     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.3031     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.4588     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.6144     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.7701     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.9258     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.0815     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.2371     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.3928     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
       </set>
      </set>
      <set comment="ion 2">
       <set comment="spin 1">
        <r>   -34.3096     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -34.1539     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.9983     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.8426     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.6869     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.5312     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.3756     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.2199     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.0642     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.9085     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.7529     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.5972     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.4415     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.2858     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.1302     0.0221     0.0017     0.0081     0.0031     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.9745     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.8188     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.6631     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.5075     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.3518     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.1961     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.0404     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.8848     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.7291     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.5734     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.4177     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.2621     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.1064     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.9507     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.7950     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.6394     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.4837     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.3280     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.1723     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.0167     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.8610     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.7053     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.5496     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.3940     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.2383     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.0826     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.9269     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.7713     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.6156     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.4599     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.3042     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.1486     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.9929     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.8372     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.6815     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.5259     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.3702     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.2145     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.0588     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.9032     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.7475     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.5918     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.4361     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.2805     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.1248     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.9691     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.8134     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.6578     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.5021     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.3464     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.1907     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.0351     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.8794     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.7237     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.5680     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.4124     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.2567     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.1010     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.9454     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.7897     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.6340     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.4783     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.3227     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.1670     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.0113     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.8556     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.7000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.5443     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.3886     0.1834     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.2329     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.0773     3.8482     0.0001     0.0001     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.9216     0.7312     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.7659     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.6102     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.4546     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.2989     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.1432     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.9875     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.8319     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.6762     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.5205     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.3648     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.2092     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.0535     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.8978     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.7421     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.5865     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.4308     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.2751     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.1194     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.9638     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.8081     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.6524     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.4967     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.3411     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.1854     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.0297     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.8740     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.7184     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.5627     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.4070     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.2513     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.0957     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.9400     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.7843     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.6286     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.4730     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.3173     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.1616     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.0059     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.8503     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.6946     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.5389     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.3832     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.2276     0.0463     0.0400     0.0142     0.0327     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.0719     0.4257     0.0294     0.0144     0.0231     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.9162     0.0313     0.0004     0.0001     0.0002     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.7605     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.6049     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.4492     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.2935     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.1378     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.9822     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.8265     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.6708     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.5151     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.3595     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.2038     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.0481     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.8924     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.7368     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.5811     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.4254     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.2697     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.1141     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.9584     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.8027     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.6470     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.4914     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.3357     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.1800     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.0243     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.8687     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.7130     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.5573     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.4017     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.2460     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.0903     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.9346     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.7790     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.6233     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.4676     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.3119     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.1563     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.0006     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.8449     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.6892     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.5336     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.3779     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.2222     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.0665     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.9109     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.7552     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.5995     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.4438     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.2882     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.1325     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.9768     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.8211     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.6655     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.5098     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.3541     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.1984     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.0428     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.8871     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.7314     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.5757     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.4201     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.2644     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.1087     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.9530     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.7974     0.0001     0.0005     0.1594     0.0020     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.6417     0.0004     0.0022     0.4388     0.0190     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.4860     0.0009     0.2053     0.8372     0.3089     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.3303     0.0018     0.5300     1.5943     0.8804     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.1747     0.0023     0.8747     1.0731     1.9532     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.0190     0.0027     1.0426     0.4891     0.8436     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.8633     0.0013     1.3496     0.1249     0.6810     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.7076     0.0027     0.6068     0.5279     0.2462     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.5520     0.0023     0.6712     0.5828     0.3579     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.3963     0.0013     1.3206     0.5649     0.9083     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.2406     0.0015     1.4123     1.1443     1.5413     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.0849     0.0009     1.7337     3.6787     3.3285     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.9293     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.7736     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.6179     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.4622     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.3066     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.1509     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.9952     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.8395     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.6839     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.5282     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.3725     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.2168     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.0612     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.0945     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.2502     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.4059     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.5615     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.7172     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.8729     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.0286     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.1842     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.3399     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.4956     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.6513     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.8069     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.9626     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.1183     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.2740     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.4296     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.5853     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.7410     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.8967     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.0523     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.2080     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.3637     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.5194     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.6750     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.8307     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.9864     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.1421     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.2977     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.4534     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.6091     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.7647     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.9204     0.0003     0.0000     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.0761     0.0014     0.0001     0.0003     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.2318     0.0035     0.0002     0.0007     0.0002     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.3874     0.0043     0.0007     0.0010     0.0007     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.5431     0.0050     0.0009     0.0019     0.0009     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.6988     0.0059     0.0010     0.0029     0.0010     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.8545     0.0067     0.0012     0.0039     0.0012     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.0101     0.0078     0.0015     0.0052     0.0015     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.1658     0.0095     0.0024     0.0079     0.0024     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.3215     0.0132     0.0050     0.0770     0.0089     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.4772     0.0212     0.0079     0.1479     0.0234     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.6328     0.0168     0.0102     0.1051     0.0278     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.7885     0.0162     0.0130     0.0557     0.0182     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.9442     0.0075     0.0074     0.0248     0.0102     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.0999     0.0057     0.0048     0.0136     0.0056     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.2555     0.0039     0.0031     0.0062     0.0031     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.4112     0.0015     0.0012     0.0019     0.0012     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.5669     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.7226     0.0026     0.0010     0.0028     0.0010     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.8782     0.0108     0.0102     0.0080     0.0126     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.0339     0.0287     0.0201     0.0115     0.0229     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.1896     0.0642     0.0305     0.0367     0.0267     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.3453     0.1372     0.0297     0.0527     0.0306     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.5009     0.0191     0.0111     0.0143     0.0295     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.6566     0.0109     0.0063     0.0073     0.0187     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.8123     0.0090     0.0061     0.0080     0.0096     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.9680     0.1259     0.0313     0.1077     0.0559     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.1236     0.0309     0.0112     0.0335     0.0142     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.2793     0.0179     0.0083     0.0240     0.0091     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.4350     0.0129     0.0082     0.0198     0.0086     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.5907     0.0080     0.0071     0.0165     0.0073     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.7463     0.0054     0.0055     0.0130     0.0056     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.9020     0.0031     0.0045     0.0090     0.0045     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.0577     0.0005     0.0036     0.0063     0.0037     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.2134     0.0000     0.0003     0.0004     0.0003     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.3690     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.5247     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.6804     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.8361     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.9917     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.1474     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.3031     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.4588     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.6144     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.7701     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.9258     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.0815     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.2371     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.3928     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
       </set>
      </set>
      <set comment="ion 3">
       <set comment="spin 1">
        <r>   -34.3096     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -34.1539     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.9983     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.8426     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.6869     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.5312     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.3756     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.2199     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -33.0642     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.9085     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.7529     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.5972     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.4415     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.2858     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -32.1302     0.0221     0.0017     0.0081     0.0031     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.9745     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.8188     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.6631     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.5075     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.3518     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.1961     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -31.0404     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.8848     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.7291     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.5734     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.4177     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.2621     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -30.1064     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.9507     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.7950     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.6394     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.4837     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.3280     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.1723     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -29.0167     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.8610     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.7053     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.5496     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.3940     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.2383     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -28.0826     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.9269     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.7713     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.6156     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.4599     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.3042     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -27.1486     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.9929     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.8372     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.6815     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.5259     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.3702     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.2145     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -26.0588     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.9032     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.7475     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.5918     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.4361     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.2805     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -25.1248     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.9691     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.8134     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.6578     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.5021     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.3464     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.1907     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -24.0351     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.8794     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.7237     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.5680     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.4124     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.2567     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -23.1010     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.9454     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.7897     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.6340     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.4783     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.3227     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.1670     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -22.0113     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.8556     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.7000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.5443     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.3886     0.1834     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.2329     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -21.0773     3.8482     0.0001     0.0001     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.9216     0.7312     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.7659     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.6102     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.4546     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.2989     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -20.1432     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.9875     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.8319     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.6762     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.5205     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.3648     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.2092     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -19.0535     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.8978     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.7421     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.5865     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.4308     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.2751     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -18.1194     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.9638     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.8081     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.6524     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.4967     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.3411     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.1854     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -17.0297     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.8740     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.7184     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.5627     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.4070     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.2513     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -16.0957     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.9400     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.7843     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.6286     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.4730     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.3173     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.1616     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -15.0059     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.8503     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.6946     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.5389     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.3832     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.2276     0.0463     0.0400     0.0142     0.0327     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -14.0719     0.4257     0.0294     0.0144     0.0231     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.9162     0.0313     0.0004     0.0001     0.0002     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.7605     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.6049     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.4492     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.2935     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -13.1378     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.9822     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.8265     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.6708     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.5151     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.3595     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.2038     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -12.0481     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.8924     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.7368     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.5811     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.4254     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.2697     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -11.1141     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.9584     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.8027     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.6470     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.4914     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.3357     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.1800     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>   -10.0243     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.8687     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.7130     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.5573     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.4017     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.2460     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -9.0903     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.9346     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.7790     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.6233     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.4676     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.3119     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.1563     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -8.0006     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.8449     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.6892     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.5336     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.3779     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.2222     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -7.0665     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.9109     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.7552     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.5995     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.4438     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.2882     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -6.1325     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.9768     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.8211     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.6655     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.5098     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.3541     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.1984     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -5.0428     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.8871     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.7314     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.5757     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.4201     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.2644     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -4.1087     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.9530     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.7974     0.0001     0.0005     0.1594     0.0020     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.6417     0.0004     0.0022     0.4388     0.0190     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.4860     0.0009     0.2053     0.8372     0.3089     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.3303     0.0018     0.5300     1.5943     0.8804     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.1747     0.0023     0.8747     1.0731     1.9532     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -3.0190     0.0027     1.0426     0.4891     0.8436     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.8633     0.0013     1.3496     0.1249     0.6810     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.7076     0.0027     0.6068     0.5279     0.2462     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.5520     0.0023     0.6712     0.5828     0.3579     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.3963     0.0013     1.3206     0.5649     0.9083     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.2406     0.0015     1.4123     1.1443     1.5413     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -2.0849     0.0009     1.7337     3.6787     3.3285     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.9293     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.7736     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.6179     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.4622     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.3066     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -1.1509     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.9952     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.8395     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.6839     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.5282     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.3725     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.2168     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    -0.0612     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.0945     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.2502     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.4059     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.5615     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.7172     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     0.8729     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.0286     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.1842     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.3399     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.4956     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.6513     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.8069     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     1.9626     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.1183     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.2740     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.4296     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.5853     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.7410     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     2.8967     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.0523     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.2080     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.3637     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.5194     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.6750     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.8307     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     3.9864     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.1421     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.2977     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.4534     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.6091     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.7647     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     4.9204     0.0003     0.0000     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.0761     0.0014     0.0001     0.0003     0.0001     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.2318     0.0035     0.0002     0.0007     0.0002     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.3874     0.0043     0.0007     0.0010     0.0007     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.5431     0.0050     0.0009     0.0019     0.0009     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.6988     0.0059     0.0010     0.0029     0.0010     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     5.8545     0.0067     0.0012     0.0039     0.0012     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.0101     0.0078     0.0015     0.0052     0.0015     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.1658     0.0095     0.0024     0.0079     0.0024     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.3215     0.0132     0.0050     0.0770     0.0089     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.4772     0.0212     0.0079     0.1479     0.0234     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.6328     0.0168     0.0102     0.1051     0.0278     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.7885     0.0162     0.0130     0.0557     0.0182     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     6.9442     0.0075     0.0074     0.0248     0.0102     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.0999     0.0057     0.0048     0.0136     0.0056     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.2555     0.0039     0.0031     0.0062     0.0031     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.4112     0.0015     0.0012     0.0019     0.0012     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.5669     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.7226     0.0026     0.0010     0.0028     0.0010     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     7.8782     0.0108     0.0102     0.0080     0.0126     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.0339     0.0287     0.0201     0.0115     0.0229     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.1896     0.0642     0.0305     0.0367     0.0267     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.3453     0.1372     0.0297     0.0527     0.0306     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.5009     0.0191     0.0111     0.0143     0.0295     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.6566     0.0109     0.0063     0.0073     0.0187     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.8123     0.0090     0.0061     0.0080     0.0096     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     8.9680     0.1259     0.0313     0.1077     0.0559     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.1236     0.0309     0.0112     0.0335     0.0142     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.2793     0.0179     0.0083     0.0240     0.0091     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.4350     0.0129     0.0082     0.0198     0.0086     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.5907     0.0080     0.0071     0.0165     0.0073     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.7463     0.0054     0.0055     0.0130     0.0056     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>     9.9020     0.0031     0.0045     0.0090     0.0045     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.0577     0.0005     0.0036     0.0063     0.0037     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.2134     0.0000     0.0003     0.0004     0.0003     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.3690     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.5247     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.6804     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.8361     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    10.9917     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.1474     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.3031     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.4588     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.6144     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.7701     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    11.9258     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.0815     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.2371     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
        <r>    12.3928     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000     0.0000 </r>
       </set>
      </set>
     </set>
    </array>
   </partial>
  </dos>
  <projected>
   <eigenvalues>
    <array>
     <dimension dim="1">band</dimension>
     <dimension dim="2">kpoint</dimension>
     <dimension dim="3">spin</dimension>
     <field>eigene</field>
     <field>occ</field>
     <set>
      <set comment="spin 1">
       <set comment="kpoint 1">
        <r>  -32.1868    1.0000 </r>
        <r>  -21.2679    1.0000 </r>
        <r>  -20.8827    1.0000 </r>
        <r>  -14.1647    1.0000 </r>
        <r>  -14.1647    1.0000 </r>
        <r>  -14.1647    1.0000 </r>
        <r>   -3.5680    1.0000 </r>
        <r>   -3.5680    1.0000 </r>
        <r>   -3.5680    1.0000 </r>
        <r>   -2.0575    1.0000 </r>
        <r>   -2.0575    1.0000 </r>
        <r>   -2.0575    1.0000 </r>
        <r>    4.8047    0.0000 </r>
        <r>    7.9756    0.0000 </r>
        <r>    7.9756    0.0000 </r>
        <r>   10.2700    0.0000 </r>
       </set>
       <set comment="kpoint 2">
        <r>  -32.1777    1.0000 </r>
        <r>  -21.2851    1.0000 </r>
        <r>  -20.9117    1.0000 </r>
        <r>  -14.1781    1.0000 </r>
        <r>  -14.1781    1.0000 </r>
        <r>  -14.1489    1.0000 </r>
        <r>   -3.4863    1.0000 </r>
        <r>   -3.4863    1.0000 </r>
        <r>   -3.3995    1.0000 </r>
        <r>   -2.2376    1.0000 </r>
        <r>   -2.1158    1.0000 </r>
        <r>   -2.1158    1.0000 </r>
        <r>    5.2843    0.0000 </r>
        <r>    7.9822    0.0000 </r>
        <r>    7.9822    0.0000 </r>
        <r>   10.0479    0.0000 </r>
       </set>
       <set comment="kpoint 3">
        <r>  -32.1572    1.0000 </r>
        <r>  -21.3043    1.0000 </r>
        <r>  -20.9970    1.0000 </r>
        <r>  -14.2078    1.0000 </r>
        <r>  -14.2078    1.0000 </r>
        <r>  -14.1075    1.0000 </r>
        <r>   -3.2930    1.0000 </r>
        <r>   -3.2930    1.0000 </r>
        <r>   -3.0220    1.0000 </r>
        <r>   -2.5753    1.0000 </r>
        <r>   -2.2511    1.0000 </r>
        <r>   -2.2511    1.0000 </r>
        <r>    6.3644    0.0000 </r>
        <r>    8.0146    0.0000 </r>
        <r>    8.0146    0.0000 </r>
        <r>    9.5517    0.0000 </r>
       </set>
       <set comment="kpoint 4">
        <r>  -32.1407    1.0000 </r>
        <r>  -21.2895    1.0000 </r>
        <r>  -21.0980    1.0000 </r>
        <r>  -14.2313    1.0000 </r>
        <r>  -14.2313    1.0000 </r>
        <r>  -14.0688    1.0000 </r>
        <r>   -3.1213    1.0000 </r>
        <r>   -3.1213    1.0000 </r>
        <r>   -2.8111    1.0000 </r>
        <r>   -2.7072    1.0000 </r>
        <r>   -2.3709    1.0000 </r>
        <r>   -2.3709    1.0000 </r>
        <r>    7.4953    0.0000 </r>
        <r>    8.0564    0.0000 </r>
        <r>    8.0564    0.0000 </r>
        <r>    8.6482    0.0000 </r>
       </set>
       <set comment="kpoint 5">
        <r>  -32.1747    1.0000 </r>
        <r>  -21.2932    1.0000 </r>
        <r>  -20.9179    1.0000 </r>
        <r>  -14.1982    1.0000 </r>
        <r>  -14.1982    1.0000 </r>
        <r>  -14.1129    1.0000 </r>
        <r>   -3.4748    1.0000 </r>
        <r>   -3.4748    1.0000 </r>
        <r>   -3.2995    1.0000 </r>
        <r>   -2.4727    1.0000 </r>
        <r>   -2.0472    1.0000 </r>
        <r>   -2.0472    1.0000 </r>
        <r>    5.4424    0.0000 </r>
        <r>    7.7724    0.0000 </r>
        <r>    8.1854    0.0000 </r>
        <r>    9.8833    0.0000 </r>
       </set>
       <set comment="kpoint 6">
        <r>  -32.1580    1.0000 </r>
        <r>  -21.3155    1.0000 </r>
        <r>  -20.9797    1.0000 </r>
        <r>  -14.2321    1.0000 </r>
        <r>  -14.2178    1.0000 </r>
        <r>  -14.0757    1.0000 </r>
        <r>   -3.3282    1.0000 </r>
        <r>   -3.3180    1.0000 </r>
        <r>   -2.9515    1.0000 </r>
        <r>   -2.8343    1.0000 </r>
        <r>   -2.1310    1.0000 </r>
        <r>   -2.1049    1.0000 </r>
        <r>    6.2593    0.0000 </r>
        <r>    7.7099    0.0000 </r>
        <r>    8.3333    0.0000 </r>
        <r>    9.4387    0.0000 </r>
       </set>
       <set comment="kpoint 7">
        <r>  -32.1401    1.0000 </r>
        <r>  -21.3032    1.0000 </r>
        <r>  -21.0849    1.0000 </r>
        <r>  -14.2541    1.0000 </r>
        <r>  -14.2137    1.0000 </r>
        <r>  -14.0676    1.0000 </r>
        <r>   -3.1795    1.0000 </r>
        <r>   -3.1351    1.0000 </r>
        <r>   -3.0386    1.0000 </r>
        <r>   -2.5856    1.0000 </r>
        <r>   -2.2620    1.0000 </r>
        <r>   -2.2560    1.0000 </r>
        <r>    6.9333    0.0000 </r>
        <r>    8.0192    0.0000 </r>
        <r>    8.3193    0.0000 </r>
        <r>    9.0227    0.0000 </r>
       </set>
       <set comment="kpoint 8">
        <r>  -32.1346    1.0000 </r>
        <r>  -21.2710    1.0000 </r>
        <r>  -21.1468    1.0000 </r>
        <r>  -14.2481    1.0000 </r>
        <r>  -14.2059    1.0000 </r>
        <r>  -14.0824    1.0000 </r>
        <r>   -3.2111    1.0000 </r>
        <r>   -3.0194    1.0000 </r>
        <r>   -2.9960    1.0000 </r>
        <r>   -2.4895    1.0000 </r>
        <r>   -2.4490    1.0000 </r>
        <r>   -2.2202    1.0000 </r>
        <r>    7.1649    0.0000 </r>
        <r>    8.1319    0.0000 </r>
        <r>    8.1592    0.0000 </r>
        <r>    8.9692    0.0000 </r>
       </set>
       <set comment="kpoint 9">
        <r>  -32.1456    1.0000 </r>
        <r>  -21.3015    1.0000 </r>
        <r>  -21.0589    1.0000 </r>
        <r>  -14.2185    1.0000 </r>
        <r>  -14.2085    1.0000 </r>
        <r>  -14.1046    1.0000 </r>
        <r>   -3.3006    1.0000 </r>
        <r>   -3.0869    1.0000 </r>
        <r>   -2.8666    1.0000 </r>
        <r>   -2.7314    1.0000 </r>
        <r>   -2.4572    1.0000 </r>
        <r>   -2.0923    1.0000 </r>
        <r>    6.7929    0.0000 </r>
        <r>    7.9674    0.0000 </r>
        <r>    8.1153    0.0000 </r>
        <r>    9.2616    0.0000 </r>
       </set>
       <set comment="kpoint 10">
        <r>  -32.1648    1.0000 </r>
        <r>  -21.3023    1.0000 </r>
        <r>  -20.9597    1.0000 </r>
        <r>  -14.2063    1.0000 </r>
        <r>  -14.1873    1.0000 </r>
        <r>  -14.1247    1.0000 </r>
        <r>   -3.4228    1.0000 </r>
        <r>   -3.3305    1.0000 </r>
        <r>   -3.1287    1.0000 </r>
        <r>   -2.5434    1.0000 </r>
        <r>   -2.2840    1.0000 </r>
        <r>   -2.0358    1.0000 </r>
        <r>    5.9387    0.0000 </r>
        <r>    7.8865    0.0000 </r>
        <r>    8.0850    0.0000 </r>
        <r>    9.7029    0.0000 </r>
       </set>
       <set comment="kpoint 11">
        <r>  -32.1474    1.0000 </r>
        <r>  -21.3485    1.0000 </r>
        <r>  -20.9964    1.0000 </r>
        <r>  -14.2725    1.0000 </r>
        <r>  -14.2725    1.0000 </r>
        <r>  -13.9937    1.0000 </r>
        <r>   -3.2686    1.0000 </r>
        <r>   -3.2218    1.0000 </r>
        <r>   -3.2218    1.0000 </r>
        <r>   -2.6426    1.0000 </r>
        <r>   -2.0743    1.0000 </r>
        <r>   -2.0743    1.0000 </r>
        <r>    6.4645    0.0000 </r>
        <r>    7.8560    0.0000 </r>
        <r>    8.7273    0.0000 </r>
        <r>    8.9553    0.0000 </r>
       </set>
       <set comment="kpoint 12">
        <r>  -32.1334    1.0000 </r>
        <r>  -21.3523    1.0000 </r>
        <r>  -21.0634    1.0000 </r>
        <r>  -14.2986    1.0000 </r>
        <r>  -14.2786    1.0000 </r>
        <r>  -13.9703    1.0000 </r>
        <r>   -3.5306    1.0000 </r>
        <r>   -3.0696    1.0000 </r>
        <r>   -3.0491    1.0000 </r>
        <r>   -2.2982    1.0000 </r>
        <r>   -2.1838    1.0000 </r>
        <r>   -2.1546    1.0000 </r>
        <r>    6.4571    0.0000 </r>
        <r>    8.4875    0.0000 </r>
        <r>    8.7554    0.0000 </r>
        <r>    8.8458    0.0000 </r>
       </set>
       <set comment="kpoint 13">
        <r>  -32.1265    1.0000 </r>
        <r>  -21.2892    1.0000 </r>
        <r>  -21.1660    1.0000 </r>
        <r>  -14.2911    1.0000 </r>
        <r>  -14.2260    1.0000 </r>
        <r>  -14.0290    1.0000 </r>
        <r>   -3.5282    1.0000 </r>
        <r>   -3.0505    1.0000 </r>
        <r>   -2.8650    1.0000 </r>
        <r>   -2.4261    1.0000 </r>
        <r>   -2.2162    1.0000 </r>
        <r>   -2.1019    1.0000 </r>
        <r>    6.5485    0.0000 </r>
        <r>    8.3239    0.0000 </r>
        <r>    8.5849    0.0000 </r>
        <r>    9.0540    0.0000 </r>
       </set>
       <set comment="kpoint 14">
        <r>  -32.1320    1.0000 </r>
        <r>  -21.2605    1.0000 </r>
        <r>  -21.1698    1.0000 </r>
        <r>  -14.2557    1.0000 </r>
        <r>  -14.1532    1.0000 </r>
        <r>  -14.1314    1.0000 </r>
        <r>   -3.3622    1.0000 </r>
        <r>   -3.0883    1.0000 </r>
        <r>   -2.7706    1.0000 </r>
        <r>   -2.6599    1.0000 </r>
        <r>   -2.3734    1.0000 </r>
        <r>   -2.0512    1.0000 </r>
        <r>    6.7470    0.0000 </r>
        <r>    8.2018    0.0000 </r>
        <r>    8.3340    0.0000 </r>
        <r>    9.0226    0.0000 </r>
       </set>
       <set comment="kpoint 15">
        <r>  -32.1254    1.0000 </r>
        <r>  -21.3922    1.0000 </r>
        <r>  -21.0574    1.0000 </r>
        <r>  -14.3311    1.0000 </r>
        <r>  -14.3311    1.0000 </r>
        <r>  -13.8951    1.0000 </r>
        <r>   -3.8191    1.0000 </r>
        <r>   -2.9334    1.0000 </r>
        <r>   -2.9334    1.0000 </r>
        <r>   -2.1890    1.0000 </r>
        <r>   -2.1890    1.0000 </r>
        <r>   -2.0433    1.0000 </r>
        <r>    6.1881    0.0000 </r>
        <r>    8.1365    0.0000 </r>
        <r>    9.2681    0.0000 </r>
        <r>   10.0125    0.0000 </r>
       </set>
       <set comment="kpoint 16">
        <r>  -32.1224    1.0000 </r>
        <r>  -21.3679    1.0000 </r>
        <r>  -21.1003    1.0000 </r>
        <r>  -14.3278    1.0000 </r>
        <r>  -14.3063    1.0000 </r>
        <r>  -13.9217    1.0000 </r>
        <r>   -3.8077    1.0000 </r>
        <r>   -2.9296    1.0000 </r>
        <r>   -2.8544    1.0000 </r>
        <r>   -2.2934    1.0000 </r>
        <r>   -2.2052    1.0000 </r>
        <r>   -1.9710    1.0000 </r>
        <r>    6.2203    0.0000 </r>
        <r>    8.0973    0.0000 </r>
        <r>    9.1132    0.0000 </r>
        <r>    9.6793    0.0000 </r>
       </set>
       <set comment="kpoint 17">
        <r>  -32.1426    1.0000 </r>
        <r>  -21.3222    1.0000 </r>
        <r>  -21.0510    1.0000 </r>
        <r>  -14.2609    1.0000 </r>
        <r>  -14.2269    1.0000 </r>
        <r>  -14.0496    1.0000 </r>
        <r>   -3.2711    1.0000 </r>
        <r>   -3.1642    1.0000 </r>
        <r>   -3.0779    1.0000 </r>
        <r>   -2.5844    1.0000 </r>
        <r>   -2.3078    1.0000 </r>
        <r>   -2.0570    1.0000 </r>
        <r>    6.6456    0.0000 </r>
        <r>    7.9961    0.0000 </r>
        <r>    8.4666    0.0000 </r>
        <r>    9.0021    0.0000 </r>
       </set>
       <set comment="kpoint 18">
        <r>  -32.1303    1.0000 </r>
        <r>  -21.2790    1.0000 </r>
        <r>  -21.1587    1.0000 </r>
        <r>  -14.2891    1.0000 </r>
        <r>  -14.1732    1.0000 </r>
        <r>  -14.0801    1.0000 </r>
        <r>   -3.3236    1.0000 </r>
        <r>   -3.2255    1.0000 </r>
        <r>   -2.8389    1.0000 </r>
        <r>   -2.4755    1.0000 </r>
        <r>   -2.2836    1.0000 </r>
        <r>   -2.1243    1.0000 </r>
        <r>    6.7068    0.0000 </r>
        <r>    8.3620    0.0000 </r>
        <r>    8.4234    0.0000 </r>
        <r>    8.8673    0.0000 </r>
       </set>
       <set comment="kpoint 19">
        <r>  -32.1248    1.0000 </r>
        <r>  -21.3370    1.0000 </r>
        <r>  -21.1223    1.0000 </r>
        <r>  -14.3321    1.0000 </r>
        <r>  -14.2455    1.0000 </r>
        <r>  -13.9738    1.0000 </r>
        <r>   -3.6607    1.0000 </r>
        <r>   -3.0836    1.0000 </r>
        <r>   -2.8156    1.0000 </r>
        <r>   -2.3430    1.0000 </r>
        <r>   -2.1591    1.0000 </r>
        <r>   -2.0660    1.0000 </r>
        <r>    6.3618    0.0000 </r>
        <r>    8.3089    0.0000 </r>
        <r>    8.8585    0.0000 </r>
        <r>    9.1262    0.0000 </r>
       </set>
       <set comment="kpoint 20">
        <r>  -32.1234    1.0000 </r>
        <r>  -21.2618    1.0000 </r>
        <r>  -21.2088    1.0000 </r>
        <r>  -14.3295    1.0000 </r>
        <r>  -14.1573    1.0000 </r>
        <r>  -14.0615    1.0000 </r>
        <r>   -3.5427    1.0000 </r>
        <r>   -3.1881    1.0000 </r>
        <r>   -2.6522    1.0000 </r>
        <r>   -2.5342    1.0000 </r>
        <r>   -2.1600    1.0000 </r>
        <r>   -2.0432    1.0000 </r>
        <r>    6.4691    0.0000 </r>
        <r>    8.4327    0.0000 </r>
        <r>    8.6083    0.0000 </r>
        <r>    8.8510    0.0000 </r>
       </set>
      </set>
     </set>
    </array>
   </eigenvalues>
   <array>
    <dimension dim="1">ion</dimension>
    <dimension dim="2">band</dimension>
    <dimension dim="3">kpoint</dimension>
    <dimension dim="4">spin</dimension>
    <field>  s</field>
    <field> py</field>
    <field> pz</field>
    <field> px</field>
    <field>dxy</field>
    <field>dyz</field>
    <field>dz2</field>
    <field>dxz</field>
    <field>dx2</field>
    <set>
     <set comment="spin1">
      <set comment="kpoint 1">
       <set comment="band 1">
        <r>  0.9689  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0139  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4201  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4201  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4396  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4396  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.3167  0.3167  0.3167  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0006  0.0006  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0006  0.0006  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4610  0.1376  0.3516  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0009  0.0003  0.0007  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0009  0.0003  0.0007  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.1724  0.4958  0.2819  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0003  0.0010  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0003  0.0010  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0157  0.0157  0.0000  0.0155  0.0000 </r>
        <r>  0.0000  0.1099  0.1112  0.1110  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1099  0.1112  0.1110  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0273  0.0035  0.0000  0.0162  0.0000 </r>
        <r>  0.0000  0.1146  0.1931  0.0244  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1146  0.1931  0.0244  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0039  0.0278  0.0000  0.0152  0.0000 </r>
        <r>  0.0000  0.1076  0.0278  0.1967  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1076  0.0278  0.1967  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0038  0.0038  0.0038  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1319  0.1319  0.1319  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1319  0.1319  0.1319  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0059  0.0023  0.0033  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.2030  0.0781  0.1145  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.2030  0.0781  0.1145  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0018  0.0054  0.0043  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0607  0.1856  0.1492  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0607  0.1856  0.1492  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.1203  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0437  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0437  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.5468  0.0000  0.0338 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0338  0.0000  0.5468 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0000  0.0000  0.1358  0.2436  0.0000  0.2206  0.0000 </r>
        <r>  0.0000  0.0339  0.0209  0.0375  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0339  0.0209  0.0375  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 2">
       <set comment="band 1">
        <r>  0.9702  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0119  0.0015  0.0015  0.0015  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4185  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4185  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0001  0.0001  0.0001  0.0002  0.0002  0.0000  0.0002  0.0000 </r>
        <r>  0.4385  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4385  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.1581  0.1581  0.6322  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0004  0.0004  0.0015  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0004  0.0004  0.0015  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4742  0.4742  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0011  0.0011  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0011  0.0011  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.3141  0.3141  0.3141  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0034  0.0007  0.0007  0.0007  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0034  0.0007  0.0007  0.0007  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0002  0.0002  0.0009  0.0074  0.0296  0.0000  0.0074  0.0001 </r>
        <r>  0.0000  0.0558  0.0558  0.2232  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0558  0.0558  0.2232  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0007  0.0007  0.0000  0.0222  0.0000  0.0001  0.0222  0.0000 </r>
        <r>  0.0000  0.1674  0.1674  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1674  0.1674  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0021  0.0021  0.0021  0.0130  0.0130  0.0000  0.0130  0.0000 </r>
        <r>  0.0003  0.1122  0.1122  0.1123  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.1122  0.1122  0.1123  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0052  0.0026  0.0026  0.0026  0.0001  0.0001  0.0000  0.0001  0.0000 </r>
        <r>  0.0010  0.1278  0.1278  0.1278  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0010  0.1278  0.1278  0.1278  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0022  0.0022  0.0087  0.0000  0.0001  0.0003  0.0000  0.0010 </r>
        <r>  0.0000  0.0653  0.0653  0.2611  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0653  0.0653  0.2611  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0066  0.0066  0.0000  0.0001  0.0000  0.0010  0.0001  0.0003 </r>
        <r>  0.0000  0.1959  0.1958  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1959  0.1958  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.1100  0.0035  0.0035  0.0035  0.0005  0.0005  0.0000  0.0005  0.0000 </r>
        <r>  0.0398  0.0051  0.0051  0.0051  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0398  0.0051  0.0051  0.0051  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0001  0.0000  0.0002  0.0000  0.0000  0.0997  0.0000  0.4685 </r>
        <r>  0.0000  0.0014  0.0007  0.0038  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0014  0.0007  0.0038  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0001  0.0002  0.0000  0.0000  0.0000  0.4685  0.0000  0.0997 </r>
        <r>  0.0000  0.0025  0.0033  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0025  0.0033  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0003  0.0000  0.0000  0.0000  0.1985  0.1992  0.0000  0.1996  0.0000 </r>
        <r>  0.0037  0.0265  0.0263  0.0264  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0037  0.0265  0.0263  0.0264  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 3">
       <set comment="band 1">
        <r>  0.9732  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0071  0.0045  0.0045  0.0045  0.0001  0.0001  0.0000  0.0001  0.0000 </r>
        <r>  0.4164  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4164  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0004  0.0006  0.0006  0.0006  0.0006  0.0006  0.0000  0.0006  0.0000 </r>
        <r>  0.4345  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4345  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.1574  0.1574  0.6296  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0005  0.0005  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0005  0.0005  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4722  0.4722  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0014  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0014  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.3082  0.3082  0.3083  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0114  0.0008  0.0008  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0114  0.0008  0.0008  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0005  0.0005  0.0020  0.0064  0.0257  0.0004  0.0064  0.0011 </r>
        <r>  0.0000  0.0569  0.0569  0.2275  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0569  0.0569  0.2275  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0015  0.0015  0.0000  0.0192  0.0000  0.0011  0.0192  0.0004 </r>
        <r>  0.0000  0.1706  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1706  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0002  0.0069  0.0069  0.0069  0.0065  0.0065  0.0000  0.0065  0.0000 </r>
        <r>  0.0008  0.1159  0.1159  0.1159  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.1159  0.1159  0.1159  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0137  0.0005  0.0005  0.0005  0.0004  0.0004  0.0000  0.0004  0.0000 </r>
        <r>  0.0018  0.1222  0.1222  0.1222  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0018  0.1222  0.1222  0.1222  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0031  0.0031  0.0122  0.0000  0.0002  0.0007  0.0000  0.0021 </r>
        <r>  0.0000  0.0640  0.0640  0.2559  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0640  0.0640  0.2559  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0092  0.0092  0.0000  0.0001  0.0000  0.0021  0.0001  0.0007 </r>
        <r>  0.0000  0.1919  0.1919  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1919  0.1919  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0804  0.0105  0.0105  0.0105  0.0095  0.0095  0.0000  0.0095  0.0000 </r>
        <r>  0.0317  0.0117  0.0117  0.0117  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0317  0.0117  0.0117  0.0117  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0001  0.0001  0.0003  0.0000  0.0000  0.1370  0.0000  0.4097 </r>
        <r>  0.0000  0.0030  0.0030  0.0120  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0030  0.0030  0.0120  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0002  0.0002  0.0000  0.0000  0.0000  0.4097  0.0000  0.1370 </r>
        <r>  0.0000  0.0090  0.0090  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0090  0.0090  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0001  0.0031  0.0031  0.0031  0.1729  0.1729  0.0000  0.1729  0.0000 </r>
        <r>  0.0116  0.0203  0.0203  0.0203  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0116  0.0203  0.0203  0.0203  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 4">
       <set comment="band 1">
        <r>  0.9756  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0014  0.0075  0.0075  0.0075  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4155  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4155  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0026  0.0004  0.0004  0.0004  0.0009  0.0009  0.0000  0.0009  0.0000 </r>
        <r>  0.4300  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4300  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.1569  0.1569  0.6276  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0006  0.0006  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0006  0.0006  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4707  0.4707  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0017  0.0017  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0017  0.0017  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.3037  0.3037  0.3037  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0183  0.0009  0.0009  0.0009  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0183  0.0009  0.0009  0.0009  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0001  0.0001  0.0006  0.0056  0.0225  0.0013  0.0056  0.0039 </r>
        <r>  0.0000  0.0577  0.0578  0.2310  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0577  0.0578  0.2310  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0004  0.0004  0.0000  0.0169  0.0000  0.0039  0.0169  0.0013 </r>
        <r>  0.0000  0.1733  0.1732  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1733  0.1732  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0183  0.0010  0.0010  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0017  0.1198  0.1198  0.1198  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0017  0.1198  0.1198  0.1198  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0009  0.0092  0.0092  0.0092  0.0010  0.0010  0.0000  0.0010  0.0000 </r>
        <r>  0.0007  0.1191  0.1191  0.1191  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.1191  0.1191  0.1191  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0043  0.0043  0.0174  0.0000  0.0001  0.0002  0.0000  0.0006 </r>
        <r>  0.0000  0.0631  0.0631  0.2522  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0631  0.0631  0.2522  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0130  0.0130  0.0000  0.0000  0.0000  0.0006  0.0000  0.0002 </r>
        <r>  0.0000  0.1892  0.1892  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1892  0.1892  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0436  0.0118  0.0118  0.0118  0.0486  0.0486  0.0000  0.0486  0.0000 </r>
        <r>  0.0255  0.0118  0.0118  0.0118  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0255  0.0118  0.0118  0.0118  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0001  0.1328  0.0000  0.4017 </r>
        <r>  0.0000  0.0045  0.0044  0.0178  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0045  0.0044  0.0178  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.4017  0.0000  0.1328 </r>
        <r>  0.0000  0.0133  0.0134  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0133  0.0134  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0079  0.0127  0.0127  0.0127  0.0833  0.0833  0.0000  0.0833  0.0000 </r>
        <r>  0.0170  0.0155  0.0155  0.0155  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0170  0.0155  0.0155  0.0155  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 5">
       <set comment="band 1">
        <r>  0.9706  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0018  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0018  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0112  0.0000  0.0061  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4179  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4179  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0008  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4384  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4384  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4728  0.0000  0.4728  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0013  0.0000  0.0013  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0013  0.0000  0.0013  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4728  0.0000  0.4728  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0013  0.0000  0.0013  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0013  0.0000  0.0013  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.0000  0.9441  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0044  0.0000  0.0016  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0044  0.0000  0.0016  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0032  0.0000  0.0032  0.0000  0.0206  0.0000  0.0206  0.0000 </r>
        <r>  0.0000  0.1672  0.0000  0.1672  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1672  0.0000  0.1672  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0032  0.0000  0.0032  0.0000  0.0206  0.0000  0.0206  0.0000 </r>
        <r>  0.0000  0.1672  0.0000  0.1672  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1672  0.0000  0.1672  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0408  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.0000  0.3419  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.0000  0.3419  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0064  0.0000  0.0083  0.0000  0.0000  0.0000  0.0038  0.0000  0.0000 </r>
        <r>  0.0011  0.0000  0.3690  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0011  0.0000  0.3690  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0062  0.0000  0.0062  0.0000  0.0004  0.0000  0.0004  0.0000 </r>
        <r>  0.0000  0.1981  0.0000  0.1982  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1982  0.0000  0.1982  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0062  0.0000  0.0062  0.0000  0.0004  0.0000  0.0004  0.0000 </r>
        <r>  0.0000  0.1982  0.0000  0.1981  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1982  0.0000  0.1982  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.1059  0.0000  0.0142  0.0000  0.0000  0.0000  0.0014  0.0000  0.0000 </r>
        <r>  0.0384  0.0000  0.0211  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0384  0.0000  0.0211  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0041  0.0000  0.0002  0.0000  0.0000  0.0000  0.5300  0.0000  0.0000 </r>
        <r>  0.0009  0.0000  0.0114  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0009  0.0000  0.0114  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.5940 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0000  0.0000  0.5826  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0051  0.0000  0.0794  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0051  0.0000  0.0794  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 6">
       <set comment="band 1">
        <r>  0.9730  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0076  0.0010  0.0113  0.0010  0.0000  0.0001  0.0000  0.0001  0.0000 </r>
        <r>  0.4160  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4160  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0001  0.0006  0.0000  0.0006  0.0015  0.0001  0.0000  0.0001  0.0000 </r>
        <r>  0.4354  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4354  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4705  0.0000  0.4705  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0017  0.0000  0.0017  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0017  0.0000  0.0017  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4452  0.0494  0.4452  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0012  0.0008  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0012  0.0008  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.0233  0.8873  0.0233  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0096  0.0004  0.0009  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0096  0.0004  0.0009  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0059  0.0000  0.0059  0.0000  0.0172  0.0000  0.0172  0.0007 </r>
        <r>  0.0000  0.1693  0.0000  0.1693  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1693  0.0000  0.1693  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0050  0.0020  0.0050  0.0046  0.0148  0.0006  0.0148  0.0000 </r>
        <r>  0.0000  0.1492  0.0401  0.1492  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1492  0.0401  0.1492  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0001  0.0025  0.0005  0.0025  0.0269  0.0005  0.0000  0.0005  0.0000 </r>
        <r>  0.0008  0.0189  0.3169  0.0189  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.0189  0.3169  0.0189  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0120  0.0001  0.0054  0.0001  0.0002  0.0000  0.0053  0.0000  0.0000 </r>
        <r>  0.0015  0.0116  0.3283  0.0116  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0015  0.0116  0.3283  0.0116  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0009  0.0056  0.0024  0.0056  0.0002  0.0008  0.0011  0.0008  0.0000 </r>
        <r>  0.0001  0.1850  0.0211  0.1850  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.1850  0.0211  0.1850  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0072  0.0000  0.0072  0.0000  0.0010  0.0000  0.0010  0.0006 </r>
        <r>  0.0000  0.1966  0.0000  0.1966  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1966  0.0000  0.1966  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0727  0.0024  0.0263  0.0024  0.0005  0.0050  0.0267  0.0050  0.0000 </r>
        <r>  0.0285  0.0022  0.0394  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0285  0.0022  0.0394  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0213  0.0003  0.0011  0.0003  0.0005  0.0016  0.4615  0.0016  0.0000 </r>
        <r>  0.0054  0.0024  0.0097  0.0024  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0054  0.0024  0.0097  0.0024  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0001  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.5902 </r>
        <r>  0.0000  0.0033  0.0000  0.0033  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0033  0.0000  0.0033  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0001  0.0007  0.0003  0.0007  0.5184  0.0227  0.0010  0.0227  0.0000 </r>
        <r>  0.0115  0.0032  0.0520  0.0033  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0115  0.0032  0.0520  0.0032  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 7">
       <set comment="band 1">
        <r>  0.9756  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0006  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0006  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0029  0.0031  0.0136  0.0031  0.0000  0.0002  0.0000  0.0002  0.0000 </r>
        <r>  0.4157  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4157  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0010  0.0021  0.0000  0.0021  0.0017  0.0004  0.0000  0.0004  0.0000 </r>
        <r>  0.4299  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4299  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4691  0.0000  0.4692  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.3679  0.1996  0.3678  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0030  0.0006  0.0021  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0030  0.0006  0.0021  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.0946  0.7301  0.0946  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0152  0.0011  0.0001  0.0011  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0152  0.0011  0.0001  0.0011  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0018  0.0071  0.0007  0.0071  0.0085  0.0066  0.0062  0.0066  0.0000 </r>
        <r>  0.0002  0.0634  0.2107  0.0634  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0634  0.2107  0.0634  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0062  0.0000  0.0062  0.0000  0.0139  0.0000  0.0140  0.0034 </r>
        <r>  0.0000  0.1724  0.0000  0.1724  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1724  0.0000  0.1724  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0154  0.0004  0.0057  0.0004  0.0013  0.0009  0.0008  0.0009  0.0000 </r>
        <r>  0.0011  0.1027  0.1445  0.1027  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0011  0.1027  0.1445  0.1027  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0051  0.0021  0.0051  0.0118  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.0474  0.2745  0.0474  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.0474  0.2745  0.0474  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0095  0.0000  0.0095  0.0000  0.0019  0.0000  0.0019  0.0003 </r>
        <r>  0.0000  0.1925  0.0000  0.1925  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1925  0.0000  0.1925  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0015  0.0038  0.0104  0.0038  0.0000  0.0014  0.0015  0.0014  0.0000 </r>
        <r>  0.0002  0.1500  0.0839  0.1500  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.1500  0.0839  0.1500  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0151  0.0037  0.0173  0.0037  0.0008  0.0139  0.1859  0.0139  0.0000 </r>
        <r>  0.0099  0.0022  0.0457  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0099  0.0022  0.0457  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0424  0.0008  0.0116  0.0008  0.0448  0.0548  0.2178  0.0548  0.0000 </r>
        <r>  0.0203  0.0089  0.0004  0.0089  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0203  0.0089  0.0004  0.0089  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0001  0.0000  0.0001  0.0000  0.0001  0.0000  0.0001  0.5639 </r>
        <r>  0.0000  0.0098  0.0000  0.0098  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0098  0.0000  0.0098  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0003  0.0091  0.0067  0.0091  0.3726  0.0086  0.0564  0.0086  0.0000 </r>
        <r>  0.0151  0.0062  0.0280  0.0062  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0151  0.0062  0.0280  0.0062  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 8">
       <set comment="band 1">
        <r>  0.9764  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0002  0.0076  0.0076  0.0076  0.0004  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4166  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4166  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0026  0.0004  0.0037  0.0004  0.0009  0.0009  0.0000  0.0009  0.0000 </r>
        <r>  0.4271  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4271  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4696  0.0000  0.4696  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.2213  0.4925  0.2213  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0034  0.0005  0.0023  0.0005  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0034  0.0005  0.0023  0.0005  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.2380  0.4359  0.2380  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0174  0.0010  0.0007  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0174  0.0010  0.0007  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0035  0.0097  0.0000  0.0097  0.0120  0.0021  0.0066  0.0021  0.0000 </r>
        <r>  0.0002  0.0118  0.3125  0.0118  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0118  0.3125  0.0118  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0160  0.0008  0.0017  0.0008  0.0042  0.0005  0.0006  0.0005  0.0000 </r>
        <r>  0.0009  0.1611  0.0289  0.1611  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0009  0.1611  0.0289  0.1611  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0024  0.0000  0.0024  0.0000  0.0143  0.0000  0.0143  0.0053 </r>
        <r>  0.0000  0.1754  0.0000  0.1754  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1754  0.0000  0.1754  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0001  0.0029  0.0123  0.0029  0.0020  0.0009  0.0001  0.0009  0.0000 </r>
        <r>  0.0005  0.1337  0.1051  0.1337  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.1337  0.1051  0.1337  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0128  0.0000  0.0128  0.0000  0.0017  0.0000  0.0017  0.0006 </r>
        <r>  0.0000  0.1874  0.0000  0.1874  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1874  0.0000  0.1874  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0008  0.0030  0.0129  0.0030  0.0003  0.0020  0.0000  0.0020  0.0000 </r>
        <r>  0.0001  0.0550  0.2767  0.0550  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0550  0.2767  0.0550  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0015  0.0069  0.0040  0.0069  0.0171  0.0000  0.2652  0.0000  0.0000 </r>
        <r>  0.0036  0.0112  0.0210  0.0112  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0036  0.0112  0.0210  0.0112  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0370  0.0023  0.0024  0.0023  0.1676  0.1027  0.0263  0.1027  0.0000 </r>
        <r>  0.0289  0.0031  0.0155  0.0031  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0289  0.0031  0.0155  0.0031  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0001  0.0000  0.0001  0.5401 </r>
        <r>  0.0000  0.0135  0.0000  0.0135  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0135  0.0000  0.0135  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0001  0.0132  0.0201  0.0132  0.0527  0.0713  0.1599  0.0713  0.0000 </r>
        <r>  0.0123  0.0088  0.0195  0.0088  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0123  0.0088  0.0195  0.0088  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 9">
       <set comment="band 1">
        <r>  0.9748  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0046  0.0077  0.0012  0.0077  0.0005  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4163  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4163  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0004  0.0001  0.0047  0.0001  0.0001  0.0010  0.0000  0.0010  0.0000 </r>
        <r>  0.4311  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4311  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4715  0.0000  0.4716  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0016  0.0000  0.0016  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0016  0.0000  0.0016  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.0575  0.8216  0.0575  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0029  0.0010  0.0012  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0029  0.0010  0.0012  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.4037  0.1122  0.4037  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0133  0.0003  0.0022  0.0003  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0133  0.0003  0.0022  0.0003  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0003  0.0102  0.0000  0.0102  0.0243  0.0007  0.0038  0.0007  0.0000 </r>
        <r>  0.0000  0.0210  0.2930  0.0210  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0210  0.2930  0.0210  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0184  0.0000  0.0184  0.0012 </r>
        <r>  0.0000  0.1752  0.0000  0.1752  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1752  0.0000  0.1752  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0167  0.0004  0.0000  0.0004  0.0013  0.0000  0.0007  0.0000  0.0000 </r>
        <r>  0.0015  0.1551  0.0453  0.1551  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0015  0.1551  0.0453  0.1551  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0012  0.0148  0.0012  0.0000  0.0065  0.0000  0.0065  0.0000 </r>
        <r>  0.0008  0.1560  0.0498  0.1560  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.1560  0.0498  0.1560  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0119  0.0000  0.0119  0.0000  0.0001  0.0000  0.0001  0.0054 </r>
        <r>  0.0000  0.1857  0.0000  0.1857  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1857  0.0000  0.1857  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0003  0.0007  0.0136  0.0007  0.0001  0.0016  0.0002  0.0016  0.0000 </r>
        <r>  0.0000  0.0261  0.3416  0.0261  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0261  0.3416  0.0261  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0418  0.0168  0.0014  0.0168  0.0408  0.0033  0.0686  0.0033  0.0000 </r>
        <r>  0.0206  0.0191  0.0010  0.0191  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0206  0.0191  0.0010  0.0191  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0001  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.5297 </r>
        <r>  0.0000  0.0129  0.0000  0.0129  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0129  0.0000  0.0129  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0258  0.0020  0.0001  0.0020  0.0342  0.0094  0.4016  0.0094  0.0000 </r>
        <r>  0.0093  0.0004  0.0234  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0093  0.0004  0.0234  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0001  0.0024  0.0075  0.0024  0.0012  0.2521  0.0203  0.2521  0.0000 </r>
        <r>  0.0150  0.0154  0.0115  0.0154  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0150  0.0154  0.0115  0.0154  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 10">
       <set comment="band 1">
        <r>  0.9721  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0091  0.0050  0.0000  0.0050  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4170  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4170  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0014  0.0000  0.0000  0.0006  0.0000  0.0006  0.0000 </r>
        <r>  0.4361  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4361  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.0000  0.9417  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0011  0.0008  0.0012  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0011  0.0008  0.0012  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4736  0.0000  0.4736  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0012  0.0000  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0012  0.0000  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.4670  0.0000  0.4670  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0072  0.0002  0.0018  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0072  0.0002  0.0018  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0000  0.0060  0.0000  0.0060  0.0360  0.0000  0.0010  0.0000  0.0000 </r>
        <r>  0.0000  0.0108  0.3127  0.0108  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0108  0.3127  0.0108  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0212  0.0000  0.0212  0.0000 </r>
        <r>  0.0000  0.1706  0.0000  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1706  0.0000  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0000  0.0098  0.0000  0.0000  0.0150  0.0000  0.0150  0.0000 </r>
        <r>  0.0007  0.1626  0.0214  0.1626  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.1626  0.0214  0.1626  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0108  0.0022  0.0000  0.0022  0.0006  0.0000  0.0010  0.0000  0.0000 </r>
        <r>  0.0016  0.1717  0.0239  0.1717  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0016  0.1717  0.0239  0.1717  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0084  0.0000  0.0084  0.0000  0.0000  0.0000  0.0000  0.0047 </r>
        <r>  0.0000  0.1905  0.0000  0.1905  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1905  0.0000  0.1905  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0132  0.0000  0.0000  0.0007  0.0000  0.0007  0.0000 </r>
        <r>  0.0000  0.0117  0.3735  0.0117  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0117  0.3735  0.0117  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0912  0.0124  0.0000  0.0124  0.0093  0.0000  0.0040  0.0000  0.0000 </r>
        <r>  0.0341  0.0154  0.0006  0.0154  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0341  0.0154  0.0006  0.0154  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0002  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.5396 </r>
        <r>  0.0000  0.0087  0.0000  0.0087  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0087  0.0000  0.0087  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0060  0.0000  0.0000  0.0000  0.0009  0.0000  0.5491  0.0000  0.0000 </r>
        <r>  0.0013  0.0019  0.0045  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0013  0.0019  0.0045  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0007  0.0000  0.0000  0.2937  0.0000  0.2946  0.0000 </r>
        <r>  0.0088  0.0287  0.0061  0.0286  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0088  0.0287  0.0061  0.0286  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 11">
       <set comment="band 1">
        <r>  0.9746  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0009  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0009  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0054  0.0000  0.0193  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4136  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4136  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0025  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4353  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4353  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4678  0.0000  0.4678  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0021  0.0000  0.0021  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0021  0.0000  0.0021  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4678  0.0000  0.4678  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0021  0.0000  0.0021  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0021  0.0000  0.0021  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.0000  0.9312  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0143  0.0000  0.0009  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0143  0.0000  0.0009  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0154  0.0000  0.0034  0.0000  0.0000  0.0000  0.0104  0.0000  0.0000 </r>
        <r>  0.0013  0.0000  0.3305  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0013  0.0000  0.3305  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0113  0.0000  0.0113  0.0000  0.0130  0.0000  0.0130  0.0000 </r>
        <r>  0.0000  0.1706  0.0000  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1706  0.0000  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0113  0.0000  0.0113  0.0000  0.0130  0.0000  0.0130  0.0000 </r>
        <r>  0.0000  0.1706  0.0000  0.1705  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1706  0.0000  0.1706  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0235  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.0000  0.3698  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0008  0.0000  0.3698  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0061  0.0000  0.0061  0.0000  0.0025  0.0000  0.0025  0.0000 </r>
        <r>  0.0000  0.1978  0.0000  0.1978  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1978  0.0000  0.1978  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0061  0.0000  0.0061  0.0000  0.0025  0.0000  0.0025  0.0000 </r>
        <r>  0.0000  0.1978  0.0000  0.1978  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1978  0.0000  0.1978  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0202  0.0000  0.0236  0.0000  0.0000  0.0000  0.1784  0.0000  0.0000 </r>
        <r>  0.0105  0.0000  0.0691  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0105  0.0000  0.0691  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0784  0.0000  0.0262  0.0000  0.0000  0.0000  0.2538  0.0000  0.0000 </r>
        <r>  0.0226  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0226  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.6362 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0000  0.0000  0.5518  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0163  0.0000  0.0443  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0163  0.0000  0.0443  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 12">
       <set comment="band 1">
        <r>  0.9766  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0023  0.0003  0.0232  0.0003  0.0000  0.0001  0.0000  0.0001  0.0000 </r>
        <r>  0.4129  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4129  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0001  0.0014  0.0000  0.0014  0.0030  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4317  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4317  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4661  0.0000  0.4661  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0023  0.0000  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0023  0.0000  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4610  0.0068  0.4610  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0022  0.0020  0.0006  0.0020  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0022  0.0020  0.0006  0.0020  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.0030  0.9187  0.0030  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0177  0.0003  0.0003  0.0003  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0177  0.0003  0.0003  0.0003  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0176  0.0012  0.0013  0.0012  0.0001  0.0002  0.0113  0.0002  0.0000 </r>
        <r>  0.0007  0.0014  0.3189  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.0014  0.3189  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0011  0.0148  0.0016  0.0148  0.0020  0.0064  0.0005  0.0064  0.0000 </r>
        <r>  0.0000  0.1695  0.0060  0.1695  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1695  0.0060  0.1695  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0148  0.0000  0.0148  0.0000  0.0083  0.0000  0.0083  0.0011 </r>
        <r>  0.0000  0.1732  0.0000  0.1732  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1732  0.0000  0.1732  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0006  0.0002  0.0006  0.0110  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.0133  0.3603  0.0133  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.0133  0.3603  0.0133  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0054  0.0000  0.0054  0.0000  0.0051  0.0000  0.0051  0.0000 </r>
        <r>  0.0000  0.1953  0.0000  0.1953  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1953  0.0000  0.1953  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0004  0.0038  0.0034  0.0038  0.0000  0.0046  0.0005  0.0046  0.0000 </r>
        <r>  0.0000  0.1842  0.0229  0.1842  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1842  0.0229  0.1842  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0009  0.0003  0.0082  0.0003  0.0002  0.0014  0.2741  0.0014  0.0000 </r>
        <r>  0.0020  0.0010  0.0635  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0020  0.0010  0.0635  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0141  0.0005  0.0092  0.0005  0.4271  0.0206  0.0123  0.0206  0.0000 </r>
        <r>  0.0237  0.0007  0.0162  0.0007  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0237  0.0007  0.0162  0.0007  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0504  0.0024  0.0473  0.0024  0.1037  0.0357  0.0929  0.0357  0.0000 </r>
        <r>  0.0248  0.0026  0.0089  0.0026  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0248  0.0026  0.0089  0.0026  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0001  0.0000  0.0001  0.0000  0.0003  0.0000  0.0003  0.6297 </r>
        <r>  0.0000  0.0039  0.0000  0.0039  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0039  0.0000  0.0039  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 13">
       <set comment="band 1">
        <r>  0.9776  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0003  0.0008  0.0203  0.0008  0.0000  0.0005  0.0000  0.0005  0.0000 </r>
        <r>  0.4165  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4165  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0006  0.0046  0.0003  0.0046  0.0024  0.0001  0.0000  0.0001  0.0000 </r>
        <r>  0.4252  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4252  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4667  0.0000  0.4667  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0023  0.0000  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0023  0.0000  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4514  0.0180  0.4514  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0074  0.0012  0.0018  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0074  0.0012  0.0018  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0083  0.9056  0.0083  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0162  0.0008  0.0001  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0162  0.0008  0.0001  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0168  0.0046  0.0002  0.0046  0.0009  0.0001  0.0085  0.0001  0.0000 </r>
        <r>  0.0003  0.0043  0.3162  0.0043  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.0043  0.3162  0.0043  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0044  0.0144  0.0008  0.0144  0.0062  0.0010  0.0026  0.0010  0.0000 </r>
        <r>  0.0001  0.1676  0.0078  0.1676  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.1676  0.0078  0.1676  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0150  0.0000  0.0150  0.0000  0.0048  0.0000  0.0048  0.0037 </r>
        <r>  0.0000  0.1764  0.0000  0.1764  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1764  0.0000  0.1764  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0046  0.0000  0.0046  0.0000  0.0087  0.0000  0.0087  0.0001 </r>
        <r>  0.0000  0.1895  0.0000  0.1895  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1895  0.0000  0.1895  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0002  0.0000  0.0139  0.0000  0.0008  0.0013  0.0002  0.0013  0.0000 </r>
        <r>  0.0002  0.1868  0.0151  0.1868  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.1868  0.0151  0.1868  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0001  0.0012  0.0016  0.0012  0.0012  0.0039  0.0000  0.0039  0.0000 </r>
        <r>  0.0001  0.0079  0.3805  0.0079  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0079  0.3805  0.0079  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0002  0.0015  0.0015  0.0015  0.0084  0.0005  0.2827  0.0005  0.0000 </r>
        <r>  0.0011  0.0059  0.0452  0.0059  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0011  0.0059  0.0452  0.0059  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0094  0.0059  0.0020  0.0059  0.4236  0.0220  0.0115  0.0220  0.0000 </r>
        <r>  0.0252  0.0002  0.0109  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0252  0.0002  0.0109  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0001  0.0000  0.0001  0.0000  0.0001  0.0000  0.0001  0.5826 </r>
        <r>  0.0000  0.0100  0.0000  0.0100  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0100  0.0000  0.0100  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0059  0.0022  0.0368  0.0022  0.0390  0.1925  0.0291  0.1925  0.0000 </r>
        <r>  0.0209  0.0022  0.0078  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0209  0.0022  0.0078  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 14">
       <set comment="band 1">
        <r>  0.9768  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0021  0.0080  0.0000  0.0080  0.0014  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4189  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4189  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0130  0.0000  0.0000  0.0009  0.0000  0.0009  0.0000 </r>
        <r>  0.4241  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4241  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4690  0.0000  0.4690  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4585  0.0000  0.4585  0.0002  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0119  0.0004  0.0028  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0119  0.0004  0.0028  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0000  0.9272  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0099  0.0012  0.0003  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0099  0.0012  0.0003  0.0012  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0081  0.0123  0.0000  0.0123  0.0077  0.0000  0.0060  0.0000  0.0000 </r>
        <r>  0.0003  0.0001  0.3299  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.0001  0.3299  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0126  0.0045  0.0000  0.0045  0.0075  0.0000  0.0020  0.0000  0.0000 </r>
        <r>  0.0006  0.1721  0.0006  0.1721  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0006  0.1721  0.0006  0.1721  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0159  0.0000  0.0159  0.0000 </r>
        <r>  0.0000  0.1824  0.0000  0.1824  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1824  0.0000  0.1824  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0159  0.0000  0.0159  0.0000  0.0000  0.0000  0.0000  0.0062 </r>
        <r>  0.0000  0.1801  0.0000  0.1801  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1801  0.0000  0.1801  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0000  0.0166  0.0000  0.0000  0.0011  0.0000  0.0011  0.0000 </r>
        <r>  0.0005  0.1616  0.0572  0.1616  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.1616  0.0572  0.1616  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0095  0.0000  0.0000  0.0043  0.0000  0.0043  0.0000 </r>
        <r>  0.0000  0.0287  0.3398  0.0287  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0287  0.3398  0.0287  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0049  0.0073  0.0000  0.0073  0.0341  0.0000  0.2295  0.0000  0.0000 </r>
        <r>  0.0055  0.0130  0.0163  0.0130  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0055  0.0130  0.0163  0.0130  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.5430 </r>
        <r>  0.0000  0.0132  0.0000  0.0132  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0132  0.0000  0.0132  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0271  0.0111  0.0000  0.0111  0.2557  0.0000  0.1332  0.0000  0.0000 </r>
        <r>  0.0211  0.0001  0.0289  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0211  0.0001  0.0289  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0183  0.0000  0.0000  0.2683  0.0000  0.2683  0.0000 </r>
        <r>  0.0202  0.0043  0.0099  0.0043  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0202  0.0043  0.0099  0.0043  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 15">
       <set comment="band 1">
        <r>  0.9778  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0007  0.0000  0.0294  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4102  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4102  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0038  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4332  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4332  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4638  0.0000  0.4642  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0027  0.0000  0.0027  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0027  0.0000  0.0027  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4642  0.0000  0.4639  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0027  0.0000  0.0027  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0027  0.0000  0.0027  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0000  0.9219  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0221  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0221  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0201  0.0000  0.0004  0.0000  0.0000  0.0000  0.0144  0.0000  0.0000 </r>
        <r>  0.0002  0.0000  0.3103  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0000  0.3103  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0000  0.0216  0.0000  0.0216  0.0000  0.0027  0.0000  0.0027  0.0000 </r>
        <r>  0.0000  0.1747  0.0000  0.1746  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1747  0.0000  0.1746  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0216  0.0000  0.0216  0.0000  0.0027  0.0000  0.0027  0.0000 </r>
        <r>  0.0000  0.1746  0.0000  0.1747  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1746  0.0000  0.1746  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0086  0.0000  0.0086  0.0000 </r>
        <r>  0.0000  0.1958  0.0000  0.1958  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1958  0.0000  0.1958  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0019  0.0000  0.0019  0.0000  0.0086  0.0000  0.0086  0.0000 </r>
        <r>  0.0000  0.1958  0.0000  0.1958  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1958  0.0000  0.1958  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0036  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0000  0.4014  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0000  0.4014  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0003  0.0000  0.0019  0.0000  0.0000  0.0000  0.2910  0.0000  0.0000 </r>
        <r>  0.0002  0.0000  0.0672  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0000  0.0672  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0000  0.0000  0.0000  0.5377  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0252  0.0000  0.0066  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0252  0.0000  0.0066  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.6935 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0634  0.0000  0.1310  0.0000  0.0000  0.0000  0.0533  0.0000  0.0000 </r>
        <r>  0.0323  0.0000  0.0097  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0323  0.0000  0.0097  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 16">
       <set comment="band 1">
        <r>  0.9782  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0000  0.0000  0.0284  0.0000  0.0000  0.0002  0.0000  0.0002  0.0000 </r>
        <r>  0.4116  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4116  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0017  0.0000  0.0017  0.0036  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4302  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4302  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.4642  0.0000  0.4642  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0026  0.0000  0.0026  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0026  0.0000  0.0026  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.4620  0.0000  0.4620  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0026  0.0023  0.0005  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0026  0.0023  0.0005  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0000  0.9210  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0214  0.0002  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0214  0.0002  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0200  0.0012  0.0000  0.0012  0.0000  0.0000  0.0131  0.0000  0.0000 </r>
        <r>  0.0000  0.0017  0.3089  0.0017  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0017  0.3089  0.0017  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0012  0.0223  0.0000  0.0223  0.0018  0.0000  0.0011  0.0000  0.0000 </r>
        <r>  0.0000  0.1726  0.0024  0.1726  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1726  0.0024  0.1726  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0233  0.0000  0.0233  0.0000  0.0000  0.0000  0.0000  0.0011 </r>
        <r>  0.0000  0.1758  0.0000  0.1758  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1758  0.0000  0.1758  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0114  0.0000  0.0114  0.0000 </r>
        <r>  0.0000  0.1936  0.0000  0.1936  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1936  0.0000  0.1936  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0000  0.0049  0.0000  0.0000  0.0087  0.0000  0.0087  0.0000 </r>
        <r>  0.0000  0.1916  0.0073  0.1916  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.1916  0.0073  0.1916  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0004  0.0000  0.0004  0.0000 </r>
        <r>  0.0000  0.0039  0.3981  0.0039  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0039  0.3981  0.0039  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0005  0.0001  0.0000  0.0001  0.0010  0.0000  0.2913  0.0000  0.0000 </r>
        <r>  0.0001  0.0019  0.0619  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0019  0.0619  0.0019  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0003  0.0023  0.0000  0.0023  0.5264  0.0000  0.0015  0.0000  0.0000 </r>
        <r>  0.0259  0.0000  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0259  0.0000  0.0008  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0002  0.0000  0.0002  0.0000  0.0000  0.0000  0.0000  0.6573 </r>
        <r>  0.0000  0.0039  0.0000  0.0039  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0039  0.0000  0.0039  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0582  0.0000  0.0000  0.2399  0.0000  0.2399  0.0000 </r>
        <r>  0.0190  0.0022  0.0017  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0190  0.0022  0.0017  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 17">
       <set comment="band 1">
        <r>  0.9753  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0044  0.0024  0.0160  0.0000  0.0000  0.0004  0.0000  0.0000  0.0000 </r>
        <r>  0.4150  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4150  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0000  0.0043  0.0020  0.0000  0.0000  0.0003  0.0000 </r>
        <r>  0.4316  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4316  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.8999  0.0360  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0008  0.0009  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0008  0.0009  0.0023  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.0000  0.0000  0.9330  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0033  0.0027  0.0004  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0033  0.0027  0.0004  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0001  0.0330  0.8939  0.0000  0.0000  0.0001  0.0000  0.0000  0.0000 </r>
        <r>  0.0132  0.0004  0.0004  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0132  0.0004  0.0004  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0001  0.0231  0.0029  0.0000  0.0000  0.0218  0.0025  0.0000  0.0016 </r>
        <r>  0.0000  0.0257  0.0471  0.2611  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0257  0.0471  0.2611  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0164  0.0000  0.0043  0.0000  0.0000  0.0002  0.0052  0.0000  0.0001 </r>
        <r>  0.0012  0.0035  0.2751  0.0618  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0012  0.0035  0.2751  0.0618  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0000  0.0000  0.0130  0.0058  0.0000  0.0000  0.0232  0.0000 </r>
        <r>  0.0000  0.2987  0.0354  0.0149  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.2987  0.0354  0.0149  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0000  0.0000  0.0066  0.0162  0.0000  0.0000  0.0003  0.0000 </r>
        <r>  0.0007  0.0238  0.3201  0.0276  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0007  0.0238  0.3201  0.0276  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0011  0.0111  0.0055  0.0000  0.0000  0.0037  0.0018  0.0000  0.0006 </r>
        <r>  0.0001  0.3498  0.0153  0.0164  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.3498  0.0153  0.0164  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0000  0.0125  0.0006  0.0000  0.0000  0.0050  0.0000 </r>
        <r>  0.0000  0.0291  0.0154  0.3519  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0291  0.0154  0.3519  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0176  0.0040  0.0202  0.0000  0.0000  0.0179  0.1667  0.0000  0.0104 </r>
        <r>  0.0104  0.0017  0.0536  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0104  0.0017  0.0536  0.0010  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0508  0.0042  0.0183  0.0000  0.0000  0.0486  0.2733  0.0000  0.0096 </r>
        <r>  0.0179  0.0055  0.0005  0.0061  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0179  0.0055  0.0005  0.0061  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0060  0.0000  0.0016  0.0000  0.0000  0.0103  0.0016  0.0000  0.5467 </r>
        <r>  0.0020  0.0042  0.0014  0.0118  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0020  0.0042  0.0014  0.0118  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0000  0.0043  0.5040  0.0000  0.0000  0.0488  0.0000 </r>
        <r>  0.0172  0.0010  0.0309  0.0046  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0172  0.0010  0.0309  0.0046  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 18">
       <set comment="band 1">
        <r>  0.9771  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.0000  0.0001  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0003  0.0000  0.0001  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0012  0.0029  0.0154  0.0013  0.0000  0.0010  0.0000  0.0000  0.0000 </r>
        <r>  0.4173  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4173  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0006  0.0003  0.0003  0.0094  0.0018  0.0002  0.0000  0.0003  0.0000 </r>
        <r>  0.4253  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4253  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.8708  0.0353  0.0261  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0007  0.0016  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0007  0.0016  0.0022  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.0100  0.0800  0.8383  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0074  0.0022  0.0008  0.0003  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0074  0.0022  0.0008  0.0003  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0471  0.8103  0.0625  0.0000  0.0001  0.0000  0.0000  0.0000 </r>
        <r>  0.0145  0.0015  0.0000  0.0009  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0145  0.0015  0.0000  0.0009  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0192  0.0004  0.0018  0.0009  0.0002  0.0000  0.0028  0.0002  0.0007 </r>
        <r>  0.0006  0.0043  0.2389  0.0953  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0006  0.0043  0.2389  0.0953  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0001  0.0318  0.0036  0.0004  0.0017  0.0098  0.0052  0.0000  0.0031 </r>
        <r>  0.0000  0.0172  0.0803  0.2322  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0172  0.0803  0.2322  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0007  0.0000  0.0004  0.0112  0.0073  0.0016  0.0003  0.0141  0.0008 </r>
        <r>  0.0000  0.3138  0.0317  0.0133  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.3138  0.0317  0.0133  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0005  0.0070  0.0134  0.0038  0.0001  0.0044  0.0013  0.0000  0.0002 </r>
        <r>  0.0001  0.3505  0.0143  0.0081  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.3505  0.0143  0.0081  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0013  0.0000  0.0056  0.0051  0.0010  0.0000  0.0002  0.0000 </r>
        <r>  0.0004  0.0163  0.3128  0.0576  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0163  0.3128  0.0576  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0002  0.0001  0.0027  0.0084  0.0009  0.0000  0.0001  0.0084  0.0000 </r>
        <r>  0.0000  0.0301  0.0408  0.3221  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0301  0.0408  0.3221  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0010  0.0026  0.0062  0.0008  0.0009  0.0123  0.2226  0.0003  0.0453 </r>
        <r>  0.0024  0.0013  0.0381  0.0144  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0024  0.0013  0.0381  0.0144  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0144  0.0014  0.0109  0.0011  0.0542  0.1072  0.1307  0.0239  0.1717 </r>
        <r>  0.0137  0.0067  0.0009  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0137  0.0067  0.0009  0.0002  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0117  0.0002  0.0062  0.0018  0.0846  0.0921  0.0156  0.0228  0.2753 </r>
        <r>  0.0128  0.0026  0.0072  0.0177  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0128  0.0026  0.0072  0.0177  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0020  0.0049  0.0106  0.0127  0.3158  0.0884  0.0325  0.0106  0.0248 </r>
        <r>  0.0182  0.0000  0.0121  0.0114  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0182  0.0000  0.0121  0.0114  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 19">
       <set comment="band 1">
        <r>  0.9779  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0006  0.0003  0.0246  0.0000  0.0000  0.0007  0.0000  0.0000  0.0000 </r>
        <r>  0.4138  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4138  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0000  0.0000  0.0000  0.0064  0.0031  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4283  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4283  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.9248  0.0025  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0001  0.0010  0.0042  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0001  0.0010  0.0042  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.0000  0.0000  0.9260  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0048  0.0042  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0048  0.0042  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0022  0.9197  0.0000  0.0000  0.0001  0.0000  0.0000  0.0000 </r>
        <r>  0.0187  0.0009  0.0001  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0187  0.0009  0.0001  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0194  0.0034  0.0003  0.0000  0.0000  0.0001  0.0104  0.0000  0.0000 </r>
        <r>  0.0002  0.0007  0.3075  0.0113  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0007  0.3075  0.0113  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0016  0.0413  0.0010  0.0000  0.0000  0.0039  0.0022  0.0000  0.0021 </r>
        <r>  0.0000  0.0067  0.0083  0.3238  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0067  0.0083  0.3238  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0000  0.0000  0.0000  0.0343  0.0036  0.0000  0.0000  0.0052  0.0000 </r>
        <r>  0.0000  0.3417  0.0049  0.0095  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.3417  0.0049  0.0095  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0002  0.0028  0.0087  0.0000  0.0000  0.0140  0.0003  0.0000  0.0000 </r>
        <r>  0.0000  0.3746  0.0016  0.0061  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.3746  0.0016  0.0061  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0000  0.0000  0.0040  0.0001  0.0000  0.0000  0.0171  0.0000 </r>
        <r>  0.0000  0.0136  0.0339  0.3453  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0136  0.0339  0.3453  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0000  0.0007  0.0027  0.0000  0.0000  0.0003  0.0000 </r>
        <r>  0.0002  0.0014  0.3601  0.0389  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0014  0.3601  0.0389  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0000  0.0004  0.0018  0.0000  0.0000  0.0015  0.2813  0.0000  0.0074 </r>
        <r>  0.0004  0.0000  0.0570  0.0081  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0004  0.0000  0.0570  0.0081  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0000  0.0000  0.0000  0.0085  0.5227  0.0000  0.0000  0.0038  0.0000 </r>
        <r>  0.0244  0.0002  0.0050  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0244  0.0002  0.0050  0.0006  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0004  0.0004  0.0000  0.0000  0.0006  0.0248  0.0000  0.5928 </r>
        <r>  0.0001  0.0010  0.0014  0.0101  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0010  0.0014  0.0101  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0144  0.0010  0.0510  0.0000  0.0000  0.3873  0.0191  0.0000  0.0035 </r>
        <r>  0.0227  0.0019  0.0009  0.0048  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0227  0.0019  0.0009  0.0048  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
      <set comment="kpoint 20">
       <set comment="band 1">
        <r>  0.9781  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0001  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.0001  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 2">
        <r>  0.0000  0.0000  0.0193  0.0000  0.0000  0.0014  0.0000  0.0001  0.0000 </r>
        <r>  0.4184  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4184  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 3">
        <r>  0.0003  0.0011  0.0000  0.0127  0.0022  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4223  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.4223  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 4">
        <r>  0.0000  0.9091  0.0000  0.0181  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0002  0.0019  0.0033  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0002  0.0002  0.0019  0.0033  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 5">
        <r>  0.0000  0.0168  0.0000  0.9057  0.0001  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0101  0.0030  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0101  0.0030  0.0004  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 6">
        <r>  0.0000  0.0000  0.9226  0.0000  0.0000  0.0001  0.0000  0.0000  0.0000 </r>
        <r>  0.0146  0.0020  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0146  0.0020  0.0000  0.0001  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 7">
        <r>  0.0200  0.0034  0.0000  0.0012  0.0003  0.0000  0.0050  0.0000  0.0005 </r>
        <r>  0.0001  0.0005  0.2746  0.0540  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0001  0.0005  0.2746  0.0540  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 8">
        <r>  0.0018  0.0419  0.0000  0.0010  0.0020  0.0000  0.0061  0.0000  0.0033 </r>
        <r>  0.0000  0.0092  0.0487  0.2708  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0092  0.0487  0.2708  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 9">
        <r>  0.0002  0.0022  0.0000  0.0286  0.0061  0.0000  0.0000  0.0000  0.0009 </r>
        <r>  0.0000  0.3536  0.0004  0.0097  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.3536  0.0004  0.0097  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 10">
        <r>  0.0000  0.0000  0.0138  0.0000  0.0000  0.0121  0.0000  0.0052  0.0000 </r>
        <r>  0.0000  0.3385  0.0038  0.0306  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.3385  0.0038  0.0306  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 11">
        <r>  0.0000  0.0000  0.0067  0.0000  0.0000  0.0001  0.0000  0.0146  0.0000 </r>
        <r>  0.0000  0.0351  0.0473  0.3098  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0351  0.0473  0.3098  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 12">
        <r>  0.0000  0.0000  0.0000  0.0000  0.0000  0.0014  0.0000  0.0020  0.0000 </r>
        <r>  0.0000  0.0000  0.3488  0.0531  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0000  0.3488  0.0531  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 13">
        <r>  0.0002  0.0008  0.0000  0.0010  0.0046  0.0000  0.2516  0.0000  0.0334 </r>
        <r>  0.0005  0.0006  0.0390  0.0224  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0005  0.0006  0.0390  0.0224  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 14">
        <r>  0.0036  0.0017  0.0000  0.0192  0.4773  0.0000  0.0117  0.0000  0.0005 </r>
        <r>  0.0241  0.0005  0.0050  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0241  0.0005  0.0050  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 15">
        <r>  0.0000  0.0000  0.0000  0.0001  0.0006  0.0000  0.0703  0.0000  0.5140 </r>
        <r>  0.0000  0.0025  0.0051  0.0126  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0000  0.0025  0.0051  0.0126  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
       <set comment="band 16">
        <r>  0.0000  0.0000  0.0318  0.0000  0.0000  0.4723  0.0000  0.0270  0.0000 </r>
        <r>  0.0224  0.0011  0.0019  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
        <r>  0.0224  0.0011  0.0019  0.0014  0.0000  0.0000  0.0000  0.0000  0.0000 </r>
       </set>
      </set>
     </set>
    </set>
   </array>
  </projected>
 </calculation>
 <structure name="finalpos" >
  <crystal>
   <varray name="basis" >
    <v>       0.00000000       2.93369200       2.93369200 </v>
    <v>       2.93369200       0.00000000       2.93369200 </v>
    <v>       2.93369200       2.93369200       0.00000000 </v>
   </varray>
   <i name="volume">     50.49792644 </i>
   <varray name="rec_basis" >
    <v>      -0.17043371       0.17043371       0.17043371 </v>
    <v>       0.17043371      -0.17043371       0.17043371 </v>
    <v>       0.17043371       0.17043371      -0.17043371 </v>
   </varray>
  </crystal>
  <varray name="positions" >
   <v>       0.00000000       0.00000000       0.00000000 </v>
   <v>       0.75000000       0.75000000       0.75000000 </v>
   <v>       0.25000000       0.25000000       0.25000000 </v>
  </varray>
 </structure>
</modeling>
"""

from lxml import etree

doc = etree.fromstring(s)

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

# def get_stru(set):
#     t = {}
#     for child in set.iterchildren():
#         # print(child.tag)
#         t.setdefault(child.tag, {})
#         d = t
#         # print(d)
#         if child.tag not in ("v", "i", "r"):
#
#             t[child.tag] = get_stru(child)
#         else:
#             # print("you should assign value like the following")
#             if child.tag == "i":
#                 t[child.attrib.get('name')] = "tagv"
#             if child.tag == "v":
#                 t[child.tag] = "v"
#
#     return t


def get_incar(set):
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
        elif child.tag not in ("v", "i", "r","incar","kpoints","atominfo","calculation"):
            t[child.tag] = get_incar(child)
        elif child.tag == "structure" and child.attrib.get("name")=="finalpos":
            pass
        else:
            return None

    return t

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





    calculation = {}
    calculation["stress"] = stress
    calculation["efermi"] = efermi
    calculation["force"] = force
    calculation["eigenvalues"] = eigenvalues
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

last = get_incar(doc)

print(last)



