from colorama import Fore as f
import os

arena = [[1,2,3], [4,5,6], [7,8,9]]
def carregar_jogo(arena):
    for x in range(0,3):
        for y in range(0,3):
            print(f"    |{arena[x][y]:^1}|",end="")
        print()
    print()
    cont = 0
def verificar_jogada(arena,jogador_X_O):
    X_player1 = f.BLUE + "\033[1mX\033[0m"
    if arena[0][0] == arena[0][1] == arena[0][2] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena,jogador_X_O)
        return True
    elif arena[1][0] == arena[1][1] == arena[1][2] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena, jogador_X_O)
        return True
    elif arena[2][0] == arena[2][1] == arena[2][2] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena, jogador_X_O)
        return True
    elif arena[0][0] == arena[1][0] == arena[2][0] == jogador_X_O:
        print("Jogador 1 Ganhou")
        resltado_jogador(arena,jogador_X_O)
        return True
    elif arena[0][1] == arena[1][1] == arena[2][1] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena, jogador_X_O)
        return True
    elif arena[0][2] == arena[1][2] == arena[2][2] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena, jogador_X_O)
        return True
    elif arena[0][0] == arena[1][1] == arena[2][2] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena, jogador_X_O)
        return True
    elif arena[0][2] == arena[1][1] == arena[2][0] == jogador_X_O:
        if jogador_X_O == X_player1:
            print("Jogador 1 Ganhou")
        else:
            print("Jogador 2 Ganhou")
        resltado_jogador(arena, jogador_X_O)
        return True
def resltado_jogador(arena,jogador_X_O):
    if arena[0][0] == arena[0][1] == arena[0][2] == jogador_X_O:
        arena[1][0] = "'"
        arena[1][1] = "'"
        arena[1][2] = "'"
        arena[2][0] = "'"
        arena[2][1] = "'"
        arena[2][2] = "'"
        carregar_jogo(arena)
    elif arena[1][0] == arena[1][1] == arena[1][2] == jogador_X_O:
        arena[0][0] = "'"
        arena[0][1] = "'"
        arena[0][2] = "'"
        arena[2][0] = "'"
        arena[2][1] = "'"
        arena[2][2] = "'"
        carregar_jogo(arena)
    elif arena[2][0] == arena[2][1] == arena[2][2] == jogador_X_O:
        arena[0][0] = "'"
        arena[0][1] = "'"
        arena[0][2] = "'"
        arena[1][0] = "'"
        arena[1][1] = "'"
        arena[1][2] = "'"
        carregar_jogo(arena)
    elif arena[0][0] == arena[1][0] == arena[2][0] == jogador_X_O:
        arena[0][1] = "'"
        arena[0][2] = "'"
        arena[1][1] = "'"
        arena[1][2] = "'"
        arena[2][1] = "'"
        arena[2][2] = "'"
        carregar_jogo(arena)
    elif arena[0][1] == arena[1][1] == arena[2][1] == jogador_X_O:
        arena[0][0] = "'"
        arena[0][2] = "'"
        arena[1][0] = "'"
        arena[1][2] = "'"
        arena[2][0] = "'"
        arena[2][2] = "'"
        carregar_jogo(arena)
    elif arena[0][2] == arena[1][2] == arena[2][2] == jogador_X_O:
        arena[0][0] = "'"
        arena[0][1] = "'"
        arena[1][0] = "'"
        arena[1][1] = "'"
        arena[2][0] = "'"
        arena[2][1] = "'"
        carregar_jogo(arena)
    elif arena[0][0] == arena[1][1] == arena[2][2] == jogador_X_O:
        arena[0][1] = "'"
        arena[0][2] = "'"
        arena[1][0] = "'"
        arena[1][2] = "'"
        arena[2][0] = "'"
        arena[2][1] = "'"
        carregar_jogo(arena)
    elif arena[0][2] == arena[1][1] == arena[2][0] == jogador_X_O:
        arena[0][0] = "'"
        arena[0][1] = "'"
        arena[1][0] = "'"
        arena[1][2] = "'"
        arena[2][1] = "'"
        arena[2][2] = "'"
        carregar_jogo(arena)

X_player1 = f.BLUE+"\033[1mX\033[0m"
O_player2 = f.RED+"\033[1mO\033[0m"
def partida(arena,X_player1,O_player2):
    cont = 0
    for x in range(9):
        cont+=1
        jogador1 = input("Jogador 1 [X], Qual posição: ")
        while jogador1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Valor invalido")
            jogador1 = input("Jogador 1 [X], Qual posição: ")

        while True:
            if jogador1 == "1":
                if arena[0][0] == X_player1 or arena[0][0] == O_player2:
                    print("Campo ja ocpado, oscolha outro!")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[0][0] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "2":
                if arena[0][1] == X_player1 or arena[0][1] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[0][1] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "3":
                if arena[0][2] == X_player1 or arena[0][2] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[0][2] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "4":
                if arena[1][0] == X_player1 or arena[1][0] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[1][0] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "5":
                if arena[1][1] == X_player1 or arena[1][1] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[1][1] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "6":
                if arena[1][2] == X_player1 or arena[1][2] == O_player2:
                    print("Campo ja ocupado, escoha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[1][2] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "7":
                if arena[2][0] == X_player1 or arena[2][0] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[2][0] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "8":
                if arena[2][1] == X_player1 or arena[2][1] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[2][1] = X_player1
                    carregar_jogo(arena)
                    break
            elif jogador1 == "9":
                if arena[2][2] == X_player1 or arena[2][2] == O_player2:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador1 = input("Jogador 1 [X], Qual posição: ")
                else:
                    arena[2][2] = X_player1
                    carregar_jogo(arena)
                    break

        if verificar_jogada(arena,X_player1):
            break

        if cont == 5:
            print("Empate no game, o jogo deu VELHA!")
            break

        jogador2 = input("Jogador 2 [0], Qual posição: ")
        while jogador1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Valor invalido")
            jogador2 = input("Jogador 2 [0], Qual posição: ")

        while True:
            if jogador2 == "1":
                if arena[0][0] == O_player2 or arena[0][0] == X_player1:
                    print("Campo ja ocpado, oscolha outro!")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[0][0] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "2":
                if arena[0][1] == O_player2 or arena[0][1] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[0][1] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "3":
                if arena[0][2] == O_player2 or arena[0][2] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[0][2] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "4":
                if arena[1][0] == O_player2 or arena[1][0] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[1][0] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "5":
                if arena[1][1] == O_player2 or arena[1][1] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[1][1] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "6":
                if arena[1][2] == O_player2 or arena[1][2] == X_player1:
                    print("Campo ja ocupado, escoha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[1][2] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "7":
                if arena[2][0] == O_player2 or arena[2][0] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[2][0] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "8":
                if arena[2][1] == O_player2 or arena[2][1] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[2][1] = O_player2
                    carregar_jogo(arena)
                    break
            elif jogador2 == "9":
                if arena[2][2] == O_player2 or arena[2][2] == X_player1:
                    print("Campo ja ocupado, escolha outro")
                    carregar_jogo(arena)
                    jogador2 = input("Jogador 2 [0], Qual posição: ")
                else:
                    arena[2][2] = O_player2
                    carregar_jogo(arena)
                    break
            
        if verificar_jogada(arena,O_player2):
            break
            
def rodar_jogo_da_velha():
    print()
    print("               ---------------------------------- Jogo da Velha ----------------------------------")
    print()
    while (True):
        op = int(input("Pressione ( 1 ) para iniciando a partida ou ( 0 ) para encerrar aplicação. OBS: Jogo da velha so tem no modo Multiplayer"))
        match op:
            case 1:
                os.system('cls')
                print("....Iniciando partida....")
                print()
                carregar_jogo(arena)
                partida(arena,X_player1,O_player2)
            case 0:
                os.system('cls')
                print("Encerrando aplicação (Jogo da Velha)")
                break
            case _:
                print("Opção invalida! Digite novamente.")


