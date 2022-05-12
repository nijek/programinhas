"""
simulador de colisões
Feito inspirado nas classes desse link: https://exercism.org/tracks/python/exercises/ellens-nave-game
"""


from random import seed
from random import random
from math import sqrt
from datetime import datetime
#from string import split

eixoX = 200
eixoY = 200
eixoZ = 200
numNaves = 1000

class Nave:          
    
    total = 0
    diametro = 5
    
    @classmethod
    def change_diametro(cls, diametro):
        cls.diametro = diametro
        
    def __init__(self, name, pos):
        self.name = str(name)
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.health = 3
        Nave.total += 1
    
    def colision_detection (self, obj):
        def distance(x0, y0, z0, x1, y1, z1):
            return sqrt(pow(x1-x0,2) + pow(y1-y0,2) + pow(z1-z0, 2))
        
        return distance (self.x, self.y, self.z, obj.x, obj.y, obj.z) < Nave.diametro
    
    def total_naves_created():
        return Nave.total
    

"""
fim da classe
"""

def initNaves (posList):
    naves = []

    for i in range(len(posList)):
        naves.append(Nave(i, posList[i]))
    
    return naves    

def printNaves (naves):
    for nave in naves:
        print("nave " + str(nave.name) + " em posição (" + str(nave.x) + "; " + str(nave.y) + "; " + str(nave.z) + ")") 

def get_colisions(naves):
    coliders = []
    skipIndex = [] #para não contar duas vezes a mesma colisão
    
    for i in range(len(naves)):
        colidded = False
        colisions = []
        for j in range(len(naves)):
            if (i != j and i not in skipIndex and j not in skipIndex):
                if naves[i].colision_detection(naves[j]):
                    colidded = True
                    colisions.append(naves[j])
                    skipIndex.append(j)
        if colidded:
            colisions.append(naves[i])
            coliders.append(colisions)

    return coliders
                
def print_colisions(colisions):
    count = 0

    if colisions == []:
        print("Sem colisões")
    
    else: 
        for l in colisions:
            count += 1
            print("Colisão " + str(count) + ":")
            printNaves(l)
while True:
    inp = input("Tecle 'e' para escolher os valores, 'd' para usar default (espaço (200,200,200) com 1000 naves de diametro 5) ou qualquer outra tecla para sair")
    if inp == 'e':
        eixos = input("Digite os eixos x, y, z separados por ; ")
        eixos = eixos.split(';')
        eixoX = float(eixos[0])
        eixoY = float(eixos[1])
        eixoZ = float(eixos[2])
        Nave.diametro = float(input("Qual o diametro da nave: ")) 
        numNaves = int(input("Digite o número de naves: "))    

    elif inp != 'd':
        quit()
    
    seed(datetime.now().second) #tentar ser aleatório

    naves = initNaves ([(round(random() * eixoX, 3) , round(random() * eixoY, 3), round(random() * eixoZ, 3)) for _ in range (numNaves)]) 
    printNaves(naves)
    print_colisions(get_colisions(naves))

















    
