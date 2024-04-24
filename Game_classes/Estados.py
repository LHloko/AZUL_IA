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
        self.first_ply = None

    '''
    Entrada: vazia 
    Saida: Verdadeiro caso seja o fim do jogo e Falso senao 
    Verifica se algun dos jogadores tem uma linha completa no seu tabuleiro 
    '''
    def is_game_over(self):
        for ply in self.players:
            if ply.board_full():
                print(f"======== O JOGADOR {ply.get_name()} TERMINOU O GAME AZUL ========")
                return True

            return False

    '''
    Entrada: vazia 
    Saida: Anuncia o ganhador e seu score, em caso de empate so o score
    '''
    def fim_de_jogo(self):
        #Ultima contagem de pontos
        for ply in self.players:
            ply.pontuar_ultimate_final()

        #Anuncia o Ganhador
        win = self.is_winner()
        if isinstance(win, int):
            print(f"======== O JOGO EMPATOU com SOCORE: {win} ========")
        else:
            print(f"======== O JOGADOR {win.get_name()} GANHOU com SOCORE: {win.get_score()} ========")


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
                p.pontuar()
            return True

        return False


    '''
    Entrada: Vazia 
    Saida: Vazia 
    Reinicia um turno de jogo, reiniciando a mesa de jogo 
    '''
    def iniciar_turno(self):
        #verifico a quantidade de peças do saco
        calc = self.fab.num_factorys * 4
        if len(self.pocket.pkt) < calc:
            #reembaralhar o saco
            self.pocket.set_pocket_adj_pkt(self.chao_limpo_board())
            self.pocket.bag()

        #Reiniciar a mesa de jogo
        self.fab.re_manufacture_board()


    '''
    Entrada: Vazia
    Saida: O indice do player que tem o -1, senao falso em erro
    '''
    def less_one_player(self):
        idx = 0
        for p in self.players:
            tab = p.get_tabuleiro()
            floor = tab.get_floor()
            if -1 == floor[0][0]:
                return idx
            idx += 1

        return False

    '''
    Entrada: Vazia
    Saida: Vazia
    Pega o indice do jogador que tem o -1 no piso de seu tabuleiro e o coloca 
    no inicio da list de players, sendo o primeiro a iniciar a rodada
    '''
    def first_player(self):
        um = self.less_one_player()
        self.players[0], self.players[um] = self.players[um], self.players[0]
        return True

    '''
    Entrada: Vazia
    Saida: O player que tem o maior numero de pontos ou falso em caso de empate
    '''
    def is_winner(self):
        player = []
        player.append(self.players[0])
        scr = player[0].get_score()

        #pega a maior pontuaçao
        for p in self.players:
            if p.score > scr:
                scr = p.score
                player = p

        player = []
        #Verifica se tem mais de um com a mesma pontuaçao
        for p in self.players:
            if p.score == scr:
                player.append(p)

        if len(player) == 1:
            return player[0]
        else:
            return player[0].score


    '''
    Entrada: Vazia 
    Saida: Uma list contendo todas as peças dos lixos de cada tabuleiro 
    '''
    def chao_limpo_board(self):
        sacoadj = []

        for p in self.players:
            trash = p.board.get_trash()
            for _ in range(len(trash)):
                sacoadj.append(trash.pop())

        return sacoadj

    '''
    Entrada: vazia
    Saida: Imprime o tabuleiro de cada jogador 
    '''
    def game_player_status(self):
        for p in self.players:
            print(p)
            print()

#End class --------------------------------------------------------------------
