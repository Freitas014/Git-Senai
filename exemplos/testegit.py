class Conta:
    numero = "00000-0"
    saldo = 0.0

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if(self.saldo > 0):
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")

if __name__ == '_main_':
    conta = Conta()
    conta.saldo = 20
    conta.numero = "13131-2"
    print(conta.saldo)
    print(conta.numero)