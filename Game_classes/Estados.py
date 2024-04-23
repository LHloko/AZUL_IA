"""
Created on Wed Apr  3 09:48:11 2024

@author: lbalieiro@lince.lab
"""

'''Criar funçoes que qualificam quao bom eh aquele estado de tabuleiro'''

import Fabrica
import Tabuleiro
import Jogador
import Saco

#Start class ------------------------------------------------------------------
class Estados():

    '''
    Entrada: Uma tupla: [ fabrica, saco, [jogadores]] chamada dados
    '''
    def __init__(self, dados):
        self.fab = dados[0]
        self.pocket = dados[1]
        self.players = dados[2]

    '''
    Entrada: vazia 
    Saida: Verdadeiro caso seja o fim do jogo e Falso senao 
    Verifica se algun dos jogadores tem uma linha completa no seu tabuleiro 
    '''
    def is_game_over(self):
        for ply in self.players:
            if ply.board_full():
                print("======== O JOGADOR {ply.get_name()} TERMINOU O GAME AZUL ========")
                return True

            return False

    '''
    Entrada: vazia 
    Saida: Anuncia o ganhador e seu score, em caso de empate so o score
    '''
    def fim_de_jogo(self):
        if self.is_game_over():
            #Anuncia o Ganhador
            win = self.is_winner()
            if isinstance(win, int):
                print("======== O JOGO EMPATOU com SOCORE: {win} ========")
            else:
                print("======== O JOGADOR {win.get_name()} GANHOU com SOCORE: {win.get_score()} ========")


    '''
    Entrada: Vazia
    Saida: Verdadeiro para fim de do turno e falso senao
    Condiçao de fim de jogo: Todas as fabricas estao vazias e o chao tambem esta
    '''
    def fim_de_turno(self):
        # Verifico se as fabricas e o chao estao vazios
        if self.fab.is_board_empty() and self.fab.is_floor_empty():
            for p in self.players:
                # Somo os pontos e preencho a parede
                p.emparedar()
            return True

        return False


    '''
    Entrada: Vazia 
    Saida: Vazia 
    Verifica a quantidade de peças no saco, se necessario o reembaralha, e 
    distribui as ceramicas nas fabricas novamente 
    '''
    def iniciar_turno(self):
        '''
        #verifico a quantidade de peças no saco [ preciso reembaralhar ? ]
        #sorteio as peças e distribuo nas fabricas     
        '''

    '''
    Entrada: Vazia
    Saida: O player que tem o -1 e começara a proxima rodada, senao falso em erro
    '''
    def first_player(self):
        for p in self.players:
            tab = p.get_tabuleiro()
            floor = tab.get_floor()
            if -1 in floor[0][0]:
                return p

        return False

    '''
    Entrada: Vazia
    Saida: O player que tem o maior numero de pontos ou falso em caso de empate
    '''
    def is_winner(self):
        player = []
        player.append(self.players[0])
        score = player.get_score()

        #pega a maior pontuaçao
        for p in self.players:
            if p.score() > score:
                score = p.score
                player = p

        #Verifica se tem mais de um com a mesma pontuaçao
        for p in self.players:
            if p.score == score:
                player.append(p)

        if len(player) == 1:
            return player[0]
        else:
            return player[0].score


#End class --------------------------------------------------------------------
