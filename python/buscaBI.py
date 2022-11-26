listaT = [1,2,3,4,5,6,7,8,9,10]
 
def busca() :
    definicao = 'SIM'
    while definicao == 'SIM':
        buscaa = 0
        começo = 0
        fim = None
        item = 6
        if fim == None:
            fim = len(listaT)
            print(fim)
            definicao = 'n'
    while buscaa == 0:
        meio = (começo + fim)/2
        print(meio)
        if item == meio:
            print('alllll')
            buscaa == 1
        else:
            if item < meio:
                fim = meio - 1
                print('aa')
            else:
                começo = meio + 1
                print('bb')
    
    
        if buscaa == 1:
            print(f'Sim o número \033[0;31m-{item}-\033[m está na lista')
        else:
            print(f'Seu número não foi localizado na lista')
            
        definicao = input('Deseja continuar ? [SIM/NAO]').upper()


busca()
