def aste():
    print(30 * '\033[0;36m*\033[m')


def calculo(valor_da_casa, salario, tempo):
    tempo = tempo*12
    valor_da_casa = valor_da_casa/tempo
    salario = (salario * 30)/100
    if valor_da_casa >= salario:
        print("\033[4;31mINFELIZMENTE NÃO É POSSÍVEL COMPRA A CASA\033[m")
    else:
        print("\033[4;31mPARABÉNS VOCÊ PODE COMPRAR ESSA CASA\033[m")
        

aste()
valor_da_casa = int(input("DIGITE O PREÇO DA CASA EM R$\033[0;32m\n"))
salario = int(input("\033[mDIGITE SEU SÁLARIO\033[0;32m\n"))
tempo = int(input("\033[mEM QUANTO TEMPO PRETENDE PAGAR\033[0;32m\n"))
aste()


calculo(valor_da_casa, salario, tempo)