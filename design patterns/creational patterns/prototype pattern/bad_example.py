
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
"""
ISSUE - 
1. A lot of manual copying is happening -> Error Prone Code
2. We're making the clone manually outside class, it should happen inside the ChessBoard Class.
3. The copying of chess pieces is currently manual, should be handled by ChessPiece class.

Responsibilities per class isn't well defined.

Solution - 

The Prototype Pattern is perfect for board games 
    when you need to save the current game state 
    (including where all the pieces are positioned)
    for features like - 
        Undo / Redo, 
        save points, or
        creating a copy of the board for new player.

Each chess piece has its own clone method, 
    which means the entire board can be easily copied along with all the pieces 
    in their current poistions by just 1 simple command instead of manually copying everything.
"""