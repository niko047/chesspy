from chesspiece import ChessPiece
from utils.coordinates_mapper import COORDINATE_MAPPER_X

class Pawn(ChessPiece):

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        self.attacking_squares = []
        self.piece_name = 'pawn'
        self.algebraic_notation = COORDINATE_MAPPER_X[position[1]]
        self.en_passant_enabled = False

    def __repr__(self):
        return 'p'

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        :return: (is_move_legal, new_square)
        """

        if new_square in self.attacking_squares :
            self.Chessboard.referee_controls(color=self.color,
                                             move_from=self.position,
                                             move_to=new_square)

            old_y, old_x = self.position
            new_y, new_x = new_square

            #I need to know if last move was au-passantable
            is_last_move_au_passantable = self.Chessboard.moves_count - 1 in self.Chessboard.en_passantable_pawns
            if is_last_move_au_passantable:
                passant_y, passant_x = self.Chessboard.en_passantable_pawns[self.Chessboard.moves_count - 1]\
                    .get('move_to')
                #If this pawn is next to the pawn that made the 2 moves ahead, y does not change, x does +- 1
                if new_x == passant_x:
                    #Right side of the passant, remove the black passant pawn and move white pawn there
                    self.Chessboard.chessboard[passant_y][passant_x] = 0

            self.Chessboard.chessboard[old_y][old_x] = 0
            self.Chessboard.chessboard[new_y][new_x] = self
            self.position = new_square

            if abs(new_y - old_y) == 2:
                self.Chessboard.en_passantable_pawns[self.Chessboard.moves_count] = {'move_to': new_square}


            #Updates the algebraic notation
            self.Chessboard.refresh_all_possible_moves()
        else:
            print(f'Move to square {new_square}not possible, handle error')

    def refresh_possible_moves(self):
        attacking_squares = []
        y, x = self.position
        match self.color:
            case 'white':
                #Speaking moving forward
                opponent_pieces_positions = self.Chessboard.occupied_squares(color='black')

                if self.position[0] == 6:
                    attacking_squares.extend([(self.position[0] - 1, self.position[1])]) if not (self.position[0] - 1, self.position[1]) \
                        in opponent_pieces_positions else None
                    attacking_squares.extend([(self.position[0] - 2, self.position[1])]) if not (self.position[0] - 2, self.position[1]) \
                        in opponent_pieces_positions else None
                elif self.position[0] > 0:
                    attacking_squares.extend([(self.position[0] - 1, self.position[1])]) if not (self.position[0] - 1, self.position[1]) \
                        in opponent_pieces_positions else None



                en_passant_move = self.Chessboard.moves_count  in self.Chessboard.en_passantable_pawns
                if en_passant_move:
                    en_passant_move = self.Chessboard.en_passantable_pawns[self.Chessboard.moves_count ]

                    if en_passant_move.get('move_to') == (self.position[0], self.position[1] - 1):
                        # can capture in sx
                        attacking_squares.extend([(self.position[0] - 1, self.position[1] - 1)])

                    elif en_passant_move.get('move_to') == (self.position[0], self.position[1] + 1):
                        # can capture in dx
                        attacking_squares.extend([(self.position[0] - 1, self.position[1] + 1)])

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
                opponent_pieces_positions = self.Chessboard.occupied_squares(color='white')

                if self.position[0] == 1:
                    attacking_squares.extend([(self.position[0] + 1, self.position[1])])if not (self.position[0] + 1, self.position[1]) \
                        in opponent_pieces_positions else None
                    attacking_squares.extend([(self.position[0] + 2, self.position[1])])if not (self.position[0] + 2, self.position[1]) \
                        in opponent_pieces_positions else None
                elif self.position[0] < 7:
                    attacking_squares.extend([(self.position[0] + 1, self.position[1])])if not (self.position[0] + 1, self.position[1]) \
                        in opponent_pieces_positions else None



                #Check if last move was en passant
                en_passant_move = self.Chessboard.moves_count  in self.Chessboard.en_passantable_pawns
                if en_passant_move:
                    en_passant_move = self.Chessboard.en_passantable_pawns[self.Chessboard.moves_count ]

                    if en_passant_move.get('move_to') == (self.position[0], self.position[1]+1):
                        attacking_squares.extend([(self.position[0] + 1, self.position[1] + 1)])

                    elif en_passant_move.get('move_to') == (self.position[0], self.position[1]-1):
                        #can capture in sx
                        attacking_squares.extend([(self.position[0] + 1, self.position[1] - 1)])

                c1 = (y + 1, x + 1) in opponent_pieces_positions
                c2 = (y + 1, x - 1) in opponent_pieces_positions

                if c1 and c2:
                    attacking_squares.extend([(y + 1, x + 1), (y + 1, x - 1)])
                elif c1:
                    attacking_squares.extend([(y + 1, x + 1)])
                elif c2:
                    attacking_squares.extend([(y + 1, x - 1)])


        self.attacking_squares = attacking_squares

