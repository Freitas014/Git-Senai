def numero(num):
    return str(num)[::-1]   # Converte o número para uma string, inverte a string e retorna a string invertida.

n = int(input("Digite um número: ")) # Número digitado armazenando o valor na variável 'n'.
print(f"Reverso --> {numero(n)}")
# Chama a função numero(n) para inverter o número e imprime o resultado.
# A função f-string é usada para formatar a saída, mostrando a palavra "Reverso" seguida do número invertido.
