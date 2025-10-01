# --- Código CORRIGIDO para o arquivo scripts/01_data_simulation.py ---

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import date, timedelta

# --- Configuração ---
NUM_PRODUTOS = 15
NUM_VENDAS = 300
DATA_INICIO = date(2023, 1, 1)
DATA_FIM = date(2023, 12, 31)

# Inicializa o Faker
fake = Faker('pt_BR')

print("Iniciando a simulação dos dados...")

# --- 1. Criação da Dimensão Produto ---
print("Gerando Dimensão Produto...")
categorias = ['Eletrônicos', 'Casa e Cozinha', 'Esportes', 'Livros', 'Roupas']
produtos_lista = []
for i in range(NUM_PRODUTOS):
    produto = {
        'ID_Produto': i + 1,
        'Nome_Produto': fake.word().capitalize() + ' ' + fake.word().capitalize(),
        'Categoria': random.choice(categorias)
    }
    produtos_lista.append(produto)
dim_produto = pd.DataFrame(produtos_lista)

# --- 2. Criação da Dimensão Tempo ---
print("Gerando Dimensão Tempo...")
dias = (DATA_FIM - DATA_INICIO).days + 1
datas_lista = []
for i in range(dias):
    data_atual = DATA_INICIO + timedelta(days=i)
    datas_lista.append({
        'ID_Data': i + 1,
        'Data_Completa': data_atual,
        'Ano': data_atual.year,
        'Mes': data_atual.month,
        'Dia': data_atual.day,
        'Nome_Mes': data_atual.strftime('%B'),
        'Trimestre': f"T{(data_atual.month - 1) // 3 + 1}"
    })
dim_tempo = pd.DataFrame(datas_lista)
meses_pt = {
    'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março', 'April': 'Abril',
    'May': 'Maio', 'June': 'Junho', 'July': 'Julho', 'August': 'Agosto',
    'September': 'Setembro', 'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
}
dim_tempo['Nome_Mes'] = dim_tempo['Nome_Mes'].map(meses_pt)

# --- 3. Criação da Tabela Fato Vendas ---
print("Gerando Tabela Fato Vendas...")
vendas_lista = []
for i in range(NUM_VENDAS):
    preco = round(random.uniform(19.90, 899.99), 2)
    
    if preco < 300:
        quantidade = random.randint(5, 20)
    elif preco > 600:
        quantidade = random.randint(1, 4)
    else:
        quantidade = random.randint(1, 10)
    
    quantidade = max(1, quantidade + random.choice([-1, 0, 1, 2]))
    
    id_data = random.randint(1, dias)
    
    venda = {
        'ID_Venda': i + 1,
        'ID_Produto': random.randint(1, NUM_PRODUTOS),
        'ID_Data': id_data,
        'Quantidade': quantidade,
        'Preco_Unitario': preco
    }
    vendas_lista.append(venda)

fato_vendas = pd.DataFrame(vendas_lista)

# --- 4. Salvando os arquivos em CSV ---
print("Salvando arquivos CSV na pasta 'data'...")
try:
    dim_produto.to_csv('data/dim_produto.csv', index=False, encoding='utf-8')
    dim_tempo.to_csv('data/dim_tempo.csv', index=False, encoding='utf-8')
    
    # CORREÇÃO AQUI: Adicionado float_format para garantir 2 casas decimais no CSV
    fato_vendas.to_csv('data/fato_vendas.csv', index=False, encoding='utf-8', float_format='%.2f')
    
    print("Sucesso! Arquivos salvos em 'data/'.")
except FileNotFoundError:
    print("Erro: A pasta 'data' não foi encontrada.")