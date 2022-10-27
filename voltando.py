

x = 1
lista = []
armazen = ()


def asterisco():
    print(30 * '*')


def interface():
    asterisco()
    print('1 - ADICIONAR CARRO\n2 - EXCLUIR CARRO\n3- INFORMAÇÕES DOS CARRO\n4 - SAIR')
    asterisco()


def func_1():
    asterisco()
    marca =input('DIGITE A MARCA DO SEU CARRO\n')
    tempo_de_uso = input('QUANTOS ANOS ELE TEM\n')
    cor = input('COR DO SEU CARRO\n')
    armazen = (f'{marca} {tempo_de_uso} {cor} ')
    lista.append(armazen)
    armazen = ()
    print('OBRIGADO PELA PARTICIPAÇÃO :)')


def func_2():
    c = len(lista)
    if c == 0:
        print("CADASTRE UM CARRO")
    else :
        x = int(input('DIGITE O NÚMERO DO CARRO PARA SER EXCLIDO\n'))
        lista.pop(x-1)
        print(lista)
    

def func_3():
    cont = 1
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