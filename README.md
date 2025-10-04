# Teste técnico de analytics - Guilherme Pimentel

## 1. Contexto do projeto

Este repositorio contem a solução copleta para o teste tecnico do processo seletivo para a vaga de Estagiário de Dados na Quod. O projeto abrange desde a simulação de dados até a análise exploratória, consultas SQL e a criação de um dashboard interativo

## 2. Estrutura do repositório

O projeto está organizado da seguinte forma para garantir clarza e reprodutibilidade:

/
│
├── data/
│   ├── dim_produto.csv      #Dimensão de produtos
│   ├── dim_tempo.csv        # Dimensão de tempo
│   ├── fato_vendas.csv      # Tabela de fatos com as transações
│   └── data_clean.csv       # Arquivo final de dados limpos e unidos
│
├── scripts/
│   ├── 01_data_simulation.py          # Script para simular os dados brutos
│   ├── 02_data_cleaning_analysis.py   # Script para limpeza e análise inicial
│   ├── 03_sql_queries.py              # Script para execução das consultas SQL
│   └── consultas_sql.sql              # Arquivo final com as queries SQL
│
├── report/
│   └── relatorio - insights.pdf        # Relatório final com os insights detalhados
│
├── dashboard/
│   └── (Arquivo .pbix do Power BI)
│
├── analise_exploratoria.ipynb   # Notebook Jupyter com a análise exploratoria visual
│
├── requirements.txt             #lista de dependencias Python do projeto
│
└── README.md                    # Esta documentação


## 3. tecnologias utilizadas

* **Linguagem:** Python 3
* **Bibliotecas Principais:** Pandas, NumPy, Matplotlib, Seaborn, Scipy, Faker
* **Banco de Dados:** SQLite (utilizado em memória via Python para as consultas SQL)
* **Ferramenta de BI:** Power BI


## 4. como executar o projeto

#### Ordem de execução dos scripts

Os scripts devem ser executados na ordem numérica a partir da pasta raiz do projeto:

1.  **`python scripts/01_data_simulation.py`**
    * *O que faz: Simula e salva os três arquivos CSV brutos (`dim_produto`, `dim_tempo`, `fato_vendas`) na pasta `/data`.*

2.  **`python scripts/02_data_cleaning_analysis.py`**
    * *O que faz: Carrega os dados brutos, aplica o processo de limpeza e qualidade, realiza a análise inicial e salva o `data_clean.csv`.*

3.  **`python scripts/03_sql_queries.py`**
    * *O que faz: Carrega os dados modelados em um banco de dados SQLite em memória, executa as consultas SQL solicitadas e salva o arquivo `consultas_sql.sql`.*

O arquivo `analise_exploratoria.ipynb` pode ser aberto em um ambiente Jupyter (como o VS Code) para visualizar a análise exploratória detalhada


## 5. Decisões estratégicas e diferenciais

Durante o projeto, algumas decisões foram tomadas para ir além do escopo mínimo:

* **Modelagem de Dados (modelagem estrela):** Os dados foram simulados em um modelo estrela (1 tabela fato, 2 dimensões) para demonstrar conhecimento em estruturação de dados para fins analíticos

* **Análise Estatística (Regressão Linear):** Foi incluída uma análise de correlação e regressão linear para testar uma hipótese de negócio e demonstrar a aplicação de técnicas estatísticas.

* **Uso de Ambiente Virtual (`venv`):** O projeto foi desenvolvido em um ambiente virtual para garantir 100% de reprodutibilidade.

* **Dashboard em Power BI:** Foi desenvolvido um painel interativo para apresentar os resultados de forma visual e gerencial


## 6. principais insights encontrados

Com base na análise final dos dados, os principais resultados foram:

* **Pico de Vendas Atípico:** O faturamento mais alto do ano ocorreu em **Fevereiro**, não no final do ano, indicando uma sazonalidade incomum que precisa ser investigada para ser replicada.

* **Oportunidade no Final do Ano:** Contrariando a tendência do varejo, **Dezembro foi o mês de menor faturamento**, apontando para uma grande oportunidade de crescimento com a criação de campanhas de Natal e Black Friday.

* **Elasticidade de Preço:** Uma forte correlação negativa (**-0.69**) foi confirmada entre preço e quantidade, provando que a precificação é uma ferramenta estratégica crucial para influenciar o volume de vendas, especialmente nos meses de baixa