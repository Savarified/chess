import os
pieces = []
moves = 0
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

            self.x = position[0]
            self.y = position[1]
            return True
        return False

class Queen():
    def __init__(self, x, y, color, captured, type):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured
        self.type = type

    def move(self, position):
        onAxis = not (self.x != position[0] and self.y != position[1])
        diagonal = abs(self.x - position[0]) == abs(self.y - position[1])

        if not onAxis and not diagonal:
            return False

        if board.exists(position):
            temp_piece = board.findPiece(position)
            temp_piece.captured = True
            temp_piece.x = -1
        self.x = position[0]
        self.y = position[1]
        return True

class Rook():
    def __init__(self, x, y, color, captured, type):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured
        self.type = type

    def move(self, position):
        if self.x != position[0] and self.y != position[1]:
            return False
        if board.exists(position):
            temp_piece = board.findPiece(position)
            temp_piece.captured = True
            temp_piece.x = -1

        self.x = position[0]
        self.y = position[1]
        return True

class Bishop():
    def __init__(self, x, y, color, captured, type):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured
        self.type = type

    def move(self, position):
        if abs(self.x - position[0]) != abs(self.y - position[1]):
            return False

        if board.exists(position):
            temp_piece = board.findPiece(position)
            temp_piece.captured = True
            temp_piece.x = -1

        self.x = position[0]
        self.y = position[1]
        return True

class Knight():
    def __init__(self, x, y, color, captured, type):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured
        self.type = type

    def move(self, position):
        if (abs(self.x-position[0])==1 and abs(self.y-position[1])==2) or (abs(self.x-position[0])==2 and abs(self.y-position[1])==1):
            print(abs(self.x - position[0]))
            if board.exists(position):
                temp_piece = board.findPiece(position)
                temp_piece.captured = True
                temp_piece.x = -1

            self.x = position[0]
            self.y = position[1]
            return True
        else:
            return False

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

'''
K   Q   R   B   N   P
♔	♕	♖	♗	♘	♙
♚	♛	♜	♝	♞	♟

'''

def initializeBoard():
    pieces.append(Rook(0, 7, 'black', False, '♖'))
    pieces.append(Knight(1,7, 'black', False, '♘'))
    pieces.append(Bishop(2, 7, 'black', False, '♗'))
    pieces.append(King(3,7, 'black', False, '♔'))
    pieces.append(Queen(4, 7, 'black', False, '♕'))
    pieces.append(Bishop(5, 7, 'black', False, '♗'))
    pieces.append(Knight(6,7, 'black', False, '♘'))
    pieces.append(Rook(7, 7, 'black', False, '♖'))

    for x in range(8):
        pieces.append(Pawn(x, 6, 'black', False, '♙'))


    pieces.append(Rook(0, 0, 'white', False, '♜'))
    pieces.append(Knight(1,0, 'white', False, '♞'))
    pieces.append(Bishop(2, 0, 'white', False, '♝'))
    pieces.append(King(3,0, 'white', False, '♚'))
    pieces.append(Queen(4, 0, 'white', False, '♛'))
    pieces.append(Bishop(5, 0, 'white', False, '♝'))
    pieces.append(Knight(6,0, 'white', False, '♞'))
    pieces.append(Rook(7, 0, 'white', False, '♜'))

    for x in range(8):
        pieces.append(Pawn(x, 1, 'white', False, '♟'))

def drawBoard():
    print('  _ _ _ _ _ _ _ _')
    ys = list(range(board.height))
    ys.sort(reverse=True)
    for y in ys:
        line = ''
        line += str(y+1) + '|'
        for x in range(board.width):
            found = False
            for piece in pieces:
                if [piece.x, piece.y] == [x,y]:
                    line+=piece.type + '|'
                    found = True
            if not found:
                if board.isBlack([x,y]):
                    line+='#|'
                else:
                    line+='_|'
        print(line)
    print('  A B C D E F G H')

def actionBoard():
    invalid = True
    while invalid:
        move = input('>')
        if 'q' in move.lower():
            return False
            break
        move = move.split(' ')
        currentPos = [ord(move[0][0].lower()) - ord('a'), int(move[0][1])-1]
        nextPos = [ord(move[1][0].lower()) - ord('a'), int(move[1][1])-1]
        if not board.isValid(currentPos):
            print('^Piece outside board.')
            invalid = True
            continue
        if not board.exists(currentPos):
            print('^Piece does not exist')
            invalid = True
            continue
        if currentPos == nextPos:
            print('^Piece did not move')
            invalid = True
            continue

        if board.exists(nextPos):
            if board.findPiece(nextPos).color == board.findPiece(currentPos).color:
                print(f'^Invalid position: [{chr(nextPos[0]+ord('A'))}, {nextPos[1]+1}] is occupied by a piece of your color')
                invalid = True
                continue

        currentPiece = board.findPiece(currentPos)
        invalid = not currentPiece.move(nextPos)
        if invalid:
            print('^Invalid move.')
    return True

def checkWin():
    for piece in pieces:
        if piece.type == '♚':
            if piece.captured == True:
                return 'White won in ' + str(moves) + ' moves!'
        if piece.type == '♔':
            if piece.captured == True:
                return 'White won in ' + str(moves) + ' moves!'
    return False

initializeBoard()
run = True
while run:
    moves += 1
    os.system('clear')
    drawBoard()
    if not actionBoard():
        run = False
    if checkWin() != False:
        os.system('clear')
        print(checkWin())
        drawBoard()
        run = False



