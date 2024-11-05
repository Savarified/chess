pieces = []

class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def exists(position):
        for piece in pieces:
            if position == [piece.x, piece.y]:
                return True
    def findPiece(position):
        for piece in pieces:
            if position == [piece.x, piece.y]:
                return piece
        return False

board = Board(8,8)

#p n r b q k
class Pawn():
    def __init__(self, x, y, color, captured):
        self.x = x
        self.y = y
        self.color = color
        self.captured = captured

    def move(position):
        if abs(self.x-position[0]) == 1 and position[1] == self.y+1:
            if not board.exists(position):
                return
            if board.findPiece(position).color == self.color:
                return
            else:
                temp_piece = board.findPiece(position)
                temp_piece.captured = True
                temp_piece.x = -1

                self.x = position[0]
                self.y = position[1]

        if position[1] == self.y+1 and position[0] == self.x:
            if not board.exists(position):
                self.x = position[0]
                self.y = position[1]
