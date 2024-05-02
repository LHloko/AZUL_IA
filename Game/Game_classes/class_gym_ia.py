import gymnasium as gym
from gymnasium import spaces
import numpy as np

class AzulEnv(gym.Env):
    
    def __init__(self):
        metadata = {"render_modes": ["ansi"], "render_fps": 1}

        # Definir action space: bounds, space type, shape 


        # Definir o espaço de ação como Discrete, com ações numeradas de 0 a 181
        self.action_space = spaces.Discrete(182)
        
        
        
        
        
        
        
        

        factory_shape = (5,4) # matriz das fábricas
        floor_fab_shape = (16) # list do chao de fábrica
        

        # Definir o espaço de observação como um espaço Box
        # Aqui, vamos considerar uma representação simplificada do estado do tabuleiro
        # Será necessário ajustar isso conforme necessário para representar o estado real do jogo
        self.observation_space = spaces.Box(low=0, high=4, shape=(5, 5), dtype=np.int)

        # Definir outras variáveis de estado, como o tabuleiro e o jogador atual
        self.board = np.zeros((5, 5), dtype=np.int)
        self.current_player = 1  # Começamos com o jogador 1

    '''
    Entrada: Vazia
    Saida:
    '''
    def reset(self):
        # Reinicializar o ambiente para um novo jogo
        self.board = np.zeros((5, 5), dtype=np.int)
        self.current_player = 1
        return self._get_observation()

    '''
    Entrada: 
    Saida:
    '''
    def step(self, action):
        # Executar uma ação e avançar um passo no ambiente
        # Implementação lógica da ação aqui
        # Retornar a observação, a recompensa, se o jogo terminou e informações adicionais

    '''
    Entrada: Vazia
    Saida:
    '''
    def _get_observation(self):
        # Retornar a observação atual do ambiente (estado atual do tabuleiro)
        return self.board
    
    '''
    Entrada: Vazia
    Saida:
    '''
    def _is_game_over(self):
        # Verificar se o jogo terminou
        # Implementação da lógica de término do jogo aqui
        return False  # Placeholder, substituir com a lógica real

    '''
    Entrada: 
    Saida:
    '''
    def _take_action(self, action):
        # Implementação para executar a ação escolhida pelo agente
        pass  # Placeholder, implementação real necessária

    '''
    Entrada: Vazia 
    Saida:
    '''
    def _get_reward(self):
        # Calcular a recompensa com base no estado atual do tabuleiro
        # Implementação da função de recompensa aqui
        return 0  # Placeholder, substituir com a lógica real
