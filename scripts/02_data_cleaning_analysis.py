# --- Código FINAL (v4) para o arquivo scripts/02_data_cleaning_analysis.py ---

import pandas as pd
import numpy as np

print("Iniciando o script de limpeza e análise (v4)...")

# --- 1. Carregando e Unindo os Dados Brutos ---
try:
    fato_vendas = pd.read_csv('data/fato_vendas.csv')
    dim_produto = pd.read_csv('data/dim_produto.csv')
    dim_tempo = pd.read_csv('data/dim_tempo.csv')
    print("Arquivos de dados brutos carregados.")
except FileNotFoundError:
    print("Erro: Arquivos não encontrados. Execute o script 01_data_simulation.py primeiro.")
    exit()

df = pd.merge(fato_vendas, dim_produto, on='ID_Produto', how='left')
df = pd.merge(df, dim_tempo, on='ID_Data', how='left')
print("Dados unidos em um único DataFrame.")

df['Preco_Unitario'] = df['Preco_Unitario'].round(2)
print("Coluna 'Preco_Unitario' padronizada com 2 casas decimais.")


# --- 2. Processo de Limpeza de Dados (Controle de Qualidade) ---
print("\n--- INICIANDO CONTROLE DE QUALIDADE ---")

# ... (as seções de tratamento de nulos, duplicatas e conversão de tipos permanecem iguais)
print(f"Valores nulos encontrados antes do tratamento: {df.isnull().sum().sum()}")
df['Preco_Unitario'] = df.groupby('Categoria')['Preco_Unitario'].transform(
    lambda x: x.fillna(x.median()).round(2)
)
print("Processo de tratamento de nulos executado.")

linhas_duplicadas = df.duplicated().sum()
print(f"Linhas duplicadas encontradas: {linhas_duplicadas}")
df.drop_duplicates(inplace=True)
if linhas_duplicadas > 0:
    print(f"{linhas_duplicadas} linhas duplicadas foram removidas.")

df['Data_Completa'] = pd.to_datetime(df['Data_Completa'])
print("Coluna 'Data_Completa' verificada e convertida para o tipo datetime.")

print("--- CONTROLE DE QUALIDADE FINALIZADO ---\n")


# --- 3. Análise Obrigatória (Parte 1 do Teste) ---
print("--- INICIANDO ANÁLISE OBRIGATÓRIA ---")

df['Receita'] = (df['Quantidade'] * df['Preco_Unitario']).round(2)

vendas_por_produto = df.groupby('Nome_Produto')['Receita'].sum().sort_values(ascending=False)
produto_mais_vendido = vendas_por_produto.idxmax()
valor_produto_mais_vendido = vendas_por_produto.max()

print(f"Análise concluída: O produto com maior receita é '{produto_mais_vendido}'.")
print(f"Valor total: R$ {valor_produto_mais_vendido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
print("--- FIM DA ANÁLISE ---\n")


# --- 4. Salvando o Dataset Limpo (COM FORMATAÇÃO) ---
try:
    # CORREÇÃO AQUI: Adicionado float_format para garantir 2 casas decimais no CSV
    df.to_csv('data/data_clean.csv', index=False, encoding='utf-8', float_format='%.2f')
    print(f"Arquivo 'data_clean.csv' salvo com sucesso na pasta 'data' com a formatação de 2 casas decimais.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo: {e}")