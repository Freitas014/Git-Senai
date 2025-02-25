def exibir_tabuleiro(tabuleiro):
    """Função para exibir o tabuleiro do jogo da velha."""
    for linha in tabuleiro:
        print(" | ".join(linha))  # Exibe os elementos da linha separados por '|'
        print("-" * 9)  # Linha divisória entre as linhas do tabuleiro


def verificar_vitoria(tabuleiro, jogador):
    """Função para verificar se o jogador atual venceu o jogo."""
    # Verificar linhas e colunas
    for i in range(3):
        # Verifica se todas as posições da linha são do mesmo jogador
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):  # Verifica colunas
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False  # Retorna False se não houver vitória


def jogo_da_velha():
    """Função principal que gerencia o jogo da velha."""
    # Criar tabuleiro 3x3 preenchido com espaços em branco
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    
    # Lista com os símbolos dos jogadores
    jogadores = ["X", "O"]
    
    # Variável para alternar turnos
    turno = 0

    # O jogo pode ter no máximo 9 jogadas
    for _ in range(9):
        exibir_tabuleiro(tabuleiro)  # Exibe o tabuleiro atualizado
        jogador_atual = jogadores[turno % 2]  # Define o jogador da vez
        print(f"Vez do jogador {jogador_atual}")

        while True:
            try:
                # Solicita a entrada do jogador e converte para inteiros
                linha, coluna = map(int, input("Digite linha e coluna (0-2, separados por espaço): ").split())

                # Verifica se a posição está livre
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual  # Marca a jogada no tabuleiro
                    break  # Sai do loop se a jogada for válida
                else:
                    print("Posição já ocupada! Tente novamente.")  # Erro caso a posição esteja ocupada
            except (ValueError, IndexError):
                print("Entrada inválida! Digite dois números entre 0 e 2.")  # Erro caso a entrada seja inválida

        # Verifica se o jogador atual venceu
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)  # Mostra o tabuleiro final
            print(f"Parabéns! O jogador {jogador_atual} venceu! 🏆")  # Mensagem de vitória
            return  # Encerra o jogo

        turno += 1  # Passa a vez para o próximo jogador

    # Se o loop terminar sem vitória, significa que houve empate
    exibir_tabuleiro(tabuleiro)
    print("Empate! Deu velha! 🤝")


# Executar o jogo
jogo_da_velha()
