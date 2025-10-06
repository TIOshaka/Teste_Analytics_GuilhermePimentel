import sqlite3
import pandas as pd

print("iniciando o script de consultas sql")

# -=-=-=-=- 1.carregar os csv para dataframes do pandas  -=-=-=-=-
try:
    dim_produto =pd.read_csv('data/dim_produto.csv')
    dim_tempo = pd.read_csv('data/dim_tempo.csv')
    fato_vendas= pd.read_csv('data/fato_vendas.csv')
    print("arquivos CSV carregados")
except FileNotFoundError:
    print("Erro:arquivos CSV nao encontrados na pasta data")
    exit()

# -=-=-=-=- 2.Criar um banco de dados s1Lite em Memopria e carregar os dados-=-=-=-=-
conn = sqlite3.connect(':memory:')
print("conexao com banco de dados sqite em memoria criada")

dim_produto.to_sql('produtos', conn,index=False, if_exists='replace')
dim_tempo.to_sql('tempo', conn, index=False, if_exists='replace')
fato_vendas.to_sql('vendas',conn, index=False, if_exists='replace')
print("dados caeregdos nas tabelas SQL:produtos,tempo,vendas")


# -=-=-=-=- 3. Definir e executar as consultas sqk -=-=-=-=-

# Query 1: Listar o total de vendas por produto, ordenado de forma decrescnte
query1 = """

SELECT
    p.Nome_Produto,
    p.Categoria,
    SUM(v.Quantidade * v.Preco_Unitario) AS Receita_Total
FROM
    vendas AS v
JOIN
    produtos AS p ON v.ID_Produto = p.ID_Produto
GROUP BY
    p.Nome_Produto, p.Categoria
ORDER BY
    Receita_Total DESC;
"""

# Query 2: Identificar produtos que venderam menos em junho de 2024 (2023)
query2 = """


SELECT
    p.Nome_Produto,
    p.Categoria,
    SUM(v.Quantidade * v.Preco_Unitario) AS Receita_Junho_2023
FROM
    vendas AS v
JOIN
    produtos AS p ON v.ID_Produto = p.ID_Produto
JOIN
    tempo AS t ON v.ID_Data = t.ID_Data
WHERE
    t.Ano = 2023 AND t.Mes = 6
GROUP BY
    p.Nome_Produto, p.Categoria
ORDER BY
    Receita_Junho_2023 ASC
LIMIT 5;
"""

print("\n-=-=-=-=-RESULTADO DA CONSULTA 1 -=-=-=-=-")
resultado_q1 =pd.read_sql_query(query1, conn)
print(resultado_q1)

print("\n-=-=-=-=- RESULTADO DA CONSULTA 2  -=-=-=-=-")
resultado_q2 = pd.read_sql_query(query2, conn)
print(resultado_q2)


# -=-=-=-=- 4. Salvar as consultas no arquivo .sql -=-=-=-=-
try:
    with open('scripts/consultas_sql.sql','w', encoding='utf-8') as f: 
        f.write(query1)
        f.write("\n\n")
        f.write(query2)
    print("\narquivo consultas_sql.sql salvo com sucesso na pasta 'scripts'")
except Exception as e:
    print(f"ocorreu um erro ao salvar o arquivo .sql: {e}")

conn.close()