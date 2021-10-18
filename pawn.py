from chessboard import ChessPiece

class Pawn(ChessPiece):
    #TODO - Handle promotion of the pawn to something else

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.possible_moves = self.get_possible_moves()

    def move(self, new_square: tuple) -> (bool):
        """
        :param new_square: New square where the piece is supposed to go
        :return: (is_move_legal, new_square)
        """

        if new_square not in self.possible_moves:
            return False
        elif new_square in self.Chessboard.occupied_squares():
            return False
        else:
            #Change the position for the pawn
            self.position = new_square
            self.possible_moves = self.get_possible_moves()
            return True

    def get_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A pawn can capture in diagonal by going up the board for white (and down for black), therefore

        x, y = self.position
        match self.color:
            case 'white':
                #Check that it's not at the borders of the board
                if x == 0:
                    return [(x+1, y+1)]
                elif x == 7:
                    return [(x-1, y+1)]
                else:
                    return [(x+1, y+1), (x-1, y+1)]

            case 'black':
                if x == 0:
                    return [(x + 1, y - 1)]
                elif x == 7:
                    return [(x - 1, y - 1)]
                else:
                    return [(x + 1, y - 1), (x - 1, y - 1)]
