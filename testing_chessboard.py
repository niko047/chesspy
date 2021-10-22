from chessboard import Chessboard

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



#Tests for en passant
c.chessboard[6][1].move((4,1))
c.chessboard[1][2].move((3,2))
c.chessboard[4][1].move((3,1))
c.chessboard[1][0].move((3,0))
c.chessboard[3][1].attacking_squares
c.en_passantable_pawns
c.chessboard[3][1].move((2,0))