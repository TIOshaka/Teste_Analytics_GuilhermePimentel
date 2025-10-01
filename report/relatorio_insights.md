# Relatório de Insights - Análise de Vendas 2023

A análise dos dados de vendas simulados para o ano de 2023 revelou padrões significativos e oportunidades estratégicas para o negócio. A partir da análise exploratória, das consultas SQL e de testes estatísticos, os três principais insights encontrados são detalhados abaixo.

### 1. Forte Sazonalidade de Vendas e Concentração de Receita

**Observação:** A análise da tendência mensal demonstrou um aumento expressivo na receita durante o último bimestre do ano. A consulta SQL de vendas por produto aprofundou essa visão, mostrando que a receita anual é liderada por produtos específicos, como o **'Dolores Quos'** da categoria **Casa e Cozinha**, que sozinho gerou **R$ 63.187,31** em vendas.

**Implicação de Negócio:** Existe uma forte dependência das vendas de final de ano. Além disso, o sucesso da empresa está concentrado em um grupo seleto de produtos "campeões de venda".

**Ação Recomendada:** Recomenda-se o reforço do planejamento de estoque para os produtos de maior receita. Ações de marketing direcionadas para o produto **'Dolores Quos'** e outros do topo da lista podem maximizar o faturamento no período de alta demanda.

### 2. Oportunidade de Crescimento em Períodos e Produtos de Baixa

**Observação:** Excluindo o pico de final de ano, a receita mantém-se em um patamar estável. A consulta dos produtos menos vendidos em um mês de baixa, como junho, identificou itens com baixo giro, como o produto **'Pariatur Expedita'** (categoria **Roupas**), que gerou apenas **R$ 250,20** no período.

**Implicação de Negócio:** A ausência de outros picos de venda e a existência de produtos com baixo desempenho indicam um potencial não explorado para alavancar a receita e otimizar o portfólio.

**Ação Recomendada:** Sugere-se a criação de um calendário comercial com campanhas promocionais para outras datas. Ações de queima de estoque ou "combos" podem ser focadas em produtos de baixo giro, como os identificados na análise de junho, para aumentar sua movimentação.

### 3. Confirmação Estatística da Elasticidade de Preço

**Observação:** A análise de correlação entre o preço unitário e a quantidade vendida resultou em um coeficiente de Pearson de **-0.69**, com um p-valor de 0.0000. Este valor indica uma correlação negativa forte e estatisticamente significativa.

**Implicação de Negócio:** O preço é uma alavanca crítica que impacta diretamente o volume de vendas. Estratégias de precificação terão um efeito previsível no comportamento de compra do consumidor.

**Ação Recomendada:** A empresa pode usar essa relação para modelar o impacto de futuras estratégias de preço e promoções, buscando encontrar o ponto ótimo que maximize a receita total (equilíbrio entre preço x quantidade).