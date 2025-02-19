palíndromo = str(input("Digite um texto: ")).strip()
inversa = palíndromo.split()
junto = "".join(inversa)
frase = junto[::-1]

if junto == frase:
    print(f"{palíndromo} é um palíndromo!")

else:
    print(f"{palíndromo} Não é um Palíndromo\n")