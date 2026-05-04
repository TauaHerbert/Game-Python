import random as r
import colorama as c
import os
def rodar_jokenpo():
    vet = ['Pedra','Papel','Tesoura']
    player = 0
    computer = 0

    print()
    print("----------------------------- Jokempo -----------------------------")
    print()
    while(True):
        print("Faça a sua jogada!")
        print("( 1 ) Pedra")
        print("( 2 ) Papel")
        print("( 3 ) Tesoura")
        print("( 0 ) Encerrar o jogo e voltar para o menu.")
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
        elif ply == 2:
            if com == "Papel":
                print(f"Player [{c.Style.BRIGHT}{c.Fore.RED}Papel{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{com}{c.Style.RESET_ALL}] Computer")
                print(f"{c.Style.BRIGHT}{c.Fore.MAGENTA}Empate!{c.Style.RESET_ALL}")
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
                print()
            elif player < computer:
                print()
                print(f" ------ {c.Style.BRIGHT}{c.Fore.CYAN}Computer Vencedor!{c.Style.RESET_ALL} ------")
                print(" ------------ Placar ------------")
                print(f" --- Player [{player}] X [{c.Style.BRIGHT}{c.Fore.CYAN}{computer}{c.Style.RESET_ALL}] Computer ---")
                print()
            else:
                print()
                print(f" ------------ {c.Style.BRIGHT}{c.Fore.MAGENTA}EMPATE{c.Style.RESET_ALL} ------------")
                print(" ------------ Placar ------------")
                print(f" --- Player [{c.Style.BRIGHT}{c.Fore.MAGENTA}{player}{c.Style.RESET_ALL}] X [{c.Style.BRIGHT}{c.Fore.MAGENTA}{computer}{c.Style.RESET_ALL}] Computer ---")
                print()

            print("Game encerrado! reotrnando para o menu!")
            break

