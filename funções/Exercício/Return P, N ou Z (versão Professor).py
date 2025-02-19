def numero(num):
    if numero < 0:
        return 'N'
    elif numero > 0:
        return 'P'
    else:
        return 'Z'

num = int(input("Digite um número: "))
resultado = numero(num)
print(f"O resultado é: {resultado}")