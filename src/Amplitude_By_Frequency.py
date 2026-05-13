# Amplitude_By_Frequency.py

import utils
import os
from matplotlib import pyplot as plt
import numpy as np

# 100 kHz -> 1 MHz (step: 100kHz)

# Obtem o path da pasta de dados que sera analisada.
with open("info.txt", encoding="utf-8") as f:
    data_path = f.read()

# As pastas são nomeadas da forma "i_i+1", sendo CH1 o referente a célula i e o CH2 referente a célula i+1
cells_data_directorys = os.listdir(data_path)
number_of_cells = len(cells_data_directorys) * 2

data = []
amplitudes = []
amplitudes_Error = []
frequencies_Error = []

for i in range(number_of_cells):
    data.append([])
    amplitudes.append([])
    amplitudes_Error.append([])

cell_idx = 0

for cells_directory_idx, cells_data_directory in enumerate(cells_data_directorys):

    cell_directory_path = os.path.join(data_path,cells_data_directory) 
    
    output_files_directorys = os.listdir(cell_directory_path)
    
    number_of_outputs_files = len(output_files_directorys)

    for output_directory_idx, output_files_directory in enumerate(output_files_directorys):
        output_file_path = os.path.join(cell_directory_path, output_files_directory, "F{:04d}CH1.CSV".format(output_directory_idx)) 
        OutputMetadata, OutputData = utils.read_oscillator_channel_output(output_file_path)
        data[cell_idx].append([OutputMetadata, OutputData])

    cell_idx += 1
    for output_directory_idx, output_files_directory in enumerate(output_files_directorys):
        output_file_path = os.path.join(cell_directory_path, output_files_directory, "F{:04d}CH2.CSV".format(output_directory_idx))
        OutputMetadata, OutputData = utils.read_oscillator_channel_output(output_file_path)
        data[cell_idx].append([OutputMetadata,OutputData])

    cell_idx += 1

for cell_idx, cell in enumerate(data):
    for data_from_cell in cell:
        popt, pcov = utils.data_FFT(data_from_cell[0], data_from_cell[1])
        ampU = utils.amplitude_Uncertainty(popt,pcov)
        amplitudes[cell_idx].append(np.abs(popt[0]))
        amplitudes_Error[cell_idx].append(ampU)

step = 100
frequencies = np.arange(100, 1000 + step, step)

for i in range(len(frequencies)):
    freqU = utils.frequencies_Error(frequencies[i])
    frequencies_Error.append(freqU)

## Plotagem da amplitude em função da frequencia da última célula.
fig, axs = plt.subplots(2,int(number_of_cells/2))
for i in range(2):
    for j in range(int(number_of_cells/2)):
        cell_number = int((i * number_of_cells/2) + j)
        axs[i,j].errorbar(frequencies,amplitudes[cell_number],amplitudes_Error[cell_number], frequencies_Error, 'o', markersize=5)
        axs[i,j].set_title(f"Nó {cell_number+1}")
    
    for ax in axs.flat:
        ax.set(xlabel='Frequência (kHz)', ylabel='Amplitude (V)')
        ax.grid(color='black',linestyle='--',alpha = 0.3)
plt.tight_layout()
plt.show()