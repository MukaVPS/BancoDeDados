# Bíbliotecas
import pandas as pd

# Base de dados
df = pd.read_csv('vgsales.csv')
print(df)

# Limpeza de dados

# Top 10 por vendas globais
top10 = df.sort_values('Global_Sales', ascending=False).head(10)
print("\nTop 10 jogos por Global_Sales:")
print(top10[['Name','Platform','Year','Genre','Global_Sales']].to_string(index=False))

# Pontuação Total dos Gêneros dos jogos
gen = df.groupby('Genre')['Global_Sales'].sum()
print(gen)

# Visualização
