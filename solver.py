# Stephan McGlashan
# CS3 quarto solver
# Currently implements 'random selection' logic

import random
from quarto import *


class Solver(Player):

    def __init__(self, token, spot):
        super().__init__()
        self.quarto = Quarto(4)
        self.token = token
        self.spot = spot

    def pick_random_piece(self):
        size = str(random.randint(0, 1))
        color = str(random.randint(0, 1))
        shape = str(random.randint(0, 1))
        hole = str(random.randint(0, 1))

        self.token = Token(size, color, shape, hole)
        return self.token

    def play_random_spot(self):
        xcoord = random.randint(0,3)
        ycoord = random.randint(0,3)
        self.spot = [xcoord, ycoord]

        return self.spot