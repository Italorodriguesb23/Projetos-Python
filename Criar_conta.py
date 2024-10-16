class Usuario:
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha

usuarios = []

def criar_usuario():
    cpf = input('Digite cpf do usuário: ')
    senha = input('Digite a senha do usuário: ')
    return Usuario(cpf, senha)


while True:
    print('\nBem vindo!')
    print('1. Criar conta')
    print('2. Acessar conta')
    print('3. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        usuario = criar_usuario()
        usuarios.append(usuario)
        print(f'Usuário com cpf {usuario.cpf} e com senha {usuario.senha} criado com sucesso.')
    elif opcao == '2':
        cpf = input('Digite o cpf para acessar a conta: ')
        senha = input('Digite a senha para acessar a conta: ')
        usuario_encontrado = next((u for u in usuarios if u.cpf == cpf and u.senha == senha), None)

        if usuario_encontrado:
            print('Conta acessada com sucesso!')
        else:
            print('Cpf ou senha incorretos.')
    elif opcao == '3':
        break
    else:
        print('Escolha inválida. Tente novamente!')
        break
