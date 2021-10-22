from rook import Rook
from pawn import Pawn
from bishop import Bishop
from queen import Queen
from knight import Knight
from king import King
from utils.coordinates_mapper import COORDINATE_MAPPER_X, COORDINATE_MAPPER_Y

class Chessboard:
    #TODO - Implement checkmate
    #TODO - Implement stalemate

    def __init__(self):
        self.chessboard = [
            [0 for i in range(8)] for i in range(8)
        ]
        self.initial_setup()
        #Update the threatening position of every piece and the overall threatens of the player
        for y in range(len(self.chessboard)):
            for x in range(len(self.chessboard[y])):
                if self.chessboard[y][x]:
                    self.chessboard[y][x].refresh_possible_moves()


        self.moves_count = 0
        self.moves_log = {"turn": "white"}
        #{int : {'w': str, 'b': str}}

        self.black_threatens = self.get_all_threatened_squares(threatening='black')
        self.white_threatens = self.get_all_threatened_squares(threatening='white')


    def __repr__(self):
        res = ''
        for y in range(len(self.chessboard)):
            for x in range(len(self.chessboard[y])):
                res += f'{self.chessboard[y][x]}\t'
            res += '\n'
        return res

    def refresh_all_possible_moves(self):
        for y in range(len(self.chessboard)):
            for x in range(len(self.chessboard[y])):
                if self.chessboard[y][x]:
                    self.chessboard[y][x].refresh_possible_moves()


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
            for x in [2,5]:
                self.chessboard[y][x] = \
                    Bishop(position=(y,x), color='white', Chessboard=self) if y else \
                    Bishop(position=(y,x), color='black', Chessboard=self)

        for y in [0,7]:
            self.chessboard[y][3] = \
                Queen(position=(y, 3), color='white', Chessboard=self) if y else \
                Queen(position=(y, 3), color='black', Chessboard=self)

        for y in [0,7]:
            for x in [1,6]:
                self.chessboard[y][x] = \
                    Knight(position=(y,x), color='white', Chessboard=self) if y else \
                    Knight(position=(y,x), color='black', Chessboard=self)

        for y in [0,7]:
            self.chessboard[y][4] = \
                King(position=(y, 4), color='white', Chessboard=self) if y else \
                King(position=(y, 4), color='black', Chessboard=self)

    def referee_controls(self, color: str, move_from: tuple, move_to: tuple):
        if self.moves_log['turn'] != color:
            raise Exception(f'It is {self.moves_log["turn"]}\'s turn to play')
        else:
            self.moves_log[self.moves_count] = self.record_move(move_from, move_to)
            self.moves_count += 1
            self.moves_log['turn'] = 'white' if self.moves_log['turn'] == 'black' else 'black'

    def record_move(self, square_1, square_2):
        return {'piece_from': self.chessboard[square_1[0]][square_1[1]].piece_name,
                'square_from': square_1,
                'piece_to': self.chessboard[square_2[0]][square_2[1]].piece_name if \
                    self.chessboard[square_2[0]][square_2[1]] else 'nan',
                'square_to': square_2}




    def occupied_squares(self, color: str):
        """Returns the list of occupied squares by a color in the chessboard"""
        return [(y, x) for y in range(len(self.chessboard)) for x in range(len(self.chessboard[y]))\
                if self.chessboard[y][x] if self.chessboard[y][x].color == color]

    def update_threatened_squares(self, piece):
        match piece.color:
            case 'white':
                self.white_threatens = self.get_all_threatened_squares(threatening='white')
            case 'black':
                self.black_threatens = self.get_all_threatened_squares(threatening='black')

    def get_all_threatened_squares(self, threatening: str):
        #Function used especially for kings, since they cannot move to squares which are threatened
        threatened_squares = []

        for y in range(len(self.chessboard)):
            for x in range(len(self.chessboard[y])):
                if self.chessboard[y][x]:
                    threatened_squares.extend(self.chessboard[y][x].attacking_squares) if \
                        self.chessboard[y][x].color == threatening else threatened_squares.extend([])
        return threatened_squares