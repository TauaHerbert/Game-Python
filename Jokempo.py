import random as r
import colorama as c
import os
def rodar_jokenpo():
    vet = ['Pedra','Papel','Tesoura']
    player = 0
    computer = 0
    empate = 0

    os.system('cls')

    while(True):
        print()
        print("----------------------------- Jokempo -----------------------------")
        print()
        op = int(input("( 1 ) Partidas infinitas\n"
                       "( 2 ) O melhor de 3\n"
                       "( 0 ) Voltar para o menu Principal\n"))
        match op:
            case 1:
                os.system('cls')
                jokenpo_infinito(vet, player,computer, empate)
            case 2:
                os.system('cls')
                jokenpo_melhor_3(vet, player, computer, empate)
            case 0:
                print("Encerrando aplicação e retornando para o menu.")
                os.system('cls')
                break
            case _:
                print("Opção invalida! Escolha novamente")

def jokenpo_melhor_3(vet, player, computer, empate):
    for x in range(0, 3):
        print("------------------ O melhor de 3 ------------------")
        print(f"------------------ Rodada {x+1} ------------------")
        print("Faça a sua jogada!")
        print("( 1 ) Pedra")
        print("( 2 ) Papel")
        print("( 3 ) Tesoura")
        print("( 0 ) Encerrar a partida")
        ply = int(input())
        com = r.choice(vet)
        if ply > 3 or ply < 0:
            print("Opaão Invalida!")
        elif ply == 1:
            if com == "Tesoura":
                print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Pedra{c.Style.RESET_ALL}] X [{com}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.RED}Player vencedor!{c.Style.RESET_ALL}")
                player+=1
            elif com == "Papel":
                print(f"Player [Pedra] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.CYAN}Computer vencedor!{c.Style.RESET_ALL}")
                computer+=1
            else:
                print(
                    f"Player [{c.Style.BRIGHT}{c.Fore.RED}Pedra{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
                empate+=1
        elif ply == 2:
            if com == "Papel":
                print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Papel{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
                empate+=1
            elif com == "Tesoura":
                print(f"Player [Papel] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.CYAN}Computer vencedor!{c.Style.RESET_ALL}")
                computer+=1
            else:
                print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Papel{c.Style.RESET_ALL}] X [{com}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.RED}Player vencedor!{c.Style.RESET_ALL}")
                player+=1
        elif ply == 3:
            if com == "Pedra":
                print(f"Player [Tesoura] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.CYAN}Computer vencedor!{c.Style.RESET_ALL}")
                computer+=1
            elif com == "Tesoura":
                print(
                    f"Player [{c.Style.BRIGHT}{c.Fore.RED}Tesoura{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
                empate+=1
            else:
                print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Tesoura{c.Style.RESET_ALL}] X [{com}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.RED}Player vencedor!{c.Style.RESET_ALL}")
                player+=1

    if player > computer:
        print()
        print(f" ------- {c.Style.BRIGHT}{c.Fore.RED}Player Vencedor!{c.Style.RESET_ALL} -------")
        print(" ------------ Placar ------------")
        print(f" --- Player [{c.Style.BRIGHT}{c.Fore.RED}{player}{c.Style.RESET_ALL}] X [{computer}] Computer ---")
        print(f" --- Total de Partidas empatadas: {c.Style.BRIGHT}{c.Fore.MAGENTA}{empate}{c.Style.RESET_ALL}")
        print()
        print("Game encerrado! reotrnando para o menu!")
    elif player < computer:
        print()
        print(f" ------ {c.Style.BRIGHT}{c.Fore.CYAN}Computer Vencedor!{c.Style.RESET_ALL} ------")
        print(" ------------ Placar ------------")
        print(f" --- Player [{player}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{computer}{c.Style.RESET_ALL}] Computer ---")
        print(f" --- Total de Partidas empatadas: {c.Style.BRIGHT}{c.Fore.MAGENTA}{empate}{c.Style.RESET_ALL}")
        print()
        print("Game encerrado! reotrnando para o menu!")
    else:
        print()
        print(f" ------------ {c.Style.BRIGHT}{c.Fore.MAGENTA}EMPATE{c.Style.RESET_ALL} ------------")
        print(" ------------ Placar ------------")
        print(f" --- Player [{c.Style.BRIGHT}{c.Fore.MAGENTA}{player}{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.MAGENTA}{computer}{c.Style.RESET_ALL}] Computer ---")
        print()
        print("Game encerrado! reotrnando para o menu!")

def jokenpo_infinito(vet, player, computer, empate):
        while(True):
            print("Faça a sua jogada!")
            print("( 1 ) Pedra")
            print("( 2 ) Papel")
            print("( 3 ) Tesoura")
            print("( 0 ) Encerrar a partida")
            ply = int(input())
            com = r.choice(vet)
            if ply > 3 or ply < 0:
                print("Opaão Invalida!")
            elif ply == 1:
                if com == "Tesoura":
                    print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Pedra{c.Style.RESET_ALL}] X [{com}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.RED}Player vencedor!{c.Style.RESET_ALL}")
                    player+=1
                elif com == "Papel":
                    print(f"Player [Pedra] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.CYAN}Computer vencedor!{c.Style.RESET_ALL}")
                    computer+=1
                else:
                    print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Pedra{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
                    empate+=1
            elif ply == 2:
                if com == "Papel":
                    print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Papel{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
                    empate+=1
                elif com == "Tesoura":
                    print(f"Player [Papel] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.CYAN}Computer vencedor!{c.Style.RESET_ALL}")
                    computer+=1
                else:
                    print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Papel{c.Style.RESET_ALL}] X [{com}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.RED}Player vencedor!{c.Style.RESET_ALL}")
                    player+=1
            elif ply == 3:
                if com == "Pedra":
                    print(f"Player [Tesoura] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.CYAN}Computer vencedor!{c.Style.RESET_ALL}")
                    computer+=1
                elif com == "Tesoura":
                    print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Tesoura{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
                    empate+=1
                else:
                    print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Tesoura{c.Style.RESET_ALL}] X [{com}] Computer")
                    print(f"{c.Style.BRIGHT}{c.Fore.RED}Player vencedor!{c.Style.RESET_ALL}")
                    player+=1
            else:
                os.system('cls')
                if player > computer:
                    print()
                    print(f" ------- {c.Style.BRIGHT}{c.Fore.RED}Player Vencedor!{c.Style.RESET_ALL} -------")
                    print(" ------------ Placar ------------")
                    print(f" --- Player [{c.Style.BRIGHT}{c.Fore.RED}{player}{c.Style.RESET_ALL}] X [{computer}] Computer ---")
                    print(f" --- Total de Partidas empatadas: {c.Style.BRIGHT}{c.Fore.MAGENTA}{empate}{c.Style.RESET_ALL}")
                    print()
                elif player < computer:
                    print()
                    print(f" ------ {c.Style.BRIGHT}{c.Fore.CYAN}Computer Vencedor!{c.Style.RESET_ALL} ------")
                    print(" ------------ Placar ------------")
                    print(f" --- Player [{player}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{computer}{c.Style.RESET_ALL}] Computer ---")
                    print(f" --- Total de Partidas empatadas: {c.Style.BRIGHT}{c.Fore.MAGENTA}{empate}{c.Style.RESET_ALL}")
                    print()
                else:
                    print()
                    print(f" ------------ {c.Style.BRIGHT}{c.Fore.MAGENTA}EMPATE{c.Style.RESET_ALL} ------------")
                    print(" ------------ Placar ------------")
                    print(f" --- Player [{c.Style.BRIGHT}{c.Fore.MAGENTA}{player}{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.MAGENTA}{computer}{c.Style.RESET_ALL}] Computer ---")
                    print()

                print("Game encerrado! reotrnando para o menu!")
                break

