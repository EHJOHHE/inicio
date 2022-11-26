lista = []
verificação_de_usuario = []


def asterisco():
    print('*' * 30)


def cadastro():
    x = 1
    asterisco()
    pessoa = input('SEU NOME COMPLETO:\n')
    a = ('cls','w')
    a
    usuario = input('LOGIN:\n').upper().strip()
    if usuario in verificação_de_usuario:
        print('USUARIO JA EXISTENTE')
        cadastro()
    else:    
        senha = input('SENHA:\n').strip()
        confimar_senha = input('CONFIRME SUA SENHA:\n').strip()
        print(senha , confimar_senha)
        if senha == confimar_senha:
            asterisco()
            verificação_de_usuario.append(usuario)
            lista[usuario] = senha
            with open('dados_py/clientes_cadastrados.txt', 'a+')as file:
                file.write(f'{lista}')
                
            lista.clear
            print('CADASTRO FEITO COM SUCESSO!!')
            asterisco()
        else:
            print('COMFIRMAÇÃO DA SENHA ERRADA TENTE NOVAMENTE')
            cadastro()
            
            
def login():
    with open('dados_py/clientes_cadastrados.txt', 'a+')as file:
        file.seek(0)
        lista = file.read()
    print('SEJA BEM VINDO NOVAMENTE!!')
    user = input('LOGIN\n')
    senha = input('SENHA\n')





cadastro()