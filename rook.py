from chesspiece import ChessPiece

class Rook(ChessPiece):

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        y,x = position
        self.Chessboard.chessboard[y][x] = self
        self.attacking_squares = self.refresh_possible_moves()

    def __repr__(self):
        return 'R'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        :return: (is_move_legal, new_square)
        """

        if new_square in self.attacking_squares:
            self.position = new_square
            self.attacking_squares = self.refresh_possible_moves()
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
        return attacking_squares
