class Onibus:
    def __init__(self, num_poltronas=50):
        self.poltronas = [False] * num_poltronas  # Vetor que indica se a poltrona está ocupada ou não
        self.vendas = 0

    def vender_passagem(self, numero_poltrona):
        if 1 <= numero_poltrona <= len(self.poltronas):
            index = numero_poltrona - 1  # Ajusta o índice para começar em 0
            if not self.poltronas[index]:
                self.poltronas[index] = True  # Marca a poltrona como ocupada
                self.vendas += 1
                print(f"✅ Passagem vendida para a poltrona {numero_poltrona}.")
            else:
                print(f"❌ Erro: A poltrona {numero_poltrona} já está ocupada.")
        else:
            print("❌ Erro: Número da poltrona inválido.")

    def relatorio_vendas(self):
        print(f"📊 Total de passagens vendidas: {self.vendas}.")
        print("Situação das poltronas:")
        for i, ocupada in enumerate(self.poltronas):
            status = "Ocupada" if ocupada else "Livre"
            print(f"🪑 Poltrona {i + 1}: {status}")

    def mostrar_layout(self):
        print("          ONIBUS")
        print("   |------------------------|")
        for i in range(0, len(self.poltronas), 5):  # 5 poltronas por linha
            linha = "   | " + " | ".join(str(i + j + 1) for j in range(5) if i + j < len(self.poltronas)) + " |"
            print(linha)
            print("   |------------------------|")

# Exemplo de uso
onibus = Onibus()

# Mostrar layout do ônibus
onibus.mostrar_layout()

while True:
    try:
        poltrona_desejada = int(input("Escolha o número da poltrona que deseja comprar (1 a 50) ou 0 para sair: "))
        if poltrona_desejada == 0:
            break
        onibus.vender_passagem(poltrona_desejada)
    except ValueError:
        print("❌ Erro: Por favor, insira um número válido.")

# Relatório de vendas
onibus.relatorio_vendas()
