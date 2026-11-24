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
        return copy.deepcopy(self) # not copy.copy() aka shallow copy [explained later]
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


#====UNDERSTAND SHALLOW AND DEEP COPY=========

list1 = [1, 4, 5, 2, [65,43,21,54], 99, 76, 54]
#index = 0  1  2  3   4  4  4  4     5   6   7

list2 = copy.copy(list1)

list2[4][1] = 1000

print(f"list 1 = {list1}")
print(f"list 2 = {list2}")
# list 1 = [1, 4, 5, 2, [65, 1000, 21, 54], 99, 76, 54]
# list 2 = [1, 4, 5, 2, [65, 1000, 21, 54], 99, 76, 54]

print(id(list1[4]))     # 2114737993984
print(id(list2[4]))     # 2114737993984
# Same Address ID.

"""
As you can see we only made changes in list 2's 4's 1st index 
but the change appears in list 1 as well.

This is known as shallow copy. [.copy()]
Meaning on 1st level of list, the addresses of indexes 0 to 3 then 5 to 7 will be different in list 2.
But, the addresses of all index 4 elements which are a list will be copied as same. 
So if you make changes in a list 2's index 4's elements, they'll reflect on the original list1.

Hence we use [.deepcopy()]
This method makes addresse changes one all levels of every nested data structure while copying.
Hence produces a true clone with data being same, structure being same but different addresses.
Thus .deepcopy() doesn't affect the original.
"""

list3 = copy.deepcopy(list1)

list3[4][1] = 3000

print(f"list 1 = {list1}")
print(f"list 3 = {list3}")
# list 1 = [1, 4, 5, 2, [65, 1000, 21, 54], 99, 76, 54]
# list 3 = [1, 4, 5, 2, [65, 3000, 21, 54], 99, 76, 54]

# Thus we used deepcopy() for the chessboard and chess piece 
# as the changes in the clone such as last added piece 
# "Black Soldier" would have been added in original with shallow copy.
