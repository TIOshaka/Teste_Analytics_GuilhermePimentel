

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
