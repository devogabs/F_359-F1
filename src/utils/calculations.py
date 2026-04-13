import numpy
import pandas

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
