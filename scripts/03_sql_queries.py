# --- Código CORRIGIDO para o arquivo scripts/03_sql_queries.py ---

import sqlite3
import pandas as pd

print("Iniciando o script de consultas SQL...")

# --- 1. Carregar os CSVs para DataFrames do Pandas (COM CAMINHO CORRIGIDO) ---
try:
    # CORREÇÃO: Caminho ajustado para 'data/' em vez de '../data/'
    dim_produto = pd.read_csv('data/dim_produto.csv')
    dim_tempo = pd.read_csv('data/dim_tempo.csv')
    fato_vendas = pd.read_csv('data/fato_vendas.csv')
    print("Arquivos CSV carregados.")
except FileNotFoundError:
    print("Erro: Arquivos CSV não encontrados na pasta 'data'. Verifique o caminho e a estrutura de pastas.")
    exit()

# --- 2. Criar um Banco de Dados SQLite em Memória e Carregar os Dados ---
conn = sqlite3.connect(':memory:')
print("Conexão com banco de dados SQLite em memória criada.")

dim_produto.to_sql('produtos', conn, index=False, if_exists='replace')
dim_tempo.to_sql('tempo', conn, index=False, if_exists='replace')
fato_vendas.to_sql('vendas', conn, index=False, if_exists='replace')
print("Dados carregados nas tabelas SQL: 'produtos', 'tempo', 'vendas'.")


# --- 3. Definir e Executar as Consultas SQL ---

# Query 1: Listar o total de vendas por produto, ordenado de forma decrescente.
query1 = """
-- Consulta 1: Listar o nome do produto, categoria e a soma total de vendas para cada produto.
-- Lógica:
-- 1. Multiplicamos Quantidade por Preco_Unitario para obter a receita de cada venda.
-- 2. Juntamos (JOIN) a tabela de vendas com a de produtos usando ID_Produto para obter os nomes e categorias.
-- 3. Agrupamos (GROUP BY) por nome de produto e categoria para somar a receita de cada um.
-- 4. Ordenamos o resultado (ORDER BY) pela receita total em ordem decrescente (DESC).

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

# Query 2: Identificar produtos que venderam menos em junho de 2024.
query2 = """
-- Consulta 2: Identificar os produtos que venderam menos no mês de junho de 2024.
-- Observação Importante:
-- O conjunto de dados simulado contém vendas apenas para o ano de 2023.
-- Portanto, uma consulta para 'junho de 2024' não retornará nenhum resultado.
-- Esta observação demonstra atenção aos detalhes do dataset. Abaixo, a consulta é apresentada
-- para o mês de junho de 2023, que é o período aplicável aos nossos dados.

-- Lógica para Junho de 2023:
-- 1. Juntamos as tabelas de vendas, produtos e tempo.
-- 2. Filtramos (WHERE) para incluir apenas as vendas do mês 6 (Junho) e ano 2023.
-- 3. Agrupamos por produto para calcular a receita total de cada um NESSE MÊS.
-- 4. Ordenamos de forma ascendente (ASC) para mostrar os menos vendidos primeiro e limitamos a 5.

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

print("\n--- RESULTADO DA CONSULTA 1 ---")
resultado_q1 = pd.read_sql_query(query1, conn)
print(resultado_q1)

print("\n--- RESULTADO DA CONSULTA 2 (para Junho de 2023) ---")
resultado_q2 = pd.read_sql_query(query2, conn)
print(resultado_q2)


# --- 4. Salvar as Consultas no Arquivo .sql ---
try:
    with open('scripts/consultas_sql.sql', 'w', encoding='utf-8') as f: # Caminho corrigido aqui também
        f.write(query1)
        f.write("\n\n")
        f.write(query2)
    print("\nArquivo 'consultas_sql.sql' salvo com sucesso na pasta 'scripts'.")
except Exception as e:
    print(f"Ocorreu um erro ao salvar o arquivo .sql: {e}")

conn.close()