import random

jogadas = ['pedra','papel','tesoura']
vitorias = 0

while True:
    try:
        if vitorias>0:
            print(f'Você tem {vitorias} vitórias!')

        escolha = int(input('Vamos Jogar *Jokenpô*?\nEscolha Pedra, Papel ou Tesoura [0,1,2] Ou digite [9] Para sair.\n'))

        if escolha == 9:
            
            break

        elif (escolha<3 and escolha>-1):
            jogador = jogadas[escolha]
                  
            computador = random.choice(jogadas)
            
            print(f'Você escolheu {jogador}.')
            print(f'Computador escolheu {computador}.\n')

            if (jogador == computador):
                print('Empate!')

            elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):

                print('Você venceu!')
                vitorias+=1

            else:
                print('Você perdeu!')            
        else:
            
            print('Opção Inválida!')
    except:
        
        print('Opção Inválida! Digite um número válido.')