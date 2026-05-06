# utils/calculations.py
import numpy as np
import scipy
import pandas as pd

def data_FFT(metadata: list, data: pd.Dataframe) -> list[list[float]]:
    
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