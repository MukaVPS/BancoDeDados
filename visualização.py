import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import sys

plt.style.use('ggplot')

df = pd.read_csv('vgsales.csv')
top_10_mais = pd.read_csv('top10_vendas_globais.csv')
top_10_menos = pd.read_csv('top10_menores_vendas_globais.csv')

plt.rcParams['font.family'] = 'Segoe UI Emoji'

print("Informações gerais:")
print(df.info())
print()

print("Prévia dos dados:")
print(df.head())
print()

colunas = ["Name", "Platform", "Genre", "Publisher",
            "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

df = df[colunas].dropna()

fig, axs = plt.subplots(3, 2, figsize=(14, 14))
fig.suptitle("📊 Análise Completa de Vendas Globais de Jogos", fontsize=16, weight='bold', color='#006600')

axs[0, 0].barh(top_10_mais["Name"][::-1], top_10_mais["Global_Sales"][::-1], color="#00FF00")
axs[0, 0].set_title("Top 10 Jogos Mais Vendidos")
axs[0, 0].set_xlabel("Vendas Globais (milhões)")
axs[0, 0].set_ylabel("Jogo")

axs[0, 1].barh(top_10_menos["Name"], top_10_menos["Global_Sales"], color="#FF0000")
axs[0, 1].set_title("Top 10 Jogos Menos Vendidos")
axs[0, 1].set_xlabel("Vendas Globais (milhões)")
axs[0, 1].set_ylabel("Jogo")

regioes = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
somas_regioes = top_10_mais[regioes].sum().sort_values(ascending=False)
axs[1, 0].bar(regioes, somas_regioes, color=["#00BFFF", "#FFCC00", "#FF66FF", "gray"])
axs[1, 0].set_title("Distribuição de Vendas por Região (Mais Vendidos)")
axs[1, 0].set_ylabel("Vendas Totais (milhões)")

somas_regioes_menos = top_10_menos[regioes].sum().sort_values(ascending=False)
axs[1, 1].bar(regioes, somas_regioes_menos, color=["#00BFFF", "#FFCC00", "#FF66FF", "gray"])
axs[1, 1].set_title("Distribuição de Vendas por Região (Menos Vendidos)")
axs[1, 1].set_ylabel("Vendas Totais (milhões)")

axs[2, 0].pie(
    somas_regioes,
    labels=somas_regioes.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#00BFFF", "#FFCC00", "#FF66FF", "gray"]
)
axs[2, 0].set_title("Participação das Regiões nas Vendas (Mais Vendidos)")

axs[2, 1].pie(
    somas_regioes_menos,
    labels=somas_regioes_menos.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#00BFFF", "#FFCC00", "#FF66FF", "gray"]
)
axs[2, 1].set_title("Participação das Regiões nas Vendas (Menos Vendidos)")

plt.tight_layout(rect=[0, 0, 1, 0.97], pad=3.0)
plt.show()

