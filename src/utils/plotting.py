import matplotlib.pyplot as plt
import pandas as pd

def plot_tension_function_of_time(dataCh1: pd.DataFrame) -> None:
    plt.plot(dataCh1["time"],dataCh1["signal"], 'o')
    plt.show()