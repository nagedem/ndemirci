#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:51:07 2019

@author: nagedem
"""

# Discrete vs Continuous Result Comparisons for Surface Data

# Mean of the White Surface

import matplotlib.pyplot as plt
import numpy as np

white_Hcont_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/continuous/white/lh.white.H.cont.asc")
white_Hdisc_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/discrete/white/lh.white.H.discrete.asc")

white_Hcont = white_Hcont_data[:, 4]
white_Hdisc = white_Hdisc_data[:, 4]

vertices = white_Hcont_data[:, 0]

plt.plot(vertices, white_Hdisc, ',r')
# plt.figure(2)
plt.plot(vertices, white_Hcont, ',k')
plt.show()

# Gaussian of the White Surface

white_Kcont_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/continuous/white/lh.white.K.cont.asc")
white_Kdisc_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/discrete/white/lh.white.K.discrete.asc")

white_Kcont = white_Kcont_data[:, 4]
white_Kdisc = white_Kdisc_data[:, 4]

vertices = white_Kcont_data[:, 0]

#plt.ylim(-50, 50)
plt.plot(vertices, white_Kdisc, ',r')
plt.figure(2)
plt.plot(vertices, white_Kcont, ',k')
plt.show()

# Mean of the Pial Surface

# Mean of the Pial Surface

import matplotlib.pyplot as plt
import numpy as np

pial_Hcont_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/continuous/pial/lh.pial.H.cont.asc")
pial_Hdisc_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/discrete/pial/lh.pial.H.discrete.asc")

pial_Hcont = pial_Hcont_data[:, 4]
pial_Hdisc = pial_Hdisc_data[:, 4]

vertices = white_Hcont_data[:, 0]

plt.plot(vertices, pial_Hdisc, ',r')
# plt.figure(2)
plt.plot(vertices, pial_Hcont, ',k')
plt.show()

# Gaussian of the Pial Surface

pial_Kcont_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/continuous/pial/lh.pial.K.cont.asc")
pial_Kdisc_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/discrete/pial/lh.pial.K.discrete.asc")

pial_Kcont = pial_Kcont_data[:, 4]
pial_Kdisc = pial_Kdisc_data[:, 4]

vertices = pial_Kcont_data[:, 0]

#plt.ylim(-50, 50)
plt.plot(vertices, pial_Kdisc, ',r')
plt.figure(2)
plt.plot(vertices, pial_Kcont, ',k')
plt.show()

# Principal Curvatures of the Pial Surface

pial_K1cont_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/continuous/pial/lh.pial.K1.cont.asc")
pial_K1disc_data = np.loadtxt(fname = "/Users/nagedem/Desktop/Spyder/new_subj/discrete/pial/lh.pial.K1.discrete.asc")

pial_K1cont = pial_K1cont_data[:, 4]
pial_K1disc = pial_K1disc_data[:, 4]

vertices = pial_K1cont_data[:, 0]

#plt.ylim(-50, 50)
plt.plot(vertices, pial_K1disc, ',r')
plt.figure(2)
plt.plot(vertices, pial_K1cont, ',k')
plt.show()