def aste():
    print('\033[0;36m*\033[m' * 30)


def comparar(valor_um, valor_dois):
    if valor_um > valor_dois:
        print(f"O PRIMEIRO VALOR -- \033[0;32m{valor_um}\033[m -- \nÉ MAIOR QUE O SEGUNDO -- \033[0;32m{valor_dois}\033[m --")
    else:
        print(f"O SEGUNDO VALOR -- \033[0;32m{valor_dois}\033[m -- \nÉ MAIOR QUE O PRIMEIRO -- \033[0;32m{valor_um}\033[m --")


aste()    
valor_um = int(input('PRIMEIRO VALOR\033[0;32m\n'))
valor_dois = int(input('\033[mSEGUNDO VALOR\033[0;32m\n'))
aste()

comparar(valor_um,valor_dois)
aste()