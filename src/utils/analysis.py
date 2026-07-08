# util/analysis.py

import pandas as pd
import os

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

def read_pack_data(path: str) -> list:
    data = []

    cells_data_directorys = os.listdir(path)
    number_of_cells = len(cells_data_directorys) * 2

    cell_idx = 0

    for _ in range(number_of_cells):
        data.append([])

    for cells_directory_idx, cells_data_directory in enumerate(cells_data_directorys):

        cell_directory_path = os.path.join(path,cells_data_directory) 

        output_files_directorys = os.listdir(cell_directory_path)

        number_of_outputs_files = len(output_files_directorys)

        for output_directory_idx, output_files_directory in enumerate(output_files_directorys):
            output_file_path = os.path.join(cell_directory_path, output_files_directory, "F{:04d}CH1.CSV".format(output_directory_idx)) 
            OutputMetadata, OutputData = read_oscillator_channel_output(output_file_path)
            data[cell_idx].append([OutputMetadata, OutputData])

        cell_idx += 1
        for output_directory_idx, output_files_directory in enumerate(output_files_directorys):
            output_file_path = os.path.join(cell_directory_path, output_files_directory, "F{:04d}CH2.CSV".format(output_directory_idx))
            OutputMetadata, OutputData = read_oscillator_channel_output(output_file_path)
            data[cell_idx].append([OutputMetadata,OutputData])

        cell_idx += 1
    
    return data