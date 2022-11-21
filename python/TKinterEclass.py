"""
Conhecendo o tkinter e o entry
"""

from tkinter import *
from tkinter import ttk


def imprimirDados():
    print("Nome: %s" % nome.get())
    print("Idade: %s" % idade.get())
    print("Gênero %s" % cb_genero.get())
    print("Observação: %s" % obs.get(1.0, END))


def SalvarDados():
    with open('lpo_aprendizagem/dados.txt' , "a+") as file:
        file.write(f"Nome :{nome.get()} \n")
        
        file.write(f"Idade : {idade.get()} \n")
       
        file.write(f"Gênero : {cb_genero.get()} \n")
        
        file.write(f"Obeservação : {obs.get(1.0, END)} \n -------------------------------------------------------------------------------")
        



app=Tk()
app.title("CADASTRO DE PESSOAS")
app.geometry("320x360")
#app.configure(background="Gainsboro")

txt1=Label(app, text="CADASTRO DE PESSOAS", background="black", foreground="#fff")
txt1.pack(ipadx=10, ipady=0, padx=0, pady=0, fill=X)

app['bg'] = '#49A'

Label(app, text="Nome", background="#49A", foreground="#fff", anchor=W).place(x=10, y=30, width=150, height=30)
nome = Entry(app)
nome.place(x=10, y=60, width=300, height=20)

Label(app, text="Idade", background="#49A", foreground="#fff", anchor=W).place(x=10, y=80, width=150, height=30)
idade = Entry(app)
idade.place(x=10, y=110, width=300, height=20)

Label(app, text="Gênero", background="#49A", foreground="#fff", anchor=W).place(x=10, y=130, width=150, height=30)
generolista = ['Masculino', 'Feminino' , 'gaysafado']

cb_genero = ttk.Combobox(app, values=generolista, state="readonly")
cb_genero.set("Masculino")
cb_genero.pack()


cb_genero.place(x=10, y=160, width=300, height=24)

#Widget Text
Label(app, text="Observação", background="#49A", foreground="#fff", anchor=W).place(x=10, y=190, width=150, height=10)
obs = Text(app)
obs.place(x=10, y=208, width=300, height=50)

btnImprimir = Button(app, text="Imprimir", command=imprimirDados).place(x=10, y=280, width=302, height=30)
btnSalvar = Button(app, text="Salvar dados", command=SalvarDados).place(x=10, y=320, width=302, height=30)
app.mainloop()

