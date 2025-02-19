def numero(num):
    return int(num)  # Retorna o número como inteiro

def contar_digitos(num):
    return len(str(abs(num)))  # Converte para string e conta os caracteres, ignorando o sinal negativo

n = int(input("Digite um número: "))  # Solicita um número ao usuário
quantidade_digitos = contar_digitos(n)  # Conta os dígitos do número

print(f"Número digitado: {numero(n)}")
print(f"Quantidade de dígitos: {quantidade_digitos}")
