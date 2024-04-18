"""
Created on Mon Apr  1 18:30:45 2024

@author: lbalieiro@lince.lab
"""

import Fabrica
import Tabuleiro
import Jogador

#Start class ------------------------------------------------------------------
def main():

    fab = Fabrica.Fabrica()
    luiz = Jogador.Jogador()

    print(fab)

    while True:
        luiz.playar(fab)
        print(luiz.board)
        print(fab)

#End class --------------------------------------------------------------------


if __name__ == "__main__":
    main()





















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
