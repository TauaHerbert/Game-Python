from _Game_ import Jokempo
import os

while(True):
    print("Escolha o Game que deseja jogar ou ( 0 ) para encerrar a aplicação: ")
    print("( 1 ) Jogo da velha")
    print("( 2 ) Jockempo")
    print("( 3 ) Jogo da Probabilidade (Sorte) ")
    op = int(input())

    match op:
        case 1:
            os.system('cls')
            print("Game 1")
        case 2:
            os.system('cls')
            Jokempo.rodar_jokenpo()
        case 3:
            os.system('cls')
            print("Game 3")
        case 4:
            os.system('cls')
            print("Game 4")
        case 0:
            print("Aplicação encerrada!")
            break
        case _:
            os.system('cls')
            print("Alternativa incorreta!")

