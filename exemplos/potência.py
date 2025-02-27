# Função que recebe um número inteiro e o retorna
def numero():
    num = int(input("Digite um número inteiro: "))
    return num

# Função que recebe a potência e calcula a potência do número
def potenciadonum(num):
    potencia = int(input("Digite a potência: "))
    resultado = 1  # Inicializa o resultado com 1 (identidade da multiplicação)

    # Usando um loop for para multiplicar o número por ele mesmo 'potencia' vezes
    for i in range(potencia):
        resultado *= num
    
    return resultado

# Chamando as funções
n = numero()  # Chama a função para obter o número
resultado = potenciadonum(n)  # Chama a função para calcular a potência

# Exibindo o resultado
print(f"O número {n} elevado à potência fornecida é: {resultado}")
