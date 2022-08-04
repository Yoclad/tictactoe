# Stephan McGlashan
# CS3 quarto solver
# Currently implements 'random selection' logic

import random
from quarto import *


class Solver(Player):

    def __init__(self):
        super().__init__()
        self.bot_piece_number = None
        self.quarto = Quarto(4)
        self.player = Player()

    def pick_random_piece(self):
        """
        Picks random number from 0-16 to pass into
        player.pick_piece
        """

        random_piece_number = random.randint(0, 16)

        self.bot_piece_number = self.player.pick_piece(base_input=random_piece_number)
        return self.bot_piece_number

    def play_random_spot(self):
        spot_list = self.quarto.spots
        num_spots = len(spot_list)  # Initializing number of available spots to pick random spot
        random_spot_index = random.randint(range(num_spots))  # Picks random index in
        self.spot = spot_list[random_spot_index]
        return self.spot
