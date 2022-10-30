

x = 1
lista = []
armazen = ()


def asterisco():
    print(30 * '*')


def interface():
    asterisco()
    print('1 - ADICIONAR CARRO\n2 - EXCLUIR CARRO\n3 - INFORMAÇÕES DOS CARRO\n4 - SAIR')
    asterisco()


def func_1():
    asterisco()
    marca =input('DIGITE A MARCA DO SEU CARRO\n').upper()
    try:
        tempo_de_uso = int(input('QUANTOS ANOS ELE TEM\n'))
        cor = input('COR DO SEU CARRO\n').upper()
        armazen = (f'{marca} DE {2022 - tempo_de_uso} NA COR {cor} ')
        lista.append(armazen)
        armazen = ()
        print('OBRIGADO PELA PARTICIPAÇÃO :)')
    except ValueError:
        print("POR FAVOR DIGITE QUANTOS ANOS ELE TEM OU DE QUANDO ELE É EM NÚMEROS")
    

def func_2():
    c = len(lista)
    if c == 0:
        print("CADASTRE UM CARRO")
    else :
        x = int(input('DIGITE O NÚMERO DO CARRO PARA SER EXCLIDO\n'))
        lista.pop(x-1)
    

def func_3():
    cont = 1
    c = len(lista)
    if c == 0:
        print("CADASTRE UM CARRO")
    else :
        for index in lista:
            print(f'{cont} - {index}')
            cont = cont + 1
        
while x == 1:
    interface()
    opção = int(input('ESCOLHA UMA OPÇÃO\n'))
    if opção == 1:
        func_1()
    elif opção == 2:
        func_2()
    elif opção == 3:
        func_3()
    elif opção == 4:
        x = 0