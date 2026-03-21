# Análise de Rede de Células LC

Este projeto automatiza o processamento de dados de osciloscópio para caracterização de uma rede de células LC.

## Tecnologias
* Python 3.x
* Pandas & Numpy (Processamento)
* Matplotlib (Visualização)

## Objetivos
1. Calcular a transmitância temporal ($V_{out}/V_{in}$).
2. Determinar a resposta em frequência via FFT.
3. Comparar resultados experimentais com o modelo teórico de $N$ células.

## Como usar
1. Coloque seus arquivos `.csv` na pasta `/data`.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o script principal: `python src/main.py`.