import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

def top10_vendas_globais():
    top10.plot(figsize=(10,6), x='Name', y='Global_Sales', kind='bar')
    plt.subplots_adjust(bottom=0.38)
    plt.show()

# Bases de dados
top10 = pd.read_csv('top10_vendas_globais.csv')

# Interface
windows = tk.Tk()
windows.geometry('1920x1080')
windows.title("Vendas de Jogos")

# Botão de top10 vendas globais
botaotop10 = tk.Button(windows, text="Top 10 de Vendas Globais", command=top10_vendas_globais)
botaotop10.pack(pady = 20)

# Executar Interface
windows.mainloop()
