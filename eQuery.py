import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

# Função chamada quando alguma opção é selecionada ou desselecionada
def option_changed():
    print("Opção selecionada:", selected_option.get())

def submit_form():
    server_name = server_entry.get()
    database_name = database_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    selection = selection_combobox.get()
    
    print("Server Name:", server_name)
    print("Database Name:", database_name)
    print("Login:", login)
    print("Password:", password)
    print("Selection:", selection)

root = tk.Tk()
root.title("Querry Executor -- Developer by Carlos Souza")
root.geometry('550x570')

# Variável para armazenar a opção selecionada
selected_option = tk.IntVar()

# Campo para o nome do servidor
database_type = ttk.Frame(root)
dbtype_label = ttk.Label(root, text="Tipo de banco de dados:")
database_type.pack()
dbtype_label.pack()

# Criação dos Radiobuttons
option1_rb = ttk.Radiobutton(root, text="SQL Server", variable=selected_option, value=1, command=option_changed)
option2_rb = ttk.Radiobutton(root, text="MySQL", variable=selected_option, value=2, command=option_changed)
option3_rb = ttk.Radiobutton(root, text="SQLite", variable=selected_option, value=3, command=option_changed)
option4_rb = ttk.Radiobutton(root, text="PostgreSQL", variable=selected_option, value=4, command=option_changed)

# Posicionamento dos Radiobuttons na janela
option1_rb.pack()
option2_rb.pack()
option3_rb.pack()
option4_rb.pack()

# Campo para o nome do servidor
input_server = ttk.Frame(root)
server_label = ttk.Label(root, text="Nome do Servidor:")
server_entry = ttk.Entry(root)
server_label.pack()
server_entry.pack(side = 'left')
input_server.pack(pady = 10)

# Campo para o banco de dados
database_label = ttk.Label(root, text="Banco de Dados:")
database_label.pack()
database_entry = ttk.Entry(root)
database_entry.pack()

# Campo para o login
login_label = ttk.Label(root, text="Login:")
login_label.pack()
login_entry = ttk.Entry(root)
login_entry.pack()

# Campo para a senha
password_label = ttk.Label(root, text="Senha:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

# Caixa seletora
selection_label = ttk.Label(root, text="Opções:")
selection_label.pack()
selection_combobox = ttk.Combobox(root, values=["Opção 1", "Opção 2", "Opção 3"])
selection_combobox.pack()

# Botão de envio
submit_button = ttk.Button(root, text="Enviar", command=submit_form)
submit_button.pack()

root.mainloop()
 