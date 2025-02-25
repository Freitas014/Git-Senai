class ContaCorrente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f'Seu saldo atual é de: R${self.saldo:.2f} ')
        pass
    
    def depositar_dinheiro(self, valor):
        self.saldo += valor
        pass

    def sacar_dinehiro(self, valor):
        self.saldo -= valor
        pass

#programa   
conta_neymar = ContaCorrente("Neymar","382.443.358-31")
conta_neymar.consultar_saldo()

#depositar dinheirinho na conta
conta_neymar.depositar_dinheiro(1000)
conta_neymar.consultar_saldo()
conta_neymar = ContaCorrente()
print('Saldo da conta é: ', conta_neymar.saldo)
print(conta_neymar.cpf)

