class ContaBancaria:
    def __init__(self):
        self.__saldo = 0.0
        self.__extrato = []
        self.__saques_realizados = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.__saques_realizados >= 3:
            print("Limite de saques diários atingido. Você já realizou 3 saques.")
            return
        if valor <= 500:
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__extrato.append(f'Saque: R$ {valor:.2f}')
                self.__saques_realizados += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque não pode exceder R$ 500.00.")

    def extrato(self):
        print("\nExtrato:")
        if not self.__extrato:
            print("Não foram realizadas movimentações.")
        else:
            for operacao in self.__extrato:
                print(operacao)
            print(f'Saldo atual: R$ {self.__saldo:.2f}')

def main():
    print("======================================")
    print("        SISTEMA BANCÁRIO V1          ")
    print("======================================\n")
    
    conta = ContaBancaria()

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            try:
                conta.depositar(valor)
            except ValueError as e:
                print(e)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

