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

# Limpeza de dados - removendo anos faltantes
df_clean = df.dropna(subset=['Year'])
df_clean['Year'] = df_clean['Year'].astype(int)

# Por ano
jogos_por_ano = df_clean['Year'].value_counts().sort_index()
print("\nTop 10 anos com mais lançamentos:")
print(jogos_por_ano.tail(10))

# Por década
df_clean['Decada'] = (df_clean['Year'] // 10) * 10
jogos_por_decada = df_clean['Decada'].value_counts().sort_index()
print("\nJogos lançados por década:")
print(jogos_por_decada)

# Região com mais compra de jogos
print("\n=== ANÁLISE 2: REGIÕES COM MAIS VENDAS ===")

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
print(vendas_df.sort_values('Vendas (Milhões)', ascending=False))

# Região com mais vendas
regiao_mais_vendas = max(vendas_por_regiao, key=vendas_por_regiao.get)
print(f"\n→ Região com mais vendas: {regiao_mais_vendas}")

# Tendência de gênero de jogos mais lucrativos
print("\n=== ANÁLISE 3: GÊNEROS MAIS LUCRATIVOS ===")

# Vendas totais por gênero
vendas_por_genero = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
print("Vendas globais por gênero:")
print(vendas_por_genero)

# Vendas médias por gênero
vendas_medias_por_genero = df.groupby('Genre')['Global_Sales'].mean().sort_values(ascending=False)
print("\nVendas médias por gênero:")
print(vendas_medias_por_genero)

# Top 3 gêneros mais lucrativos
top3_generos = vendas_por_genero.head(3)
print(f"\n→ Top 3 gêneros mais lucrativos: {', '.join(top3_generos.index)}")

# Top 10 anos com mais vendas
top10_anos_vendas = vendas_por_ano.sort_values(ascending=False).head(10)
print("Top 10 anos com mais vendas:")
print(top10_anos_vendas)

# Vendas por década
vendas_por_decada = df_clean.groupby('Decada')['Global_Sales'].sum()
print("\nVendas por década:")
print(vendas_por_decada)

# Evolução temporal dos gêneros
print("\n=== EVOLUÇÃO DOS GÊNEROS ===")

# Gêneros mais populares por década
for decada in sorted(df_clean['Decada'].unique()):
    dados_decada = df_clean[df_clean['Decada'] == decada]
    genero_mais_popular = dados_decada.groupby('Genre')['Global_Sales'].sum().idxmax()
    print(f"Década {decada}s: {genero_mais_popular}")
   
