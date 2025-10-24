# Bíbliotecas
import pandas as pd

# Base de dados
df = pd.read_csv('vgsales.csv'))

# Top 10 por vendas globais
top10 = df.sort_values('Global_Sales', ascending=False).head(10)

# Top 10 por vendas globais com as Menores pontuações
top10_negative = df.sort_values('Global_Sales', ascending=True).head(10)

# Pontuação Total dos Gêneros dos jogos
gen = df.groupby('Genre')['Global_Sales'].sum()

# Visualização
