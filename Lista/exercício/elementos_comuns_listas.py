def main():  
    # Lendo as duas listas de 5 números digitados pelo usuário  
    lista1 = [int(input(f"Digite o {i+1}º número da primeira lista: ")) for i in range(5)]  # 📥 Cria a primeira lista com 5 números inseridos  
    lista2 = [int(input(f"Digite o {i+1}º número da segunda lista: ")) for i in range(5)]   # 📥 Cria a segunda lista com 5 números inseridos  

    # Encontrando elementos em comum entre as listas  
    comuns = list(set(lista1) & set(lista2))  # 🔎 Converte as listas em conjuntos e obtém os elementos que aparecem em ambas  

    # Exibindo o resultado  
    if comuns:  # ✅ Se houver números repetidos nas duas listas  
        print(f"Os 5 números de cada lista são: \n1° Lista: {lista1}  \n2° Lista: {lista2}")  # 📤 Exibe as listas digitadas  
        print()  
        print(f"Os elementos em comum são: {comuns}😁👍")  # 📤 Mostra os números que aparecem nas duas listas  
    else:  # ❌ Caso não haja elementos repetidos  
        print()  
        print("Não há elementos em comum entre as listas.")  # 📤 Exibe uma mensagem informando que não há números em comum  

# Garante que o código só execute se o script for rodado diretamente  
if __name__ == "__main__":  
    main()  # 🚀 Chama a função principal para executar o programa  
