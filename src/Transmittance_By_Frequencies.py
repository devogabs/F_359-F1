import utils
import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(legacy='1.25')

with open("info.txt", encoding="utf-8") as f:
    data_path = f.read()

data = utils.read_pack_data(data_path)

amplitudes = [[],[]]
amplitudes_error = [[],[]]
transmittance = []
transmittance_error = []
frequencies_error = []

for data_from_cell in data[0]:
    popt, pcov = utils.data_FFT(data_from_cell[0], data_from_cell[1])
    ampU = utils.amplitude_Uncertainty(popt,pcov)
    amplitudes[0].append(np.abs(popt[0]))
    amplitudes_error[0].append(ampU)

for data_from_cell in data[-1]:
    popt, pcov = utils.data_FFT(data_from_cell[0], data_from_cell[1])
    ampU = utils.amplitude_Uncertainty(popt,pcov)
    amplitudes[1].append(np.abs(popt[0]))
    amplitudes_error[1].append(ampU)

for i in range(len(amplitudes[0])):
    transmittance_value = amplitudes[1][i] / amplitudes[0][i]
    transmittance_error_value = np.sqrt( np.square( ( amplitudes[1][i] * np.log(amplitudes[0][i]) * amplitudes_error[0][i] ) ) + np.square( amplitudes_error[1][i] / amplitudes[0][i] ) ) 
    transmittance.append(transmittance_value)
    transmittance_error.append(transmittance_error_value)

print("Transmittance:")
print(transmittance)
print("Transmittance Error:")
print(transmittance_error)

step = 50
frequencies = np.arange(100, 1000 + step, step)

for i in range(len(frequencies)):
    freqU = utils.frequencies_Error(frequencies[i])
    frequencies_error.append(freqU)

plt.figure()

plt.xlabel("Frequência (kHz)")
plt.ylabel("Amplitude (V)")
plt.xlim([0,1100])
plt.grid(color='black',linestyle='--',alpha = 0.3)

plt.errorbar(frequencies, amplitudes[0], amplitudes_error[0], frequencies_error, '-o', color="blue")
plt.errorbar(frequencies, amplitudes[1], amplitudes_error[1], frequencies_error, '-o', color="red")
plt.errorbar(frequencies, transmittance, transmittance_error, frequencies_error, '-o', color="green")

plt.plot([],[], 'o', color="blue", label="First cell")
plt.plot([],[], 'o', color="red", label="Last cell")
plt.plot([],[], 'o', color="green", label="Transmittance")    

plt.legend()
plt.show()
