import random
def busca():
    a = []
    x = random.randint(1, 10)
    c = random.randint(1, 10)
    b = random.randint(1, 10)
    a.append(x)
    if c == x:
        c = random.randint(1, 10)
        a.append(c)
    else:
        a.append(c)
    if b == x or c:
        b = random.randint(1, 10)
        a.append(b)
    else:
        a.append(b)
    info = int(input("Digite um número caso esse número\nesteja em nossa lista você ganha\nesses números são gerados automaticamente escolha:"))
    if info in a:
        print("Boa rapa c acertou!!!!")
        print(f"essa aqui era a lista {a}")
    else:
        print("é falha meu consagrado!!")
        print(f"essa aqui era a lista {a}")
        
busca()