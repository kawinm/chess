import string
from functions import *

a = [[' ','1','2','3','4','5','6','7','8'],['1','R','P',' ',' ',' ',' ','p','r'],['2','N','P',' ',' ',' ',' ','p','n'],['3','B','P',' ',' ',' ',' ','p','b'],['4','Q','P',' ',' ',' ',' ','p','q'],['5','K','P',' ',' ',' ',' ','p','k'],['6','B','P',' ',' ',' ',' ','p','b'],['7','N','P',' ',' ',' ',' ','p','n'],['8','R','P',' ',' ',' ',' ','p','r']]

class pieces:
    def __init__(self, max_x, max_y, power):
        self.max_x = max_x
        self.max_y = max_y
        self.power = power

    def max_x(self):
        return self.max_x

    def max_y(self):
        return self.max_y

    def power(self):
        return self.power

k = pieces(1,1,10)
q = pieces(8,8,10)
b = pieces(8,8,4)
n = pieces(1,2,4)
p = pieces(1,1,1)
r = pieces(8,8,7)

ch = 1
player = 1
while ch == 1:
    printBoard(a)
    print("Turn of Player ",player)
    ch = input("Enter the character: ")
    if ch == 'k' or ch == 'K':
        char = k
    elif ch == 'q' or ch == 'Q':
        char = q
    elif ch == 'b' or ch == 'B':
        char = b
    elif ch == 'n' or ch == 'N':
        char = n
    elif ch == 'p' or ch == 'P':
        char = p
    elif ch == 'r' or ch == 'R':
        char = r
    pos = input("Enter the position: ")
    chn = input("Enter the position to change: ")
    if checkPlayer(ch, player):
        if checkCharacter(ch,pos,a):
            x1, y1 = int(pos[0]), int(pos[1])
            x2, y2 = int(chn[0]), int(chn[1])
            if checkMove(a,ch, char.max_x, char.max_y, abs(x2-x1), abs(y2-y1), x1,y1,x2,y2):
                a[x1][y1], a[x2][y2] = ' ', a[x1][y1]
                player = (player %2) +1
            else:
                print("invalid move")
        else:
            print("That piece is not on that position")
    else:
        print("It is the other player's turn")
    print("\n\n")
    ch = 1