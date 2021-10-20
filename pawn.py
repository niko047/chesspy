from chesspiece import ChessPiece

class Pawn(ChessPiece):
    #TODO - Handle promotion of the pawn to something else
    #TODO - Handle au passant
    #TODO - Handle double initial move ahead

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'pawn'

    def __repr__(self):
        return 'p'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        :return: (is_move_legal, new_square)
        """

        if new_square in self.attacking_squares:
            self.position = new_square
            self.attacking_squares = self.refresh_possible_moves()
            self.Chessboard.update_threatened_squares(color=self.color)
        else:
            print(f'Move to square {new_square}not possible, handle error')


    def refresh_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A pawn can capture in diagonal bx going up the board for white (and down for black), therefore

        y, x = self.position
        match self.color:
            case 'white':
                #Check that it's not at the borders of the board
                if x == 0:
                    self.attacking_squares = [(y-1, x+1)]
                elif x == 7:
                    self.attacking_squares = [(y-1, x-1)]
                else:
                    self.attacking_squares = [(y-1, x+1), (y-1, x-1)]

            case 'black':
                if y == 0:
                    self.attacking_squares = [(y + 1, x + 1)]
                elif y == 7:
                    self.attacking_squares = [(y + 1, x - 1)]
                else:
                    self.attacking_squares = [(y + 1, x + 1), (y + 1, x - 1)]

