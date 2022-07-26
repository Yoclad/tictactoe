# Stephan McGlashan
# CS3 tictactoe/quarto


class Board:  # Main game

    def __init__(self, dim):
        """
        Initializes a 'dim' by 'dim' board
        Uses generators to initialize spots on virtual board.
        """

        # self.playernumber = playernumber, True
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
        Checks to see if group of three exists in
        row / column / diagonal
        """

        Mdiagonallist = []  # Creating diagonal lists prior to appendage
        mdiagonallist = []
        # Checks if full row of same token has been played using set length of row
        for i in range(self.dim):
            rowlist = self.board[i]  # Creates row element
            if len(set(rowlist)) == 1 and " " not in rowlist:  # Checks to see if all values are the same token
                return True
            columnlist = [self.board[j][i] for j in range(self.dim)]
            if len(set(columnlist)) == 1 and " " not in columnlist:
                return True
            Mdiagonallist.append(self.board[i][i])
            mdiagonallist.append(self.board[i][(self.dim - 1) - i])
        if (len(set(Mdiagonallist)) == 1 and " " not in Mdiagonallist) or (
                len(set(mdiagonallist)) == 1 and " " not in mdiagonallist):
            return True

    def winner(self, playernumber):
        """
        Checks match conditions, if a winner arises
        ends match loop and announces victory
        """

        if not self.groupcheck():  # Checks to see if a row / column / diagonal win condition has been met
            return playernumber, False
        else:
            print("Congratulations! Player:", str(playernumber[1]), "has won!")
            return playernumber, True  # Will end game loop

    def updateboard(self, playernumber, usercoords, spots):
        """
        Players token in correct spot
        """

        if playernumber[0]:  # Uses boolean value in playernumber to determine turn
            token = "x"
        else:
            token = "o"
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

        playernumber = (True, "1")
        usercoords = [self.dim, self.dim]
        turn = 0
        while not (self.winner(playernumber)[1]):  # Main game loop
            if turn % 2 == 0:
                playernumber = (True, "1")  # Player 1 / "x" plays on even iterations
            else:
                playernumber = (False, "2")
            usercoords[0] = int(input("Player " + playernumber[1] + " Enter Y coordinate: "))
            usercoords[1] = int(input("Player " + playernumber[1] + " Enter X coordinate: "))  # Main inputs
            if not self.legality(usercoords,
                                 self.spots):  # If move played is illegal, turn is not counted and player is given help
                print("Your input was invalid, idiot, available coords are " + str(self.spots))
            else:
                self.updateboard(playernumber, usercoords, spots=self.spots)
                turn += 1  # Progress
            print(Quarto)
        return self.winner(playernumber)


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
