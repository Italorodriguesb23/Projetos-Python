from datetime import datetime


class Banco:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        self.saques_diarios = 0
        self.data_ultimo_saque = None

    def deposito(self, valor):
        if valor <= 0:
            print("Não é possível fazer o depósito. O valor deve ser positivo.")
            return

        self.saldo += valor
        self.transacoes.append(f'Depósito: R${valor:.2f}')
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        self.mostrar_extrato()

    def saque(self, valor):
        hoje = datetime.now().date()


        if self.data_ultimo_saque != hoje:
            self.data_ultimo_saque = hoje
            self.saques_diarios = 0

        if valor > 500:
            print('O valor do saque não pode exceder R$500.')
            return

        if valor > self.saldo:
            print('Saldo insuficiente para o saque.')
            return

        if self.saques_diarios >= 3:
            print('Limite de saques diários atingido.')
            return

        self.saldo -= valor
        self.transacoes.append(f'Saque: R${valor:.2f}')
        self.saques_diarios += 1
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
        self.mostrar_extrato()

    def mostrar_extrato(self):
        print("\nExtrato Bancário:")
        print(f'Saldo atual: R${self.saldo:.2f}')
        print("Transações:")
        for transacao in self.transacoes:
            print(f'  - {transacao}')



banco = Banco()

while True:
    print('\nBem-vindo ao sistema bancário!')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Mostrar Extrato')
    print('4. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        try:
            valor = float(input("Digite o valor do depósito: "))
            banco.deposito(valor)
        except ValueError:
            print("Valor inválido. Digite um número.")
    elif opcao == '2':
        try:
            valor = float(input('Digite o valor do saque: '))
            banco.saque(valor)
        except ValueError:
            print("Valor inválido. Digite um número.")
    elif opcao == '3':
        banco.mostrar_extrato()
    elif opcao == '4':
        print('Saindo do sistema...')
        break
    else:
        print('Operação inválida. Tente novamente.')
