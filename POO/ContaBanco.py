from datetime import datetime
import pytz

class ContaCorrente():

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self.cpf = cpf
        self._saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []
        

    def consultar__saldo(self):
        print(f'Seu saldo atual é de: R${self._saldo:.2f} ')
        print()
        pass
    
    def limite_conta(self):
        self.limite = -1000
        return self.limite
    
    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self.transacoes.append(('Depósito' ,valor, self._saldo, ContaCorrente.data_hora()))   
        pass

    def sacar_dinheiro(self, valor):
        if (self._saldo - valor) < self.limite_conta():
            print('Você é pobre, e não tem saldo suficiente para sacar esse valor! ... FAZ O L 👆')
            self.consultar__saldo()
        else:
            self._saldo -=valor
            self.transacoes.append((valor, self._saldo, ContaCorrente.data_hora()))
        pass

    def consultar_historico_transicoes(self):
        print('Histórico de Transações')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        conta_destino._saldo += valor
        conta_destino.transacoes.append((valor, conta_destino._saldo, ContaCorrente.data_hora()))


#programa   
conta_neymar = ContaCorrente("Neymar","382.443.358-31", 5555, 656565)
conta_neymar.consultar__saldo()

#depositar dinheirinho na conta
conta_neymar.depositar_dinheiro(1000)
conta_neymar.consultar__saldo()

#sacando dinheirinho da conta
conta_neymar.sacar_dinheiro(10)
print()
print("Saldo Final:")
conta_neymar.consultar__saldo()


#transferência
conta_luisito = ContaCorrente("luisito", "400.289.220-44", 5555, 656565)#criando conta para receber a transferência
conta_neymar.transferir(10, conta_luisito)

#histórico transferencia
conta_neymar.consultar_historico_transicoes()

#=========================================================================#===================================================================#

from datetime import datetime
import pytz
from random import randint

class CartaoCredito:
     
     @staticmethod
     def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

     def __init__(self, titular, conta_corrente):
        self.numero = randint(100000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_segurança = '{} {} {}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

#Cria uma nova instância da classe ContaCorrente (conta_neymar)
conta_neymar = ContaCorrente("Neymar", "111.222.333-45", 1234, 34602)

#Cria uma nova instância da classe CartaoCredito (cartao_neymar)
cartao_neymar = CartaoCredito("Neymar", conta_neymar)

print(cartao_neymar.numero,
      cartao_neymar.titular,
      cartao_neymar.validade,
      cartao_neymar.cod_segurança,
      cartao_neymar.limite,
)

print(cartao_neymar.__dict__)




