import pandas as pd
import numpy as np

print("Iniciando o script de limpeza e analise")

# -=-=-=-=- 1. carregando e unindo os dados brutos -=-=-=-=-
try:
    fato_vendas =pd.read_csv('data/fato_vendas.csv')
    dim_produto = pd.read_csv('data/dim_produto.csv')
    dim_tempo= pd.read_csv('data/dim_tempo.csv')
    print("arquivos de dados brutos carregados")
except FileNotFoundError:
    print("Erro:Arquivos nao encontrados")
    exit()

df =pd.merge(fato_vendas, dim_produto,on='ID_Produto', how='left')
df = pd.merge(df, dim_tempo, on='ID_Data',how='left')
print("dados unidos em um unico dataFrame")

df['Preco_Unitario']= df['Preco_Unitario'].round(2)
print("coluna Preco_Unitario padronizada com 2 casas decimais")


# -=-=-=-=- 2.processo de limpeza de fdados -=-=-=-=-
print("\n-=-=-=-=- INICIANDO CONTROLE DE QUALIDADE -=-=-=-=-")


print(f"valores nulos encontrados antes do tratamento: {df.isnull().sum().sum()}")
df['Preco_Unitario']= df.groupby('Categoria')['Preco_Unitario'].transform(
    lambda x: x.fillna(x.median()).round(2)
)
print("processo de tratamento de nulos executado")

linhas_duplicadas =df.duplicated().sum()
print(f"Linhas duplicadas encontradas:{linhas_duplicadas}")
df.drop_duplicates(inplace=True)
if linhas_duplicadas>0:
    print(f"{linhas_duplicadas} linhas dupliadas foram removidas")

df['Data_Completa'] =pd.to_datetime(df['Data_Completa'])
print("Coluna 'data_completa verificada e convertida para o tipo datetime")

print("-=-=-=-=-CONTROLE DE QUALIDADE FINALIZADO -=-=-=-=-\n")

# -=-=-=-=- 3. analise obrigatoria (parte 1 do teste)-=-=-=-=----
print("--- INICIANDO ANALISE OBRIGATORIA ---")

df['Receita']= (df['Quantidade']*df['Preco_Unitario']).round(2)

vendas_por_produto = df.groupby('Nome_Produto')['Receita'].sum().sort_values(ascending=False)
produto_mais_vendido =vendas_por_produto.idxmax()
valor_produto_mais_vendido= vendas_por_produto.max()

print(f"analise concluida: o produto com maior receita é '{produto_mais_vendido}'.")
print(f"Valor total:R$ {valor_produto_mais_vendido:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
print("---FIM DA ANaLISE ---\n")


# -=-=-=-=- 4. salvando o dataset limpo -=-=-=-=-
try:
    df.to_csv('data/data_clean.csv',index=False, encoding='utf-8',float_format='%.2f')
    print(f"Arquivo 'data_clean.csv'salvo")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo:{e}")