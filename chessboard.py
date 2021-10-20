from rook import Rook
from pawn import Pawn
from bishop import Bishop
from queen import Queen
from knight import Knight

class Chessboard:

    def __init__(self):
        self.chessboard = [
            [0 for i in range(8)] for i in range(8)
        ]

    def __repr__(self):
        res = ''
        for y in range(len(self.chessboard)):
            for x in range(len(self.chessboard[y])):
                res += f'{self.chessboard[y][x]}\t'
            res += '\n'
        return res


    def initial_setup(self):
        """
        Creates the initial setup of a chessboard, where each piece has the classical position.
        """
        #Sets up the pawns in the chesssboard
        for x in range(8):
            for y in [1, 6]:
                self.chessboard[y][x] = \
                    Pawn(position=(y, x), color='black', Chessboard=self) if y == 1 else \
                    Pawn(position=(y, x), color='white', Chessboard=self)

        for y in [0,7]:
            for x in [0,7]:
                self.chessboard[y][x] = \
                    Rook(position=(y,x), color='white', Chessboard=self) if y else \
                    Rook(position=(y,x), color='black', Chessboard=self)

        for y in [0,7]:
            for x in [1,6]:
                self.chessboard[y][x] = \
                    Bishop(position=(y,x), color='white', Chessboard=self) if y else \
                    Bishop(position=(y,x), color='black', Chessboard=self)

        for y in [0,7]:
            self.chessboard[y][3] = \
                Queen(position=(y, 3), color='white', Chessboard=self) if y else \
                Queen(position=(y, 3), color='black', Chessboard=self)

        for y in [0,7]:
            for x in [1,6]:
                self.chessboard[y][2] = \
                    Knight(position=(y,x), color='white', Chessboard=self) if y else \
                    Knight(position=(y,x), color='black', Chessboard=self)


    def is_legal_move(self, move: tuple, color: str) -> bool:
        """
        Checks whether a move is valid or not.
        Does not check for piece-specific moves, just for two general rules:
        1. New move needs to be inside chessboard boundaries
        2. No overlapping between same color pieces in the chessboard
        """
        y, x = move
        if not 0 <= y <= 7 or not 0 <= x <= 7:
            return False
        if self.chessboard[y][x].color == color:
            return False
        return True

    def occupied_squares(self):
        """Returns the list of occupied squares in the chessboard"""
        return [(y, x) for y in self.chessboard for x in y if self.chessboard[y][x]]














