dic_1 = {'primeiro' : 1, 'segundo' : 2, 'terceiro' : 3, 'quarto' : 4}
dic_2 = dict(primeiro=1, segundo=2, terceiro=3)




print(dic_1['primeiro'])
print('*' * 30)
print(dic_2)
print('*' * 30)
print(dic_1['quarto'])
print('*' * 30)
# print(dic_1['quinto'])
print('*' * 30)
print(dic_1.get('quinto'))
print('*' * 30)
print(dic_1.get('quarto' , 'essa chave não existe'))
print('*' * 30)# uma especie de if
print(dic_1.get('quinto' , 'essa chave não existe'))
print('*' * 30)
print(dic_1.values())
print('*' * 30)
print(dic_1.keys())
print('*' * 30)
for chave in dic_1.keys():
    print(f'chave = {chave} é Valor = {dic_1[chave]}')
print('*' * 30)
for valor in dic_1.values():
    print(f'')
print('*' * 30)
print(dic_1.items())
for chave, valor in dic_1.item():
    print(f'chave = {chave} - Valor ={valor}')
