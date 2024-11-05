pieces = []
class Board():
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def isValid(position):
    for piece in pieces:
      if position == [piece.x, piece.y]:
        return False
