from chesspiece import ChessPiece

class Rook(ChessPiece):

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'rook'
        self.algebraic_notation = 'R'

    def __repr__(self):
        return 'R'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        """

        if new_square in self.attacking_squares:
            old_y, old_x = self.position
            new_y, new_x = new_square
            self.Chessboard.chessboard[old_y][old_x] = 0
            self.Chessboard.chessboard[new_y][new_x] = self

            self.position = new_square
            self.Chessboard.refresh_all_possible_moves()
        else:
            print(f'Move to square {new_square}not possible, handle error')

    def refresh_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A rook can travel all the line until it meets some ther piece, and can alwaxs eat that
        y, x = self.position

        #Get all possible squares, then restrict them to the squares where it can go
        #It's a stupid approach as of now, update it later
        attacking_squares = []
        for hdy in range(y+1, 8):
            if not self.Chessboard.chessboard[hdy][x]:
                attacking_squares.append((hdy, x))
            elif self.Chessboard.chessboard[hdy][x].color != self.color:
                attacking_squares.append((hdy, x))
                break
            else:
                break
        for hsy in range(y-1, -1, -1):
            if not self.Chessboard.chessboard[hsy][x]:
                attacking_squares.append((hsy, x))
            elif self.Chessboard.chessboard[hsy][x].color != self.color:
                attacking_squares.append((hsy, x))
                break
            else:
                break
        for vup in range(x+1, 8):
            if not self.Chessboard.chessboard[y][vup]:
                attacking_squares.append((y, vup))
            elif self.Chessboard.chessboard[y][vup].color != self.color:
                attacking_squares.append((y, vup))
                break
            else:
                break
        for vdo in range(x-1, -1, -1):
            if not self.Chessboard.chessboard[y][vdo]:
                attacking_squares.append((y, vdo))
            elif self.Chessboard.chessboard[y][vdo].color != self.color:
                attacking_squares.append((y, vdo))
                break
            else:
                break
        self.attacking_squares = attacking_squares
