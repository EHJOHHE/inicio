# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os 
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

def b():
    print(30*"*")

def exerc94():
    listaT= []
    pessoas = {}   

    x = "S"
    n = 0
    
    soma = 0

    
    while x == "S":
        b()
        pessoas.clear()
        pessoas["NOME"] = input(" NOME: ").upper()
        
        pessoas["SEXO"] = input(" SEXO [M/F]: ") #FDS A INCLUSÃO E OLHA QUE EU SOU BI SA POURA
        pessoas["SEXO"] = pessoas["SEXO"].upper()
        
        if pessoas["SEXO"] == "M":
            n=1
        elif pessoas["SEXO"] == "F":
            n=2
        else :
            print("Por favor escolha M ou F seu gay safado")
            break
        
        
        pessoas["IDADE"] = int(input(" IDADE: "))
        soma = soma + pessoas["IDADE"]
        print("\n")
        
        listaT.append(pessoas.copy())
        print(listaT)
        y = input(" MAIS ALGUEM? [S/N]:")
        y = y.upper()
        b()
        
        if y ==  "S":
            x = "S"
        else :
            x = "N"
    media = soma/len(listaT)
    b()
    print(f"A) Quantas pessoas foram cadastradas: {len(listaT)}")
    b()
    print(f"B) A média de idade é: {soma/len(listaT):.0f}")
    b()
    print(f"C) Uma lista com as mulheres:", end=" ")
    for s in listaT:
        if s["SEXO"] == "F":
            print(f'{s["NOME"]}, ', end="")
    print("")
        
    b()
    print("D) Uma lista de pessoas com idade acima da média:" , end=" ")
    for p in listaT:
        if p["IDADE"] >= media:
            print(f'{p["NOME"]}, ', end="")
    print("")
    
    
exerc94()
