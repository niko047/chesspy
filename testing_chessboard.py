from chessboard import *
from pawn import Pawn

c = Chessboard()
r = Rook(position=(5,5), color='white',Chessboard=c)
p1 = Pawn(position=(5,3), color='white', Chessboard=c)
p2 = Pawn(position=(3,5), color='black', Chessboard=c)



from chessboard import Chessboard
from pawn import Pawn
from bishop import Bishop
c = Chessboard()
b = Bishop(position=(3,5), color='white', Chessboard=c)
p = Pawn(position=(4,4), color='white', Chessboard=c)
b.refresh_possible_moves()
b.attacking_squares