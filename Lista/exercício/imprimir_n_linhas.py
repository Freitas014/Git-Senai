num = int(input("Digite um número para imprimir: ")) # Entrada

for i in range(1, num + 1): # Loop de 1 até 'num'
    for n in range(1, i + 1):  # Loop interno para imprimir os números da linha atual
        print(n, end = " ") # Imprime na mesma linha com espaço
    print()  # Pula para a próxima linha