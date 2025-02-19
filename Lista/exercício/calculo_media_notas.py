# Mostra as n notas
notas = [] # Cria uma lista vazia para armazenar as notas
n = int(input("Digite o número de notas: "))# Solicita ao usuário que digite o número de notas que deseja inserir
for i in range(n): # Laço que vai de 0 até n-1 para permitir que o usuário insira as notas
    dado = float(input(f"Digite a nota {i + 1}: ")) # Solicita a entrada da nota e converte para float (número decimal)
    notas.append(dado) # Adiciona a nota digitada na lista "notas"
print(notas)# Exibe a lista de notas inseridas

#calcula a média

soma = 0 # Calcula a soma de todas as notas 
for i in range(len(notas)):

    soma = soma + notas[i] # Adiciona cada nota à variável soma
media = soma / len(notas) # Calcula a média dividindo a soma total das notas pelo número de notas

print(f"Notas: {notas}") # Exibe a lista de notas
print(format(f"Média: {media}")) #Exibe a média