import sqlite3
import tkinter as tk
from tkinter import messagebox

# --- Configuração do Banco de Dados ---
def criar_banco():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

# --- Funções do Programa ---
def salvar_cliente():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos antes de salvar.")
        return

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    limpar_formulario()

def limpar_formulario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# --- Interface Gráfica ---
root = tk.Tk()
root.title("Cadastro de Clientes")

# Labels e Entradas
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="E-mail:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_telefone = tk.Entry(root, width=40)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

# Botões
btn_salvar = tk.Button(root, text="Salvar", command=salvar_cliente, bg="lightgreen")
btn_salvar.grid(row=3, column=0, padx=10, pady=10)

btn_limpar = tk.Button(root, text="Limpar", command=limpar_formulario, bg="lightcoral")
btn_limpar.grid(row=3, column=1, padx=10, pady=10)

# Inicializar banco
criar_banco()

# Executar aplicação
root.mainloop()
