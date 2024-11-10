import os
pieces = []

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def exists(self, position):
        for piece in pieces:
            if position == [piece.x, piece.y]:
                return True
        return False

    def findPiece(self, position):
        for piece in pieces:
            if position == [piece.x, piece.y]:
                return piece
        return False

    def isValid(self, position):
        if 0 <= position[0] < self.width and 0 <= position[1] < self.height:
            return True
        return False

    def isBlack(self, position):
        if position[1]%2!=0:
            if position[0]%2!=0:
                return True
            else:
                return False
        else:
            if position[0]%2!=0:
                return False
            else:
                return True

board = Board(8,8)

'''
K   Q   R   B   N   P
♔	♕	♖	♗	♘	♙
♚	♛	♜	♝	♞	♟

'''
class Pawn():
    def __init__(self, x, y, color, captured, type):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured
        self.type = type

    def move(self, position):
        if self.color == 'white':
            front = self.y+1
        else:
            front = self.y-1
        if abs(self.x-position[0]) == 1 and position[1] == front:
            if board.exists(position):
                if board.findPiece(position).color == self.color:
                    print(f'^Invalid position: [{chr(position[0]+ord('A')-1)}, {position[1]}] is occupied by a piece of your color')
                    return False
                else:
                    temp_piece = board.findPiece(position)
                    temp_piece.captured = True
                    temp_piece.x = -1

                    self.x = position[0]
                    self.y = position[1]
                    return True

        if board.isValid(position) and position[1] == front and position[0] == self.x:
            if not board.exists(position):
                self.x = position[0]
                self.y = position[1]
                return True

class King():
    def __init__(self, x, y, color, captured, type):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured
        self.type = type

    def move(position):
        if abs(self.x - position[0]) <= 1 and abs(self.y - position[1]) <= 1:
            if board.exists(position):
                temp_piece = board.findPiece(position)
                temp_piece.captured = True
                temp_piece.x = -1

            if board.isValid(position):
                self.x = position[0]
                self.y = position[1]
                return True
        return False

def initializeBoard():
    pieces.append(Pawn(0,0,'white', False, '♟'))
    pieces.append(Pawn(1,1,'white', False, '♟'))
    pieces.append(Pawn(7,7,'black', False, '♙'))


def drawBoard():
    ys = list(range(board.height))
    ys.sort(reverse=True)
    for y in ys:
        line = ''
        for x in range(board.width):
            found = False
            for piece in pieces:
                if [piece.x, piece.y] == [x,y]:
                    line+=piece.type + ' '
                    found = True
            if not found:
                if board.isBlack([x,y]):
                    line+='# '
                else:
                    line+='_ '
        print(line)

def actionBoard():
    invalid = True
    while invalid:
        move = input('>')
        if 'q' in move:
            return False
            break
        move = move.split(' ')
        currentPos = [ord(move[0][0].lower()) - ord('a'), int(move[0][1])-1]
        nextPos = [ord(move[1][0].lower()) - ord('a'), int(move[1][1])-1]
        if board.exists(currentPos):
            currentPiece = board.findPiece(currentPos)
        invalid = not currentPiece.move(nextPos)
    return True

initializeBoard()
run = True
while run:
    os.system('clear')
    drawBoard()
    if not actionBoard():
        run = False
        break
