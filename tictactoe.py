# Stephan McGlashan
# CS3 tictactoe/quarto


class Token:  # Piece attributes

    def __init__(piece, size, shape, color, hole):
        """
        Initializes each piece's dimensions
        as boolean values. Between color, height,
        having a hole, and shape.
        """

        piece.color = color  # Booleans since each only has 2 states
        piece.size = size
        piece.hole = hole
        piece.shape = shape


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
        Checks to see if four pieces exist in
        row / column / diagonal to pass into 'winner'
        to identify potential winner and end game loop.
        """

        Mdiagonallist = []  # Creating Major/minor diagonal lists prior to appendage
        mdiagonallist = []
        for i in range(self.dim):  # Creates board in list format to check contents
            rowlist = self.board[i]
            columnlist = [self.board[j][i] for j in range(self.dim)]
            Mdiagonallist.append(self.board[i][i])
            mdiagonallist.append(self.board[i][(self.dim - 1) - i])

        master_list = [rowlist, columnlist, Mdiagonallist, mdiagonallist]
        for line in master_list:  # Checks all lists for whitespaces
            if " " not in line:
                master_list.remove(line)
            return master_list

    @staticmethod
    def attribute_conversion(attributes):
        """
        Converts the player's numeric string input into
        boolean values so the winner function can find
        winning patterns of 4 during the game. Effectively
        just a helper function.

        Key (order matters):
        size: True = big, False = small,
        color: True = beige, False = chocolate,
        shape: True = square, False = circle,
        hole: True = hole, False = hallow,
        """

        token_attributes = []
        for attribute in attributes:  # Converts numeric entry to boolean
            if attribute == "1":
                token_attributes.append(True)
            else:
                token_attributes.append(False)
        return token_attributes

    @staticmethod
    def piece_list(piece_number):
        """
        Stores game pieces and log of which are
        availible to play. If user tries to use
        or give piece that has already been played
        it returns an error message and prompts the player
        to pick another piece from the remaining pieces.
        """
        piece_list = []
        if piece_list[piece_number] not in piece_list:
            return "Your piece is unavailable\nAvailable pieces are: " + str(piece_list)
        else:
            piece_list.remove(piece_list[piece_number])  # removes played / given piece
            return piece_list[piece_number]

    @staticmethod
    def character_conversion(token):
        """
        Checks passed token's attributes to determine
        which piece to use from piece list
        """
        piece_numbers = [0, 1, 2, 3,
                         4, 5, 6, 7,
                         8, 9, 10, 11,
                         12, 13, 14, 15]

        if token.size:
            piece_list.remove(smalls)
        if token.color:
            piece_list.remove(chocolates)
        if token.shape:
            piece_list.remove(circles)
        if token.hole:
            piece_list.remove(holes)

        return piece_list(piece_number)

    def updateboard(self, token_attributes, usercoords, spots):
        """
        Places passed token, and its passed attributes, in
        passed coordinates,
        """

        token = Token(token_attributes[0], token_attributes[1], token_attributes[2], token_attributes[3])
        token_character = character_conversion(token)
        self.board[usercoords[0]][usercoords[1]] = token_character  # Places token in designated spot
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

    @staticmethod
    def moves_made(played, coordinates, gave):
        """
        Generates list of moves made for each player
        to keep game record. Will be returned by end
        of the game.

        A single move consists of the piece played,
        the coordinates where the piece was played,
        and the piece given to the opposing player.
        """

        player_moves = [[], []]
        player[0].append(played, "at", coordinates)
        player[1].append("Gave", gave)
        return player_moves

    def winner(self, turns=None, player=None):
        """
        Checks token attributes of lines with groups of 4.
        Attributes are assigned each turn. If a winner arises
        ends match loop and announces victory
        """
        for line in self.groupcheck():
            size = []  # Initializing lists for later set comprehension
            shape = []
            color = []
            hole = []
            for token in line:  # Appends each token's attributes to the line's attribute lists above
                height.append(token.size)
                shape.append(token.shape)
                color.append(token.color)
                hole.append(token.hole)
            if (len(set(size)) or len(set(shape)) or len(set(color)) or len(set(hole))) == 1:
                print("Congratulations! Player:", player, "has won over the course of", str(turns), "moves!\n")
                print("The winner played: " + str(moves_made()[turns % 2]))
                return True  # Will end game loop
            else:
                return False  # Game continues

    def play(self):
        """
        Main game loop, runs until winner returns True,
        runs user inputs through wincheck and legality functions
        """

        attributes = []
        usercoords = [self.dim, self.dim]
        turn = 0
        playernum = 1
        player1_moves = []
        player2_moves = []
        while not (self.winner()):  # Main game loop
            size = int(input("Enter 1 for big: "))
            color = int(input("Enter 1 for light: "))
            shape = int(input("Enter 1 for square: "))
            hole = int(input("Enter 1 for hole: "))
            usercoords[0] = int(input("Player " + str(playernum) + " Enter Y coordinate: "))
            usercoords[1] = int(input("Player " + str(playernum) + " Enter X coordinate: "))

            attributes.extend([size, color, shape, hole])
            token_attributes = self.attribute_conversion(attributes)

            if not self.legality(usercoords, self.spots):  # If move illegal, turn not counted and player is helped
                print("Your input was invalid, available coords are: " + str(self.spots))
            else:
                if turn % 2 == 0:
                    token[0] = "character"
                else:
                    token[0] = "character"

                if playernum == 1:
                    player1_moves.append(self.moves_made("character", usercoords, ))
                else:
                    player2_moves.append(self.moves_made("character", usercoords, ))
                self.updateboard(token_attributes, usercoords, spots=self.spots)
            turn += 1  # Progress
            playernum = str((turn % 2) + 1)  # Changes active player number
            print(Quarto)
        return self.winner(turns=turns, player=playernum)


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
