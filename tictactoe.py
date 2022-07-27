# Stephan McGlashan
# CS3 tictactoe/quarto
# TODO: recon group cons, clean win out

class Piece:

    def __init__(piece):
        """
        Initializes each piece's dimensions
        as boolean values. Between color, height,
        having a hole, and shape.
        """

        piece.color = color  # Booleans since each only has 2 states
        piece.size = size
        piece.hallow = hallow
        piece.shape = shape
        piece.player = player

    @staticmethod
    def pieces(size, color, shape, hallow):
        piece_attributes = [size, color, shape, hallow]
        for attribute in piece_attributes:
            if attribute == 1:
                attribute = False
            else:
                attribute = True
        return piece_attributes

    def moves_made(piece, received, gave):
        """
        Counts passed type of pieces received
        and given by first player. Pieces received and
        given by player 1 effectively just models player 1's
        pieces played and player 2's pieces played
        respectively. Output will be displayed in endgame output.
        """

        piece.player = [[], []]
        piece.player[0].append(received)  # Player 1's pieces
        piece.player[1].append(gave)  # Player 2's pieces
        return piece.player


class Board:  # Main game

    def __init__(self, dim):
        """
        Initializes a 'dim' by 'dim' board
        Uses generators to initialize spots on virtual board.
        """

        self.dim = dim
        self.board = [[" "] * dim for _ in range(dim)]
        self.spots = [[j, i] for i in range(dim) for j in range(dim)]  # Generates lists of possible spots on board

    @staticmethod
    def stringify(row):
        """
        Creates 'columns' on board
        """

        return " " + " | ".join(row) + "\n"  # Creates whitespace / columns on board

    def __str__(self):
        """
        Concatenates rows to list and adds horizontal 'bars'
        """

        rows = [self.stringify(row) for row in self.board]
        horizontal_rule = ("---" * self.dim + "-" * (self.dim - 1) + "\n")  # Creates horizontal bars on board
        return horizontal_rule.join(rows)

    def __repr__(self):
        """
        Ensures output will look clean
        """

        return str(self)

    def groupcheck(self):
        """
        Checks to see if group of four exists in
        row / column / diagonal
        """

        Mdiagonallist = []  # Creating Major/minor diagonal lists prior to appendage
        mdiagonallist = []
        # Checks if full row of same token has been played using set length of row
        for i in range(self.dim):
            rowlist = self.board[i]  # Creates row element
            token_attribute_list = [token for token in rowlist]
            if " " in rowlist:  # Checks to see if all values are the same token
                return False
            columnlist = [self.board[j][i] for j in range(self.dim)]
            if " " in columnlist:
                return False
            Mdiagonallist.append(self.board[i][i])
            mdiagonallist.append(self.board[i][(self.dim - 1) - i])
            if (" " in Mdiagonallist) or (" " in mdiagonallist):
                return False
            shared_attributes = []
            for n, j in zip(token_attribute_list, test_list2):
                if n == j:
                    shared_attributes.append(n)
            if len(set(shared_attributes)) == 4:
                return True

    def winner(self, turns=None, player=None):
        """
        Checks match conditions, if a winner arises
        ends match loop and announces victory
        """

        if not self.groupcheck():  # Checks to see if a row / column / diagonal win condition has been met
            return False
        else:
            print("Congratulations! Player:", player, "has won over the course of", str(turns), "moves!\n")
            print("The winner played: " + str(Piece.moves_made()[turns % 2]))
            return True  # Will end game loop

    def updateboard(self, token, usercoords, spots):
        """
        Places passed token, and its attributes, in
        passed coordinates, will only update board with "x/o"
        """
        self.board[usercoords[0]][usercoords[1]] = token  # Places token in designated spot
        spots.remove(usercoords)  # Removes played spot from list of playable spots

    @staticmethod
    def legality(usercoords, spots):
        """
        Checks to see if user input is valid
        coordinate, rejects bad inputs
        """

        if usercoords not in spots:
            return False  # Reports move as illegal if input is not in playable move list
        else:
            return True

    def play(self):
        """
        Main game loop, runs until winner returns True,
        runs user inputs through wincheck and legality functions
        """

        usercoords = [self.dim, self.dim]
        turn = 0
        playernum = 1
        token = ["x"]
        while not (self.winner()):  # Main game loop
            usercoords[0] = int(input("Player " + str(playernum) + " Enter Y coordinate: "))
            usercoords[1] = int(input("Player " + str(playernum) + " Enter X coordinate: "))  # Main inputs
            size = int(input("Enter 1 for light: "))
            color = int(input("Enter 1 for big: "))
            shape = int(input("Enter 1 for hole: "))
            hallow = int(input("Enter 1 for square: "))
            Piece.pieces(size, color, shape, hallow)

            if not self.legality(usercoords, self.spots):  # If move illegal, turn not counted and player is helped
                print("Your input was invalid, available coords are: " + str(self.spots))
            else:
                if turn % 2 == 0:
                    token[0] = "x{}".format(str(turn))
                else:
                    token[0] = "o{}".format(str(turn))
                self.updateboard(token[0], usercoords, spots=self.spots)
            turn += 1  # Progress
            playernum = str((turn % 2) + 1)  # Changes active player number
            print(Quarto)
        return self.winner(player=playernum)


def main():
    """
    Runs game code
    """
    global Quarto
    Quarto = Board(4)
    # TTT = Board(3)
    Quarto.play()
    # TTT.play()


if __name__ == "__main__":
    main()
