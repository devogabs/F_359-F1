import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # não usei ainda mas vai ser importante pra fazer os calculos

"""
Processamento de dados do osciloscópio para rede de células LC.

Este script automatiza a leitura dos dados exportados do osciloscópio (formato .csv) e realiza o 
cálculo da transmitância (ganho) da rede de células LC, comparando V_out com V_in.

Também gera um gráfico da transmitância em função da frequência, permitindo a análise do comportamento da rede LC.
"""


def process_oscilloscope_data(file_path):
    """
    Lê um arquivo .csv do osciloscópio e extrai os parâmetros de voltagem e ganho.
    Args:
        file_path (str): Caminho para o arquivo .csv exportado do osciloscópio.

    Returns:
        pd.DataFrame: DataFrame contendo as colunas ['Tempo', 'V_in', 'V_out'].
    """
    try:
        # Lê o arquivo .csv usando pandas
        data = pd.read_csv(file_path)

        # Verifica se as colunas necessárias estão presentes
        if 'Tempo' not in data.columns or 'V_in' not in data.columns or 'V_out' not in data.columns:
            raise ValueError(
                "O arquivo .csv deve conter as colunas 'Tempo', 'V_in' e 'V_out'.")

        return data[['Tempo', 'V_in', 'V_out']]
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return None


def calculate_transmittance_corrected(data):
    """
    Calcula a transmitância (ganho) da rede de células LC.
    Args:
        data (pd.DataFrame): DataFrame contendo as colunas ['Tempo', 'V_in', 'V_out'].

    Returns:
        pd.DataFrame: DataFrame contendo as colunas ['Tempo', 'Transmittance'].
    """
    try:
        # Calcula a transmitância como a razão entre as amplitudes de saída e entrada
        amplitude_in = data['V_in'].abs().max()
        amplitude_out = data['V_out'].abs().max()

        transmitancia = amplitude_out / amplitude_in if amplitude_in != 0 else 0
        return transmitancia
    except Exception as e:
        print(f"Erro ao calcular a transmitância: {e}")
        return None


def plot(data):
    """
    Gera um gráfico ...
    Args:
        data (pd.DataFrame): DataFrame contendo as colunas ['Tempo', 'Transmittance'].
    """

    plt.figure(figsize=(10, 5))
    plt.plot(data['Tempo'], data['V_in'], label='Entrada (Nó 0)', alpha=0.8)
    plt.plot(data['Tempo'], data['V_out'],
             label='Saída (Nó N)', alpha=0.8, linestyle='--')
    plt.title('Resposta Temporal da Rede LC - Verificação de Fase e Amplitude')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Voltagem (V)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    # Caminho para o arquivo .csv exportado do osciloscópio
    file_path = './data/dados_osciloscopio.csv'

    # Processa os dados do osciloscópio
    dados = process_oscilloscope_data(file_path)

    if dados is not None:
        # Calcula a transmitância
        transmittance_data = calculate_transmittance_corrected(dados)

        # Gera o gráfico da resposta temporal
        plot(dados)

