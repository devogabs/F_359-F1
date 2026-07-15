import utils
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import os

np.set_printoptions(legacy='1.25')

Indutance_L = 82e-6
Capacitance_C = 2e-9
Cut_frequence = 786.01

with open("info.txt", encoding="utf-8") as f:
    data_path = f.read()

data = utils.read_pack_data(data_path)

cells_data_directorys = os.listdir(data_path)
number_of_cells = len(cells_data_directorys) * 2

amplitudes = []
amplitudes_Error = []

for i in range(number_of_cells):
    amplitudes.append([])
    amplitudes_Error.append([])

for cell_idx, cell in enumerate(data):
    for data_from_cell in cell:
        popt, pcov = utils.data_FFT(data_from_cell[0], data_from_cell[1])
        ampU = utils.amplitude_Uncertainty(popt,pcov)
        amplitudes[cell_idx].append(np.abs(popt[0]))
        amplitudes_Error[cell_idx].append(ampU)

v_in = amplitudes[0]

step = 50
frequencies = np.arange(100, 1000 + step, step)

dispersion_relation = utils.dispersion_Relation(frequencies, Indutance_L, Capacitance_C, Cut_frequence)

theorical_amplitudes = utils.theorical_Amplitude(dispersion_relation, v_in)

print(len(frequencies))
print(dispersion_relation)
print(theorical_amplitudes[0])
print(theorical_amplitudes[1])

plt.figure()
plt.scatter(frequencies, theorical_amplitudes[0], color="b")
plt.scatter(frequencies, theorical_amplitudes[1], color="r")
plt.show()