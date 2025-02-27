class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []


    def verificar_caixa(self):
        if self.caixa <1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor de Caixa está ok. Caixa atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa>valor:
            self.emprestimos.append((valor, cpf, juros))
            print('Empréstimo efetuado')
        else:
             print('Empréstimo não é possível. Dinheiro não Disponível em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


#checando classes criando "agencia1"
agencia1 = Agencia(22223333, 2000000, 4568)

agencia1.caixa= 100000

print(agencia1.__dict__)

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(10, 11122233344, 0.1)


#adicionar cliente
agencia1.adicionar_cliente('Neymar', 11122233344, 10000)
print(agencia1.clientes)


class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -=valor
        self.caixa_paypal -= valor 

    def sacar(self, valor):
        self.caixa_paypal -= valor
        self.caixa +=valor
    pass


from random import randint

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 1000000
    pass


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 1000000
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não possui o patrimônio mínimo necessário!')
    pass


#Agencia Virtual
agencia_virtual = AgenciaVirtual("www.agenciavirtual.com.br", 22224444, 152000000000, 1000)

print(agencia_virtual.__dict__)

agencia_virtual.verificar_caixa()
print(agencia_virtual.__dict__)

agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

agencia_virtual.adicionar_cliente('Neymar', 11111111111, 1000000)

#Agencia Comum
agencia_comum = AgenciaComum
agencia_comum = AgenciaComum(33334444, 222000000000)
agencia_comum.verificar_caixa()


print(agencia_comum.caixa)

print(agencia_comum)

agencia_comum.adicionar_cliente('Neymar', 11111111111, 1000000)
#Agencia Premium
agencia_premium = AgenciaPremium
agencia_premium  = AgenciaPremium(33333333, 3000000000000)

agencia_premium.adicionar_cliente('Neymar', 11111111111, 1000000)
print('cliente agencia_premium: ', agencia_premium.clientes)
