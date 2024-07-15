###############################################################################
# SNAP-10A/2 Critical benchmark : Case_fig12
# Data library: ENDF/B-VII.1
# Date: 2022.5.4
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

# 4.54 kg in 39 gal of water
M2 = openmc.Material(name='boron water')
M2.temperature = 300.0
#M2.id = 2
M2.set_density('atom/b-cm', 0.1001866)
M2.add_nuclide('B10' ,  0.0000663, 'ao')
M2.add_nuclide('B11' ,  0.0002667, 'ao')
M2.add_nuclide('H1'  ,  0.0662583, 'ao')
M2.add_nuclide('N14' ,  0.0000666, 'ao')
M2.add_nuclide('O16' ,  0.0335287, 'ao')
M2.add_s_alpha_beta('c_H_in_H2O')

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

# c --- natural B for poison splines$
M28 = openmc.Material(name='natB')
M28.set_density('atom/b-cm', 0.022702)
M28.temperature = 300.0
M28.add_nuclide('B10'  , 0.004518 , 'ao')
M28.add_nuclide('B11'  , 0.018184, 'ao')
# c --- natural B for poison splines$
M29 = openmc.Material(name='natB')
M29.set_density('atom/b-cm', 0.018214)
M29.temperature = 300.0
M29.add_nuclide('B10'  , 0.003625 , 'ao')
M29.add_nuclide('B11'  , 0.014589, 'ao')
# c --- natural B for poison splines$
M33 = openmc.Material(name='natB')
M33.set_density('atom/b-cm', 0.015970)
M33.temperature = 300.0
M33.add_nuclide('B10'  , 0.003178 , 'ao')
M33.add_nuclide('B11'  , 0.012792, 'ao')
# c --- natural B for poison splines$
M30 = openmc.Material(name='natB')
M30.set_density('atom/b-cm', 0.019006)
M30.temperature = 300.0
M30.add_nuclide('B10'  , 0.003782 , 'ao')
M30.add_nuclide('B11'  , 0.015224, 'ao')
# c --- natural B for poison splines$
M23 = openmc.Material(name='natB')
M23.set_density('atom/b-cm', 0.015574)
M23.temperature = 300.0
M23.add_nuclide('B10'  , 0.003099 , 'ao')
M23.add_nuclide('B11'  , 0.012475, 'ao')
# c --- natural B for poison splines$
M32 = openmc.Material(name='natB')
M32.set_density('atom/b-cm', 0.018742)
M32.temperature = 300.0
M32.add_nuclide('B10'  , 0.003730 , 'ao')
M32.add_nuclide('B11'  , 0.015012, 'ao')
# c --- natural B for poison splines$
M27 = openmc.Material(name='natB')
M27.set_density('atom/b-cm', 0.021117)
M27.temperature = 300.0
M27.add_nuclide('B10'  , 0.004202 , 'ao')
M27.add_nuclide('B11'  , 0.016915, 'ao')
# c --- natural B for poison splines$
M21 = openmc.Material(name='natB')
M21.set_density('atom/b-cm', 0.014650)
M21.temperature = 300.0
M21.add_nuclide('B10'  , 0.002915 , 'ao')
M21.add_nuclide('B11'  , 0.011735, 'ao')
# c --- natural B for poison splines$
M22 = openmc.Material(name='natB')
M22.set_density('atom/b-cm', 0.013066)
M22.temperature = 300.0
M22.add_nuclide('B10'  , 0.002600 , 'ao')
M22.add_nuclide('B11'  , 0.010466, 'ao')
# c --- natural B for poison splines$
M26 = openmc.Material(name='natB')
M26.set_density('atom/b-cm', .021910)
M26.temperature = 300.0
M26.add_nuclide('B10'  , 0.004360 , 'ao')
M26.add_nuclide('B11'  , 0.017550, 'ao')
# c --- natural B for poison splines$
M24 = openmc.Material(name='natB')
M24.set_density('atom/b-cm', 0.020854)
M24.temperature = 300.0
M24.add_nuclide('B10'  , 0.004150 , 'ao')
M24.add_nuclide('B11'  , 0.016704, 'ao')
# c --- natural B for poison splines$
M31 = openmc.Material(name='natB')
M31.set_density('atom/b-cm', 0.018478)
M31.temperature = 300.0
M31.add_nuclide('B10'  , 0.003677 , 'ao')
M31.add_nuclide('B11'  , 0.014801, 'ao')

# Definitions for the fuel elements:
M81 = openmc.Material()
M81.temperature = 300.0
M81.set_density('atom/b-cm', 0.1021332)
M81.add_nuclide('U235' ,  0.001430699 )
M81.add_nuclide('U238' ,  0.000103873 )
M81.add_element('Zr'   ,  0.035252214 )
M81.add_nuclide('H1'   ,  0.065346421 )
M81.add_s_alpha_beta('c_Zr_in_ZrH')
M81.add_s_alpha_beta('c_H_in_ZrH')

M82 = openmc.Material()
M82.temperature = 300.0
M82.set_density('atom/b-cm', 0.1001835)
M82.add_nuclide('U235' ,  0.001432362 )
M82.add_nuclide('U238' ,  0.000103982 )
M82.add_element('Zr'   ,  0.035151269 )
M82.add_nuclide('H1'   , 0.063495921  )
M82.add_s_alpha_beta('c_Zr_in_ZrH')
M82.add_s_alpha_beta('c_H_in_ZrH')

M83 = openmc.Material()
M83.temperature = 300.0
M83.set_density('atom/b-cm', 0.1013194)
M83.add_nuclide('U235' ,  0.001423493 )
M83.add_nuclide('U238' ,  0.000101903 )
M83.add_element('Zr'   ,  0.035011378 )
M83.add_nuclide('H1'   , 0.064782612  )
M83.add_s_alpha_beta('c_Zr_in_ZrH')
M83.add_s_alpha_beta('c_H_in_ZrH')

M84 = openmc.Material()
M84.temperature = 300.0
M84.set_density('atom/b-cm', 0.1012824)
M84.add_nuclide('U235' ,  0.001431586 )
M84.add_nuclide('U238' ,  0.000103982 )
M84.add_element('Zr'   ,  0.035287436 )
M84.add_nuclide('H1'   , 0.064459356  )
M84.add_s_alpha_beta('c_Zr_in_ZrH')
M84.add_s_alpha_beta('c_H_in_ZrH')

M85 = openmc.Material()
M85.temperature = 300.0
M85.set_density('atom/b-cm', 0.1012830)
M85.add_nuclide('U235' ,  0.001430255 )
M85.add_nuclide('U238' ,  0.000103763 )
M85.add_element('Zr'   ,  0.035273259 )
M85.add_nuclide('H1'   , 0.064475748  )
M85.add_s_alpha_beta('c_Zr_in_ZrH')
M85.add_s_alpha_beta('c_H_in_ZrH')

M86 = openmc.Material()
M86.temperature = 300.0
M86.set_density('atom/b-cm', 0.1011813)
M86.add_nuclide('U235' ,  0.001430588 )
M86.add_nuclide('U238' ,  0.000103763 )
M86.add_element('Zr'   ,  0.035251872 )
M86.add_nuclide('H1'   , 0.064395062  )
M86.add_s_alpha_beta('c_Zr_in_ZrH')
M86.add_s_alpha_beta('c_H_in_ZrH')

M87 = openmc.Material()
M87.temperature = 300.0
M87.set_density('atom/b-cm', 0.1011842)
M87.add_nuclide('U235' ,  0.001433581 )
M87.add_nuclide('U238' ,  0.000102669 )
M87.add_element('Zr'   ,  0.035262547 )
M87.add_nuclide('H1'   , 0.064385381  )
M87.add_s_alpha_beta('c_Zr_in_ZrH')
M87.add_s_alpha_beta('c_H_in_ZrH')

M88 = openmc.Material()
M88.temperature = 300.0
M88.set_density('atom/b-cm', 0.1011694)
M88.add_nuclide('U235' ,  0.001431031 )
M88.add_nuclide('U238' ,  0.000103763 )
M88.add_element('Zr'   ,  0.03523959  )
M88.add_nuclide('H1'   , 0.064395062  )
M88.add_s_alpha_beta('c_Zr_in_ZrH')
M88.add_s_alpha_beta('c_H_in_ZrH')

M89 = openmc.Material()
M89.temperature = 300.0
M89.set_density('atom/b-cm', 0.1006995)
M89.add_nuclide('U235' ,  0.001421165 )
M89.add_nuclide('U238' ,  0.000102341 )
M89.add_element('Zr'   ,  0.035274751 )
M89.add_nuclide('H1'   , 0.063901235  )
M89.add_s_alpha_beta('c_Zr_in_ZrH')
M89.add_s_alpha_beta('c_H_in_ZrH')

M90 = openmc.Material()
M90.temperature = 300.0
M90.set_density('atom/b-cm', 0.1010355)
M90.add_nuclide('U235' ,  0.00143092  )
M90.add_nuclide('U238' ,  0.000103873 )
M90.add_element('Zr'   ,  0.035232421 )
M90.add_nuclide('H1'   , 0.064268326  )
M90.add_s_alpha_beta('c_Zr_in_ZrH')
M90.add_s_alpha_beta('c_H_in_ZrH')

M91 = openmc.Material()
M91.temperature = 300.0
M91.set_density('atom/b-cm', 0.1001852)
M91.add_nuclide('U235' ,  0.001432472 )
M91.add_nuclide('U238' ,  0.000103982 )
M91.add_element('Zr'   ,  0.035277465 )
M91.add_nuclide('H1'   , 0.063371257  )
M91.add_s_alpha_beta('c_Zr_in_ZrH')
M91.add_s_alpha_beta('c_H_in_ZrH')

M92 = openmc.Material()
M92.temperature = 300.0
M92.set_density('atom/b-cm', 0.09996072)
M92.add_nuclide('U235' ,  0.001435466 )
M92.add_nuclide('U238' ,  0.000104311 )
M92.add_element('Zr'   ,  0.035292717 )
M92.add_nuclide('H1'   , 0.063128228  )
M92.add_s_alpha_beta('c_Zr_in_ZrH')
M92.add_s_alpha_beta('c_H_in_ZrH')

M93 = openmc.Material()
M93.temperature = 300.0
M93.set_density('atom/b-cm', 0.09988016)
M93.add_nuclide('U235' ,  0.001435576 )
M93.add_nuclide('U238' ,  0.000104092 )
M93.add_element('Zr'   ,  0.035293905 )
M93.add_nuclide('H1'   , 0.063046588  )
M93.add_s_alpha_beta('c_Zr_in_ZrH')
M93.add_s_alpha_beta('c_H_in_ZrH')

M94 = openmc.Material()
M94.temperature = 300.0
M94.set_density('atom/b-cm', 0.1003007)
M94.add_nuclide('U235' ,  0.001434579 )
M94.add_nuclide('U238' ,  0.000103326 )
M94.add_element('Zr'   ,  0.035310848 )
M94.add_nuclide('H1'   , 0.063451929  )
M94.add_s_alpha_beta('c_Zr_in_ZrH')
M94.add_s_alpha_beta('c_H_in_ZrH')

M95 = openmc.Material()
M95.temperature = 300.0
M95.set_density('atom/b-cm', 0.1014506)
M95.add_nuclide('U235' ,  0.001421719 )
M95.add_nuclide('U238' ,  0.00010245  )
M95.add_element('Zr'   ,  0.03498275  )
M95.add_nuclide('H1'   , 0.064943676  )
M95.add_s_alpha_beta('c_Zr_in_ZrH')
M95.add_s_alpha_beta('c_H_in_ZrH')

M96 = openmc.Material()
M96.temperature = 300.0
M96.set_density('atom/b-cm', 0.09987647)
M96.add_nuclide('U235' ,  0.001425267 )
M96.add_nuclide('U238' ,  0.000102669 )
M96.add_element('Zr'   ,  0.035080958 )
M96.add_nuclide('H1'   , 0.063267573  )
M96.add_s_alpha_beta('c_Zr_in_ZrH')
M96.add_s_alpha_beta('c_H_in_ZrH')

M97 = openmc.Material()
M97.temperature = 300.0
M97.set_density('atom/b-cm', 0.1003130)
M97.add_nuclide('U235' ,  0.001423161 )
M97.add_nuclide('U238' ,  0.000103107 )
M97.add_element('Zr'   ,  0.035280544 )
M97.add_nuclide('H1'   , 0.063506173  )
M97.add_s_alpha_beta('c_Zr_in_ZrH')
M97.add_s_alpha_beta('c_H_in_ZrH')

M98 = openmc.Material()
M98.temperature = 300.0
M98.set_density('atom/b-cm', 0.1019487)
M98.add_nuclide('U235' ,  0.00143347  )
M98.add_nuclide('U238' ,  0.000103763 )
M98.add_element('Zr'   ,  0.035522615 )
M98.add_nuclide('H1'   , 0.064888889  )
M98.add_s_alpha_beta('c_Zr_in_ZrH')
M98.add_s_alpha_beta('c_H_in_ZrH')

M99 = openmc.Material()
M99.temperature = 300.0
M99.set_density('atom/b-cm', 0.1006542)
M99.add_nuclide('U235' ,  0.001417396 )
M99.add_nuclide('U238' ,  0.000102559 )
M99.add_element('Zr'   ,  0.035331825 )
M99.add_nuclide('H1'   , 0.063802469  )
M99.add_s_alpha_beta('c_Zr_in_ZrH')
M99.add_s_alpha_beta('c_H_in_ZrH')

M100 = openmc.Material()
M100.temperature = 300.0
M100.set_density('atom/b-cm', 0.1007018)
M100.add_nuclide('U235' ,  0.001406643 )
M100.add_nuclide('U238' ,  0.000101793 )
M100.add_element('Zr'   ,  0.035094624 )
M100.add_nuclide('H1'   , 0.064098765  )
M100.add_s_alpha_beta('c_Zr_in_ZrH')
M100.add_s_alpha_beta('c_H_in_ZrH')

M101 = openmc.Material()
M101.temperature = 300.0
M101.set_density('atom/b-cm', 0.1010338)
M101.add_nuclide('U235' ,  0.001420057 )
M101.add_nuclide('U238' ,  0.000102778 )
M101.add_element('Zr'   ,  0.035313464 )
M101.add_nuclide('H1'   , 0.064197531  )
M101.add_s_alpha_beta('c_Zr_in_ZrH')
M101.add_s_alpha_beta('c_H_in_ZrH')

M102 = openmc.Material()
M102.temperature = 300.0
M102.set_density('atom/b-cm', 0.09942762)
M102.add_nuclide('U235' ,  0.001416842 )
M102.add_nuclide('U238' ,  0.000102559 )
M102.add_element('Zr'   ,  0.035290936 )
M102.add_nuclide('H1'   , 0.062617284  )
M102.add_s_alpha_beta('c_Zr_in_ZrH')
M102.add_s_alpha_beta('c_H_in_ZrH')

M103 = openmc.Material()
M103.temperature = 300.0
M103.set_density('atom/b-cm', 0.1018758)
M103.add_nuclide('U235' ,  0.001419281 )
M103.add_nuclide('U238' ,  0.000103326 )
M103.add_element('Zr'   ,  0.035464348 )
M103.add_nuclide('H1'   , 0.064888889  )
M103.add_s_alpha_beta('c_Zr_in_ZrH')
M103.add_s_alpha_beta('c_H_in_ZrH')

M104 = openmc.Material()
M104.temperature = 300.0
M104.set_density('atom/b-cm', 0.1003866)
M104.add_nuclide('U235' ,  0.001413738 )
M104.add_nuclide('U238' ,  0.000102997 )
M104.add_element('Zr'   ,  0.035462436 )
M104.add_nuclide('H1'   , 0.063407407  )
M104.add_s_alpha_beta('c_Zr_in_ZrH')
M104.add_s_alpha_beta('c_H_in_ZrH')

M105 = openmc.Material()
M105.temperature = 300.0
M105.set_density('atom/b-cm', 0.09997722)
M105.add_nuclide('U235' ,  0.001410634 )
M105.add_nuclide('U238' ,  9.34746E-05 )
M105.add_element('Zr'   ,  0.035065703 )
M105.add_nuclide('H1'   , 0.063407407  )
M105.add_s_alpha_beta('c_Zr_in_ZrH')
M105.add_s_alpha_beta('c_H_in_ZrH')

M106 = openmc.Material()
M106.temperature = 300.0
M106.set_density('atom/b-cm', 0.1001341)
M106.add_nuclide('U235' ,  0.001423604 )
M106.add_nuclide('U238' ,  0.000103435 )
M106.add_element('Zr'   ,  0.035030992 )
M106.add_nuclide('H1'   , 0.063576057  )
M106.add_s_alpha_beta('c_Zr_in_ZrH')
M106.add_s_alpha_beta('c_H_in_ZrH')

M107 = openmc.Material()
M107.temperature = 300.0
M107.set_density('atom/b-cm', 0.1011631)
M107.add_nuclide('U235' ,  0.001439235 )
M107.add_nuclide('U238' ,  0.00010453  )
M107.add_element('Zr'   ,  0.035316009 )
M107.add_nuclide('H1'   , 0.064303281  )
M107.add_s_alpha_beta('c_Zr_in_ZrH')
M107.add_s_alpha_beta('c_H_in_ZrH')

M108 = openmc.Material()
M108.temperature = 300.0
M108.set_density('atom/b-cm', 0.09922896)
M108.add_nuclide('U235' ,  0.001413294 )
M108.add_nuclide('U238' ,  0.000102669 )
M108.add_element('Zr'   ,  0.034781046 )
M108.add_nuclide('H1'   , 0.062931948  )
M108.add_s_alpha_beta('c_Zr_in_ZrH')
M108.add_s_alpha_beta('c_H_in_ZrH')

M109 = openmc.Material()
M109.temperature = 300.0
M109.set_density('atom/b-cm', 0.1018237)
M109.add_nuclide('U235' ,  0.001432362 )
M109.add_nuclide('U238' ,  0.000104311 )
M109.add_element('Zr'   ,  0.035595633 )
M109.add_nuclide('H1'   , 0.064691358  )
M109.add_s_alpha_beta('c_Zr_in_ZrH')
M109.add_s_alpha_beta('c_H_in_ZrH')

M110 = openmc.Material()
M110.temperature = 300.0
M110.set_density('atom/b-cm', 0.1003593)
M110.add_nuclide('U235' ,  0.001432251 )
M110.add_nuclide('U238' ,  0.000103982 )
M110.add_element('Zr'   ,  0.035613144 )
M110.add_nuclide('H1'   , 0.063209877  )
M110.add_s_alpha_beta('c_Zr_in_ZrH')
M110.add_s_alpha_beta('c_H_in_ZrH')

M111 = openmc.Material()
M111.temperature = 300.0
M111.set_density('atom/b-cm', 0.1027395)
M111.add_nuclide('U235' , 0.001413405  )
M111.add_nuclide('U238' ,  0.000101793 )
M111.add_element('Zr'   ,  0.035150204 )
M111.add_nuclide('H1'   , 0.066074074  )
M111.add_s_alpha_beta('c_Zr_in_ZrH')
M111.add_s_alpha_beta('c_H_in_ZrH')

M112 = openmc.Material()
M112.temperature = 300.0
M112.set_density('atom/b-cm', 0.1015556)
M112.add_nuclide('U235' ,  0.001435687  )
M112.add_nuclide('U238' ,  0.000103545  )
M112.add_element('Zr'   ,  0.035468978  )
M112.add_nuclide('H1'   , 0.064547401   )
M112.add_s_alpha_beta('c_Zr_in_ZrH')
M112.add_s_alpha_beta('c_H_in_ZrH')

M113 = openmc.Material()
M113.temperature = 300.0
M113.set_density('atom/b-cm', 0.09921034)
M113.add_nuclide('U235' ,  0.00143092  )
M113.add_nuclide('U238' ,  0.000103763 )
M113.add_element('Zr'   ,  0.035308553 )
M113.add_nuclide('H1'   , 0.062367101  )
M113.add_s_alpha_beta('c_Zr_in_ZrH')
M113.add_s_alpha_beta('c_H_in_ZrH')

M114 = openmc.Material()
M114.temperature = 300.0
M114.set_density('atom/b-cm', 0.1001203)
M114.add_nuclide('U235' ,  0.001427262 )
M114.add_nuclide('U238' ,  0.000103545 )
M114.add_element('Zr'   ,  0.035208233 )
M114.add_nuclide('H1'   , 0.063381262  )
M114.add_s_alpha_beta('c_Zr_in_ZrH')
M114.add_s_alpha_beta('c_H_in_ZrH')

M115 = openmc.Material()
M115.temperature = 300.0
M115.set_density('atom/b-cm', 0.1014453)
M115.add_nuclide('U235' ,  0.001419392 )
M115.add_nuclide('U238' ,  0.000103326 )
M115.add_element('Zr'   ,  0.035428725 )
M115.add_nuclide('H1'   , 0.064493827  )
M115.add_s_alpha_beta('c_Zr_in_ZrH')
M115.add_s_alpha_beta('c_H_in_ZrH')

M116 = openmc.Material()
M116.temperature = 300.0
M116.set_density('atom/b-cm', 0.1018192)
M116.add_nuclide('U235' ,  0.001430034 )
M116.add_nuclide('U238' ,  0.000104201 )
M116.add_element('Zr'   ,  0.035494858 )
M116.add_nuclide('H1'   , 0.064790123  )
M116.add_s_alpha_beta('c_Zr_in_ZrH')
M116.add_s_alpha_beta('c_H_in_ZrH')

M117 = openmc.Material()
M117.temperature = 300.0
M117.set_density('atom/b-cm', 0.1017473)
M117.add_nuclide('U235' ,  0.001432916 )
M117.add_nuclide('U238' ,  5.05682E-05 )
M117.add_element('Zr'   ,  0.035671272 )
M117.add_nuclide('H1'   , 0.064592593  )
M117.add_s_alpha_beta('c_Zr_in_ZrH')
M117.add_s_alpha_beta('c_H_in_ZrH')

###############################################################################
materials = openmc.Materials([M5, M6, M7, M8, M9, M10, M11,
  M81 ,M82 ,M83 ,M84 ,M85 ,M86 ,M87 ,M88 ,M89 ,
  M90 ,M91 ,M92 ,M93 ,M94 ,M95 ,M96 ,M97 ,M98 ,
  M99 ,M100,M101,M102,M103,M104,M105,M106,M107,
  M108,M109,M110,M111,M112,M113,M114,M115,M116,M117,
  M28, M29, M33, M30, M23, M32, M27, M21, M22, M26, M24, M31])


#materials.cross_sections = '/mnt/d/Codes/OpenMC/LIBS/ENDF_B/VII_1/cross_sections.xml'
materials.cross_sections = '/mnt/d/Codes/OpenMC/LIBS/ENDF_B/VIII_0/cross_sections.xml'

materials.export_to_xml()

###############################################################################
#                             Create geometry
###############################################################################

# Surfaces List
s1  = openmc.ZCylinder(surface_id=1 , x0=0.0, y0=9.6012, r=1.53924 )
s2  = openmc.ZPlane(   surface_id=2 , z0=15.52575 )
s3  = openmc.ZPlane(   surface_id=3 , z0=-15.52575 )
s4  = openmc.ZCylinder(surface_id=4 , x0=0.0, y0=9.6012, r=1.5621 )
s5  = openmc.ZCylinder(surface_id=5 , x0=0.0, y0=9.6012, r=1.5875 )
s6  = openmc.ZCylinder(surface_id=6 , r=11.27125    )
s7  = openmc.ZCylinder(surface_id=7 , r=11.34999    )
s8  = openmc.ZPlane(   surface_id=8 , z0=15.8115    )
s9  = openmc.ZPlane(   surface_id=9 , z0=-15.8115   )
s10 = openmc.ZPlane(   surface_id=10, z0=16.4465    )
s11 = openmc.ZPlane(   surface_id=11, z0=-16.4465   )
s12 = openmc.ZPlane(   surface_id=12, z0=16.85925   )
s13 = openmc.ZPlane(   surface_id=13, z0=-18.93951  )
s14 = openmc.ZPlane(   surface_id=14, z0=16.70177   )
s15 = openmc.ZPlane(   surface_id=15, z0=-19.01825  )
s16 = openmc.ZCylinder(surface_id=16, r=16.46555    )
s17 = openmc.ZPlane(   surface_id=17, z0=16.93799   )
s18 = openmc.ZPlane(   surface_id=18, z0=17.49425   )
s19 = openmc.ZPlane(   surface_id=19, z0=6.22173   )
s20 = openmc.ZPlane(   surface_id=20, z0=6.06425    )
s21 = openmc.ZPlane(   surface_id=21, z0=32.73425   )
s22 = openmc.ZPlane(   surface_id=22, z0=36.22675   )

s23 = openmc.ZCylinder(surface_id=23, r=26.67       )
s24 = openmc.ZCylinder(surface_id=24, r=26.82743    )
s25 = openmc.ZPlane(   surface_id=25, z0=-40.29075  )
s26 = openmc.ZPlane(   surface_id=26, z0=-40.60825  )
s27 = openmc.ZCylinder(surface_id=27, r=34.925      )
s28 = openmc.ZCylinder(surface_id=28, r=35.08248    )
s29 = openmc.ZPlane(   surface_id=29, z0=-32.35325  )
s30 = openmc.ZPlane(   surface_id=30, z0=-32.67075  )
s31 = openmc.ZPlane(   surface_id=31, z0=21.30425   )
s35 = openmc.ZCylinder(surface_id=35, x0=8.3149, y0=-4.8006, r=1.5875 )

#s36 = openmc.ZPlane(   surface_id=36, z0=32.73425   )

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

#s200 = openmc.ZCylinder(surface_id=200, x0=19.584677 , y0=-5.247698 , r=0.7112 )
#s201 = openmc.ZCylinder(surface_id=201, x0=19.584677 , y0=-5.247698 , r=2.2225 )
#s202 = openmc.ZCylinder(surface_id=202, x0=19.584677 , y0=-5.247698 , r=8.89   )
#s203 = openmc.ZCylinder(surface_id=203, x0=-19.584677, y0= 5.247698 , r=0.7112 )
#s204 = openmc.ZCylinder(surface_id=204, x0=-19.584677, y0= 5.247698 , r=2.2225 )
#s205 = openmc.ZCylinder(surface_id=205, x0=-19.584677, y0= 5.247698 , r=8.89   )
#s206 = openmc.ZCylinder(surface_id=206, x0=5.247698  , y0= 19.584677, r= 0.7112)
#s207 = openmc.ZCylinder(surface_id=207, x0=5.247698  , y0= 19.584677, r= 2.2225)
#s208 = openmc.ZCylinder(surface_id=208, x0=5.247698  , y0= 19.584677, r= 8.89  )
#s209 = openmc.ZCylinder(surface_id=209, x0=-5.247698 , y0=-19.584677, r= 0.7112)
#s210 = openmc.ZCylinder(surface_id=210, x0=-5.247698 , y0=-19.584677, r= 2.2225)
#s211 = openmc.ZCylinder(surface_id=211, x0=-5.247698 , y0=-19.584677, r= 8.89  )
#s300 = openmc.Plane(    surface_id=300, a=0.57735, b= -1, c= 0, d= 18.74137  )
#s301 = openmc.Plane(    surface_id=301, a=-1.732 , b= -1, c= 0, d= 33.730392 )
#s302 = openmc.Plane(    surface_id=302, a=0.57735, b= -1, c= 0, d= -18.74137 )
#s303 = openmc.Plane(    surface_id=303, a=-1.732 , b= -1, c= 0, d= -33.73092 )
#s401 = openmc.Plane(    surface_id=401, a=-1.732 , b= -1, c= 0, d= 37.2427   )
#s403 = openmc.Plane(    surface_id=403, a=-1.732 , b= -1, c= 0, d= -37.2434  )
#s500 = openmc.ZPlane(   surface_id=500, z0=12.87018 )
#s501 = openmc.ZPlane(   surface_id=501, z0=-12.84478)
#s502 = openmc.ZPlane(   surface_id=502, z0=-15.5448 )
#s503 = openmc.ZPlane(   surface_id=503, z0=15.5702  )
#s504 = openmc.ZCylinder(surface_id=504,  r=16.2306  )
#s505 = openmc.ZPlane(   surface_id=505, z0=3.81     )
#s506 = openmc.ZPlane(   surface_id=506, z0=-3.81    )

s100  = openmc.ZCylinder(surface_id=100, x0=7.34, y0=-6.31, r=0.208)
s101  = openmc.ZCylinder(surface_id=101, x0=7.34, y0=-6.31, r=0.208001)

s999 = openmc.Sphere(   surface_id=999, r=55       , boundary_type = 'vacuum')
  
#============================================================================
# CELLS define
# cell: 300
C300 = openmc.Cell(cell_id=300, region=-s6 & -s8 & +s9)
un = openmc.Universe(cells=[C300])

trcl81 = [7.34     , -6.31 , 0]
trcl82 = [ -5.51  ,  -0.12, 0]
trcl84 = [ 1.795  ,  3.11 , 0]
trcl85 = [ -11.08 ,  -0.08, 0]
trcl86 = [ -6.39  ,  4.67 , 0]
trcl87 = [ -.84   ,  7.90 , 0]
trcl88 = [ -16.475,  3.11 , 0]
trcl89 = [ -11.08 ,  6.35 , 0]
trcl90 = [ -5.51  ,  9.5  , 0]
trcl91 = [ -3.66  ,  12.74, 0]
trcl93 = [ -14.7  ,  9.55 , 0]
trcl95 = [ -11.05 ,  12.7 , 0]
#
C51 = openmc.Cell(cell_id=51, fill=M28, region=-s100 &-s2 &+s3) #u=28 
C52 = openmc.Cell(cell_id=52,           region=+s100|+s2|-s3) # #u=28 
u28 = openmc.Universe()
u28.add_cells([C51,C52])
# c $
C53 = openmc.Cell(cell_id=53, fill=M29, region=-s100 &-s2 &+s3) # u=29 
C54 = openmc.Cell(cell_id=54, region=+s100|+s2|-s3) #  u=29 
u29 = openmc.Universe()
u29.add_cells([C53,C54])
# c $
#c 55 35 .021382 region=-s100 &-s2 &+s3) # u=35 
#c 56 0 region=+s100|+s2|-s3) #  u=35 
# c $
C57 = openmc.Cell(cell_id=57, fill=M33, region=-s100 &-s2 &+s3) # u=33 
C58 = openmc.Cell(cell_id=58, region=+s100|+s2|-s3) #  u=33 
u33 = openmc.Universe()
u33.add_cells([C57,C58])
# c $
C59 = openmc.Cell(cell_id=59, fill=M30, region=-s100 &-s2 &+s3) # u=30 
C60 = openmc.Cell(cell_id=60, region=+s100|+s2|-s3) #  u=30 
u30 = openmc.Universe()
u30.add_cells([C59,C60])
# c $
C61 = openmc.Cell(cell_id=61, fill=M23, region=-s100 &-s2 &+s3) # u=23 
C62 = openmc.Cell(cell_id=62, region=+s100|+s2|-s3) #  u=23 
u23 = openmc.Universe()
u23.add_cells([C61,C62])
# c $
C63 = openmc.Cell(cell_id=63, fill=M32, region=-s100 &-s2 &+s3) # u=32 
C64 = openmc.Cell(cell_id=64, region=+s100|+s2|-s3) #  u=32 
u32 = openmc.Universe()
u32.add_cells([C63,C64])
# c $
C65 = openmc.Cell(cell_id=65, fill=M27, region=-s100 &-s2 &+s3) # u=27 
C66 = openmc.Cell(cell_id=66, region=+s100|+s2|-s3) #  u=27 
u27 = openmc.Universe()
u27.add_cells([C65,C66])
# c $
C67 = openmc.Cell(cell_id=67, fill=M21, region=-s100 &-s2 &+s3) # u=21 
C68 = openmc.Cell(cell_id=68, region=+s100|+s2|-s3) #  u=21 
u21 = openmc.Universe()
u21.add_cells([C67,C68])
# c $
C69 = openmc.Cell(cell_id=69, fill=M22, region=-s100 &-s2 &+s3) # u=22 
C70 = openmc.Cell(cell_id=70, region=+s100|+s2|-s3) #  u=22 
u22 = openmc.Universe()
u22.add_cells([C69,C70])
# c $
C71 = openmc.Cell(cell_id=71, fill=M26, region=-s100 &-s2 &+s3) # u=26 
C72 = openmc.Cell(cell_id=72, region=+s100|+s2|-s3) #  u=26 
u26 = openmc.Universe()
u26.add_cells([C71,C72])
# c $
#c 73 34 .022438 region=-s100 &-s2 &+s3) # u=34 
#c 74 0 region=+s100|+s2|-s3) #  u=34 
# c $
C75 = openmc.Cell(cell_id=75, fill=M24, region=-s100 &-s2 &+s3) # u=24 
C76 = openmc.Cell(cell_id=76, region=+s100|+s2|-s3) #  u=24 
u24 = openmc.Universe()
u24.add_cells([C75,C76])
# c $
#c 77 25 .021514 region=-s100 &-s2 &+s3) # u=25 
#c 78 0 region=+s100|+s2|-s3) #  u=25 
# c $
C79 = openmc.Cell(cell_id=79, fill=M31, region=-s100 &-s2 &+s3) # u=31 
C80 = openmc.Cell(cell_id=80, region=+s100|+s2|-s3) #  u=31 
u31 = openmc.Universe()
u31.add_cells([C79,C80])

s81101 = openmc.ZCylinder(surface_id=81101, x0=s101.x0, y0=s101.y0, r=s101.r)
s82101 = openmc.ZCylinder(surface_id=82101, x0=s101.x0 + trcl82[0], y0=s101.y0 + trcl82[1], r=s101.r)
s84101 = openmc.ZCylinder(surface_id=84101, x0=s101.x0 + trcl84[0], y0=s101.y0 + trcl84[1], r=s101.r)
s85101 = openmc.ZCylinder(surface_id=85101, x0=s101.x0 + trcl85[0], y0=s101.y0 + trcl85[1], r=s101.r)
s86101 = openmc.ZCylinder(surface_id=86101, x0=s101.x0 + trcl86[0], y0=s101.y0 + trcl86[1], r=s101.r)
s87101 = openmc.ZCylinder(surface_id=87101, x0=s101.x0 + trcl87[0], y0=s101.y0 + trcl87[1], r=s101.r)
s88101 = openmc.ZCylinder(surface_id=88101, x0=s101.x0 + trcl88[0], y0=s101.y0 + trcl88[1], r=s101.r)
s89101 = openmc.ZCylinder(surface_id=89101, x0=s101.x0 + trcl89[0], y0=s101.y0 + trcl89[1], r=s101.r)
s90101 = openmc.ZCylinder(surface_id=90101, x0=s101.x0 + trcl90[0], y0=s101.y0 + trcl90[1], r=s101.r)
s91101 = openmc.ZCylinder(surface_id=91101, x0=s101.x0 + trcl91[0], y0=s101.y0 + trcl91[1], r=s101.r)
s93101 = openmc.ZCylinder(surface_id=93101, x0=s101.x0 + trcl93[0], y0=s101.y0 + trcl93[1], r=s101.r)
s95101 = openmc.ZCylinder(surface_id=95101, x0=s101.x0 + trcl95[0], y0=s101.y0 + trcl95[1], r=s101.r)

# c ------ fill each spline position with the correct spline:$
C81 = openmc.Cell(cell_id=81, fill=u28, region= -s81101 &+s9 &-s8 )
C82 = openmc.Cell(cell_id=82, fill=u29, region= -s82101 &+s9 &-s8 )
C84 = openmc.Cell(cell_id=84, fill=u33, region= -s84101 &+s9 &-s8 )
C85 = openmc.Cell(cell_id=85, fill=u30, region= -s85101 &+s9 &-s8 )
C86 = openmc.Cell(cell_id=86, fill=u23, region= -s86101 &+s9 &-s8 )
C87 = openmc.Cell(cell_id=87, fill=u32, region= -s87101 &+s9 &-s8 )
C88 = openmc.Cell(cell_id=88, fill=u27, region= -s88101 &+s9 &-s8 )
C89 = openmc.Cell(cell_id=89, fill=u21, region= -s89101 &+s9 &-s8 )
C90 = openmc.Cell(cell_id=90, fill=u22, region= -s90101 &+s9 &-s8 )
C91 = openmc.Cell(cell_id=91, fill=u26, region= -s91101 &+s9 &-s8 )
C93 = openmc.Cell(cell_id=93, fill=u24, region= -s93101 &+s9 &-s8 )
C95 = openmc.Cell(cell_id=95, fill=u31, region= -s95101 &+s9 &-s8 )

C81.translation = (0.0, 0.0, 0.0)
C82.translation = trcl82
C84.translation = trcl84
C85.translation = trcl85
C86.translation = trcl86
C87.translation = trcl87
C88.translation = trcl88
C89.translation = trcl89
C90.translation = trcl90
C91.translation = trcl91
C93.translation = trcl93
C95.translation = trcl95

un.add_cells([C81,C82,C84,C85,C86,C87,C88,C89,C90,C91,C93,C95])
# univ
C98 = openmc.Cell(cell_id=98 , fill=M10 , region = -s4 & -s2 & +s3 ) # u=2 
C99 = openmc.Cell(cell_id=99 , fill=M10 , region = +s4 | +s2 | -s3  ) # u=2 
C101= openmc.Cell(cell_id=101, fill=M81 , region = -s1 & -s2 & +s3 ) # u= 581  
C102= openmc.Cell(cell_id=102, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 581  
C103= openmc.Cell(cell_id=103, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 581  
C104= openmc.Cell(cell_id=104, fill=M82 , region = -s1 & -s2 & +s3 ) # u= 582  
C105= openmc.Cell(cell_id=105, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 582  
C106= openmc.Cell(cell_id=106, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 582  
C107= openmc.Cell(cell_id=107, fill=M83 , region = -s1 & -s2 & +s3 ) # u= 583  
C108= openmc.Cell(cell_id=108, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 583  
C109= openmc.Cell(cell_id=109, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 583  
C110= openmc.Cell(cell_id=110, fill=M84 , region = -s1 & -s2 & +s3 ) # u= 584  
C111= openmc.Cell(cell_id=111, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 584 
C112= openmc.Cell(cell_id=112, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 584 
C113= openmc.Cell(cell_id=113, fill=M85 , region = -s1 & -s2 & +s3 ) # u= 585 
C114= openmc.Cell(cell_id=114, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 585 
C115= openmc.Cell(cell_id=115, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 585 
C116= openmc.Cell(cell_id=116, fill=M86 , region = -s1 & -s2 & +s3 ) # u= 586 
C117= openmc.Cell(cell_id=117, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 586 
C118= openmc.Cell(cell_id=118, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 586 
C119= openmc.Cell(cell_id=119, fill=M87 , region = -s1 & -s2 & +s3 ) # u= 587 
C120= openmc.Cell(cell_id=120, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 587 
C121= openmc.Cell(cell_id=121, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 587 
C122= openmc.Cell(cell_id=122, fill=M88 , region = -s1 & -s2 & +s3 ) # u= 588 
C123= openmc.Cell(cell_id=123, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 588 
C124= openmc.Cell(cell_id=124, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 588 
C125= openmc.Cell(cell_id=125, fill=M89 , region = -s1 & -s2 & +s3 ) # u= 589 
C126= openmc.Cell(cell_id=126, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 589 
C127= openmc.Cell(cell_id=127, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 589 
C128= openmc.Cell(cell_id=128, fill=M90 , region = -s1 & -s2 & +s3 ) # u= 590 
C129= openmc.Cell(cell_id=129, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 590 
C130= openmc.Cell(cell_id=130, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 590 
C131= openmc.Cell(cell_id=131, fill=M91 , region = -s1 & -s2 & +s3 ) # u= 591 
C132= openmc.Cell(cell_id=132, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 591 
C133= openmc.Cell(cell_id=133, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 591 
C134= openmc.Cell(cell_id=134, fill=M92 , region =  -s1 & -s2 & +s3 ) # u= 592 
C135= openmc.Cell(cell_id=135, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 592 
C136= openmc.Cell(cell_id=136, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 592 
C137= openmc.Cell(cell_id=137, fill=M93 , region =  -s1 & -s2 & +s3 ) # u= 593 
C138= openmc.Cell(cell_id=138, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 593 
C139= openmc.Cell(cell_id=139, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 593 
C140= openmc.Cell(cell_id=140, fill=M94 , region = -s1 & -s2 & +s3 ) # u= 594 
C141= openmc.Cell(cell_id=141, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 594 
C142= openmc.Cell(cell_id=142, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 594 
C143= openmc.Cell(cell_id=143, fill=M95 , region = -s1 & -s2 & +s3 ) # u= 595 
C144= openmc.Cell(cell_id=144, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 595 
C145= openmc.Cell(cell_id=145, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 595 
C146= openmc.Cell(cell_id=146, fill=M96 , region =  -s1 & -s2 & +s3 ) # u= 596 
C147= openmc.Cell(cell_id=147, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 596 
C148= openmc.Cell(cell_id=148, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 596 
C149= openmc.Cell(cell_id=149, fill=M97 , region = -s1 & -s2 & +s3 ) # u= 597 
C150= openmc.Cell(cell_id=150, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 597 
C151= openmc.Cell(cell_id=151, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 597 
C152= openmc.Cell(cell_id=152, fill=M98 , region = -s1 & -s2 & +s3 ) # u= 598 
C153= openmc.Cell(cell_id=153, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 598 
C154= openmc.Cell(cell_id=154, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 598 
C155= openmc.Cell(cell_id=155, fill=M99 , region = -s1 & -s2 & +s3 ) # u= 599 
C156= openmc.Cell(cell_id=156, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 599 
C157= openmc.Cell(cell_id=157, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 599 
C158= openmc.Cell(cell_id=158, fill=M100, region = -s1 & -s2 & +s3 ) # u= 500 
C159= openmc.Cell(cell_id=159, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 500 
C160= openmc.Cell(cell_id=160, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 500 
C161= openmc.Cell(cell_id=161, fill=M101, region = -s1 & -s2 & +s3 ) # u= 501 
C162= openmc.Cell(cell_id=162, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 501 
C163= openmc.Cell(cell_id=163, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 501 
C164= openmc.Cell(cell_id=164, fill=M102, region =  -s1 & -s2 & +s3 ) # u= 502 
C165= openmc.Cell(cell_id=165, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 502 
C166= openmc.Cell(cell_id=166, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 502 
C167= openmc.Cell(cell_id=167, fill=M103, region = -s1 & -s2 & +s3 ) # u= 503 
C168= openmc.Cell(cell_id=168, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 503 
C169= openmc.Cell(cell_id=169, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 503 
C170= openmc.Cell(cell_id=170, fill=M104, region = -s1 & -s2 & +s3 ) # u= 504 
C171= openmc.Cell(cell_id=171, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 504 
C172= openmc.Cell(cell_id=172, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 504 
C173= openmc.Cell(cell_id=173, fill=M105, region =  -s1 & -s2 & +s3 ) # u= 505 
C174= openmc.Cell(cell_id=174, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 505 
C175= openmc.Cell(cell_id=175, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 505 
C176= openmc.Cell(cell_id=176, fill=M106, region = -s1 & -s2 & +s3 ) # u= 506 
C177= openmc.Cell(cell_id=177, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 506 
C178= openmc.Cell(cell_id=178, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 506 
C179= openmc.Cell(cell_id=179, fill=M107, region = -s1 & -s2 & +s3 ) # u= 507 
C180= openmc.Cell(cell_id=180, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 507 
C181= openmc.Cell(cell_id=181, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 507 
C182= openmc.Cell(cell_id=182, fill=M108, region =  -s1 & -s2 & +s3 ) # u= 508 
C183= openmc.Cell(cell_id=183, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 508 
C184= openmc.Cell(cell_id=184, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 508 
C185= openmc.Cell(cell_id=185, fill=M109, region = -s1 & -s2 & +s3 ) # u= 509 
C186= openmc.Cell(cell_id=186, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 509 
C187= openmc.Cell(cell_id=187, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 509 
C188= openmc.Cell(cell_id=188, fill=M110, region = -s1 & -s2 & +s3 ) # u= 510 
C189= openmc.Cell(cell_id=189, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 510 
C190= openmc.Cell(cell_id=190, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 510 
C191= openmc.Cell(cell_id=191, fill=M111, region = -s1 & -s2 & +s3 ) # u= 511 
C192= openmc.Cell(cell_id=192, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 511 
C193= openmc.Cell(cell_id=193, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 511 
C194= openmc.Cell(cell_id=194, fill=M112, region = -s1 & -s2 & +s3 ) # u= 512 
C195= openmc.Cell(cell_id=195, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 512 
C196= openmc.Cell(cell_id=196, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 512 
C197= openmc.Cell(cell_id=197, fill=M113, region =  -s1 & -s2 & +s3 ) # u= 513 
C198= openmc.Cell(cell_id=198, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 513 
C199= openmc.Cell(cell_id=199, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 513 
C200= openmc.Cell(cell_id=200, fill=M114, region = -s1 & -s2 & +s3 ) # u= 514 
C201= openmc.Cell(cell_id=201, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 514 
C202= openmc.Cell(cell_id=202, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 514 
C203= openmc.Cell(cell_id=203, fill=M115, region = -s1 & -s2 & +s3 ) # u= 515 
C204= openmc.Cell(cell_id=204, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 515 
C205= openmc.Cell(cell_id=205, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 515 
C206= openmc.Cell(cell_id=206, fill=M116, region = -s1 & -s2 & +s3 ) # u= 516 
C207= openmc.Cell(cell_id=207, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 516 
C208= openmc.Cell(cell_id=208, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 516 
C209= openmc.Cell(cell_id=209, fill=M117, region = -s1 & -s2 & +s3 ) # u= 517 
C210= openmc.Cell(cell_id=210, fill=M5  , region = -s4 & +s1 & -s2 & +s3 ) # u= 517 
C211= openmc.Cell(cell_id=211, fill=M8  , region = +s4 | +s2 | -s3 ) # u= 517 

# uni
u2   = openmc.Universe()
u581 = openmc.Universe()
u582 = openmc.Universe()
u583 = openmc.Universe()
u584 = openmc.Universe()
u585 = openmc.Universe()
u586 = openmc.Universe()
u587 = openmc.Universe()
u588 = openmc.Universe()
u589 = openmc.Universe()
u590 = openmc.Universe()
u591 = openmc.Universe()
u592 = openmc.Universe()
u593 = openmc.Universe()
u594 = openmc.Universe()
u595 = openmc.Universe()
u596 = openmc.Universe()
u597 = openmc.Universe()
u598 = openmc.Universe()
u599 = openmc.Universe()
u500 = openmc.Universe()
u501 = openmc.Universe()
u502 = openmc.Universe()
u503 = openmc.Universe()
u504 = openmc.Universe()
u505 = openmc.Universe()
u506 = openmc.Universe()
u507 = openmc.Universe()
u508 = openmc.Universe()
u509 = openmc.Universe()
u510 = openmc.Universe()
u511 = openmc.Universe()
u512 = openmc.Universe()
u513 = openmc.Universe()
u514 = openmc.Universe()
u515 = openmc.Universe()
u516 = openmc.Universe()
u517 = openmc.Universe()


u2.add_cell(C98)
u2.add_cell(C99)
u581.add_cell(C101)
u581.add_cell(C102)
u581.add_cell(C103)
u582.add_cell(C104)
u582.add_cell(C105)
u582.add_cell(C106)
u583.add_cell(C107)
u583.add_cell(C108)
u583.add_cell(C109)
u584.add_cell(C110)
u584.add_cell(C111)
u584.add_cell(C112)
u585.add_cell(C113)
u585.add_cell(C114)
u585.add_cell(C115)
u586.add_cell(C116)
u586.add_cell(C117)
u586.add_cell(C118)
u587.add_cell(C119)
u587.add_cell(C120)
u587.add_cell(C121)
u588.add_cell(C122)
u588.add_cell(C123)
u588.add_cell(C124)
u589.add_cell(C125)
u589.add_cell(C126)
u589.add_cell(C127)
u590.add_cell(C128)
u590.add_cell(C129)
u590.add_cell(C130)
u591.add_cell(C131)
u591.add_cell(C132)
u591.add_cell(C133)
u592.add_cell(C134)
u592.add_cell(C135)
u592.add_cell(C136)
u593.add_cell(C137)
u593.add_cell(C138)
u593.add_cell(C139)
u594.add_cell(C140)
u594.add_cell(C141)
u594.add_cell(C142)
u595.add_cell(C143)
u595.add_cell(C144)
u595.add_cell(C145)
u596.add_cell(C146)
u596.add_cell(C147)
u596.add_cell(C148)
u597.add_cell(C149)
u597.add_cell(C150)
u597.add_cell(C151)
u598.add_cell(C152)
u598.add_cell(C153)
u598.add_cell(C154)
u599.add_cell(C155)
u599.add_cell(C156)
u599.add_cell(C157)
u500.add_cell(C158)
u500.add_cell(C159)
u500.add_cell(C160)
u501.add_cell(C161)
u501.add_cell(C162)
u501.add_cell(C163)
u502.add_cell(C164)
u502.add_cell(C165)
u502.add_cell(C166)
u503.add_cell(C167)
u503.add_cell(C168)
u503.add_cell(C169)
u504.add_cell(C170)
u504.add_cell(C171)
u504.add_cell(C172)
u505.add_cell(C173)
u505.add_cell(C174)
u505.add_cell(C175)
u506.add_cell(C176)
u506.add_cell(C177)
u506.add_cell(C178)
u507.add_cell(C179)
u507.add_cell(C180)
u507.add_cell(C181)
u508.add_cell(C182)
u508.add_cell(C183)
u508.add_cell(C184)
u509.add_cell(C185)
u509.add_cell(C186)
u509.add_cell(C187)
u510.add_cell(C188)
u510.add_cell(C189)
u510.add_cell(C190)
u511.add_cell(C191)
u511.add_cell(C192)
u511.add_cell(C193)
u512.add_cell(C194)
u512.add_cell(C195)
u512.add_cell(C196)
u513.add_cell(C197)
u513.add_cell(C198)
u513.add_cell(C199)
u514.add_cell(C200)
u514.add_cell(C201)
u514.add_cell(C202)
u515.add_cell(C203)
u515.add_cell(C204)
u515.add_cell(C205)
u516.add_cell(C206)
u516.add_cell(C207)
u516.add_cell(C208)
u517.add_cell(C209)
u517.add_cell(C210)
u517.add_cell(C211)

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
trcl30 = [8.3149 , -11.2014, 0]
trcl31 = [0.0    , -19.2024, 0]
trcl32 = [-2.7716, -17.6022, 0]

#
trcl37 = [8.3149 , -14.4018,  0]
trcl36 = [5.5432 , -16.002 ,  0]
trcl35 = [2.7716 , -17.6022,  0]
trcl34 = [-8.3149, -14.4018,  0]
trcl33 = [-5.5432, -16.002 ,  0]

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
s1030 = openmc.ZCylinder(surface_id = 1030, x0 = trcl1[0] + trcl30[0], y0 = trcl1[1] + trcl30[1], r=1.58750)
s1031 = openmc.ZCylinder(surface_id = 1031, x0 = trcl1[0] + trcl31[0], y0 = trcl1[1] + trcl31[1], r=1.58750)
s1032 = openmc.ZCylinder(surface_id = 1032, x0 = trcl1[0] + trcl32[0], y0 = trcl1[1] + trcl32[1], r=1.58750)
s1037 = openmc.ZCylinder(surface_id = 1037, x0 = trcl1[0] + trcl37[0], y0 = trcl1[1] + trcl37[1], r=1.58750)
s1036 = openmc.ZCylinder(surface_id = 1036, x0 = trcl1[0] + trcl36[0], y0 = trcl1[1] + trcl36[1], r=1.58750)
s1035 = openmc.ZCylinder(surface_id = 1035, x0 = trcl1[0] + trcl35[0], y0 = trcl1[1] + trcl35[1], r=1.58750)
s1034 = openmc.ZCylinder(surface_id = 1034, x0 = trcl1[0] + trcl34[0], y0 = trcl1[1] + trcl34[1], r=1.58750)
s1033 = openmc.ZCylinder(surface_id = 1033, x0 = trcl1[0] + trcl33[0], y0 = trcl1[1] + trcl33[1], r=1.58750)

# cell:1-X
C1  = openmc.Cell(cell_id=1 ,fill=u582, region=-s1001 & -s8 & +s9)
C2  = openmc.Cell(cell_id=2 ,fill=u587, region=-s1002 & -s8 & +s9)
C3  = openmc.Cell(cell_id=3 ,fill=u504, region=-s1003 & -s8 & +s9)
C4  = openmc.Cell(cell_id=4 ,fill=u583, region=-s1004 & -s8 & +s9)
C5  = openmc.Cell(cell_id=5 ,fill=u507, region=-s1005 & -s8 & +s9)
C6  = openmc.Cell(cell_id=6 ,fill=u503, region=-s1006 & -s8 & +s9)
C7  = openmc.Cell(cell_id=7 ,fill=u590, region=-s1007 & -s8 & +s9)
C8  = openmc.Cell(cell_id=8 ,fill=u594, region=-s1008 & -s8 & +s9)
C9  = openmc.Cell(cell_id=9 ,fill=u597, region=-s1009 & -s8 & +s9)
C10 = openmc.Cell(cell_id=10,fill=u593, region=-s1010 & -s8 & +s9)
C11 = openmc.Cell(cell_id=11,fill=u505, region=-s1011 & -s8 & +s9)
C12 = openmc.Cell(cell_id=12,fill=u514,   region=-s1012 & -s8 & +s9)
C13 = openmc.Cell(cell_id=13,fill=u585, region=-s1013 & -s8 & +s9)
C14 = openmc.Cell(cell_id=14,fill=u589, region=-s1014 & -s8 & +s9)
C15 = openmc.Cell(cell_id=15,fill=u500, region=-s1015 & -s8 & +s9)
C16 = openmc.Cell(cell_id=16,fill=u501, region=-s1016 & -s8 & +s9)
C17 = openmc.Cell(cell_id=17,fill=u502, region=-s1017 & -s8 & +s9)
C18 = openmc.Cell(cell_id=18,fill=u506, region=-s1018 & -s8 & +s9)
C19 = openmc.Cell(cell_id=19,fill=u513, region=-s1019 & -s8 & +s9)
C20 = openmc.Cell(cell_id=20,fill=u584, region=-s1020 & -s8 & +s9)
C21 = openmc.Cell(cell_id=21,fill=u510, region=-s1021 & -s8 & +s9)
C22 = openmc.Cell(cell_id=22,fill=u588, region=-s1022 & -s8 & +s9)
C23 = openmc.Cell(cell_id=23,fill=u599, region=-s1023 & -s8 & +s9)
C24 = openmc.Cell(cell_id=24,fill=u509, region=-s1024 & -s8 & +s9)
C25 = openmc.Cell(cell_id=25,fill=u581, region=-s1025 & -s8 & +s9)
C26 = openmc.Cell(cell_id=26,fill=u512, region=-s1026 & -s8 & +s9)
C27 = openmc.Cell(cell_id=27,fill=u515, region=-s1027 & -s8 & +s9)
C28 = openmc.Cell(cell_id=28,fill=u508, region=-s1028 & -s8 & +s9)
C29 = openmc.Cell(cell_id=29,fill=u511, region=-s1029 & -s8 & +s9)
C30 = openmc.Cell(cell_id=30,fill=u592, region=-s1030 & -s8 & +s9)
C31 = openmc.Cell(cell_id=31,fill=u516, region=-s1031 & -s8 & +s9)
C32 = openmc.Cell(cell_id=32,fill=u598, region=-s1032 & -s8 & +s9)
C37 = openmc.Cell(cell_id=37,fill=u595, region=-s1037 & -s8 & +s9)
C36 = openmc.Cell(cell_id=36,fill=u591, region=-s1036 & -s8 & +s9)
C35 = openmc.Cell(cell_id=35,fill=u596, region=-s1035 & -s8 & +s9)
C34 = openmc.Cell(cell_id=34,fill=u517, region=-s1034 & -s8 & +s9)
C33 = openmc.Cell(cell_id=33,fill=u586, region=-s1033 & -s8 & +s9)

C41 = openmc.Cell(cell_id=41,fill=M11,region=-s44 &-s45 &+s46 &+s51 &+s57 &+s58 &+s59 &+s60 &-s8 &+s9)
C42 = openmc.Cell(cell_id=42,fill=M11,region=-s44 &-s47 &+s48 &+s52 &+s60 &+s61 &+s62 &+s63 &-s8 &+s9)
C43 = openmc.Cell(cell_id=43,fill=M11,region=-s44 &-s49 &+s50 &-s53 &+s63 &+s64 &+s65 &+s66 &-s8 &+s9)
C44 = openmc.Cell(cell_id=44,fill=M11,region=-s44 &-s45 &+s46 &-s54 &+s66 &+s67 &+s68 &+s69 &-s8 &+s9)
C45 = openmc.Cell(cell_id=45,fill=M11,region=-s44 &-s47 &+s48 &-s55 &+s69 &+s70 &+s71 &+s72 &-s8 &+s9)
C46 = openmc.Cell(cell_id=46,fill=M11,region=-s44 &-s49 &+s50 &+s56 &+s72 &+s73 &+s74 &+s57 &-s8 &+s9)

# pick out the fuel pin region from C300
C300.region = C300.region & (~C1.region)
C300.region = C300.region & (~C2.region)
C300.region = C300.region & (~C3.region)
C300.region = C300.region & (~C4.region)
C300.region = C300.region & (~C5.region)
C300.region = C300.region & (~C6.region)
C300.region = C300.region & (~C7.region)
C300.region = C300.region & (~C8.region)
C300.region = C300.region & (~C9.region)
C300.region = C300.region & (~C10.region)
C300.region = C300.region & (~C11.region)
C300.region = C300.region & (~C12.region)
C300.region = C300.region & (~C13.region)
C300.region = C300.region & (~C14.region)
C300.region = C300.region & (~C15.region)
C300.region = C300.region & (~C16.region)
C300.region = C300.region & (~C17.region)
C300.region = C300.region & (~C18.region)
C300.region = C300.region & (~C19.region)
C300.region = C300.region & (~C20.region)
C300.region = C300.region & (~C21.region)
C300.region = C300.region & (~C22.region)
C300.region = C300.region & (~C23.region)
C300.region = C300.region & (~C24.region)
C300.region = C300.region & (~C25.region)
C300.region = C300.region & (~C26.region)
C300.region = C300.region & (~C27.region)
C300.region = C300.region & (~C28.region)
C300.region = C300.region & (~C29.region)
C300.region = C300.region & (~C30.region)
C300.region = C300.region & (~C31.region)
C300.region = C300.region & (~C32.region)
C300.region = C300.region & (~C33.region)
C300.region = C300.region & (~C34.region)
C300.region = C300.region & (~C35.region)
C300.region = C300.region & (~C36.region)
C300.region = C300.region & (~C37.region)

C300.region = C300.region & (~C41.region)
C300.region = C300.region & (~C42.region)
C300.region = C300.region & (~C43.region)
C300.region = C300.region & (~C44.region)
C300.region = C300.region & (~C45.region)
C300.region = C300.region & (~C46.region)

C300.region = C300.region & (~C81.region)
C300.region = C300.region & (~C82.region)
C300.region = C300.region & (~C84.region)
C300.region = C300.region & (~C85.region)
C300.region = C300.region & (~C86.region)
C300.region = C300.region & (~C87.region)
C300.region = C300.region & (~C88.region)
C300.region = C300.region & (~C89.region)
C300.region = C300.region & (~C90.region)
C300.region = C300.region & (~C91.region)
C300.region = C300.region & (~C93.region)
C300.region = C300.region & (~C95.region)


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
C30.translation = trcl30
C31.translation = trcl31
C32.translation = trcl32

C33.translation = trcl33
C34.translation = trcl34
C35.translation = trcl35
C36.translation = trcl36
C37.translation = trcl37

# add cell in un
un.add_cells([C1 , C2 , C3 , C4 , C5 , C6 , C7 , C8 , C9])
un.add_cells([C10, C11, C12, C13, C14, C15, C16, C17, C18])
un.add_cells([C19, C20, C21, C22, C23, C24, C25, C26, C27, C28])
un.add_cells([C29, C30, C31, C32, C33, C34, C35, C36, C37])
un.add_cells([C41, C42, C43, C44, C45, C46])

# add cells
C301 = openmc.Cell(cell_id=401,fill=M6,region=-s6 & +s8  & -s10)
C302 = openmc.Cell(cell_id=402,fill=M6,region=-s6 & -s9  & +s11)
C303 = openmc.Cell(cell_id=403,        region=-s6 & +s10 & -s12)
C304 = openmc.Cell(cell_id=404,        region=-s6 & -s11 & +s13)
C305 = openmc.Cell(cell_id=405,fill=M9,region=(-s7 & -s13 & +s15)|(-s7 & +s6 & -s14 & +s13)|(-s16 & +s6 & -s12 & +s14))
C306 = openmc.Cell(cell_id=406,fill=M6,region=(-s6 & -s17 & +s12)|(-s16 & +s6 &-s18 &+s12))
un.add_cells([C301,C302,C303,C304,C305,C306])

C307 = openmc.Cell(cell_id=307,fill=M7,  region=(+s29 &-s15 &-s27 )|(+s15 &-s20 &-s27 &+s7) )
C308 = openmc.Cell(cell_id=308,fill=M7,  region=(+s20 &-s31 &+s24 &-s27) )
C309 = openmc.Cell(cell_id=309,fill=M9,  region=(+s26 &-s25 &-s28)|(+s27 &-s28 &-s31 &+s25) )
C310 = openmc.Cell(cell_id=310,          region=-s27 &+s25 &-s30 )
C311 = openmc.Cell(cell_id=311,fill=M9,  region=-s29 &+s30 &-s27 )
C312 = openmc.Cell(cell_id=312,          region=+s31 &-s22 &+s24 &-s28 )
C313 = openmc.Cell(cell_id=313,fill=M9,  region=(-s19 &+s20 &+s7 &-s24)|(-s24 &+s23 &+s19 &-s22) )
C314 = openmc.Cell(cell_id=314,fill=M7,  region=(+s19 &-s14 &+s7 &-s23)|(+s14 &-s18 &+s16 &-s23)|(+s17 &-s18 &-s6)|(+s18 &-s21 &-s23) )
C315 = openmc.Cell(cell_id=315,          region=(+s21 &-s22 &-s23))
un.add_cells([C307, C308, C309, C310, C311, C312, C313, C314, C315])

C316 = openmc.Cell(cell_id=316,         region=(+s22 &-s999)|(-s22 &+s31 &+s28 &-s999)|(+s28 &-s999 &+s26 &-s31)|(-s26 &-s999)) 
un.add_cell(C316)

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

plot5 = openmc.Plot(plot_id=5)
plot5.basis = 'xy'
plot5.origin = [0.0, 0.0, 0.0]
plot5.width = [22.0, 22.0]
plot5.pixels = [2000, 2000]
plot5.color_by = 'material'

plot6 = openmc.Plot(plot_id=6)
plot6.basis = 'xy'
plot6.origin = [0.0, 0.0, 0.0]
plot6.width = [22.0, 22.0]
plot6.pixels = [2000, 2000]
plot6.color_by = 'cell'

# Instantiate a Plots collection and export to XML
plot_file = openmc.Plots([plot1,plot2,plot3,plot4,plot5,plot6])
plot_file.export_to_xml()


###############################################################################
os.system('openmc -p')

###############################################################################
os.system('openmc -s 8')