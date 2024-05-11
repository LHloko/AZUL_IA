"""
Created on Thu May  2 13:26:49 2024

@author: lbalieiro@lince.lab
"""

import gym
from gym import spaces
import numpy as np

# Minhas Classes
from Game_classes_v02 import Fabrica
from Game_classes_v02 import Estado
from Game_classes_v02 import Jogador

class AzulEnv(gym.Env):
    
    def __init__(self):
        super(AzulEnv, self).__init__()

        # Definir os espaços de ação e observação
        self.action_space = spaces.Tuple([
            spaces.Discrete(6),  # Lugar onde pegar as cerâmicas (0-5)
            spaces.Discrete(5),  # Cerâmica a pegar (0-4)
            spaces.Discrete(6)   # Lugar onde por as cerâmicas pegas (0-5)
        ])
        self.observation_space = spaces.Box(low=-3, high=4, shape=(30, 10), dtype=np.int)

        # Inicializar o estado do ambiente
        self.reset()


    '''
    Entrada: agent
    Saida: A observaçao do ambiente (fabricas-chao_de_fabrica-tabuleiros) como 
    uma matriz.
    '''
    def observe(self, agent):
        '''
        depois voce muda ai pra matriz do jogador ter um espacinho na quina su-
        perior pra colocar o -1 se houver (joinha)
        '''

        # Obter o estado atual do jogo
        state = self.estado.get_states()

        factories       = state['fac']
        factory_floor   = state['fac-flr']
        ply_bord_01     = state['ply_01']
        ply_bord_02     = state['ply_02']

        # Processar o estado para criar as observações
        table = np.concatenate((factories, factory_floor), axis=1)

        observations = np.concatenate((table,ply_bord_01,ply_bord_02), axis = 0)

        return observations


    '''
    Entrada: action como uma tupla com 3 valores 
    Saida: 
    Implementar lógica para executar uma ação no ambiente
    '''
    def step(self, action):
        terminated = False
        truncated = False
        reward = 0

        # Executar a ação no ambiente
        valid_move = self.players.playar(action)

        if valid_move:
            reward += 1 # Movimento valido
        else:
            reward -= 10 # Movimento invalido

        # Verificar se o turno acabou
        if self.estado.fim_de_turno():
            reward += self.players.pontuar() # Obter a recompensa do fim do turno
            # Verificar se o jogo acabou
            if self.estado.is_game_over():
                terminated = True
                reward += self.pontuar_ultimate_final()  # Obter a recompensa do fim do jogo

        # Atualizar o estado do jogo e retornar a observação, recompensa e sinalizadores de término
        observation = self.observe()
        info = self.get_info()

        return observation, reward, terminated, truncated, info


    '''
    Entrada: action como uma tupla com 3 valores 
    Saida: 
    Implementar lógica para executar uma ação no ambiente
    '''
    def get_info(self):
        first_player = None
        is_last_round = False

        if self.estado.fim_de_turno:
            for player in self.players:
                if player.me_have_minus_one_gd:
                    first_player = player.get_name()
                    break
    
        if self.estado.is_last_round_to_end():
            is_last_round = True
    
        info = {
            "first_player": first_player,
            "is_last_round": is_last_round
        }
    
        return info


    '''
    Entrada: Vazia
    Saida: A observaçao do estado inicial do jogo 
    Inicia um jogo do zero, com a instanciaçao de cada classe e dos jogadores 
    '''
    def reset(self):
        # Inicializar o ambiente
        self.fab = Fabrica.Fabrica()  # Instanciar a fábrica
        self.players = [Jogador.Jogador("LH")]  # Instanciar os jogadores =+= , Jogador.Jogador("VK")

        # Dados iniciais do ambiente
        self.dados = [self.fab, self.fab.pocket, self.players]

        # Estado inicial do jogo
        self.estado = Estado.Estados(self.dados)

        # Atualizar os dados do ambiente com o estado reiniciado
        self.dados = [self.fab, self.fab.pocket, self.players]
        self.estado = Estado.Estados(self.dados)
    
        # Retornar a observação inicial do ambiente
        return self.observe()


