import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

janela = tk.Tk()
janela.geometry('800x600')
janela.resizable(True, True)
janela.title('Login')

title = ttk.Label(janela, text='Bem-vindo')
title.pack(padx=10, pady=10, side=tk.TOP)

usuario = ''
senha = ''

def create_account():
    janela_create = tk.Tk()
    janela_create.geometry('400x250')
    janela_create.resizable(False, False)
    janela_create.title('Criar conta')


    usarname_label = tk.Label(janela_create, text='Digite o nome de usuario:')
    usarname_label.pack()

    username = ttk.Entry(janela_create)
    username.pack()

    password_label = tk.Label(janela_create, text='Digite a senha:')
    password_label.pack()

    password = ttk.Entry(janela_create, show='*')
    password.pack()

    def armazenar_dados():
        global usuario
        global senha
        usuario = username.get()
        senha = password.get()
        showinfo(
            title='Conta feita com sucesso',
            message='Usuario cadastrado!'
        )
        print(usuario)
        print(senha)
        janela_create.destroy()

    btn_finalizar = ttk.Button(janela_create, text='finalizar',command=armazenar_dados)
    btn_finalizar.pack(pady=8)

    janela_create.mainloop()

btn_criar_conta = ttk.Button(janela, text='Criar conta', command=create_account)
btn_criar_conta.pack(pady=5)

def login():
    janela_login = tk.Tk()
    janela_login.geometry('400x250')
    janela_login.resizable(False, False)
    janela_login.title('Login')

    usarname_label = tk.Label(janela_login, text='Usuario:')
    usarname_label.pack()

    username = ttk.Entry(janela_login)
    username.pack()

    password_label = tk.Label(janela_login, text='Senha:')
    password_label.pack()

    password = ttk.Entry(janela_login, show='*')
    password.pack()

    def verificar_dados():
        global usuario
        global senha
        usuarioCheck = username.get()
        senhaCheck = password.get()
        if usuarioCheck != usuario or senhaCheck != senha:
            showinfo(
                title='Erro',
                message='Usuario ou Senha incorretos, verifique e tente novamente'
            )
            print('Error')
        elif not usuarioCheck != usuario and not senhaCheck != senha:
            showinfo(
                title='Sucesso',
                message='Usuario logado com sucesso'
            )
            print('Sucesso')
            janela_login.destroy()

    btn_entrar = ttk.Button(janela_login, text='Entrar', command=verificar_dados)
    btn_entrar.pack(pady=8)

    janela_login.mainloop()

btn_login = ttk.Button(janela, text='Entrar', command=login)
btn_login.pack(pady=5)

janela.mainloop()