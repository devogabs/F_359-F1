import matplotlib.pyplot as plt
import pandas as pd

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

    for i in range(len(data)):
        plt.plot((data[i]["time"]) / float(metadata[i]["Horizontal Scale"]) ,(data[i]["signal"] + float(metadata[i]["Vertical Offset"])) / float(metadata[i]["Vertical Scale"]) , 'o', label = metadata[i]["Source"])

    plt.legend()
    plt.xlabel(metadata[0]["Horizontal Units"])
    plt.ylabel(metadata[0]["Vertical Units"])
    plt.show()

    return None