"""
A classe Pires vai definir as cores das ceramicas como numeros; definir um 
pires como um array de 4 posiçoes definidas como -1; sortear 4 ceramicas 
aleatorias em cada pires, considerando que sao 100 ceramicas no maximo e 20 de
cada cor (azul, amarelo, vermelho, preto, branco) 

"""
import random

class MesaDeJogo():
    #Definindo alguns parametros
    blue  = 0
    yell  = 1
    red   = 2
    black = 3
    white = 4

    def __init__(self):
        #Variaveis de uma Mesa
        self.num_factorys = 5      #Define o numero padrao de fabricas para 2 players
        self.pocket = []           #criando o Saco (rsrsrs) de ceramicas
        self.factory_board = []    #Cria a o circulo de fabricas como uma list
        self.factory_floor = [-1]  #Cria o chao de fabrica como uma list

        #Cria o *saco* com 100 ceramicas, 20 de cada cor
        for i in range(5):
            colors=[]
            for j in range(20):
                colors.append(i)
            self.pocket.append(colors)

    '''
    # Entrada: Vazia 
    # Saida: Retorna uma list com quatro ceramicas escolhidas aleatoriamente
    # Cria um conjunto com 100 peças, sendo 20 de cada cor, e retorna uma tupla
    contendo 4 cores selecionadas usando a biblioteca random
    '''
    def manufacture(self): #Avaliar para quando um dos conjuntos estiver vazio
        ceramicas_set = []
        for _ in range(4):
            select_set = random.choice(self.pocket)
            sorted_ceramic = select_set.pop(0)
            ceramicas_set.append(sorted_ceramic)

        return ceramicas_set

    '''
    # Entrada: Vazio
    # Saida: Preenche a matriz factory_board com peças aleatorias e descontadas 
    do saco (rsrs)
    # 
    '''
    def manufacture_board(self):
        for i in range(self.num_factorys):
            facture = self.manufacture() #Isso eh um pires recebendo 4 pedras
            self.factory_board.append(facture)

    '''
    # Entrada: A fabrica escolhida: factury; e a ceramica escolhida: piece
    # Saida: Uma lista contendo todas as peças semelhantes da escolhida
    # Retorna uma lista com todas as peças semelhantes a escolhida, coloca as 
    demais no chao de fabrica
    '''
    def pick_ceramic(self, factury, piece):
        self.factory_board[factury] #List: fabrica escolhida

        pushcart = [] #List com todos as ceramicas escolhidas

        pick = self.factory_board[factury].pop(piece)
        pushcart.append(pick)

        for i in range(3): #Separa as peças iguais e as que vao pro chao de f.
            lady = self.factory_board[factury].pop()
            if pick == lady:
                pushcart.append(lady)
            else:
                self.factory_floor.append(lady)

        return pushcart






















