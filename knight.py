from chesspiece import ChessPiece
import itertools

class Knight(ChessPiece):
    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'knight'

    def __repr__(self):
        return 'K'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        """

        if new_square in self.attacking_squares:
            self.position = new_square
            self.attacking_squares = self.refresh_possible_moves()
            self.Chessboard.update_threatened_squares(color=self.color)
        else:
            print(f'Move to square {new_square}not possible, handle error')

    def refresh_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A rook can travel all the line until it meets some ther piece, and can alwaxs eat that
        y, x = self.position

        attacking_squares = []

        #Combinatorics problem, need to get all 2x2 permutations of (-2, -1, 1, 2) if their abs sum == 3
        knight_range = list(filter(lambda x: abs(x[0]) + abs(x[1]) == 3, itertools.permutations([-2, -1, 1, 2], 2)))
        for kr in knight_range:
            kry, krx = y + kr[0], x + kr[1]
            if 0 <= kry <= 7 and 0 <= krx <= 7:
                if not self.Chessboard.chessboard[kry][krx]:
                    attacking_squares.append((kry, krx))
                elif self.Chessboard.chessboard[kry][krx].color != self.color:
                    attacking_squares.append((kry, krx))
                    continue
                else:
                    continue
        self.attacking_squares = attacking_squares