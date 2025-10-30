import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

# Funções para exibir gráficos
def top10_vendas_globais():
    top10.plot(figsize=(10,6), x='Name', y='Global_Sales', kind='bar', color='green')
    plt.title("Top 10 Jogos Mais Vendidos (Global)")
    plt.subplots_adjust(bottom=0.35)
    plt.xlabel("Jogo")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()

def top10_menores_vendas_globais():
    top10negative.plot(figsize=(10,6), x='Name', y='Global_Sales', kind='bar', color='red')
    plt.title("Top 10 Jogos com Menores Vendas Globais")
    plt.subplots_adjust(bottom=0.35)
    plt.xlabel("Jogo")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()

def top5_empresas():
    top5empresas.plot(figsize=(10,6), x='Publisher', y='Global_Sales', kind='bar', color='orange')
    plt.title("Top 5 Empresas com Maiores Vendas")
    plt.xlabel("Empresa")
    plt.ylabel("Vendas Globais (milhões)")
    plt.subplots_adjust(bottom=0.25)
    plt.show()

def top10_anos_vendas():
    top10anos.plot(figsize=(10,6), x='Year', y='Número de Jogos', kind='bar', color='purple')
    plt.title("Top 10 Anos com Maiores Vendas")
    plt.xlabel("Ano")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()

def vendas_por_genero():
    generos.plot(figsize=(10,6), x='Genre', y='Vendas Totais (Milhões)', kind='bar', color='blue')
    plt.title("Vendas Totais por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()

def vendas_medias_por_genero():
    generos_medias.plot(figsize=(10,6), x='Genre', y='Vendas Médias (Milhões)', kind='bar', color='cyan')
    plt.title("Vendas Médias por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Média de Vendas (milhões)")
    plt.show()

def vendas_por_decada():
    decadas.plot(figsize=(10,6), x='Decada', y='Vendas Totais (Milhões)', kind='bar', color='brown')
    plt.title("Vendas Totais por Década")
    plt.xlabel("Década")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()

def vendas_por_regiao():
    regioes.plot(figsize=(8,6), x='Região', y='Vendas (Milhões)', kind='bar', color='teal')
    plt.title("Vendas Totais por Região")
    plt.xlabel("Região")
    plt.ylabel("Vendas (milhões)")
    plt.show()

# Carregar bases de dados
top10 = pd.read_csv('top10_vendas_globais.csv')
top10negative = pd.read_csv('top10_menores_vendas_globais.csv')
top5empresas = pd.read_csv('top5_empresas_maiores_vendas.csv')
top10anos = pd.read_csv('top10_anos_com_mais_vendas.csv')
generos = pd.read_csv('vendas_por_genero.csv')
generos_medias = pd.read_csv('vendas_medias_por_genero.csv')
decadas = pd.read_csv('vendas_por_decada.csv')
regioes = pd.read_csv('vendas_por_regiao.csv')

# Interface
windows = tk.Tk()
windows.geometry('400x600')
windows.title("📊 Análises de Vendas de Jogos")

titulo = tk.Label(windows, text="Dashboard de Vendas", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Botões
botaotop10 = tk.Button(windows, text="Top 10 de Vendas Globais", width=40, command=top10_vendas_globais)
botaotop10.pack(pady=5)

botaotop10negative = tk.Button(windows, text="Top 10 Menores Vendas Globais", width=40, command=top10_menores_vendas_globais)
botaotop10negative.pack(pady=5)

botaotop5empresas = tk.Button(windows, text="Top 5 Empresas com Maiores Vendas", width=40, command=top5_empresas)
botaotop5empresas.pack(pady=5)

botao_top10_anos = tk.Button(windows, text="Top 10 Anos com Maiores Vendas", width=40, command=top10_anos_vendas)
botao_top10_anos.pack(pady=5)

botao_genero = tk.Button(windows, text="Vendas Totais por Gênero", width=40, command=vendas_por_genero)
botao_genero.pack(pady=5)

botao_genero_medias = tk.Button(windows, text="Vendas Médias por Gênero", width=40, command=vendas_medias_por_genero)
botao_genero_medias.pack(pady=5)

botao_decada = tk.Button(windows, text="Vendas por Década", width=40, command=vendas_por_decada)
botao_decada.pack(pady=5)

botao_regiao = tk.Button(windows, text="Vendas por Região", width=40, command=vendas_por_regiao)
botao_regiao.pack(pady=5)

# Executar Interface
windows.mainloop()
