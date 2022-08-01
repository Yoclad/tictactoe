# Stephan McGlashan
# CS3 tictactoe/quarto

from termcolor import colored, cprint  # Piece colors


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
        color: True = red, False = blue,
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

        piece_list = [colored("●", "red"), colored("●", "red", attrs=["underline"]), colored("◉", "red"),
                      colored("◉", "red", attrs=["underline"]),
                      colored("■", "red"), colored("■", "red", attrs=["underline"]), colored("◙", "red"),
                      colored("◙", "red", attrs=["underline"]),
                      colored("●", "blue"), colored("●", "blue", attrs=["underline"]), colored("◉", "blue"),
                      colored("◉", "blue", attrs=["underline"]),
                      colored("■", "blue"), colored("■", "blue", attrs=["underline"]), colored("◙", "blue"),
                      colored("◙", "blue", attrs=["underline"])]
        if piece_list[piece_number] not in piece_list:
            return "Your piece is unavailable\nAvailable pieces are: " + str(piece_list)
        else:
            piece_list.remove(piece_list[piece_number])  # removes played / given piece
            return piece_list[piece_number]

    @staticmethod
    def character_conversion(token):
        """
        Checks passed token's attributes to determine
        which ASCII piece to use from list then eliminates
        all other characters from ASCII list
        """

        piece_numbers = [0, 1, 2, 3,
                         4, 5, 6, 7,
                         8, 9, 10, 11,
                         12, 13, 14, 15]  # Translates 1:1 to ASCII list

        circles = [0, 1, 2, 3, 8, 9, 10, 11]  # No divisibility pattern availible for these attributes
        holes = [2, 3, 6, 7, 10, 11, 14, 15]

        for piece in range(len(piece_numbers)):  # Loops for all piece and removes respective attributes
            if token.size:
                if piece % 2 == 1:
                    piece_list.remove(piece)
            if token.color:
                if piece > 7:
                    piece_list.remove(piece)
            if token.shape:
                if piece in circles:
                    piece_list.remove(piece)
            if token.hole:
                if piece in holes:
                    piece_list.remove(piece)

        return piece_list(piece_number)  # Returns last remaining char that meets conditions

    def updateboard(self, token_attributes, usercoords, spots):
        """
        Places passed token, and its passed attributes, in
        passed coordinates,
        """

        token = Token(token_attributes[0], token_attributes[1], token_attributes[2], token_attributes[3])
        token_item = character_conversion(token), token
        self.board[usercoords[0]][usercoords[1]] = token_item[0]  # Places token in designated spot
        spots.remove(usercoords)  # Removes played spot from list of playable spots
        return

    @staticmethod
    def legality(usercoords, spots):
        """
        Checks to see if user input is valid
        coordinate, rejects bad inputs
        """

        if usercoords not in spots:
            return False  # Reports move as illegal if input is not in spot list
        else:
            return True

    @staticmethod
    def moves_made(played=None, coordinates=None):
        """
        Generates string of moves made for each player
        to keep game record. Returned every turn to each
        player's move list to be reported at the end of
        the game.

        A single move consists of the piece played,
        the coordinates where the piece was played,
        and the piece given to the opposing player.
        """

        player_moves = []
        player.append(played, "at", str(coordinates))
        return player_moves

    @staticmethod
    def token_retrieval(line):
        """
        Helper function for the winner main loop.
        will retrieve each token object from the
        line in the current iteration so the boolean
        attributes can be operated on to find similarities.
        """

        size = []  # Initializing lists for later set comprehension
        shape = []
        color = []
        hole = []
        for token in line:  # Appends each token's attributes to the line's attribute lists above
            token_attributes = token[1]  # Accesses attributes in token tuple
            size.append(token_attributes.size)
            shape.append(token_attributes.shape)
            color.append(token_attributes.color)
            hole.append(token_attributes.hole)

        return size, shape, color, hole

    def winner(self, turns=None, playernum=None, winners_moves=None):
        """
        Checks token attributes of lines with groups of 4.
        Attributes are assigned each turn. If a winner arises
        ends match loop and announces victory with metrics
        from 'moves_made' generated list and amount of turns.
        """

        for line in self.groupcheck():  # Retrieves groups from 'groupcheck' function to pass through 'token_retrieval'
            size, shape, color, hole = self.token_retrieval(line)
            if (len(set(size)) or len(set(shape)) or len(set(color)) or len(set(hole))) == 1:
                print("Congratulations! Player:", str(playernum), "has won over the course of", str(turns), "moves!\n")
                print("Winner's moves: " + str(winners_moves))
                return True  # Will end game loop
            else:
                return False  # Game continues

    def play(self):
        """
        Main game loop, runs until winner returns True,
        runs user inputs through 'winner' and 'legality'
        functions. Also uses several arbitrary vars,
        'turn', 'playernum', 'attributes' to ensure functionality
        of all backend game functions.

        Full game functionality. 1 to 1 transfer to real game. First player
        chooses what piece to give next player, player with piece
        chooses where to play the given piece. Continues until a played
        piece meets the win conditions.
        """

        attributes = []  # Arbitrary vars for functionality
        usercoords = [self.dim, self.dim]
        turn = 0
        playernum = 1
        player1_moves = []
        player2_moves = []
        while not (self.winner()):  # Main game loop
            print("Player", str(playernum), ", choose the next piece to be played")
            size = int(input("Enter 1 for big: "))
            color = int(input("Enter 1 for light: "))
            shape = int(input("Enter 1 for square: "))
            hole = int(input("Enter 1 for hole: "))

            playernum = str((turn % 2) + 1)  # Changes active player number

            usercoords[0] = int(input("Player " + str(playernum) + " Enter Y coordinate: "))
            usercoords[1] = int(input("Player " + str(playernum) + " Enter X coordinate: "))

            attributes.extend([size, color, shape, hole])  # Adds desired attributes and converts to ASCII shape
            token_attributes = self.attribute_conversion(attributes)

            if not self.legality(usercoords, self.spots):  # If input is illegal, turn not counted and player is helped
                print("Your input was invalid, available coords are: " + str(self.spots))
            else:
                if playernum == 1:
                    player1_moves.append(self.moves_made("character", usercoords))  # Logs legal moves
                else:
                    player2_moves.append(self.moves_made("character", usercoords))
                self.updateboard(token_attributes, usercoords, spots=self.spots)  # Places ASCII char in usercoords
            turn += 1  # Progress
            print(Quarto)
        if playernum == 1:
            winners_moves = player1_moves
        else:
            winners_moves = player2_moves
        return self.winner(turns=turns, player=playernum, winners_moves=winners_moves)  # Returns winner / report at end


def main():
    """
    Driver code
    """

    global Quarto
    Quarto = Board(4)
    # TTT = Board(3)
    Quarto.play()
    # TTT.play()


if __name__ == "__main__":
    main()
