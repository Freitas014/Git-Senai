# Solicita ao usuário que insira um número inteiro positivo e o converte para um inteiro
n = int(input("Digite um número inteiro positivo: "))

# Exibe uma mensagem pedindo o primeiro número da sequência
print("Informe o número: ")

# Lê o primeiro número da sequência
anterior = int(input())

# Inicializa o contador i com 1, já que o primeiro número foi lido
i = 1

# A variável "ordenado" é um indicador de que a sequência está ordenada
# Inicialmente, assume-se que a sequência está ordenada
ordenado = True

# Inicia o laço while, que vai continuar até que todos os números sejam lidos (i < n) ou até encontrar uma sequência desordenada (ordenado == False)
while (i < n) and (ordenado):
    # Solicita ao usuário o próximo número da sequência
    print("Informe o número: ")
    
    # Lê o número atual
    atual = int(input())
    
    # Incrementa o contador i, pois um número foi lido
    i = 1
    
    # Verifica se o número atual é menor que o número anterior
    # Caso seja, significa que a sequência não está ordenada
    if (atual < anterior):
        # Define a variável "ordenado" como False, indicando que a sequência não está ordenada
        ordenado = False
    
    # Atualiza a variável "anterior" com o número atual para a próxima iteração
    anterior = atual

# Após sair do laço, verifica se a sequência estava ordenada ou não
if (ordenado):
    # Se "ordenado" for True, imprime que a sequência está ordenada
    print("Sequência ordenada.")
else:
    # Se "ordenado" for False, imprime que a sequência não está ordenada
    print("Sequência não ordenada.5")
