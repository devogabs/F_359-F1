# analysis.py

import pandas as pd

def read_oscillator_channel_output(path: str)-> tuple[dict,pd.DataFrame]:

    """
    Essa função lê o arquivo de output do osciloscópio e retorna separadamente os metadados e os dados.

    Args:
    - path: Caminho do arquivo de output .csv.
    Return:
    - metadados_dict: Dicionário com os metadados da medida.
    - dados: Dataframe com os dados referente a medida do osciloscópio.
    """

    df = pd.read_csv(path, header=None)

    metadados = df[[0,1]].dropna()
    metadados_dict = dict(zip(metadados[0],metadados[1]))

    dados = df[[3,4]].dropna()
    dados = dados.astype(float)
    dados.columns = ["time","signal"]

    return metadados_dict, dados    