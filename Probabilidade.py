import random as r
import os

def partida():
    while(True):
        num_p = int(input("(Numeros validos de 0 a 100 ) Informe o seu numero: "))
        if num_p > 100 or num_p < 0:
            print("O numero informado não é valido para o desafio!")
        else:
            break
    valor_final = r.randint(0, 100)
    num_c = r.randint(0, 100)
    print(f"Numero do Computer: {num_c}")
    print()

    if num_p > valor_final:
        res_p = num_p - valor_final
    else:
        res_p = valor_final - num_p

    if num_c > valor_final:
        res_c = num_c - valor_final
    else:
        res_c = valor_final - num_c

    if res_p < res_c:
        print(" ------ Player vencedor! ------ ")
        print(f"Numero do player = {num_p}")
        print(f"Numero do Computer = {num_c}")
        print(f"Resultado do numero escolhido = {valor_final}")
    else:
        print(" ------ Computer vencedor! ------ ")
        print(f"Numero do player = {num_p}")
        print(f"Numero do Computer = {num_c}")
        print(f"Resultado do numero escolhido = {valor_final}")


def CarregarJogo():
    print(" ----------------- Jogo da Probabilidade -----------------  ")
    print()

    while (True):
        op = int(input("( 1 ) Partida contra Computer\n"
                       "( 2 ) Partida Multiplayer\n"
                       "( 0 ) Voltar para o menu"))
        match op:
            case 1:
                os.system('cls')
                partida()
            case 2:
                print()
            case 0:
                os.system('cls')
                print("Retornando para o menu")
                break
            case _:
                print("Opção invalida")
