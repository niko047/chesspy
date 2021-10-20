from chessboard import *

c = Chessboard()

#Check that all the figures in upper rows are black and in lower they are white
for i in c.chessboard[:2]:
    for j in i:
        assert j.color == 'black'
for i in c.chessboard[6:]:
    for j in i:
        assert j.color == 'white'

#Assert that the figures in the first row (except the knight) have no moves available
for i in c.chessboard[0] + c.chessboard[7]:
    if j.piece_name != 'knight':
        assert not j.attacking_squares

from chessboard import *
c = Chessboard()
c.chessboard[1][1].move((3,1))
c.chessboard[6][2].move((4,2))
c.chessboard[4][2].move((3,1))
c.chessboard[1][2].move((2,2))
c.chessboard[2][2].move((3,1))
c.chessboard[0][2].move((2,0))
