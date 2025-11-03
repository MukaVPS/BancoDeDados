import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

plt.style.use('ggplot')


# Funções para exibir gráficos
def top10_vendas_globais():
    top10.plot(figsize=(15, 8), x='Name', y='Global_Sales', kind='bar', legend=False, color='#00FF00')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 10 Jogos Mais Vendidos (Global)")
    plt.subplots_adjust(bottom=0.35)
    plt.xlabel("Jogo")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()


def top10_menores_vendas_globais():
    top10negative.plot(figsize=(10, 6), x='Name', y='Global_Sales', kind='bar', color='#FF0000')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 10 Jogos com Menores Vendas Globais")
    plt.subplots_adjust(bottom=0.35)
    plt.xlabel("Jogo")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()


def top5_empresas():
    top5empresas.plot(figsize=(10, 6), x='Publisher', y='Global_Sales', kind='bar', color='#00FFFF')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 5 Empresas com Maiores Vendas")
    plt.xlabel("Empresa")
    plt.ylabel("Vendas Globais (milhões)")
    plt.subplots_adjust(bottom=0.25)
    plt.show()


def top10_anos_vendas():
    top10anos.plot(figsize=(10, 6), x='Year', y='Número de Jogos', kind='bar', color='#FFCC00')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 10 Anos com Maiores Vendas")
    plt.xlabel("Ano")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()


def vendas_por_genero():
    generos.plot(figsize=(10, 6), x='Genre', y='Vendas Totais (Milhões)', kind='bar', color='#FF66FF')
    plt.xticks(rotation=45, ha='right')
    plt.title("Vendas Totais por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()


def vendas_medias_por_genero():
    generos_medias.plot(figsize=(10, 6), x='Genre', y='Vendas Médias (Milhões)', kind='bar', color='#00BFFF')
    plt.xticks(rotation=45, ha='right')
    plt.title("Vendas Médias por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Média de Vendas (milhões)")
    plt.show()


def vendas_por_decada():
    decadas.plot(figsize=(10, 6), x='Decada', y='Vendas Totais (Milhões)', kind='bar', color='#00FF00')
    plt.xticks(rotation=45, ha='right')
    plt.title("Vendas Totais por Década")
    plt.xlabel("Década")
    plt.ylabel("Vendas Globais (milhões)")
    plt.show()


def vendas_por_regiao():
    regioes.plot(figsize=(8, 6), x='Região', y='Vendas (Milhões)', kind='bar', color='#FF0000')
    plt.xticks(rotation=45, ha='right')
    plt.title("Vendas Totais por Região")
    plt.xlabel("Região")
    plt.ylabel("Vendas (milhões)")
    plt.show()


def jogos_ano():
    jogos_por_ano.plot(figsize=(8, 6), x='Year', y='Número de Jogos', kind='bar', color='#00FFFF')
    plt.xticks(rotation=45, ha='right')
    plt.title("Jogos por Ano")
    plt.xlabel("Anos")
    plt.ylabel("Quantidade Jogos")
    plt.show()


def jogos_decada():
    jogos_por_decada.plot(figsize=(8, 6), x='Decada', y='Número de Jogos', kind='bar', color='#FFCC00')
    plt.xticks(rotation=45, ha='right')
    plt.title("Jogos por Década")
    plt.xlabel("Décadas")
    plt.ylabel("Quantidade Jogos")
    plt.show()


def top3_mais_lucrativos():
    top3_generos_mais_lucrativos.plot(figsize=(8, 6), x='Genre', y='Global_Sales', kind='bar', color='#FF66FF')
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 3 Gêneros Mais Lucrativos")
    plt.xlabel("Gêneros")
    plt.ylabel("Vendas")
    plt.show()


# Função para estilização dos botões da interface
def botao(text, command):
    btn = tk.Button(windows, text=text, command=command)
    btn.configure(
        width=35, height=2,
        bg='#333333', fg='#FFFFFF',
        font=('Verdana', 10, 'bold'),
        relief=tk.RAISED, bd=4,
        activebackground='#00FF00',
        activeforeground='#000000'
    )
    btn.pack(pady=5, padx=20)


# Carregar bases de dados
top10 = pd.read_csv('top10_vendas_globais.csv')
top10negative = pd.read_csv('top10_menores_vendas_globais.csv')
top5empresas = pd.read_csv('top5_empresas_maiores_vendas.csv')
top10anos = pd.read_csv('top10_anos_com_mais_vendas.csv')
generos = pd.read_csv('vendas_por_genero.csv')
generos_medias = pd.read_csv('vendas_medias_por_genero.csv')
decadas = pd.read_csv('vendas_por_decada.csv')
regioes = pd.read_csv('vendas_por_regiao.csv')
jogos_por_ano = pd.read_csv('jogos_por_ano.csv')
jogos_por_decada = pd.read_csv('jogos_por_decada.csv')
top3_generos_mais_lucrativos = pd.read_csv('top3_generos_mais_lucrativos.csv')

# Interface
windows = tk.Tk()
windows.geometry('400x600')
windows.configure(bg='#F0F0F0')
windows.title("📊 Análises de Vendas de Jogos")

titulo = tk.Label(windows, text="Dashboard de Vendas",
                  bg='#F0F0F0',
                  fg='#006600',
                  font=("Arial", 20, "bold"))

titulo.pack(pady=10)

botao("Top 10 de Vendas Globais", command=top10_vendas_globais)
botao("Top 10 Menores Vendas Globais", command=top10_menores_vendas_globais)
botao("Top 5 Empresas com Maiores Vendas", command=top5_empresas)
botao("Top 10 Anos com Maiores Vendas", command=top10_anos_vendas)
botao("Vendas Totais por Gênero", command=vendas_por_genero)
botao("Vendas Médias por Gênero", command=vendas_medias_por_genero)
botao("Vendas por Década", command=vendas_por_decada)
botao("Vendas por Região", command=vendas_por_regiao)
botao("Top 3 Gêneros Mais Lucrativos", command=top3_mais_lucrativos)

# Executar Interface
windows.mainloop()
