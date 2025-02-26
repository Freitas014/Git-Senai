from ContaBanco import ContaCorrente, CartaoCredito

#PROGRAMA

#criar uma nova instância da classe ContaCorrente (conta_neymar)
conta_neymar = ContaCorrente("Neymar", "111.222.333-45", 1234, 34602)

#criar uma nova instância da classe ContaCorrente (conta_neymar)
cartao_neymar = CartaoCredito("Neymar", conta_neymar)
