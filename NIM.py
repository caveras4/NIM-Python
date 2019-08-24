def computador_escolhe_jogada(n, m):
    valor = m
    while (n - m) % (valor + 1) != 0:
        m = m - 1

    comp = m

    if comp == 1:
        print("\nO computador tirou uma peça.")
    else:
        print("\nO computador tirou", comp, "peças.")
        
    return comp        

def usuario_escolhe_jogada(n, m):
    jog = int(input("\nQuantas peças você vai tirar? "))
        
    if jog > m or jog <= 0:
        print("Oops! Jogada inválida! Tente de novo")
        return usuario_escolhe_jogada(n, m)
    else:
        if jog == 1:
            print("Você tirou uma peça.")
        else:
            print("Você tirou", jog, "peças.")
            
    return jog            

def partida():
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n < m:
        print("O limite de peças por jogada não pode ser maior do que a quantidade de peças")
        return partida()

    while n > 0:
        if n % (m + 1) == 0:
            print("\nVocê começa!")
            while n > 0:
                jog = usuario_escolhe_jogada(n, m)
                n = n - jog
                if n == 0:
                    print("Fim do jogo! você ganhou!")
                else:
                    print("Agora restam", n, "peças no tabuleiro.") 
                    comp = computador_escolhe_jogada(n, m)
                    n = n - comp
                    if n == 0:
                        print("Fim do jogo! O computador ganhou!")
                    else:    
                        print("Agora restam", n, "peças no tabuleiro.")            
        
        else:
            print("\nComputador começa!")
            while n > 0:
                comp = computador_escolhe_jogada(n, m)
                n = n - comp
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                else:
                    print("Agora restam", n, "peças no tabuleiro.")
                    jog = usuario_escolhe_jogada(n, m)
                    n = n - jog
                    if n == 0:
                       print("Fim do jogo! você ganhou!")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")

def campeonato():
    cont = 1
    vit_j = 0
    vit_c = 0
    
    while cont < 4:
        print("\n**** Rodada", cont, "****")
        champs = partida()
        if champs == ("Fim do jogo! você ganhou!"):
            vit_j = vit_j + 1
        else:
            vit_c = vit_c + 1
            
        cont = cont + 1

    print("**** Final do campeonato! ****")
    print("\nPlacar: Você", vit_j, "X", vit_c, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")

x = int(input("\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato \n"))

if x == 1:
    partida()
if x == 2:
    campeonato()
else:
    print("É sério? (-_-) desisto de vc")


        
