from pawn import Pawn
class ChessPiece:
    def __init__(self, position, color, Chessboard):
        self.position = position
        self.color = color
        self.Chessboard = Chessboard

class Chessboard:
    #Size is going to be 8x8, but indexes will range from 0 to 7

    def __init__(self):
        self.chessboard = [
            #Creates the row of white pawns
            *[Pawn(position=(i, 1), color='white', Chessboard=self) for i in range(0,8)],
            #Creates the row of black pawns
            *[Pawn(position=(i, 7), color='black', Chessboard=self) for i in range(0,8)],
    ]

    def occupied_squares(self):
        """Returns the list of occupied squares in the chessboard"""
        return [(piece.position, piece.color) for piece in self.chessboard]

