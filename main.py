import tkinter as tk
from tkinter import ttk
from flask import Flask, render_template

app = Flask(__name__)

# Função para pesquisar a palavra dentro do arquivo HTML
def pesquisar():
    # Limpa a lista de resultados
    lista_resultados.delete(0, tk.END)
    
    # Obtém a palavra da entrada
    palavra = entry.get().lower()
    
    # Abre o arquivo HTML e busca a palavra nele
    with open("arquivo.html", "r", encoding="utf-8") as file:
        linhas = file.readlines()
        
        for linha in linhas:
            if palavra in linha.lower():
                lista_resultados.insert(tk.END, linha.strip())

        if lista_resultados.size() == 0:
            lista_resultados.insert(tk.END, f"A palavra '{palavra}' não foi encontrada no acervo.")

# Rota inicial para renderizar o template HTML
@app.route('/')
def index():
    return render_template('index.html')

# Cria a janela Tkinter
janela = tk.Tk()
janela.title("Pesquisa em Arquivo HTML")

# Estilo para o Listbox
style = ttk.Style(janela)
style.configure("CustomListbox.TListbox", background="#f0f0f0", foreground="#30503a", font=("Arial", 10))

# Estilo para a barra de pesquisa e botão
s = ttk.Style()
s.theme_use('default')
s.configure('TEntry', background='#30503a')  # Estiliza a cor da entrada
s.configure('TButton', background='#30503a')  # Estiliza a cor do botão

# Cria uma entrada para inserir a palavra a ser pesquisada
entry = ttk.Entry(janela)
entry.pack(pady=10, ipady=5)  # ipady é o padding interno para a altura

# Cria um botão para iniciar a pesquisa
botao_pesquisar = ttk.Button(janela, text="Pesquisar", command=pesquisar)
botao_pesquisar.pack()

# Cria uma lista para exibir os resultados da pesquisa
lista_resultados = tk.Listbox(janela, width=100, height=10, bg="#f0f0f0", fg="#30503a", font=("Arial", 10))
lista_resultados.pack(pady=10)

if __name__ == '__main__':
    app.run(debug=True)

