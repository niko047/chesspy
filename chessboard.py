
class ChessPiece:
    def __init__(self, position, color, Chessboard):
        self.position = position
        self.color = color
        self.Chessboard = Chessboard

class Chessboard:
    #Size is going to be 8x8, but indexes will range from 0 to 7

    def __init__(self):
        self.chessboard = [
            [0 for i in range(8)] for i in range(8)
        ]

    def initial_setup(self):
        """
        Creates the initial setup of a chessboard, where each piece has the classical position.
        """
        #Sets up the pawns in the chesssboard
        for x in range(8):
            for y in [1, 6]:
                self.chessboard[x][y] = \
                    Pawn(position=(x, y), color='white', Chessboard=self) if y == 1 else \
                    Pawn(position=(x, y), color='black', Chessboard=self)
        for x in [0,7]:
            for y in [0,7]:
                self.chessboard[x][y] = \
                    Rook(position=(x,y), color='white', Chessboard=self) if not y else \
                    Rook(position=(x,y), color='black', Chessboard=self)


    def is_legal_move(self, move: tuple, color: str) -> bool:
        """
        Checks whether a move is valid or not.
        Does not check for piece-specific moves, just for two general rules:
        1. New move needs to be inside chessboard boundaries
        2. No overlapping between same color pieces in the chessboard
        """
        x, y = move
        if not 0 <= x <= 7 or not 0 <= y <= 7:
            return False
        if self.chessboard[x][y].color == color:
            return False
        return True

    def occupied_squares(self):
        """Returns the list of occupied squares in the chessboard"""
        return [(x, y) for x in self.chessboard for y in x if self.chessboard[x][y]]



class Pawn(ChessPiece):
    #TODO - Handle promotion of the pawn to something else
    #TODO - Handle au passant
    #TODO - Handle double initial move ahead

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        x,y = position
        self.Chessboard.chessboard[x][y] = self
        self.attacking_squares = self.refresh_possible_moves()

    def move(self, new_square: tuple):
        """
        :param new_square: New square where the piece is supposed to go
        :return: (is_move_legal, new_square)
        """

        if new_square in self.possible_moves:
            self.position = new_square
            self.attacking_squares = self.refresh_possible_moves()
        else:
            print(f'Move to square {new_square}not possible, handle error')


    def refresh_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A pawn can capture in diagonal by going up the board for white (and down for black), therefore

        x, y = self.position
        match self.color:
            case 'white':
                #Check that it's not at the borders of the board
                if x == 0:
                    self.attacking_squares = [(x+1, y+1)]
                elif x == 7:
                    self.attacking_squares = [(x-1, y+1)]
                else:
                    self.attacking_squares = [(x+1, y+1), (x-1, y+1)]

            case 'black':
                if x == 0:
                    self.attacking_squares = [(x + 1, y - 1)]
                elif x == 7:
                    self.attacking_squares = [(x - 1, y - 1)]
                else:
                    self.attacking_squares = [(x + 1, y - 1), (x - 1, y - 1)]


class Rook(ChessPiece):

    def __init__(self, position: tuple, color: str, Chessboard) -> None:
        super().__init__(position=position,
                         color=color,
                         Chessboard=Chessboard)
        x,y = position
        self.Chessboard.chessboard[x][y] = self
        self.attacking_squares = self.refresh_possible_moves()



    def refresh_possible_moves(self) -> list:
        #Going to be a function of the position in the board
        #A rook can travel all the line until it meets some ther piece, and can always eat that
        x, y = self.position

        #Get all possible squares, then restrict them to the squares where it can go
        #It's a stupid approach as of now, update it later
        attacking_squares = []
        for hdx in range(x+1, 8):
            if not self.Chessboard.chessboard[hdx][y]:
                attacking_squares.append((hdx, y))
            elif self.Chessboard.chessboard[hdx][y].color != self.color:
                attacking_squares.append((hdx, y))
                break
            else:
                break
        for hsx in range(x-1, -1, -1):
            if not self.Chessboard.chessboard[hsx][y]:
                attacking_squares.append((hsx, y))
            elif self.Chessboard.chessboard[hsx][y].color != self.color:
                attacking_squares.append((hsx, y))
                break
            else:
                break
        for vup in range(y+1, 8):
            if not self.Chessboard.chessboard[x][vup]:
                attacking_squares.append((x, vup))
            elif self.Chessboard.chessboard[x][vup].color != self.color:
                attacking_squares.append((x, vup))
                break
            else:
                break
        for vdo in range(y-1, -1, -1):
            if not self.Chessboard.chessboard[x][vdo]:
                attacking_squares.append((x, vdo))
            elif self.Chessboard.chessboard[x][vdo].color != self.color:
                attacking_squares.append((x, vdo))
                break
            else:
                break
        return attacking_squares












