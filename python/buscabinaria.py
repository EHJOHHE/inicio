import random

lista = list(range(1,101))

def busca(array, item, começo=0, fim=None):
    if fim == None:
        end = len(array)-1
    if começo <= fim:
        meio = (começo + fim)//2
        if array[meio] == item:
            return meio
        if item < array[meio]:
            return busca(array, item, começo, meio-1)
        else :
            return busca(array, item, meio+1, fim)
    
    
    