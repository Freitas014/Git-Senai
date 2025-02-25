import random  # Importa a biblioteca para gerar números aleatórios

mat = []  # Lista que representará a matriz
contador = 0  # Contador de posições não nulas

for i in range(10):  # Loop para percorrer as linhas
    l = []  # Cria uma lista vazia para representar a linha
    for j in range(10):  # Loop para percorrer as colunas
        valor = random.randint(0, 9)  # Gera um número aleatório entre 0 e 9
        l.append(valor)  # Adiciona o número na linha
        if valor != 0:  # Se o número for diferente de zero, incrementa o contador
            contador += 1
    mat.append(l)  # Adiciona a linha na matriz

# Exibe a matriz
for linha in mat:
    print(linha)

# Exibe a contagem de números diferentes de zero
print(f"Número de posições não nulas: {contador}")                                                                