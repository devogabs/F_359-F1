# utils/calculations.py
import numpy as np
import scipy
import pandas as pd

def data_FFT(metadata: list, data: pd.DataFrame) -> list[list[float]]:
    
    """
    Essa função recebe os metadados e dados do oscilador e retorna os parametros ótimos do fit de uma função seno e a estimativa aproximada
    da covariancia dos parametros. 

    Args:
    - metadata: Metadados da médida do osciloscopio.
    - data: Dados da médida do osciloscopio.
    Return:
    - popt: parametros ótimos do fit da função seno
    - pcov: estimativa aproximada da covariancia dos parametros.
    """

    def sin_function(x,amplitude,omega,phase,offset):
            return amplitude * np.sin((x * omega) + phase) + offset
    
    y = (data["signal"] - float(metadata["Vertical Offset"])) / float(metadata["Vertical Scale"])            
        
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
    
    return popt, pcov

def data_Uncertainty(data: pd.DataFrame) -> list[float]:
    scale_Uncertainty = ((8/256)/np.sqrt(12))**2
    vertical_Uncertainty = []
    osc_Uncertainty = []

    for i in data["signal"]:
        Uv = (3*i)/100
        vertical_Uncertainty.append(Uv)

    for i in vertical_Uncertainty:
        Ut = np.sqrt((i**2) + scale_Uncertainty)
        osc_Uncertainty.append(Ut)

    return osc_Uncertainty

def amplitude_Uncertainty(popt: list, pcov: list[list]):
     amplitude = popt[0]
     stat_Uncertainty = pcov[0][0]

     vertical_gain = 0.03 * amplitude
     scale_Uncertainty = ((8/256)/np.sqrt(12))

     instrumental_Uncertainty = np.sqrt((vertical_gain**2) + (scale_Uncertainty**2))

     ampU = np.sqrt(stat_Uncertainty + (instrumental_Uncertainty**2))

     return ampU

def frequencies_Error(frequency: float) -> float:
     f_Delta = frequency * (100/1000)
     f_Error = f_Delta/np.sqrt(3)

     return f_Error



        

