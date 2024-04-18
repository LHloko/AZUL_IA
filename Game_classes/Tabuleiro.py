"""
Created on Wed Mar 27 15:20:26 2024

@author: lbalieiro@lince.lab
"""

"""
definir um tabuleiro
"""
#Start class ------------------------------------------------------------------
class Tabuleiro_DeJogo():

    def __init__(self):
        self.floor = []     #Piso do tabuleiro
        self.wall = []      #Parede de ceramica
        self.pattern = []   #Parede adjacente
        self.trash = []     #Lixo do tabuleiro

        #Construindo a parede
        for i in range(5):
            line = []
            for j in range(5):
                cor = (i-j)%5
                line.append([cor, False])
            self.wall.append(line)

        #Construindo a parede adjacente
        for i in range(5):
            line = []
            for j in range(i+1):
                line.append(['',False])
            self.pattern.append(line)

        #Construindo o piso
        self.floor = [-1,False],[-1,False],[-2,False],[-2,False],[-2,False],[-3,False],[-3,False]

    """
    #  GETTERS - SETTERS - __STR__  #
    """
    def get_wall(self):
        return self.wall

    def get_floor(self):
        return self.floor

    def get_pattern(self):
        return self.pattern

    def set_wall(self, wll):
        self.wall = wll

    def set_floor(self, flr):
        self.floor = flr

    def set_pattern(self, ptr):
        self.pattern = ptr

    def __str__(self):
        return f"""
TABULEIRO: 
-----------------------------------------------------------------------------------------------------------------------------------*
{self.wall[0]}  <  {self.pattern[0]}
{self.wall[1]}  <  {self.pattern[1]}
{self.wall[2]}  <  {self.pattern[2]}
{self.wall[3]}  <  {self.pattern[3]}
{self.wall[4]}  <  {self.pattern[4]}
-----------------------------------------------------------------------------------------------------------------------------------*                  
{self.floor}

Lixo do tabuleiro:
{self.trash}
"""

    """
    #  Funçoes de Classe  ================================================== #
    """

    '''
    Entrada: list de ceramicas tiles
    Saida: Vazio 
    Pega a list tiles e coloca no piso, caso exceda envia para o lixo
    '''
    def cement_floor(self, tiles):
        flr = self.floor

        #Pega o indice que tem posiçao livre
        idx = 0
        while flr[idx][1] == True:
            idx += 1
            if idx > 6:
                break

        #Colocar as ceramicas
        for i in range(idx,len(tiles)+idx):
            if i<7: #Nao extrapolou o piso
                flr[i][0] = tiles.pop(0)
                flr[i][1] = True
            else: #Piso estourado
                self.trash.append(tiles.pop())


    '''
    Entrada: list de ceramicas tiles, e linha adjancente line
    Saida: Verdadeiro caso inserido, falso senao
    Pega a list tiles e coloca no piso, caso exceda envia para o lixo
    '''
    def cement_line(self, tiles, line):
        #se tiver o -1
        self.is_tile_um(tiles)

        #se escolhido o piso
        if line == 5:
            self.cement_floor(tiles)
            return True

        #se escolhido uma linha adjacente
        ln_adj = self.pattern[line]
        cor = tiles[0]
        cpv = self.how_is_full_line(line)
        rest = []

        #verificar se a linha esta cheia
        if cpv == -2:
            print("linha cheia [!]")
            return False

        #verifico se esta completamente vazia
        if cpv == -1:
            #pega o indice que tem posiçao livre
            idx = 0
            while ln_adj[idx][1] == True:
                idx += 1

            #meter os tijolos na linha
            for i in range(idx, len(tiles)):
                if i < len(ln_adj):
                    ln_adj[i][0] = tiles.pop()
                    ln_adj[i][1] = True

                else: #linha estourada
                    rest.append(tiles.pop())

            self.cement_floor(rest)

            return True

        #verificar se a linha esta com outra cor
        if cpv != cor:
            print("linha ja contem ceramicas de outra cor [!]")
            return False


    '''
    Entrada: Um inteiro referente a cor da ceramica, color  
    Saida: Verdadeiro caso todas as linhas estejam preenchidas com cores 
            diferentes de color 
    def full_color_dif(self, color):
        for i in range(5):
            #Se tiver pelomenos uma igua = retorna falso
            if self.how_is_full_line(i) == color:
                return False

        return True
    '''


    '''
    Entrada: Vazia  
    Saida: Verdadeiro caso todas estejam as linhas estejam cheias e falso senao 
    '''
    def all_lines_full(self):
        for i in range(5):
            if self.how_is_full_line(i) != -2:
                return False

        return True


    '''
    Entrada: List tiles com as ceramicas pegas
    Saida: Retorna a list tiles
    Verifica se a tiles contem o -1 se tiver o coloca no piso 
    '''
    def is_tile_um(self, tiles):
        flr = self.floor

        #Coloca o -1 na primeira posiçao do piso
        if tiles[0] == -1:
            flr[0][0] = tiles.pop(0)
            flr[0][1] = True

        return tiles


    '''
    Entrada: A linha escolhida 'line' a se por ceramicas
    Saida: -1 para linha vazia, -2 linha completamente cheia e o valor da cor 
            se preenchida parcialmente
    '''
    def how_is_full_line(self, line):
        flr = self.pattern[line]

        #Verifica se esta vazia
        if flr[0][1] == False:
            return -1

        #Verifica se esta completamente cheia
        if flr[line][1] == True:
            return -2

        #Retorna o valor da cor ja presente
        return flr[0][0]

#End class --------------------------------------------------------------------
