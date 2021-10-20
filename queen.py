from chesspiece import ChessPiece

class Queen(ChessPiece):

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'queen'
        self.algebraic_notation = 'Q'

    def __repr__(self):
        return 'Q'

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

        attacking_squares = []

        #Does Bishop stuff
        new_square = [y, x]
        for mode in ['updx', 'dodx', 'dosx', 'upsx']:

            while 0 <= new_square[0] <= 7 and 0 <= new_square[1] <= 7:
                if new_square[0] == y and new_square[1] == x:
                    pass
                elif not self.Chessboard.chessboard[new_square[0]][new_square[1]]:
                    attacking_squares.append((new_square[0], new_square[1]))
                elif self.Chessboard.chessboard[new_square[0]][new_square[1]].color != self.color:
                    attacking_squares.append((new_square[0], new_square[1]))
                    break
                else:
                    break
                match mode:
                    case 'updx':
                        new_square[0] += 1
                        new_square[1] += 1
                    case 'dodx':
                        new_square[0] += 1
                        new_square[1] -= 1
                    case 'dosx':
                        new_square[0] -= 1
                        new_square[1] -= 1
                    case 'upsx':
                        new_square[0] -= 1
                        new_square[1] += 1
            new_square = [y, x]
        #Does Rook stuff
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