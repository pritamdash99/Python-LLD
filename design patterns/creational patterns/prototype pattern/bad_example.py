
class ChessPiece:
    def __init__(self, pieceName : str, position : str, color : str) -> None:
        self.pieceName = pieceName
        self.position = position
        self.color = color

    def display(self):
        return f"{self.color} {self.pieceName} is at {self.position}"

class ChessBoard:
    def __init__(self) -> None:
        #The list contains all chess pieces, at first it's obviously blank.
        self.pieces : list[ChessPiece] = []

    def addPiece(self, piece : ChessPiece):
        self.pieces.append(piece)

    def displayBoard(self):
        print("Board State")
        for piece in self.pieces:
            print(f"{   piece.display()}")

piece1 = ChessPiece("King","e2","Black")
piece2 = ChessPiece("Queen","a1","Black")
piece3 = ChessPiece("King","c3","White")
piece4 = ChessPiece("Queen","d2","White")

chessBoard = ChessBoard()
chessBoard.addPiece(piece1)
chessBoard.addPiece(piece2)
chessBoard.addPiece(piece3)
chessBoard.addPiece(piece4)
chessBoard.displayBoard()
"""
Board State
Black King is at e2
Black Queen is at a1
White King is at c3
White Queen is at d2
"""

# Now if we're asked to create a checkpoint for our board to save this exact board position, how to do it?
# We can create a new chess board and use .addPiece() to add pieces to exact same locations.

new_chessBoard = ChessBoard()
for p in chessBoard.pieces:
    new_chessBoard.addPiece(p)

print("============")
new_chessBoard.displayBoard()
"""
Board State
Black King is at e2
Black Queen is at a1
White King is at c3
White Queen is at d2
"""

# Now if you want to make changes or add new pieces you make them in new_chessBoard from this point forward.
