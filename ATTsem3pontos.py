def aste():
    print(30*"*")



aste()
print('MENU - CADASTRO DE PALAVRAS')
aste()
print('  1 - CADASTRAR PALAVRAS \n  2 - EXIBIR TODAS AS PALAVRAS \n  3 - EXIBIR TODOS OS SIGNIFICADOS \n  4 - EXBIR TODAS AS PALAVRAS E SEUS SIGNIFICADOS \n  5 - SAIR')
aste()


def question():
    dict_01 = {'f':'f' }
    x = 2
    while x > 0:
        entrada = int(input('Escolha a opção, por favor: '))
        if entrada == 1:
            
            chave = input('CADASTRAR PALAVRAS: ')
            dict_01[chave] = input('SIGNIFICADO DA PALAVRA: ')
            print(dict_01)
        if entrada == 2:
            if dict_01['f'] == "f":
                print("Seu dicionário não tem nenhuma palavra cada")
            else :
                print(dict_01.keys())    
        if entrada == 3:
            print(dict_01.values())
        if entrada == 4:
            for chave, valor in dict_01.items():
                print(f' chave {chave} e o valor é {valor}')
        if entrada == 5:
            break    



question()
