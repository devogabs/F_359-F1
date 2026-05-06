# utils/plotting.py

import matplotlib.pyplot as plt
import pandas as pd
import scipy
import numpy as np

def plot_oscillator_graph(metadata: list[dict], data:list[pd.DataFrame]) -> None:
    """
    Essa função recebe os outputs do canais do oscilador e plota eles em um gráfico de tensão em função do tempo.
    
    Args:
    - metadada: Lista com os metadados dos canais.
    - data: Lista com os dados dos canais.
    """

    if len(metadata) != len(data):
        print("Numero incompativel entre metadata e data.")
        return None

    plt.figure()
    for i in range(len(data)):
        x = (data[i]["time"]) / float(metadata[i]["Horizontal Scale"])
        y = (data[i]["signal"] - float(metadata[i]["Vertical Offset"])) / float(metadata[i]["Vertical Scale"])
        plt.plot(x,y , 'o' , label = metadata[i]["Source"], markersize=5)

    plt.legend()
    plt.xlabel(metadata[0]["Horizontal Units"])
    plt.ylabel(metadata[0]["Vertical Units"])
    #plt.show()

    return None

def plot_oscillator_graph_curve(metadata: list[dict], data:list[pd.DataFrame]):
    plt.figure()
    def sin_function(x,amplitude,omega,phase,offset):
        return amplitude * np.sin((x * omega) + phase) + offset
    
    for i in range(len(data)):
        raw_x = (data[i]["time"]) * float(metadata[i]["Horizontal Scale"])
        y = (data[i]["signal"] - float(metadata[i]["Vertical Offset"])) / float(metadata[i]["Vertical Scale"])            
        
        N = len(y)
        
        x_indices = np.arange(N)

        guess_offset = np.mean(y)

        yf = scipy.fft.rfft(y - guess_offset)
        xf = scipy.fft.rfftfreq(N, d=1.0)
        
        idx_max = np.argmax(np.abs(yf))
        guess_omega_idx = 2 * np.pi * xf[idx_max]
        guess_amplitude = (np.max(y) - np.min(y)) / 2
        
        p0 = [guess_amplitude, guess_omega_idx, 0, guess_offset]

        popt, pcov = scipy.optimize.curve_fit(sin_function,x_indices,y,p0=p0)
        plt.plot(raw_x, sin_function(x_indices, *popt), label = metadata[i]["Source"])
        print(metadata[i]["Source"])
        print(popt)

    plt.legend()
    plt.xlabel(metadata[0]["Horizontal Units"])
    plt.ylabel(metadata[0]["Vertical Units"])
    #plt.show()
    return None

