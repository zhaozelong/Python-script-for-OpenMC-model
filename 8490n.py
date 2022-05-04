###############################################################################
# SNAP-10A/2 Critical benchmark : 8490a
# Data library: ENDF/B-VII.1
# Date: 2022.4.18
# Author: Zelong Zhao
###############################################################################

from math import pi
import sys
import os
import numpy
import openmc
import openmc.deplete
import matplotlib.pyplot as plt

###############################################################################
#                              Define materials
###############################################################################
# uzrhx
M1 = openmc.Material(name='uzrhx')
M1.temperature = 300.0
#M1.id = 1
M1.set_density('atom/b-cm', 0.1007323)
M1.add_nuclide('U235' ,  0.0014234, 'ao')
M1.add_nuclide('U238' ,  0.0001015, 'ao')
M1.add_element('Zr'   ,  0.0352074, 'ao')
M1.add_nuclide('H1'   ,  0.0640000, 'ao')
M1.add_s_alpha_beta('c_Zr_in_ZrH')
M1.add_s_alpha_beta('c_H_in_ZrH')

# nat boron powder
M2 = openmc.Material(name='nat boron powder')
M2.temperature = 300.0
#M2.id = 2
M2.set_density('atom/b-cm', 0.0250690)
M2.add_nuclide('B10' ,  0.0049887, 'ao')
M2.add_nuclide('B11' ,  0.0200803, 'ao')

# ss304
M3 = openmc.Material(name='ss304')
M3.temperature = 300.0
#M3.id = 3
M3.set_density('atom/b-cm', 0.0862393)
M3.add_nuclide('Fe54', 0.0035020, 'ao')
M3.add_nuclide('Fe56', 0.0544408, 'ao')
M3.add_nuclide('Fe57', 0.0012465, 'ao')
M3.add_nuclide('Fe58', 0.0001662, 'ao')
M3.add_nuclide('Cr50', 0.0007573, 'ao')
M3.add_nuclide('Cr52', 0.0146033, 'ao')
M3.add_nuclide('Cr53', 0.0016557, 'ao')
M3.add_nuclide('Cr54', 0.0004122, 'ao')
M3.add_nuclide('Ni58', 0.0052698, 'ao')
M3.add_nuclide('Ni60', 0.0020147, 'ao')
M3.add_nuclide('Ni61', 0.0000872, 'ao')
M3.add_nuclide('Ni62', 0.0002771, 'ao')
M3.add_nuclide('Ni64', 0.0000702, 'ao')
M3.add_nuclide('Mn55', 0.0017363, 'ao')

# sm2o3 coating
M5 = openmc.Material(name='sm2o3 coating')
M5.set_density('atom/b-cm', 0.0254232)
M5.temperature = 300.0
#M5.id = 5
M5.add_nuclide('O16'  ,  0.0161151, 'ao')
M5.add_nuclide('Al27' ,  0.0050217, 'ao')
M5.add_element('Si'   ,  0.0042609, 'ao')
M5.add_nuclide('Sm147',  0.0000061, 'ao')
M5.add_nuclide('Sm149',  0.0000056, 'ao')
M5.add_nuclide('Sm150',  0.0000030, 'ao')
M5.add_nuclide('Sm152',  0.0000108, 'ao')

# type 1100 aluminum
M6 = openmc.Material(name='type 1100 aluminum')
M6.set_density('atom/b-cm', 0.0602626)
M6.temperature = 300.0
#M6.id = 6
M6.add_nuclide('Al27', 0.0602626, 'ao')

# water
M7 = openmc.Material(name='water')
M7.set_density('atom/b-cm', 0.1001037)
M7.temperature = 300.0
#M7.id = 7
M7.add_nuclide('H1' , 0.0667358, 'ao')
M7.add_nuclide('O16', 0.0333679, 'ao')
M7.add_s_alpha_beta('c_H_in_H2O')

# Hastelloy N
M8 = openmc.Material(name='Hastelloy N')
M8.set_density('atom/b-cm', 0.0872946)
M8.temperature = 300.0
#M8.id = 8
M8.add_nuclide('Ni58' , 0.0440590, 'ao')
M8.add_nuclide('Ni60' , 0.0168440, 'ao')
M8.add_nuclide('Ni61' , 0.0007293, 'ao')
M8.add_nuclide('Ni62' , 0.0023169, 'ao')
M8.add_nuclide('Ni64' , 0.0005873, 'ao')
M8.add_nuclide('Fe54' , 0.0002818, 'ao')
M8.add_nuclide('Fe56' , 0.0043815, 'ao')
M8.add_nuclide('Fe57' , 0.0001003, 'ao')
M8.add_nuclide('Fe58' , 0.0000134, 'ao')
M8.add_nuclide('Cr50' , 0.0003121, 'ao')
M8.add_nuclide('Cr52' , 0.0060187, 'ao')
M8.add_nuclide('Cr53' , 0.0006824, 'ao')
M8.add_nuclide('Cr54' , 0.0001699, 'ao')
M8.add_element('Mo'   , 0.0088982, 'ao')
M8.add_element('Si'   , 0.0018998, 'ao')

# ss316
M9 = openmc.Material(name='Hastelloy N')
M9.set_density('atom/b-cm', 0.0871549)
M9.temperature = 300.0
#M9.id = 9
M9.add_nuclide('Fe54' , 0.0033463, 'ao')
M9.add_nuclide('Fe56' , 0.0520202, 'ao')
M9.add_nuclide('Fe57' , 0.0011910, 'ao')
M9.add_nuclide('Fe58' , 0.0001588, 'ao')
M9.add_nuclide('Cr50' , 0.0006870, 'ao')
M9.add_nuclide('Cr52' , 0.0132476, 'ao')
M9.add_nuclide('Cr53' , 0.0015020, 'ao')
M9.add_nuclide('Cr54' , 0.0003739, 'ao')
M9.add_nuclide('Ni58' , 0.0067490, 'ao')
M9.add_nuclide('Ni60' , 0.0025802, 'ao')
M9.add_nuclide('Ni61' , 0.0001117, 'ao')
M9.add_nuclide('Ni62' , 0.0003549, 'ao')
M9.add_nuclide('Ni64' , 0.0000900, 'ao')
M9.add_element('Mo'   , 0.0012601, 'ao')
M9.add_nuclide('Mn55' , 0.0017604, 'ao')
M9.add_element('Si'   , 0.0017218, 'ao')

# lucite
M10 = openmc.Material(name='lucite')
M10.set_density('atom/b-cm', 0.1064672)
M10.temperature = 300.0
#M10.id = 10
M10.add_element('C'  , 0.0354891, 'ao')
M10.add_nuclide('H1' , 0.0567825, 'ao')
M10.add_nuclide('O16', 0.0141956, 'ao')
M10.add_s_alpha_beta('c_H_in_C5O2H8')

# be
M11 = openmc.Material(name='Be metal')
M11.set_density('atom/b-cm', 0.1216164)
M11.temperature = 300.0
#M11.id = 11
M11.add_nuclide('Be9' , 0.1216164, 'ao')
M11.add_s_alpha_beta('c_Be')

# borated aluminum @ 10.2 w/o boron as natB4C
M12 = openmc.Material(name='natB4C')
M12.set_density('atom/b-cm', 0.0708762)
M12.temperature = 300.0
#M12.id = 12
M12.add_nuclide('B10'  , 0.0030227, 'ao')
M12.add_nuclide('B11'  , 0.0121667, 'ao')
M12.add_element('C'    , 0.0037973, 'ao')
M12.add_nuclide('Al27' , 0.0518894, 'ao')

###############################################################################
materials = openmc.Materials([M1, M2, M3, M5, M6, M7, M8, M9, M10, M11, M12])

#materials.cross_sections = '/mnt/d/Codes/OpenMC/LIBS/ENDF_B/VII_1/cross_sections.xml'
materials.cross_sections = '/mnt/d/Codes/OpenMC/LIBS/ENDF_B/VIII_0/cross_sections.xml'

materials.export_to_xml()

###############################################################################
#                             Create geometry
###############################################################################

# Surfaces List
s1   = openmc.ZCylinder(surface_id=1,     x0=0.0 , y0= 9.6012, r=1.53924)
s2   = openmc.ZPlane(   surface_id=2,     z0=15.52575 )
s3   = openmc.ZPlane(   surface_id=3,     z0=-15.52575)
s4   = openmc.ZCylinder(surface_id=4,     x0=0.0 , y0= 9.6012, r=1.56210)
s5   = openmc.ZCylinder(surface_id=5,     x0=0.0 , y0= 9.6012, r=1.58750)
s6   = openmc.ZCylinder(surface_id=6,      r= 11.303  )
s7   = openmc.ZCylinder(surface_id=7,      r= 11.38555)
s8   = openmc.ZPlane(   surface_id=8,     z0=15.8115  )
s9   = openmc.ZPlane(   surface_id=9,     z0=-15.8115 )
s10  = openmc.ZPlane(   surface_id=10,    z0=16.764   )
s11  = openmc.ZPlane(   surface_id=11,    z0=-16.60652)
s12  = openmc.ZPlane(   surface_id=12,    z0=18.08226 )
s13  = openmc.ZPlane(   surface_id=13,    z0=-16.764  )
s14  = openmc.ZPlane(   surface_id=14,    z0=17.92478 )
s15  = openmc.ZPlane(   surface_id=15,    z0=-16.84274)
s16  = openmc.ZCylinder(surface_id=16,     r=16.46555 )
s17  = openmc.ZPlane(   surface_id=17,    z0=18.161   )
s18  = openmc.ZPlane(   surface_id=18,    z0=18.71726 )
s19  = openmc.ZPlane(   surface_id=19,    z0=6.17474  )
s20  = openmc.ZPlane(   surface_id=20,    z0=6.01726  )
s21  = openmc.ZPlane(   surface_id=21,    z0=29.03474 )
s22  = openmc.ZPlane(   surface_id=22,    z0=31.57474 )
s23  = openmc.ZCylinder(surface_id=23,     r=26.62555 )
s24  = openmc.ZCylinder(surface_id=24,     r=26.78303 )
s25  = openmc.ZPlane(   surface_id=25,    z0=-17.95526)
s26  = openmc.ZPlane(   surface_id=26,    z0=-18.11274)
s27  = openmc.ZCylinder(surface_id=27,     r=27.89555 )
s28  = openmc.ZCylinder(surface_id=28,     r=28.05303 )
s29  = openmc.ZPlane(   surface_id=29,    z0=-18.52422)
s30  = openmc.ZPlane(   surface_id=30,    z0=-33.76422)
s31  = openmc.ZPlane(   surface_id=31,    z0=-18.36674)
s32  = openmc.ZPlane(   surface_id=32,    z0=-33.9217 )
s33  = openmc.ZCylinder(surface_id=33,     r=19.64055 )
s34  = openmc.ZCylinder(surface_id=34,     r=19.79803 )
s35  = openmc.ZCylinder(surface_id=35,     x0=8.3149 , y0=4.8006, r=1.5875)

s44  = openmc.ZCylinder(surface_id=44,   r=11.1506)                         
s45  = openmc.Plane(    surface_id=45 ,  a=-1.73205, b=1,       c=0, d=8.89)  
s46  = openmc.Plane(    surface_id=46 ,  a=-1.73205, b=1,       c=0, d=-8.89) 
s47  = openmc.YPlane(   surface_id=47,   y0=4.445)                            
s48  = openmc.YPlane(   surface_id=48,   y0=-4.445)                           
s49  = openmc.Plane(    surface_id=49 ,  a=1.73205,  b=1,       c=0, d=8.89)  
s50  = openmc.Plane(    surface_id=50 ,  a=1.73205,  b=1,       c=0, d=-8.89) 
s51  = openmc.Plane(    surface_id=51 ,  a=1,        b=1.73205, c=0, d=18.6944)
s52  = openmc.XPlane(   surface_id=52,   x0=9.3472)                           
s53  = openmc.Plane(    surface_id=53 ,  a=-1,       b=1.73205, c=0, d=-18.6944)
s54  = openmc.Plane(    surface_id=54 ,  a=1,        b=1.73205, c=0, d=-18.6944)
s55  = openmc.XPlane(   surface_id=55,   x0=-9.3472)                          
s56  = openmc.Plane(    surface_id=56 ,  a=-1,       b=1.73205, c=0, d=18.6944)
s57  = openmc.ZCylinder(surface_id=57, x0=0.0    , y0=9.6012 , r=1.6764)
s58  = openmc.ZCylinder(surface_id=58, x0=2.7716 , y0=8.0010 , r=1.6764)
s59  = openmc.ZCylinder(surface_id=59, x0=5.5432 , y0=6.4008 , r=1.6764)
s60  = openmc.ZCylinder(surface_id=60, x0=8.3149 , y0=4.8006 , r=1.6764)
s61  = openmc.ZCylinder(surface_id=61, x0=8.3149 , y0=1.6002 , r=1.6764)
s62  = openmc.ZCylinder(surface_id=62, x0=8.3149 , y0=-1.6002, r=1.6764)
s63  = openmc.ZCylinder(surface_id=63, x0=8.3149 , y0=-4.8006, r=1.6764)
s64  = openmc.ZCylinder(surface_id=64, x0=5.5432 , y0=-6.4008, r=1.6764)
s65  = openmc.ZCylinder(surface_id=65, x0=2.7716 , y0=-8.0010, r=1.6764)
s66  = openmc.ZCylinder(surface_id=66, x0=0.0    , y0=-9.6012, r=1.6764)
s67  = openmc.ZCylinder(surface_id=67, x0=-2.7716, y0=-8.0010, r=1.6764)
s68  = openmc.ZCylinder(surface_id=68, x0=-5.5432, y0=-6.4008, r=1.6764)
s69  = openmc.ZCylinder(surface_id=69, x0=-8.3149, y0=-4.8006, r=1.6764)
s70  = openmc.ZCylinder(surface_id=70, x0=-8.3149, y0=-1.6002, r=1.6764)
s71  = openmc.ZCylinder(surface_id=71, x0=-8.3149, y0=1.6002 , r=1.6764)
s72  = openmc.ZCylinder(surface_id=72, x0=-8.3149, y0=4.8006 , r=1.6764)
s73  = openmc.ZCylinder(surface_id=73, x0=-5.5432, y0=6.4008 , r=1.6764)
s74  = openmc.ZCylinder(surface_id=74, x0=-2.7716, y0=8.0010 , r=1.6764)

s75  = openmc.ZPlane(   surface_id=75, z0=-5.41274  )
s76  = openmc.ZPlane(   surface_id=76, z0=-5.49148  )
s77  = openmc.ZPlane(   surface_id=77, z0=-16.764   )
s78  = openmc.ZPlane(   surface_id=78, z0=-16.84274 )
s79  = openmc.ZCylinder(surface_id=79,  r=11.46429  )
s80  = openmc.ZCylinder(surface_id=80,  r=11.94181  )
s81  = openmc.ZCylinder(surface_id=81,  r=12.02055  )
s82  = openmc.ZPlane(   surface_id=82, z0=17.84604  )
s83  = openmc.ZPlane(   surface_id=83, z0=6.25348   )
s84  = openmc.ZCylinder(surface_id=84,  r=11.46429  )
s85  = openmc.ZCylinder(surface_id=85,  r=12.57681  )
s86  = openmc.ZCylinder(surface_id=86,  r=12.65555  )

s999 = openmc.Sphere(   surface_id=999, r=50       , boundary_type = 'vacuum')
  
#============================================================================
# CELLS define
# cell: 100
C100 = openmc.Cell(cell_id=100,fill=M7,region=-s6 & -s8 & +s9)
un = openmc.Universe(cells=[C100])

# univ:1
C50 = openmc.Cell(cell_id=50,fill=M1,region=-s1 & -s2 & +s3)
C51 = openmc.Cell(cell_id=51,fill=M5,region=-s4 & +s1 & -s2 & +s3)
C52 = openmc.Cell(cell_id=52,fill=M8,region=+s4 | +s2 | -s3)
u1 = openmc.Universe(cells=[C50, C51, C52])

# tral array
# ref
trcl1  = [0.0    , 9.6012  , 0]
trcl2  = [0.0    , -3.2004 , 0]
trcl3  = [-2.7716, -1.6002 , 0]
trcl4  = [2.7716 , -1.6002 , 0]
trcl5  = [0.0    , -6.4008 , 0]
trcl6  = [-2.7716, -4.8006 , 0]
trcl7  = [-5.5432, -3.2004 , 0]
trcl8  = [2.7716 , -4.8006 , 0]
trcl9  = [5.5432 , -3.2004 , 0]
trcl10 = [0.0    , -9.6012 , 0]
trcl11 = [-2.7716, -8.0010 , 0]
trcl12 = [-5.5432, -6.4008 , 0]
trcl13 = [-8.3149, -4.8006 , 0]
trcl14 = [2.7716 , -8.0010 , 0]
trcl15 = [5.5432 , -6.4008 , 0]
trcl16 = [8.3149 , -4.8006 , 0]
trcl17 = [0.0    , -12.8016, 0]
trcl18 = [-2.7716, -11.2014, 0]
trcl19 = [-5.5432, -9.6012 , 0]
trcl20 = [-8.3249, -8.0010 , 0]
trcl21 = [2.7716 , -11.2014, 0]
trcl22 = [5.5432 , -9.6012 , 0]
trcl23 = [8.3149 , -8.0010 , 0]
trcl24 = [0.0    , -16.0020, 0]
trcl25 = [-2.7716, -14.4018, 0]
trcl26 = [-5.5432, -12.8016, 0]
trcl27 = [-8.3149, -11.2014, 0]
trcl28 = [2.7716 , -14.4018, 0]
trcl29 = [5.5432 , -12.8016, 0]

# ref
trcl37 = [8.3149  , -4.8006, 0]
trcl36 = [-2.7716 , -1.6002, 0]
trcl35 = [-5.5432 , -3.2004, 0]
trcl34 = [-16.6298, 0.0    , 0]
trcl33 = [-13.8581, -1.6002, 0]
trcl32 = [-11.0865, -3.2004, 0]
trcl31 = [-8.3149 , -4.8006, 0]
trcl30 = [0.0     , 3.2004 , 0]

# surface clone

s1001 = openmc.ZCylinder(surface_id = 1001, x0 = trcl1[0]            , y0 = trcl1[1]            , r=1.58750)
s1002 = openmc.ZCylinder(surface_id = 1002, x0 = trcl1[0] + trcl2[0] , y0 = trcl1[1] + trcl2[1] , r=1.58750)
s1003 = openmc.ZCylinder(surface_id = 1003, x0 = trcl1[0] + trcl3[0] , y0 = trcl1[1] + trcl3[1] , r=1.58750)
s1004 = openmc.ZCylinder(surface_id = 1004, x0 = trcl1[0] + trcl4[0] , y0 = trcl1[1] + trcl4[1] , r=1.58750)
s1005 = openmc.ZCylinder(surface_id = 1005, x0 = trcl1[0] + trcl5[0] , y0 = trcl1[1] + trcl5[1] , r=1.58750)
s1006 = openmc.ZCylinder(surface_id = 1006, x0 = trcl1[0] + trcl6[0] , y0 = trcl1[1] + trcl6[1] , r=1.58750)
s1007 = openmc.ZCylinder(surface_id = 1007, x0 = trcl1[0] + trcl7[0] , y0 = trcl1[1] + trcl7[1] , r=1.58750)
s1008 = openmc.ZCylinder(surface_id = 1008, x0 = trcl1[0] + trcl8[0] , y0 = trcl1[1] + trcl8[1] , r=1.58750)
s1009 = openmc.ZCylinder(surface_id = 1009, x0 = trcl1[0] + trcl9[0] , y0 = trcl1[1] + trcl9[1] , r=1.58750)
s1010 = openmc.ZCylinder(surface_id = 1010, x0 = trcl1[0] + trcl10[0], y0 = trcl1[1] + trcl10[1], r=1.58750)
s1011 = openmc.ZCylinder(surface_id = 1011, x0 = trcl1[0] + trcl11[0], y0 = trcl1[1] + trcl11[1], r=1.58750)
s1012 = openmc.ZCylinder(surface_id = 1012, x0 = trcl1[0] + trcl12[0], y0 = trcl1[1] + trcl12[1], r=1.58750)
s1013 = openmc.ZCylinder(surface_id = 1013, x0 = trcl1[0] + trcl13[0], y0 = trcl1[1] + trcl13[1], r=1.58750)
s1014 = openmc.ZCylinder(surface_id = 1014, x0 = trcl1[0] + trcl14[0], y0 = trcl1[1] + trcl14[1], r=1.58750)
s1015 = openmc.ZCylinder(surface_id = 1015, x0 = trcl1[0] + trcl15[0], y0 = trcl1[1] + trcl15[1], r=1.58750)
s1016 = openmc.ZCylinder(surface_id = 1016, x0 = trcl1[0] + trcl16[0], y0 = trcl1[1] + trcl16[1], r=1.58750)
s1017 = openmc.ZCylinder(surface_id = 1017, x0 = trcl1[0] + trcl17[0], y0 = trcl1[1] + trcl17[1], r=1.58750)
s1018 = openmc.ZCylinder(surface_id = 1018, x0 = trcl1[0] + trcl18[0], y0 = trcl1[1] + trcl18[1], r=1.58750)
s1019 = openmc.ZCylinder(surface_id = 1019, x0 = trcl1[0] + trcl19[0], y0 = trcl1[1] + trcl19[1], r=1.58750)
s1020 = openmc.ZCylinder(surface_id = 1020, x0 = trcl1[0] + trcl20[0], y0 = trcl1[1] + trcl20[1], r=1.58750)
s1021 = openmc.ZCylinder(surface_id = 1021, x0 = trcl1[0] + trcl21[0], y0 = trcl1[1] + trcl21[1], r=1.58750)
s1022 = openmc.ZCylinder(surface_id = 1022, x0 = trcl1[0] + trcl22[0], y0 = trcl1[1] + trcl22[1], r=1.58750)
s1023 = openmc.ZCylinder(surface_id = 1023, x0 = trcl1[0] + trcl23[0], y0 = trcl1[1] + trcl23[1], r=1.58750)
s1024 = openmc.ZCylinder(surface_id = 1024, x0 = trcl1[0] + trcl24[0], y0 = trcl1[1] + trcl24[1], r=1.58750)
s1025 = openmc.ZCylinder(surface_id = 1025, x0 = trcl1[0] + trcl25[0], y0 = trcl1[1] + trcl25[1], r=1.58750)
s1026 = openmc.ZCylinder(surface_id = 1026, x0 = trcl1[0] + trcl26[0], y0 = trcl1[1] + trcl26[1], r=1.58750)
s1027 = openmc.ZCylinder(surface_id = 1027, x0 = trcl1[0] + trcl27[0], y0 = trcl1[1] + trcl27[1], r=1.58750)
s1028 = openmc.ZCylinder(surface_id = 1028, x0 = trcl1[0] + trcl28[0], y0 = trcl1[1] + trcl28[1], r=1.58750)
s1029 = openmc.ZCylinder(surface_id = 1029, x0 = trcl1[0] + trcl29[0], y0 = trcl1[1] + trcl29[1], r=1.58750)

s1037 = openmc.ZCylinder(surface_id = 1037, x0 = trcl37[0],             y0 = trcl37[1],             r=1.58750)
s1030 = openmc.ZCylinder(surface_id = 1030, x0 = trcl37[0] + trcl30[0], y0 = trcl37[1] + trcl30[1], r=1.58750)
s1031 = openmc.ZCylinder(surface_id = 1031, x0 = trcl37[0] + trcl31[0], y0 = trcl37[1] + trcl31[1], r=1.58750)
s1032 = openmc.ZCylinder(surface_id = 1032, x0 = trcl37[0] + trcl32[0], y0 = trcl37[1] + trcl32[1], r=1.58750)
s1033 = openmc.ZCylinder(surface_id = 1033, x0 = trcl37[0] + trcl33[0], y0 = trcl37[1] + trcl33[1], r=1.58750)
s1034 = openmc.ZCylinder(surface_id = 1034, x0 = trcl37[0] + trcl34[0], y0 = trcl37[1] + trcl34[1], r=1.58750)
s1035 = openmc.ZCylinder(surface_id = 1035, x0 = trcl37[0] + trcl35[0], y0 = trcl37[1] + trcl35[1], r=1.58750)
s1036 = openmc.ZCylinder(surface_id = 1036, x0 = trcl37[0] + trcl36[0], y0 = trcl37[1] + trcl36[1], r=1.58750)

# cell:1-28
C1  = openmc.Cell(cell_id=1 ,fill=u1,region=-s1001 & -s8 & +s9)
C2  = openmc.Cell(cell_id=2 ,fill=u1,region=-s1002 & -s8 & +s9)
C3  = openmc.Cell(cell_id=3 ,fill=u1,region=-s1003 & -s8 & +s9)
C4  = openmc.Cell(cell_id=4 ,fill=u1,region=-s1004 & -s8 & +s9)
C5  = openmc.Cell(cell_id=5 ,fill=u1,region=-s1005 & -s8 & +s9)
C6  = openmc.Cell(cell_id=6 ,fill=u1,region=-s1006 & -s8 & +s9)
C7  = openmc.Cell(cell_id=7 ,fill=u1,region=-s1007 & -s8 & +s9)
C8  = openmc.Cell(cell_id=8 ,fill=u1,region=-s1008 & -s8 & +s9)
C9  = openmc.Cell(cell_id=9 ,fill=u1,region=-s1009 & -s8 & +s9)
C10 = openmc.Cell(cell_id=10,fill=u1,region=-s1010 & -s8 & +s9)
C11 = openmc.Cell(cell_id=11,fill=u1,region=-s1011 & -s8 & +s9)
C12 = openmc.Cell(cell_id=12,fill=u1,region=-s1012 & -s8 & +s9)
C13 = openmc.Cell(cell_id=13,fill=u1,region=-s1013 & -s8 & +s9)
C14 = openmc.Cell(cell_id=14,fill=u1,region=-s1014 & -s8 & +s9)
C15 = openmc.Cell(cell_id=15,fill=u1,region=-s1015 & -s8 & +s9)
C16 = openmc.Cell(cell_id=16,fill=u1,region=-s1016 & -s8 & +s9)
C17 = openmc.Cell(cell_id=17,fill=u1,region=-s1017 & -s8 & +s9)
C18 = openmc.Cell(cell_id=18,fill=u1,region=-s1018 & -s8 & +s9)
C19 = openmc.Cell(cell_id=19,fill=u1,region=-s1019 & -s8 & +s9)
C20 = openmc.Cell(cell_id=20,fill=u1,region=-s1020 & -s8 & +s9)
C21 = openmc.Cell(cell_id=21,fill=u1,region=-s1021 & -s8 & +s9)
C22 = openmc.Cell(cell_id=22,fill=u1,region=-s1022 & -s8 & +s9)
C23 = openmc.Cell(cell_id=23,fill=u1,region=-s1023 & -s8 & +s9)
C24 = openmc.Cell(cell_id=24,fill=u1,region=-s1024 & -s8 & +s9)
C25 = openmc.Cell(cell_id=25,fill=u1,region=-s1025 & -s8 & +s9)
C26 = openmc.Cell(cell_id=26,fill=u1,region=-s1026 & -s8 & +s9)
C27 = openmc.Cell(cell_id=27,fill=u1,region=-s1027 & -s8 & +s9)
C28 = openmc.Cell(cell_id=28,fill=u1,region=-s1028 & -s8 & +s9)
C29 = openmc.Cell(cell_id=29,fill=u1,region=-s1029 & -s8 & +s9)

C37 = openmc.Cell(cell_id=37,fill=M10,region=-s1037 & -s8 & +s9)
C30 = openmc.Cell(cell_id=30,fill=M10,region=-s1030 & -s8 & +s9)
C31 = openmc.Cell(cell_id=31,fill=M10,region=-s1031 & -s8 & +s9)
C32 = openmc.Cell(cell_id=32,fill=M10,region=-s1032 & -s8 & +s9)
C33 = openmc.Cell(cell_id=33,fill=M10,region=-s1033 & -s8 & +s9)
C34 = openmc.Cell(cell_id=34,fill=M10,region=-s1034 & -s8 & +s9)
C35 = openmc.Cell(cell_id=35,fill=M10,region=-s1035 & -s8 & +s9)
C36 = openmc.Cell(cell_id=36,fill=M10,region=-s1036 & -s8 & +s9)

C41 = openmc.Cell(cell_id=41,fill=M11,region=-s44 &-s45 &+s46 &+s51 &+s57 &+s58 &+s59 &+s60 &-s8 &+s9)
C42 = openmc.Cell(cell_id=42,fill=M11,region=-s44 &-s47 &+s48 &+s52 &+s60 &+s61 &+s62 &+s63 &-s8 &+s9)
C43 = openmc.Cell(cell_id=43,fill=M11,region=-s44 &-s49 &+s50 &-s53 &+s63 &+s64 &+s65 &+s66 &-s8 &+s9)
C44 = openmc.Cell(cell_id=44,fill=M11,region=-s44 &-s45 &+s46 &-s54 &+s66 &+s67 &+s68 &+s69 &-s8 &+s9)
C45 = openmc.Cell(cell_id=45,fill=M11,region=-s44 &-s47 &+s48 &-s55 &+s69 &+s70 &+s71 &+s72 &-s8 &+s9)
C46 = openmc.Cell(cell_id=46,fill=M11,region=-s44 &-s49 &+s50 &+s56 &+s72 &+s73 &+s74 &+s57 &-s8 &+s9)

# pick out the fuel pin region from C100
C100.region = C100.region & (~C1.region)
C100.region = C100.region & (~C2.region)
C100.region = C100.region & (~C3.region)
C100.region = C100.region & (~C4.region)
C100.region = C100.region & (~C5.region)
C100.region = C100.region & (~C6.region)
C100.region = C100.region & (~C7.region)
C100.region = C100.region & (~C8.region)
C100.region = C100.region & (~C9.region)
C100.region = C100.region & (~C10.region)
C100.region = C100.region & (~C11.region)
C100.region = C100.region & (~C12.region)
C100.region = C100.region & (~C13.region)
C100.region = C100.region & (~C14.region)
C100.region = C100.region & (~C15.region)
C100.region = C100.region & (~C16.region)
C100.region = C100.region & (~C17.region)
C100.region = C100.region & (~C18.region)
C100.region = C100.region & (~C19.region)
C100.region = C100.region & (~C20.region)
C100.region = C100.region & (~C21.region)
C100.region = C100.region & (~C22.region)
C100.region = C100.region & (~C23.region)
C100.region = C100.region & (~C24.region)
C100.region = C100.region & (~C25.region)
C100.region = C100.region & (~C26.region)
C100.region = C100.region & (~C27.region)
C100.region = C100.region & (~C28.region)
C100.region = C100.region & (~C29.region)
C100.region = C100.region & (~C30.region)
C100.region = C100.region & (~C31.region)
C100.region = C100.region & (~C32.region)
C100.region = C100.region & (~C33.region)
C100.region = C100.region & (~C34.region)
C100.region = C100.region & (~C35.region)
C100.region = C100.region & (~C36.region)
C100.region = C100.region & (~C37.region)

C100.region = C100.region & (~C41.region)
C100.region = C100.region & (~C42.region)
C100.region = C100.region & (~C43.region)
C100.region = C100.region & (~C44.region)
C100.region = C100.region & (~C45.region)
C100.region = C100.region & (~C46.region)

# translate
C1.translation  = (0.0, 0.0, 0.0)
C2.translation  = trcl2 
C3.translation  = trcl3 
C4.translation  = trcl4 
C5.translation  = trcl5 
C6.translation  = trcl6 
C7.translation  = trcl7 
C8.translation  = trcl8 
C9.translation  = trcl9 
C10.translation = trcl10
C11.translation = trcl11
C12.translation = trcl12
C13.translation = trcl13
C14.translation = trcl14
C15.translation = trcl15
C16.translation = trcl16
C17.translation = trcl17
C18.translation = trcl18
C19.translation = trcl19
C20.translation = trcl20
C21.translation = trcl21
C22.translation = trcl22
C23.translation = trcl23
C24.translation = trcl24
C25.translation = trcl25
C26.translation = trcl26
C27.translation = trcl27
C28.translation = trcl28
C29.translation = trcl29
#C30.translation = trcl30
#C31.translation = trcl31
#C32.translation = trcl32
#C33.translation = trcl33
#C34.translation = trcl34
#C35.translation = trcl35
#C36.translation = trcl36
#C37.translation = trcl37

# add cell in un
un.add_cells([C1 , C2 , C3 , C4 , C5 , C6 , C7 , C8 , C9])
un.add_cells([C10, C11, C12, C13, C14, C15, C16, C17, C18])
un.add_cells([C19, C20, C21, C22, C23, C24, C25, C26, C27, C28])
un.add_cells([C29, C30, C31, C32, C33, C34, C35, C36, C37])
un.add_cells([C41, C42, C43, C44, C45, C46])

# add cells
C101 = openmc.Cell(cell_id=101,fill=M6,region=-s6 & +s8  & -s10)
C102 = openmc.Cell(cell_id=102,fill=M6,region=-s6 & -s9  & +s11)
C103 = openmc.Cell(cell_id=103,fill=M7,region=-s6 & +s10 & -s12)
C104 = openmc.Cell(cell_id=104,fill=M7,region=-s6 & -s11 & +s13)
un.add_cells([C101,C102,C103,C104])

# add cells
C105 = openmc.Cell(cell_id=105,fill=M9,region=(-s7 & -s13 & +s15)|(-s7 & +s6 & -s14 & +s13)|(-s16 & +s6 & -s12 & +s14))
C106 = openmc.Cell(cell_id=106,fill=M6,region=(-s6 & -s17 & +s12)|(-s16 & +s6 &-s18 &+s12))
C107 = openmc.Cell(cell_id=107,fill=M3, region=(+s7 &-s84 &-s82 &+s83))
C108 = openmc.Cell(cell_id=108,fill=M2, region=(-s85 &+s84 &-s82 &+s83))
C109 = openmc.Cell(cell_id=109,fill=M3, region=(+s7 &-s86 &+s19 &-s83)|(+s7 &-s86 &+s82 &-s14)|(+s83 &-s82 &+s85 &-s86))
C110 = openmc.Cell(cell_id=110,fill=M7, region=(-s23 &+s86 &-s14 &+s19)|(-s23 &+s16 &-s18 &+s14)|(-s6 &-s18 &+s17)|(-s23 &-s21 &+s18))
C111 = openmc.Cell(cell_id=111,         region=(-s23 &-s22 &+s21))
C112 = openmc.Cell(cell_id=112,fill=M9, region=(-s24 &+s7 &-s19 &+s20)|(-s24 &+s23 &-s22 &+s19))
C113 = openmc.Cell(cell_id=113,fill=M3, region=(+s7 &-s79 &+s77 &-s76))
C114 = openmc.Cell(cell_id=114,fill=M2, region=(-s80 &+s79 &-s76 &+s77))
C115 = openmc.Cell(cell_id=115,fill=M3, region=(+s7 &-s81 &+s78 &-s77)|(+s7 &-s81 &+s76 &-s75)|(+s80 &-s81 &+s77 &-s76))

C116 = openmc.Cell(cell_id=116,fill=M7,region=(-s27 &-s15 &+s25)|(-s27 &+s81 &-s75 &+s15)|(-s27 &+s7 &-s20 &+s75))
C117 = openmc.Cell(cell_id=117,fill=M9,region=(-s28 &-s25 &+s26)|(-s28 &+s27 &-s20 &+s25))
C118 = openmc.Cell(cell_id=118,fill=M7,region=-s33 &-s29 &+s30)
C119 = openmc.Cell(cell_id=119,fill=M6,region=-s34 &-s31 &+s29)
C120 = openmc.Cell(cell_id=120,fill=M9,region=(-s34 &-s30 &+s32)|(-s34 &+s33 &-s29 &+s30))

un.add_cells([C105,C106,C107,C108,C109,C110,C111,C112,C113,C114,C115,C116,C117,C118,C119,C120])

# add cells
C121 = openmc.Cell(cell_id=121,region=(-s999&+s22)|(-s999&+s24&-s22&+s20)|(-s999&+s28&-s20&+s26)|(-s999&-s26&+s31)|(-s999&+s34&-s31&+s32)|(-s999&-s32))
un.add_cell(C121)

# Define overall geometry
geometry = openmc.Geometry(un)
geometry.export_to_xml()

###############################################################################
#                     Transport calculation settings
###############################################################################

# Instantiate a Settings object, set all runtime parameters, and export to XML
settings = openmc.Settings()
settings.batches = 1000
settings.inactive = 100
settings.particles = 10000

spatial = openmc.stats.Point([0.0, 9.6012, 0.0])
angle   = openmc.stats.Isotropic()
energy = openmc.stats.Maxwell(1.2895e6)
#energy = openmc.stats.Watt(0.988e6, 2.249e-6)
settings.source = openmc.Source(spatial,angle,energy)

# export to xml file
settings.export_to_xml()

###############################################################################
###############################################################################
#                   Exporting to OpenMC plots.xml file
###############################################################################

plot1 = openmc.Plot(plot_id=1)
plot1.basis = 'xy'
plot1.origin = [0.0, 0.0, 0.0]
plot1.width = [100.0, 100.0]
plot1.pixels = [2000, 2000]
plot1.color_by = 'material'

plot2 = openmc.Plot(plot_id=2)
plot2.basis = 'xz'
plot2.origin = [0.0, 0.0, 0.0]
plot2.width = [100.0, 100.0]
plot2.pixels = [2000, 2000]
plot2.color_by = 'material'

plot3 = openmc.Plot(plot_id=3)
plot3.basis = 'xy'
plot3.origin = [0.0, 0.0, 0.0]
plot3.width = [100.0, 100.0]
plot3.pixels = [2000, 2000]
plot3.color_by = 'cell'

plot4 = openmc.Plot(plot_id=4)
plot4.basis = 'xz'
plot4.origin = [0.0, 0.0, 0.0]
plot4.width = [100.0, 100.0]
plot4.pixels = [2000, 2000]
plot4.color_by = 'cell'

# Instantiate a Plots collection and export to XML
plot_file = openmc.Plots([plot1,plot2,plot3,plot4])
plot_file.export_to_xml()


###############################################################################
os.system('openmc -p')

###############################################################################
os.system('openmc -s 8')