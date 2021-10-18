from chessboard import ChessPiece

class Rook(ChessPiece):

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.possible_moves = self.get_possible_moves()


    def get_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A rook can travel all the line until it meets some ther piece, and can always eat that
        x, y = self.position

        #Get all possible squares, then restrict them to the squares where it can go
        vertical_moves = [(x, i) for i in range(0,7) if i != y]
        horizontal_moves = [(i, y) for i in range(0,7) if i != x]

        #Get the occupied squares in the range of the rook
        occupied_squares_same_direction = [p for p in self.Chessboard.occupied_squares() if p[0] == x or p[1] == y]

        #Now get out the squares that are behind the opposite color pieces
        #And the same color pieces and after those


        vertical_up = 7-y
        vertical_down = y
        horizontal_right = 7-x
        horizontal_left = x










