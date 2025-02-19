seq_adj = 0
valor_anterior = None
while True:
    try:
        n = int(input("Informe uma quantidade de números para ler: "))

        while (n>=1):
            valor_novo = int(input(f'Insira um valor: '))
            if (valor_novo == valor_anterior):
                seq_adj = 1
            valor_anterior = valor_novo
            n-=1 

        if (seq_adj == 1):
            print(f"Adjacente!")
            break
        else: 
            print(f"Não adjacente.")
            break

    except:
        print('Opção Inválida!')