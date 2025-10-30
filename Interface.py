import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

def top10_vendas_globais():
    top10.plot(figsize=(10,6), x='Name', y='Global_Sales', kind='bar')
    plt.subplots_adjust(bottom=0.38)
    plt.show()

def top10_menores_vendas_globais():
    top10negative.plot(figsize=(10,6), x='Name', y='Global_Sales', kind='bar')
    plt.subplots_adjust(bottom=0.35)
    plt.show()

def top5_empresas():
    top5empresas.plot(figsize=(10,6), x='Publisher', y='Global_Sales', kind='bar')
    plt.subplots_adjust(bottom=0.35)
    plt.show()

# Bases de dados
top10 = pd.read_csv('top10_vendas_globais.csv')
top10negative = pd.read_csv('top10_menores_vendas_globais.csv')
top5empresas = pd.read_csv('top5_empresas_maiores_vendas.csv')

# Interface
windows = tk.Tk()
windows.geometry('1920x1080')
windows.title("Vendas de Jogos")

# Botão de top10 vendas globais
botaotop10 = tk.Button(windows, text="Top 10 de Vendas Globais", command=top10_vendas_globais)
botaotop10.pack(pady = 10)

# Botão de top10 vendas globais
botaotop10negative = tk.Button(windows, text="Top 10 Menores Vendas Globais", command=top10_menores_vendas_globais)
botaotop10negative.pack(pady = 10)

# Botão de top10 vendas globais
botaotop5empresas = tk.Button(windows, text="Top 5 empresas com maiores vendas", command=top5_empresas)
botaotop5empresas.pack(pady = 10)

# Executar Interface
windows.mainloop()
