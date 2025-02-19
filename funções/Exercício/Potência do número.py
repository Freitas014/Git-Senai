# Função que solicita ao usuário um número inteiro e retorna esse número
def numero():
    # Solicita ao usuário que digite um número inteiro
    num = int(input("Digite um número inteiro: "))
    return num  # Retorna o número digitado pelo usuário

# Função que solicita a potência e calcula o número elevado a essa potência
def potenciadonum(num):
    # Solicita ao usuário que digite a potência (um número inteiro)
    potencia = int(input("Digite a potência: "))
    resultado = 1  # Inicializa a variável 'resultado' com 1 (identidade da multiplicação)

    # Usando um loop for para calcular a potência
    # O loop repete o número 'potencia' vezes, multiplicando o resultado pelo número 'num' em cada iteração
    for i in range(potencia):
        resultado *= num  # Multiplica o resultado pelo número 'num' a cada iteração

    return resultado, potencia  # Retorna o resultado da potência e a potência solicitada

# Chamando a função numero() para obter o número
n = numero()

# Chamando a função potenciadonum() para calcular a potência do número 'n'
# O resultado da potência e a potência fornecida são armazenados nas variáveis 'resultado' e 'potencia'
resultado, potencia = potenciadonum(n)

print(f"O número {n} elevado à potência {potencia} é: {resultado}")
