import math
from dia10.Services.bala import *



def colision(Pos_x_ob1, Pos_y_ob1, Pos_x_ob2, Pos_y_ob2):
    distancia = math.sqrt(math.pow(Pos_x_ob1 - Pos_x_ob2, 2) + math.pow(Pos_y_ob2 - Pos_y_ob1, 2))
    if distancia < 27:
        return True
    else:
        return False







