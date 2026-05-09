# main.py

import utils

if __name__ == "__main__":
    pathCh1 = r"C:\Users\marce\OneDrive\Área de Trabalho\unicamp\semestres\5sem\f359 - lab3\F_359-F1\data\ALL0005\F0005CH1.CSV"
    metadataCh1, dataCh1 = utils.read_oscillator_channel_output(pathCh1)

    pathCh2 = r"C:\Users\marce\OneDrive\Área de Trabalho\unicamp\semestres\5sem\f359 - lab3\F_359-F1\data\ALL0005\F0005CH2.CSV"
    metadataCh2, dataCh2 = utils.read_oscillator_channel_output(pathCh2)

    pathMth = r"C:\Users\marce\OneDrive\Área de Trabalho\unicamp\semestres\5sem\f359 - lab3\F_359-F1\data\ALL0005\F0005MTH.CSV"
    metadataMth, dataMth = utils.read_oscillator_channel_output(pathMth)

    utils.plot_oscillator_graph([metadataCh1,metadataCh2,metadataMth], [dataCh1,dataCh2,dataMth])
