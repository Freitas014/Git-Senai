def numero(num):
    if num > 0:
        return "p"
    
    if num < 0:
        return "N"
    
    if num == 0:
        return "Z"
    
num = int(input("Digite um número: "))
print(numero(num))