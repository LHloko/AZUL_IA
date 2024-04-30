"""
Created on Mon Apr  1 18:30:45 2024

@author: lbalieiro@lince.lab
"""

import Fabrica
import Jogador
import Estados

#Start class ------------------------------------------------------------------
def main():
    fab = Fabrica.Fabrica()
    luiz = Jogador.Jogador("Luiz")
    vik = Jogador.Jogador("Viktor")
    # jean = Jogador.Jogador("Jean")

    players = [luiz, vik]
    dados = [fab, fab.pocket, players]

    '''
    #tentando preencher uma linha inteira
    ceramicas = [[0],[4],[3],[2]]
    for c in ceramicas:
        luiz.colocar_no_tabuleiro(c)
        luiz.pontuar()

    #zerando algumas fabricas
    fab.factory_board[0] = []
    fab.factory_board[1] = []
    fab.factory_board[2] = []
    fab.factory_board[3] = []
    fab.factory_board[4] = [1,2,2,2]
    '''

    estado = Estados.Estados(dados)

    while not estado.is_game_over():
        #start do game
        while not estado.fim_de_turno():
            for p in players:
                if fab.is_board_empty() and fab.is_floor_empty():#caso o jogo termine no meio de um dos jogadores
                    break
                print("-----------------------------------------------------------------------------------------------------------------------------------*")

                print(fab)
                print(f"[ JOGADOR {p.get_name()} EH SUA VEZ ]")
                print(p)
                p.playar(fab)
                print(p)
                
                print("-----------------------------------------------------------------------------------------------------------------------------------*")
                if estado.is_last_round_to_end():
                    print("-----------------------------------------------------------------------------------------------------------------------------------*")
                    print(" *** ULTIMA RODADA ANTES DO FIM DO JOGO *** ")
                    print('                 :D ')
                    print("-----------------------------------------------------------------------------------------------------------------------------------*")

        #Colocar o player com o -1 no inicio da lista de jogadores
        estado.first_player()
        print(players[0].name, players[1].name)




        #final do turno
        print("-----------------------------------------------------------------------------------------------------------------------------------*")
        print("       Fim Da Rodada")
        print("-----------------------------------------------------------------------------------------------------------------------------------*")
        estado.game_player_status()

        print("-----------------------------------------------------------------------------------------------------------------------------------*")
        print("       NOVA Rodada")
        print("-----------------------------------------------------------------------------------------------------------------------------------*")
        estado.iniciar_turno()

    #Concluindo o JOGO
    estado.fim_de_jogo()

#End class --------------------------------------------------------------------


if __name__ == "__main__":
    main()





















#Start class ------------------------------------------------------------------
def jogando_v1():

    fab = Fabrica.Fabrica()
    luiz = Jogador.Jogador("Luiz")
    vik = Jogador.Jogador("Viktor")

    dados = [fab, 0, [luiz, vik]]

    estados = Estados.Estados(dados)

    while not estados.fim_de_turno():
        for i in dados[2]:
            print(fab)
            print("************** Player", i.get_name(),"**************\n")
            i.playar(fab)
            print(i.board)


    print("************** Mamona 01 gameplay **************\n")
    print(luiz.board)

    print("************** Mamona 02 gameplay **************\n")
    print(vik.board)

#End class --------------------------------------------------------------------



#Start class ------------------------------------------------------------------
def jogando_v2():



    ceramicas = [[0],[4],[3],[2],[1]]

    player = Jogador.Jogador('luiz')
    print(player)


    #tentando preencher uma linha inteira
    for c in ceramicas:
        player.colocar_no_tabuleiro(c)
        print(player)
        player.pontuar()
        print(player)


#End class --------------------------------------------------------------------


















#Start class ------------------------------------------------------------------
def jogando_com_fabricas():
    #Inicializar a fabrica
    #Escolher uma fabrica ou o chao
    #Escolher um tipo de ceramica
    #Reiniciar a fabrica e olhar o saco
    
    fb = Fabrica.Fabrica()
    tiles = []
    while True:
        #EXIBINDO AS CERAMICAS PEGAS
        print("Ceramicas pegas +=> ", tiles)
    
        #EXIBINDO A MESA DE JOGO
        print(fb)
    
        #ESCOLHENDO ENTRE FABRICA E CHAO
        p1 = int(input("Digite o numero para onde pegar ceramicas:\n1 - Fabrica\n2 - Chao de Fabrica\n"))
    
        ### PARAR DE EXECUTAR QUANDO O CHAO E AS FABRICAS ESTIVEREM VAZIAS
        while not fb.is_board_empty() or not fb.is_floor_empty():
            #Escolhendo uma ceramica em uma fabrica ===============================
            if p1 == 1:
                #verfica se as fabricas ja nao estao vazias
                if fb.is_board_empty():
                    print("Todas as fabricas estao vazias escolha no chao de fabrica !")
                    p1 = 2
                    break
    
                p2 = int(input("Escolha uma fabrica: "))
                #verifico se a fabrica existe
                while True:
                    if p2 in range(fb.get_num_factorys()):
                        break
                    else:
                        p2 = int(input("Fabrica nao existente, tente novamente: "))
    
                #Verifico se a fabrica nao esta vazia
                while fb.is_manufacture_empty(p2):
                    p2 = int(input("Fabrica Vazia, Escolha outra fabrica: "))
    
                fac = fb.pick_ceramic_board(p2)
                tiles.append(fac)
                break
    
            #Escolhendo uma ceramica no chao de fabrica ===========================
            elif p1 == 2:
                #Verifica se o chao de fabrica esta limpo
                if fb.clear_floor() or fb.is_floor_empty():
                    print("Nao ha ceramicas no chao de fabrica")
                    p1 = 1
                else:
                    p2 = int(input("Escolha uma ceramica: "))
                    tiles.append(fb.pick_ceramic_floor(p2))
    
                if p1 == 2:
                    break
    
            #Default ==============================================================
            elif p1 != 1 and p1 != 2:
                p1 = int(input("Opçao Invalida\nDigite o numero para onde pegar ceramicas:\n1 - Fabrica\n2 - Chao de Fabrica"))
    
        print("=========================LHBalieiro=========================\n")
#End class --------------------------------------------------------------------
