# 1 – Crie um arquivo chamado menu.txt com todas as opções do menu do programa(Segunda imagem.
# 2 – Altere a função exibir_menu(), especificamente nas linhas 17 a 21, removendo o código dessas linhas
# e colocando o código necessário para ler o arquivo menu.txt e exibir os dados do arquivo na tela do
# programa.
"""
Programa cadastro de Aluno.
Cadastra o nome e a média do aluno e salva em um dicionário
"""

aluno_media = {}
QTDA_CARACTERES = 60

def criar_linha(caracter, qtda):
    print(caracter * qtda)

def exibir_menu():
    criar_linha('*', QTDA_CARACTERES)
    print("MENU".center(QTDA_CARACTERES))
    criar_linha('*', QTDA_CARACTERES)

    with open("arquivos_txt/menu.txt", "a+") as file: #criar a pasta arquivos_txt e os arquivos menu.txt cadastra_A.txt backup.txt
    #     file.write("1 - CADASTRAR ALUNO\n")
    #     file.write("2 - MOSTRAR DADOS DO ALUNO\n")
    #     file.write("3 - DELETAR ALUNO DO DICIONÁRIO\n")
    #     file.write("4 - FAZER BACKUP EM ARQUIVOS\n")
    #     file.write("5 - EXIBIR ALUNOS CADASTRADOS DO ARQUIVO\n")
    #     file.write("6 - SAIR")


        file.seek(0)
        print(file.read())
        
  
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

    with open("arquivos_txt/cadastro_A.txt", "a+") as file:
        file.write(f"{nome}:     {media}\n")

def deletar_aluno():
    nome = input("Digite o nome do aluno\n")
    aluno_media.pop(nome)

def backup():
    with open("arquivos_txt/backup.txt", "a+") as file:
        for k, v in aluno_media.items():
            file.write(f"{k}:{v}\n")

def aulos_cadastrados():
    print(20 * "-")
    print("Alunos       Média")
    print(20 * "-")
    with open("arquivos_txt/cadastro_A.txt", "a+") as file:
        file.seek(0)
        print(file.read())

while True:
    exibir_menu()
    opcao = int(input("Digite a opcao do menu.txt, por favor.\n"))
    if opcao == 1:
        inserir_dados()
    elif opcao == 2:
        mostrar_dados()
    elif opcao == 3:
        deletar_aluno()
    elif opcao == 4:
        backup()
    elif opcao == 5:
        aulos_cadastrados()
    elif opcao == 6:
        break
