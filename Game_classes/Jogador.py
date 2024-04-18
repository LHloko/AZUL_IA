"""
Created on Wed Mar 27 15:19:58 2024

@author: lbalieiro@lince.lab
"""

import Fabrica
import Tabuleiro

#Start class ------------------------------------------------------------------
class Jogador():

    def __init__(self):
        self.board = Tabuleiro.Tabuleiro_DeJogo()
        self.score = 0

    '''
    Entrada: fabrica do jogo, e o local sendo 1 para fabrica ou 2 para o chao
    Saida: Verdadeiro para caso seja possivel pegar ceramicas, falso senao
    '''
    def playar(self,fabrica):
        #Pega as ceramicas
        nome_exageradamente_grande_para_ceramicas = self.pegar_ceramica(fabrica)

        #Aloca as ceramicas
        self.colocar_no_tabuleiro(nome_exageradamente_grande_para_ceramicas)

        #Fim
        return True

    '''
    Entrada: fabrica do jogo, e o local sendo 1 para fabrica ou 2 para o chao
    Saida: Verdadeiro para caso seja possivel pegar ceramicas, falso senao
    '''
    def escolher_fab_chao(self, fb, local):
        #FABRICA
        if local == 1:
            #verfica se as fabricas ja nao estao vazias
            if fb.is_board_empty():
                print("Todas as fabricas estao vazias escolha no chao de fabrica !")
                return False

        #CHAO DE FABRICA
        elif local == 2:
            #Verifica se o chao de fabrica esta limpo ou vazio
            if fb.clear_floor() or fb.is_floor_empty():
                print("Nao ha ceramicas no chao de fabrica")
                return False

        else:
            return False

        return True


    '''
    Entrada: fb - fabrica do jogo
    Saida: Lista com as ceramicas pegas 
    '''
    def pegar_ceramica(self, fb):
        p1 = int(input("Digite o numero para onde pegar ceramicas:\n1 - Fabrica\n2 - Chao de Fabrica\n"))
        local = self.escolher_fab_chao(fb, p1)

        #verifica se e possivel pegar ceramicas no lugar passado
        while not local:
            p1 = int(input("\nTente outro Lugar: \n"))
            local = self.escolher_fab_chao(fb,p1)

        #Escolheu -> Fabrica
        if p1 == 1:
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

            #Pegando as ceramicas
            ceramicas = fb.pick_ceramic_board(p2)

        #Escolheu -> Chao de Fabrica
        else:
            cor = int(input("escolha uma cor: "))
            ceramicas = fb.pick_ceramic_floor(cor)

        return ceramicas

    '''
    Entrada: ceramicas pegas 
    Saida: Vazia
    Solicita uma linha adjacente ou o piso e insere as ceramicas
    '''
    def colocar_no_tabuleiro(self, ceramicas):
        line = int(input("Escolha onde colocar as ceramicas pegas:\n[0-4] linhas adjacentes\n  [5] piso\n"))

        while not self.board.cement_line(ceramicas, line):
            line = int(input("Escolha outra linha:\n[0 - 4] linhas adjacentes\n  [5] piso\n"))


#End class --------------------------------------------------------------------
