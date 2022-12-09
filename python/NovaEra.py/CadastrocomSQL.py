import mysql.connector
from mysql.connector import Error


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = input("Qual seu sexo M/F: ")
usuario = input("Digite o seu login: ")
senha = (input("Digite sua senha: "))

dados = (f"('{nome}',{idade},'{sexo}','{usuario}','{senha}')")
entradaDosDados = (f"INSERT INTO Usuario\n(nome,idade,sexo,usuario,senha)\nVALUES {dados}")
sql = entradaDosDados



try:
    con = mysql.connector.connect(host="localhost",database="Cadastrar",user="Paulo",password="PrDeT_17")
        
    busca = "select * from Usuario;"
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.execute(busca)
    linhas = cursor.fetchall()
    print("Pessoas cadastradas:", cursor.rowcount)
        
    for i in linhas:
        print("id:", i[0])
        print("nome:", i[1])
        print("idade:", i[2])
        print("sexo:", i[3])
        print("Usuário:", i[4])
        print("senha:", i[5])
except Error as e:
    print("Falha na conexão" , e)
finally:
    if(con.is_connected):
        con.close()
        cursor.close()
        print("Conexão com o banco de dados fechada")


# def numeroDePessoasCadastradas ():
#     busca = "select * from Usuario;"
#     cursor = con.cursor()
#     cursor.execute(busca)
#     linhas = cursor.fetchall()
#     print("Pessoas cadastradas:", cursor.rowcount)

 
# def mostraPessoasCadastradas():
#     print("Todos usuários cadastrados")
#     for i in linhas:
#         print("id", i[0])
#         print("nome", i[1])
#         print("idade", i[2])
#         print("sexo", i[3])
#         print("Usuário", i[4])
#         print("senha", i[5])
#         print("a")
        
# def fim():
#     con.close()
#     cursor.close()
#     print("Conexão com o banco de daods cancelada")


