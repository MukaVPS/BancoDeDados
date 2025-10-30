import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Carregar a base de dados
df = pd.read_csv('vgsales.csv')
top10 = pd.read_csv('top10_vendas_globais.csv')
top10_negative = pd.read_csv('top10_menores_vendas_globais.csv')
regions = pd.read_csv('vendas_por_regiao.csv')

# ----------------------------
# Top 10 Mais Vendidos
# ----------------------------
top10.plot(x='Name',y='Global_Sales',kind='bar')

# Ajustar espaçamento e exibir
plt.show()
