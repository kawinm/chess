import string

def printBoard(a):
    k = 0
    for i in range(9):
        for j in range(9):
            print(a[j][i]," | ", end='')
        print(end='\n')
        for j in range(44):
            print("_", end='')
        print(end='\n')

def checkKing(a):
    count = 0
    for i in range(1,9):
        for j in range(1,9):
            if a[i][j] == 'a' or a[i][j] == 'A':
                count += 1
    if count == 2:
        return True
    else:
        return False

def checkCharacter(char, pos, a):
    x1, y1 = int(pos[0]), int(pos[1])
    if a[x1][y1] == char:
        return True
    else:
        return False

def checkPlayer(char, player):
    if player == 1:
        if char in string.ascii_lowercase:
            return True
        else:
            return False
    elif player == 2:
        if char in string.ascii_uppercase:
            return True
        else:
            return False

def checkMove(a, ch, maxx, maxy, posx, posy, currentx, currenty, tochangex, tochangey):
    if posx <= maxx and posy <= maxy:
        if ch == 'p' or ch == 'P':
            if posy == 1 and posx == 0:
                return True
            elif a[tochangex][tochangey] != ' ':
                return True
            else:
                return False
        return True
    else:
        return False