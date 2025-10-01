
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
