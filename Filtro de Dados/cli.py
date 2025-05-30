import tkinter as tk
from backend import get_registros

def filtrar():
    msg = entrada.get()
    col, val = msg.split(", ")
    output = get_registros(col, val)
    saida.delete("1.0", "end")
    [[saida.insert("end", f"{key}: {value}\n") for key, value in info.items()] for info in output]

janela = tk.Tk()
janela.title("Filtro de Dados")
janela.config(bg="#060039")
janela.geometry("400x450+750+270")

titulo = tk.Label(
    janela,
    text="Filtro de Dados",
    font=("Gelasio", 25, "bold"),
    border=3,
    highlightcolor="#ffffff",
    highlightthickness=3,
    relief="flat",
    justify="center",
    bg="#001763",
    fg="#d9d3f3",
)
titulo.pack(pady=10)

entrada = tk.Entry(
    janela, 
    width=25,
    font=("Gelasio", 15, "bold"),
    border=3,
    relief="sunken",
    bg="#f8e6ff",
    highlightcolor="#00900c",
    highlightthickness=3
)
entrada.pack(pady=10)

botao = tk.Button(
    janela,
    text="Filtrar",
    font=("Gelasio", 18, "bold"),
    border=3,
    relief="raised",
    justify="center",
    bg="#001763",
    fg="#d9d3f3",
    activebackground="#d9d3f3",
    activeforeground="#001763",
    command=filtrar
)
botao.pack(pady=5)

saida = tk.Text(
    janela,
    wrap="word",
    width=40,
    font=("Gelasio", 12),
    bg="#202020",
    fg="#d9d3f3",
    border=2,
    relief="ridge"
)
saida.pack(pady=20, padx=40)

janela.mainloop()