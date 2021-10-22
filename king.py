from chesspiece import ChessPiece
import itertools

class King(ChessPiece):

    #TODO - Handle checks

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'king'
        self.algebraic_notation = 'K'

    def __repr__(self):
        return 'KG'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        """

        match self.color:
            case 'white':
                if new_square in self.attacking_squares and new_square not in self.Chessboard.white_threatens:
                    self.Chessboard.referee_controls(color=self.color,
                                                     move_from=self.position,
                                                     move_to=new_square)

                    old_y, old_x = self.position
                    new_y, new_x = new_square
                    self.Chessboard.chessboard[old_y][old_x] = 0
                    self.Chessboard.chessboard[new_y][new_x] = self

                    self.position = new_square
                    self.Chessboard.refresh_all_possible_moves()
                else:
                    print(f'Move to square {new_square}not possible, handle error')
            case 'black':
                if new_square in self.attacking_squares and new_square not in self.Chessboard.black_threatens:
                    self.Chessboard.referee_controls(color=self.color,
                                                     move_from=self.position,
                                                     move_to=new_square)

                    old_y, old_x = self.position
                    new_y, new_x = new_square
                    self.Chessboard.chessboard[old_y][old_x] = 0
                    self.Chessboard.chessboard[new_y][new_x] = self

                    self.position = new_square
                    self.Chessboard.refresh_all_possible_moves()
                else:
                    print(f'Move to square {new_square}not possible, handle error')


    def refresh_possible_moves(self) -> list:
        #King is different, cannot move to threatened squares
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