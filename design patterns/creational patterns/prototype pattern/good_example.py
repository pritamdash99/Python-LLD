import copy
class ChessPiece:
    def __init__(self, pieceName : str, position : str, color : str) -> None:
        self.pieceName = pieceName
        self.position = position
        self.color = color

    def display(self):
        return f"{self.color} {self.pieceName} is at {self.position}"

    def clone(self):
        # "return self" this would return the same object again, so same address, 
        # we don't want that as changing piece2(copy) shouldnot change the original piece1
        # we want to save a clone at a different address.
        return copy.deepcopy(self)
        # This will return a new object with all same information at different address.
        # Another way = 
        # return ChessPiece(self.pieceName,self.position,self.color)

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

    def clone(self):
        #Copy the entire board + it's pieces
        # return ChessBoard() doesn't work, returns - a blank chessboard object
        return copy.deepcopy(self)


piece1 = ChessPiece("King","e2","Black")
piece2 = ChessPiece("Queen","a1","Black")
piece3 = ChessPiece("King","c3","White")
piece4 = ChessPiece("Queen","d2","White")

chessBoard = ChessBoard()
print(id(chessBoard))
chessBoard.addPiece(piece1)
chessBoard.addPiece(piece2)
chessBoard.addPiece(piece3)
chessBoard.addPiece(piece4)
chessBoard.displayBoard()

print("================")
newChessBoard = chessBoard.clone()
print(id(newChessBoard))
newChessBoard.addPiece(ChessPiece("Soldier","d7","Black"))
newChessBoard.displayBoard()

"""
2856538971104                       (Object 1)
Board State
Black King is at e2
Black Queen is at a1
White King is at c3
White Queen is at d2
================
2856538838416                       (Object 2)
Board State
Black King is at e2
Black Queen is at a1
White King is at c3
White Queen is at d2
Black Soldier is at d7

Black Soldier only got added in the new board, hence it's a true clone as original is missing that piece.
"""