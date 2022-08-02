# Stephan McGlashan
# CS3 quarto

from termcolor import colored, cprint  # Piece colors


def bool_to_bin(attribute_list):
    """
    Converts user boolean input
    to binary to pass as key in
    the character function later.
    """

    binary_attribute = []  # Binary number represented as list ex.\ ["0","1","1","0"]
    for attribute in attribute_list:
        if attribute:
            binary_attribute.append(1)
        else:
            binary_attribute.append(0)

    binary = ""
    for attribute in binary_attribute:
        binary += str(attribute)
    return binary


class Token:  # Piece attributes

    def __init__(self, size, shape, color, hole):
        """
        Initializes each piece's dimensions
        as boolean values. Between color, height,
        having a hole, and shape.
        """

        self.color = color  # Booleans since each only has 2 states
        self.size = size
        self.hole = hole
        self.shape = shape

    def __str__(self):
        """
        Handles piece representation on backend
        so user input can be directly associate
        ASCII 'piece'. Order of booleans is "size
        color, shape, hole" matters.
        """

        piece_dict = {"0000": colored("●", "red"),
                      "1000": colored("●", "red", attrs=["underline"]),
                      "0001": colored("◉", "red"),
                      "1001": colored("◉", "red", attrs=["underline"]),
                      "0010": colored("■", "red"),
                      "1010": colored("■", "red", attrs=["underline"]),
                      "0011": colored("◙", "red"),
                      "1011": colored("◙", "red", attrs=["underline"]),
                      "0100": colored("●", "blue"),
                      "1100": colored("●", "blue", attrs=["underline"]),
                      "0101": colored("◉", "blue"),
                      "1101": colored("◉", "blue", attrs=["underline"]),
                      "0110": colored("■", "blue"),
                      "1110": colored("■", "blue", attrs=["underline"]),
                      "0111": colored("◙", "blue"),
                      "1111": colored("◙", "blue", attrs=["underline"])}

        attribute_list = [self.size, self.color, self.shape, self.hole]
        return piece_dict[bool_to_bin(attribute_list)]  # Returns piece


class Player:

    def __init__(self, token=None, spot=None):
        """
        Initializes the given player's
        token and spot for them to choose.
        """

        self.token = token
        self.spot = spot

    def pick_piece(self):
        """
        Prompts player to enter their desired piece
        attributes in numeric form. Passes their input
        to the Token class which will return an ASCII
        token string which is then returned.
        """

        size = int(input("Enter 1 for a tall piece: "))
        color = int(input("Enter 1 for a blue piece: "))
        shape = int(input("Enter 1 for a square piece: "))
        hole = int(input("Enter 1 for a hole piece: "))

        self.token = Token(size, color, shape, hole)
        return self.token

    def play_piece(self):
        """
        Prompts player to enter their desired
        coordinates to play the piece they had
        received.
        """

        xcoord = int(input("Enter Y coordinate: "))
        ycoord = int(input("Enter X coordinate: "))
        self.spot = [xcoord, ycoord]
        return self.spot


class Quarto:  # Main game

    def __init__(self, dim):
        """
        Initializes a 'dim' by 'dim' board
        Uses generators to initialize spots on virtual board.
        """
        self.player = Player()
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
        return master_list

    @staticmethod
    def piece_list(piece_number):
        """
        Stores game pieces and log of which are
        availible to play in binary list. List is
        generated using the built-in 'bin()' function.
        The output string is cleaned using the
        '.replace()' built-in. If user tries to use
        or give piece that has already been played
        it returns an error message and prompts the player
        to pick another piece from the remaining pieces.
        """

        bin_list = [bin(index).replace('0b', '') for index in range(16)]  # Generates list of binary indices
        if bin_list[piece_number] not in bin_list:
            return "Your piece is unavailable\nAvailable pieces are: " + str(bin_list)
        else:
            bin_list.remove(piece_number)  # Removes played / given piece
            return bin_list[piece_number]

    def updateboard(self, token, usercoords, spots):
        """
        Places passed token, and its passed attributes,
        in passed coordinates
        """

        self.board[usercoords[0]][usercoords[1]] = str(token)  # Places token in passed spot
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

        player_moves = [played, "at:", str(coordinates)]
        return player_moves

    @staticmethod
    def token_check(line):
        """
        Helper function for the winner main loop.
        will retrieve each token object from the
        line in the current iteration so the boolean
        attributes can be operated on to find similarities.
        """

        sizes = []  # Initializing lists for later set comprehension
        shapes = []
        colors = []
        holes = []
        for token in line:  # Appends each token's attributes to the line's attribute lists above
            sizes.append(token.size)
            shapes.append(token.shape)
            colors.append(token.color)
            holes.append(token.hole)
        return size, shape, color, hole

    def winner(self, turns=None, playernum=None, winners_moves=None):
        """
        Checks token attributes of lines with groups of 4.
        Attributes are assigned each turn. If a winner arises
        ends match loop and announces victory with metrics
        from 'moves_made' generated list and amount of turns.
        """

        for line in self.groupcheck():  # Retrieves groups from 'groupcheck' function to
            if ' ' not in line:
                size, shape, color, hole = self.token_check(line)
            else:
                break
            if (len(set(size)) or len(set(shape)) or len(set(color)) or len(set(hole))) == 1:
                print("Congratulations! Player:", str(playernum), "has won over the course of", str(turns), "moves!\n")
                print("Winner's moves: " + str(winners_moves))
                return True  # Will end game loop
            elif len(self.spots) == 0:
                print("The game has ended in a draw!")
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

        playernum = 2  # Arbitrary vars for functionality
        turn = 0
        player1_moves = []
        player2_moves = []
        while not (self.winner()):  # Main game loop
            print("Player", str(playernum), ", choose the next piece to be played:\n")
            token = self.player.pick_piece()

            playernum = str((turn % 2) + 1)  # Changes active player number

            print("Player", str(playernum), ", where would you like to play your piece?\n")
            usercoords = self.player.play_piece()

            if not self.legality(usercoords, self.spots):  # If input is illegal, turn not counted and player helped
                print("Your spot is not available, your options are: " + str(self.spots))
            else:
                if playernum == 1:
                    player1_moves.append(self.moves_made("character", usercoords))  # Logs legal moves
                else:
                    player2_moves.append(self.moves_made("character", usercoords))
                self.updateboard(token, usercoords, spots=self.spots)  # Places ASCII char in usercoords
            turn += 1  # Progress
            print(self)
        if playernum == 1:
            winners_moves = player1_moves
        else:
            winners_moves = player2_moves
        return self.winner(turns=turns, player=playernum, winners_moves=winners_moves)  # Returns win report at end


def main():
    """
    Driver code
    """

    quarto = Quarto(4)
    quarto.play()


if __name__ == "__main__":
    main()
