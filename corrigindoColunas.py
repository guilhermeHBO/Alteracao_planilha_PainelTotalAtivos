import pandas as pd
import re

# Caminho do arquivo carregado
caminho_arquivo = "planilha_Modificada.xlsx"

# Carregar a planilha
df = pd.read_excel(caminho_arquivo)

# Corrigir a palavra "acidente" na coluna "Rodada"
df['Rodada'] = df['Rodada'].str.replace('Aci_x0002_dente', 'Acidente')


# Salvar a planilha com as correções
novo_caminho_arquivo = 'Painel Total Ativos 26.06.2024 v.Mkohler Modificada e Corrigida.xlsx'
df.to_excel(novo_caminho_arquivo, index=False)

print("Planilha corrigida salva em:", novo_caminho_arquivo)