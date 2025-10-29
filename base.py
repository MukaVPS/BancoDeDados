# Bíbliotecas
import pandas as pd

# Base de dados
df = pd.read_csv('vgsales.csv')

# Limpeza de dados - removendo anos faltantes
df_clean = df.dropna(subset=['Year'])
df_clean['Year'] = df_clean['Year'].astype(int)

# Top 10 por vendas globais
top10 = df.sort_values('Global_Sales', ascending=False).head(10)

# Top 10 por vendas globais com as Menores pontuações
top10_negative = df.sort_values('Global_Sales', ascending=True).head(10)

# Vendas Globais de cada empresa de jogos (Falta.csv)
publisher = df.groupby('Publisher')['Global_Sales'].sum()

# Top 5 empresas com as maiores vendas
publishertop5 = publisher.sort_values(ascending=False).head(5)

# Por ano
jogos_por_ano = df_clean['Year'].value_counts().sort_index()

# Por década
df_clean['Decada'] = (df_clean['Year'] // 10) * 10
jogos_por_decada = df_clean['Decada'].value_counts().sort_index()

# Região com mais compra de jogos
vendas_por_regiao = {
    'América do Norte': df['NA_Sales'].sum(),
    'Europa': df['EU_Sales'].sum(),
    'Japão': df['JP_Sales'].sum(),
    'Outras Regiões': df['Other_Sales'].sum(),
    'Global': df['Global_Sales'].sum()
}

# Convertendo para DataFrame para melhor visualização
vendas_df = pd.DataFrame(list(vendas_por_regiao.items()), 
                        columns=['Região', 'Vendas (Milhões)'])

# Região com mais vendas (Falta.csv)
regiao_mais_vendas = max(vendas_por_regiao, key=vendas_por_regiao.get)

# Tendência de gênero de jogos mais lucrativos

# Vendas totais por gênero
vendas_por_genero = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

# Vendas médias por gênero
vendas_medias_por_genero = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False)

# Top 3 gêneros mais lucrativos (Falta.csv)
top3_generos = vendas_por_genero.head(3)

# Top 10 anos com mais vendas
top10_anos_vendas = jogos_por_ano.sort_values(ascending=False).head(10)

# Vendas por década
vendas_por_decada = df_clean.groupby('Decada')['Global_Sales'].sum()

# Evolução temporal dos gêneros

# Gêneros mais populares por década (Falta.csv)
for decada in sorted(df_clean['Decada'].unique()):
    dados_decada = df_clean[df_clean['Decada'] == decada]
    genero_mais_popular = dados_decada.groupby('Genre')['Global_Sales'].sum().idxmax()
