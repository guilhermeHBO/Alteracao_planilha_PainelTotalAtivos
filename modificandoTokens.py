import pandas as pd
import re

# Carregar a planilha
df = pd.read_excel("Painel Total Ativos 26.06.2024 v.Mkohler.xlsx")

print(df.head())

# Função para separar o texto dentro e fora dos parênteses
def separar_parenteses(texto):
    dentro_parenteses = re.findall(r'\((.*?)\)', texto)
    fora_parenteses = re.sub(r'\s?\(.*?\)', '', texto)
    dentro_parenteses = dentro_parenteses[0] if dentro_parenteses else ''
    return fora_parenteses.strip(), dentro_parenteses.strip()

# Aplicar a função a coluna 'Rodada'
df['Rodada sem Parênteses'], df['Tokens'] = zip(*df['Rodada'].apply(separar_parenteses))

# Remover o texto dentro dos parênteses da coluna original
df['Rodada'] = df['Rodada sem Parênteses']

# Remover a coluna temporária
df.drop(columns=['Rodada sem Parênteses'], inplace=True)

# Salvar a planilha com as alterações
novo_caminho_arquivo = 'planilha_modificada.xlsx'
df.to_excel(novo_caminho_arquivo, index=False)

print("Planilha processada e salva em:", novo_caminho_arquivo)
