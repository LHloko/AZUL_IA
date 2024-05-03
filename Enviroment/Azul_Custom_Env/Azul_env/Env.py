"""
Created on Thu May  2 13:26:49 2024

@author: lbalieiro@lince.lab
"""

from pettingzoo import AECEnv
from pettingzoo.utils import wrappers
import numpy as np

# Minhas Classes
import Fabrica
import Jogador
import Estados

class AzulEnv(AECEnv):
    def __init__(self):
        super().__init__()

        # Inicializar o ambiente
        self.fab = Fabrica.Fabrica()  # Instanciar a fábrica
        self.players = [Jogador.Jogador("LH"), Jogador.Jogador("VK")]  # Instanciar os jogadores

        # Dados iniciais do ambiente
        self.dados = [self.fab, self.fab.pocket, self.players]

        # Estado inicial do jogo
        self.estado = Estados.Estados(self.dados)

    '''
    Entrada: agent 
    Saida: A observaçao do ambiente (fabricas-chao de fabrica-tabuleiros) como 
    uma matriz.
    '''
    def observe(self, agent):
        # Obter o estado atual do jogo
        state = self.estado.get_states()

        # Processar o estado para criar as observações
        observations = self._process_state(state)

        return observations

    '''
    Entrada: state sendo um dicionario contendo os dados do ambiente
    Saida: Matriz com o estado atual do jogo
    Processa individualamente as fabricas, o chao de fabrica e os tabuleiros do
    jogadores, concatena tudo em uma matriz e o retorna
    '''
    def _process_states(self, state):
        factories = state['factories']
        fab_floor = state['floor']
        players_boards = state['boards']

        # Criar observações para as fábricas
        factory_observations = np.array(factories)

        # Criar observações para o centro da mesa
        floor_observations = np.array(fab_floor)

        # Criar observações para o tabuleiro de cada jogador
        players_observations = [np.array(board) for board in players_boards]

        # Concatenar todas as observações em uma única matriz
        observations = np.concatenate((factory_observations, floor_observations, *players_observations), axis=0)

        # factories [5x4]  #
        # floor     [1x1]  #
        # player1   [5x10] #
        # player2   [5x10] #

        return observations


    '''
    Entrada: action 
    Saida: 
    Implementar lógica para executar uma ação no ambiente
    '''
    def step(self, action):
        #
        pass

    '''
    Entrada: agent 
    Saida: 
    Implementar lógica para reiniciar o ambiente
    '''
    def reset(self):
        #
        pass


