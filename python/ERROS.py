"""
Programa cadastro de Aluno.
Cadastra o nome e a média do aluno e salva em um dicionário
"""
#Erro 1

aluno_media = {}
QTDA_CARACTERES = 60

def criar_linha(caracter, qtda):
    print(caracter * qtda)

def exibir_menu():
    criar_linha('*', QTDA_CARACTERES)
    print("MENU".center(QTDA_CARACTERES))
    criar_linha('*', QTDA_CARACTERES)

    print("""
          1 - CADASTRAR ALUNO  
          2 - MOSTRAR DADOS DO ALUNO     
          3 - SAIR
    """)
    criar_linha('*', QTDA_CARACTERES)

def mostrar_dados():
     if len(aluno_media) > 0:
         print("-" * QTDA_CARACTERES)
         print(f"\033[0;1;33mALUNOS CADASTRADOS = {len(aluno_media)}\033[m")
         print("-" * QTDA_CARACTERES)
         for k, v in aluno_media.items():
            print(f"\033[0;1;33m {k} => {v}\033[m")
         print("-" * QTDA_CARACTERES)
         print()
     else:
         print("\033[0;1;33mNão existe aluno cadastrado!\033[m")
         print()

def inserir_dados():
    nome = input("Digite o nome do aluno\n")
    media = float(input("Digite a média do aluno\n"))
    aluno_media[nome] = media

while True:
    exibir_menu()
    try:
        opcao = int(input("Digite a opcao do menu.txt, por favor.\n"))
    except ValueError:
        print("So aceitamos números cara")
    else:
        if opcao == 1:
            inserir_dados()
        elif opcao == 2:
            mostrar_dados()
        elif opcao == 3:
            
            break
            
            
#Erro 2            
lista = ["João", "Pedro", "Maria", "Sair"]

while True:

        print("LISTA DE NOMES:")
        for i in range(0, len(lista)):
                print(f"{i}: {lista[i]}")

        try:
            indice = int(input("Digite o número da pessoa que quer remover: \n"))
            del(lista[indice])
        except IndexError:
            print("Nada para apagar :(")

        print(f"A lista agora ficou assim: {lista}")
        if indice == 3:
            break            
            
            
            
# Funçaõ para resolver erros de índice

def validando():
    while True:
        try:
            x = int(input("Digite um número: "))
        except ValueError:
            print("Digite um número válido ")
        except KeyboardInterrupt:
            print(":)))))))")
        else:
            return x

validando()
