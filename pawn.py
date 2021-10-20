from chesspiece import ChessPiece
from utils.coordinates_mapper import COORDINATE_MAPPER_X

class Pawn(ChessPiece):
    #TODO - Handle promotion of the pawn to something else
    #TODO - Handle au passant

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'pawn'
        self.algebraic_notation = COORDINATE_MAPPER_X[position[1]]

    def __repr__(self):
        return 'p'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        :return: (is_move_legal, new_square)
        """

        if new_square in self.attacking_squares :
            old_y, old_x = self.position
            new_y, new_x = new_square
            self.Chessboard.chessboard[old_y][old_x] = 0
            self.Chessboard.chessboard[new_y][new_x] = self

            self.position = new_square
            #Updates the algebraic notation
            self.algebraic_notation = COORDINATE_MAPPER_X[self.position[1]]
            self.Chessboard.refresh_all_possible_moves()
        else:
            print(f'Move to square {new_square}not possible, handle error')

    def refresh_possible_moves(self):
        attacking_squares = []
        y, x = self.position
        match self.color:
            case 'white':
                #Speaking moving forward
                if self.position[0] == 6:
                    attacking_squares.extend([(self.position[0] - 1, self.position[1])])
                    attacking_squares.extend([(self.position[0] - 2, self.position[1])])
                elif self.position[0] > 0:
                    attacking_squares.extend([(self.position[0] - 1, self.position[1])])

                opponent_pieces_positions = self.Chessboard.occupied_squares(color='black')
                # Check that it's not at the borders of the board
                c1 = (y - 1, x + 1) in opponent_pieces_positions
                c2 = (y - 1, x - 1) in opponent_pieces_positions

                if c1 and c2:
                    attacking_squares.extend([(y - 1, x + 1), (y - 1, x - 1)])
                elif c2:
                    attacking_squares.extend([(y - 1, x - 1)])
                elif c1:
                    attacking_squares.extend([(y - 1, x + 1)])


            case 'black':
                #Speaking captures of pieces

                if self.position[0] == 1:
                    attacking_squares.extend([(self.position[0] + 1, self.position[1])])
                    attacking_squares.extend([(self.position[0] + 2, self.position[1])])
                elif self.position[0] < 7:
                    attacking_squares.extend([(self.position[0] + 1, self.position[1])])

                opponent_pieces_positions = self.Chessboard.occupied_squares(color='white')

                c1 = (y + 1, x + 1) in opponent_pieces_positions
                c2 = (y + 1, x - 1) in opponent_pieces_positions

                if c1 and c2:
                    attacking_squares.extend([(y + 1, x + 1), (y + 1, x - 1)])
                elif c1:
                    attacking_squares.extend([(y + 1, x + 1)])
                elif c2:
                    attacking_squares.extend([(y + 1, x - 1)])


        self.attacking_squares = attacking_squares

