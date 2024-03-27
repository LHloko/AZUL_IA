#Definindo as cores de cada ceramica
blue  = 0
yell  = 1
red   = 2
black = 3
white = 4

#Numero maximo de ceramicas e pratos
factory_max = 5      #Simulando para dois jogadores
ceramics_max = 100   #Cada cor tem 20

#Fabrica e um array de 4 posiçoes iniciadas com -1
factory = [-1,-1,-1,-1]

#Criando o tabuleiro
wall = []
for i in range(5):
    line = []
    for j in range(5):
        cor = (i-j)%5
        line.append([cor, False])
    wall.append(line)

for cell in wall:
    print(' '.join(map(str, cell)))

