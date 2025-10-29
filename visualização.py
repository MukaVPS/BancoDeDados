import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Pega o caminho da pasta onde o script está rodando
script_dir = os.path.dirname(os.path.abspath(__file__))

# Nome do arquivo CSV
csv_file = "vgsales.csv"

# Caminho completo
csv_path = os.path.join(script_dir, csv_file)

# Verifica se o CSV existe
if not os.path.isfile(csv_path):
    print(f"❌ Arquivo '{csv_file}' não encontrado na mesma pasta do script!")
    print(f"📂 Coloque o arquivo aqui: {script_dir}")
    sys.exit(1)

# Carregar a base de dados
df = pd.read_csv(csv_path)

# Exibir informações gerais
print("Informações gerais:")
print(df.info())
print()

# Prévia dos dados
print("Prévia dos dados:")
print(df.head())
print()

# ----------------------------
# 🔹 Selecionar colunas relevantes
# ----------------------------
colunas = ["Name", "Platform", "Genre", "Publisher",
            "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

df = df[colunas].dropna()

# ----------------------------
# 🔹 Top 10 mais e menos vendidos
# ----------------------------
top_10_mais = df.sort_values(by="Global_Sales", ascending=False).head(10)
top_10_menos = df.sort_values(by="Global_Sales", ascending=True).head(10)

# ----------------------------
# 🔹 Criar figura com subplots (3x2)
# ----------------------------
fig, axs = plt.subplots(3, 2, figsize=(14, 14))
fig.suptitle("📊 Análise Completa de Vendas Globais de Jogos", fontsize=16, weight='bold')

# ----------------------------
# 🟩 Gráfico 1 — Top 10 Mais Vendidos
# ----------------------------
axs[0, 0].barh(top_10_mais["Name"][::-1], top_10_mais["Global_Sales"][::-1], color="green")
axs[0, 0].set_title("Top 10 Jogos Mais Vendidos")
axs[0, 0].set_xlabel("Vendas Globais (milhões)")
axs[0, 0].set_ylabel("Jogo")

# ----------------------------
# 🟥 Gráfico 2 — Top 10 Menos Vendidos
# ----------------------------
axs[0, 1].barh(top_10_menos["Name"], top_10_menos["Global_Sales"], color="red")
axs[0, 1].set_title("Top 10 Jogos Menos Vendidos")
axs[0, 1].set_xlabel("Vendas Globais (milhões)")
axs[0, 1].set_ylabel("Jogo")

# ----------------------------
# 🌍 Gráfico 3 — Vendas por Região (Top 10 Mais Vendidos)
# ----------------------------
regioes = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
somas_regioes = top_10_mais[regioes].sum().sort_values(ascending=False)
axs[1, 0].bar(regioes, somas_regioes, color=["blue", "orange", "purple", "gray"])
axs[1, 0].set_title("Distribuição de Vendas por Região (Mais Vendidos)")
axs[1, 0].set_ylabel("Vendas Totais (milhões)")

# ----------------------------
# 🌎 Gráfico 4 — Vendas por Região (Menos Vendidos)
# ----------------------------
somas_regioes_menos = top_10_menos[regioes].sum().sort_values(ascending=False)
axs[1, 1].bar(regioes, somas_regioes_menos, color=["blue", "orange", "purple", "gray"])
axs[1, 1].set_title("Distribuição de Vendas por Região (Menos Vendidos)")
axs[1, 1].set_ylabel("Vendas Totais (milhões)")

# ----------------------------
# 🥧 Gráfico 5 — Pizza (Mais Vendidos)
# ----------------------------
axs[2, 0].pie(
    somas_regioes,
    labels=somas_regioes.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["blue", "orange", "purple", "gray"]
)
axs[2, 0].set_title("Participação das Regiões nas Vendas (Mais Vendidos)")

# ----------------------------
# 🥧 Gráfico 6 — Pizza (Menos Vendidos)
# ----------------------------
axs[2, 1].pie(
    somas_regioes_menos,
    labels=somas_regioes_menos.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["blue", "orange", "purple", "gray"]
)
axs[2, 1].set_title("Participação das Regiões nas Vendas (Menos Vendidos)")

# Ajustar espaçamento e exibir
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
