"""Chess Game model."""
from typing import Optional


class Board:
    """Class containing the state of the game board"""
    def __init__(self):
        self._squares = dict()
        self._lastState = dict()

    def get(self, location:str) -> Optional['Piece']:
        return self._squares.get(location, None)

    def getBoard(self):
        return self._squares

    def set(self, location:str, piece: 'Piece', setupFlag:bool = False):
        self._squares[location] = piece
        if not setupFlag:
            self._squares[location].setHasMoved()

    def removePiece(self, location:str):
        self._squares.pop(location)

    def getColor(self, location:str):
        return self._squares.get(location, None).getPieceColor()

    def isOccupied(self, location:str):
        return location in self._squares
    
    def saveBoardState(self):
        self._lastState = self._squares.copy()

    def backupBoard(self):
        self._squares = self._lastState

    def castleQueensideBlack(self):
        self.set('d8', self.get('a8'))
        self.set('c8', self.get('e8'))
        self.removePiece('a8')
        self.removePiece('e8')

    def castleKingsideBlack(self):
        self.set('f8', self.get('h8'))
        self.set('g8', self.get('e8'))
        self.removePiece('h8')
        self.removePiece('e8')

    def castleQueensideWhite(self):
        self.set('d1', self.get('a1'))
        self.set('c1', self.get('e1'))
        self.removePiece('a1')
        self.removePiece('e1')

    def castleKingsideWhite(self):
        self.set('f1', self.get('h1'))
        self.set('g1', self.get('e1'))
        self.removePiece('h1')
        self.removePiece('e1')



class Piece:
    """Abstract base class for chess pieces."""
    def __init__(self, is_white: bool, is_captured: bool, type:str) -> None:
        self._is_white = is_white
        self._is_captured = is_captured
        self._type = type
        self._has_moved = False

    def __hash__(self):
        return hash((type(self), self._is_white))

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)

    def getPieceColor(self):
        return self._is_white
    
    def getType(self):
        return self._type

    def setHasMoved(self):
        self._has_moved = True

    def getHasMoved(self):
        return self._has_moved
    


class Pawn(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured, 'pawn')

class King(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured, 'king')
        has_castled = False

class Queen(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured, 'queen')
        
class Knight(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured, 'knight')

class Bishop(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured, 'bishop')

class Rook(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured, 'rook')



class Game:
    """Class to handle mechanics of game, moving pieces, and validating user move commands"""
    def __init__(self):
        self.board = Board()
        self.white_to_play = True
        self.game_over = False
        self.number_of_moves = 0
        self.has_backedup = False
        self.white_in_check = False
        self.black_in_check = False

    def accept_move(self, move):

        # check if it's checkmate
        if self.isCheckmate():
            self.game_over = True
            print("Checkmate!")

        # make input lowercase to hanlde both cases
        move = move.lower()

        # handle backup command
        if move == 'backup' and self.number_of_moves > 0 and self.has_backedup == False:
            self.board.backupBoard()
            self.number_of_moves -= 1
            self.has_backedup = True
            self.white_to_play = not self.white_to_play
            return
        if move == 'backup' and self.number_of_moves > 0 and self.has_backedup == True:
            print('Error: Can only back up one move')
            return
        if move == 'backup' and self.number_of_moves == 0:
            return
        
        # handle castle move
        # Kingside castle
        if move == 'castlekingside' or move == 'castle kingside' or move == 'castleking' or move == 'castle king':
            CastleValid = self.checkCastleValidity(self.white_to_play, 1)
            # White kingside castle
            if CastleValid and self.white_to_play:
                self.board.castleKingsideWhite()
                self.white_to_play = not self.white_to_play
                return
            # Black kingside castle
            elif CastleValid and not self.white_to_play:
                self.board.castleKingsideBlack()
                self.white_to_play = not self.white_to_play
                return
            # Invalid castle conditions
            elif not CastleValid:
                print('Invalid castle move')
                return
        # Queenside castle
        if move == 'castlequeenside' or move == 'castle queenside' or move == 'castlequeen' or move == 'castle queen':
            CastleValid = self.checkCastleValidity(self.white_to_play, 0)
            # White kingside castle
            if CastleValid and self.white_to_play:
                self.board.castleQueensideWhite()
                self.white_to_play = not self.white_to_play
                return
            # Black kingside castle
            elif CastleValid and not self.white_to_play:
                self.board.castleQueensideBlack()
                self.white_to_play = not self.white_to_play
                return
            # Invalid castle conditions
            elif not CastleValid:
                print('Invalid castle move')
                return

        # source and destination of move
        source = move[0:2]
        destination = move[2:4]

        # input validation
        # non empty
        if len(move) == 0:
            return
        
        # 4 characters long
        if len(move) != 4:
            print('Please enter a move with length 4')
            return
        
        # within bounds of board
        if move[0] not in 'abcdefgh' or move[1] not in '12345678' or move[2] not in 'abcdefgh' or move[3] not in '12345678':
            print('Please enter a move within the bounds of the board')
            return
        
        # source space has piece in it
        if not self.board.isOccupied(source):
            print('Please choose a source that is occupied')
            return
        
        # source space belongs to player whose turn it is
        if not self.board.getColor(source) == self.white_to_play:
            print('Please choose a space occupied by you')
            return

        # valid move for this piece type
        if not self.checkMoveValidity(self.board.get(f'{source}'), self.board.getColor(f'{source}'), source, destination):
            print('Please enter a valid move for this piece')
            return

        # save the board state for backup commands before the move
        self.board.saveBoardState()

        # check if the move results in a capture
        if self.board.isOccupied(destination) and (self.board.getColor(f'{source}') != self.board.getColor(f'{destination}')):
            print(f'Capture piece at {destination}')
            # does recording captures matter? Maybe make a captured piece list

        # make the move
        self.board.set(f'{destination}', self.board.get(f'{source}'))
        self.board.removePiece(f'{source}')

        # undo the move if the move resulted in the current player checking their own king.
        whiteChecked, blackChecked = self.isInCheck()
        if self.white_to_play and whiteChecked:
            self.board.backupBoard()
            print('You can not leave your king in check.')
            return
        if not self.white_to_play and blackChecked:
            self.board.backupBoard()
            print('You can not leave your king in check.')
            return

        # toggle play turn after a valid move
        self.white_to_play = not self.white_to_play

        # update the total number of moves made
        self.number_of_moves += 1

        # allow backup again after a move
        self.has_backedup = False

        # check if either player is in check
        self.white_in_check, self.black_in_check = self.isInCheck()
        if self.white_in_check:
            print("White is in check!")
        elif self.black_in_check:
            print("Black is in check!")

    def set_up_pieces(self):
        """Place pieces on the board as per the initial setup."""
        for col in 'abcdefgh':
            self.board.set(f'{col}2', Pawn(is_white=True,is_captured=False), True)
            self.board.set(f'{col}7', Pawn(is_white=False,is_captured=False), True)
        for col in 'e':    
            self.board.set(f'{col}1', King(is_white=True,is_captured=False), True)
            self.board.set(f'{col}8', King(is_white=False,is_captured=False), True)
        for col in 'd':    
            self.board.set(f'{col}1', Queen(is_white=True,is_captured=False), True)
            self.board.set(f'{col}8', Queen(is_white=False,is_captured=False), True)
        for col in 'cf':    
            self.board.set(f'{col}1', Bishop(is_white=True,is_captured=False), True)
            self.board.set(f'{col}8', Bishop(is_white=False,is_captured=False), True)
        for col in 'bg':    
            self.board.set(f'{col}1', Knight(is_white=True,is_captured=False), True)
            self.board.set(f'{col}8', Knight(is_white=False,is_captured=False), True)        
        for col in 'ah':    
            self.board.set(f'{col}1', Rook(is_white=True,is_captured=False), True)
            self.board.set(f'{col}8', Rook(is_white=False,is_captured=False), True)  

        # save last state of board
        self.board.saveBoardState()

    def checkMoveValidity(self, piece, color, source, destination):
        """Check if the given move follows the movement rules"""

        validMove = False

        if piece.getType() == 'pawn':
            validMove = self.checkMoveValidityPawn(piece, color, source, destination)

        elif piece.getType() == 'king':
            validMove = self.checkMoveValidityKing(piece, color, source, destination)

        elif piece.getType() == 'queen':
            validMove = self.checkMoveValidityQueen(piece, color, source, destination)

        elif piece.getType() == 'knight':
            validMove = self.checkMoveValidityKnight(piece, color, source, destination)

        elif piece.getType() == 'bishop':
            validMove = self.checkMoveValidityBishop(piece, color, source, destination)

        elif piece.getType() == 'rook':
            validMove = self.checkMoveValidityRook(piece, color, source, destination)


        return validMove
    
    def checkMoveValidityPawn(self, piece, color, source, destination):
        """Check movement for pawns"""

        # boolean for if  move is valid
        validMove = False

        sourceCol = ord(source[0:1])
        sourceRow = int(source[1:2])
        destCol = ord(destination[0:1])
        destRow = int(destination[1:2])

        # pawns can only move rows in one direction, so separate logic for black and white pieces
        # white pawns
        if color:

            # first move, not attacking
            if piece.getHasMoved() == 0 and not self.board.isOccupied(destination):
                if sourceCol == destCol and (destRow - sourceRow == 1 or destRow - sourceRow == 2):
                    validMove = True
                    
            # not first move, not attacking
            elif piece.getHasMoved() != 0 and not self.board.isOccupied(destination):
                if sourceCol == destCol and (destRow - sourceRow == 1):
                    validMove = True

            # attacking
            elif self.board.isOccupied(destination) and not self.board.getColor(destination):
                if destRow - sourceRow == 1 and (abs(sourceCol - destCol) == 1):
                    validMove = True


        # black pawns
        else:

            # first move, not attacking
            if piece.getHasMoved() == 0 and not self.board.isOccupied(destination):
                if sourceCol == destCol and (destRow - sourceRow == -1 or destRow - sourceRow == -2):
                    validMove = True
                    
            # not first move, not attacking
            elif piece.getHasMoved() != 0 and not self.board.isOccupied(destination):
                if sourceCol == destCol and (destRow - sourceRow == -1):
                    validMove = True

            # attacking
            elif self.board.isOccupied(destination) and self.board.getColor(destination):
                if destRow - sourceRow == -1 and (abs(sourceCol - destCol) == 1):
                    validMove = True

        # return result
        return validMove
    
    def checkMoveValidityKing(self, piece, color, source, destination):
        """Check movement for kings"""

        # boolean for if  move is valid
        validMove = False

        sourceCol = ord(source[0:1])
        sourceRow = int(source[1:2])
        destCol = ord(destination[0:1])
        destRow = int(destination[1:2])

        # can move one square in any direction if the square is not occupied or occupied by opponent
        if (not self.board.isOccupied(destination)) or (self.board.isOccupied(destination) and color != self.board.getColor(destination)):
            if abs(sourceCol - destCol) <= 1 and abs(sourceRow - destRow) <= 1:
                validMove = True

        # return result
        return validMove

    def checkMoveValidityQueen(self, piece, color, source, destination):
        """Check movement for queens"""

        # boolean for if  move is valid
        validMove = False

        sourceCol = ord(source[0:1])
        sourceRow = int(source[1:2])
        destCol = ord(destination[0:1])
        destRow = int(destination[1:2])

        # can move in straight lines on diagonals or straight lines on row or columns
        if (not self.board.isOccupied(destination)) or (self.board.isOccupied(destination) and color != self.board.getColor(destination)):

            # moving along diagonal
            if abs(sourceCol - destCol) == abs(sourceRow - destRow):

                collision = False
                iteratorList = list(range(abs(destCol - sourceCol)))
                iteratorList = iteratorList[1:]

                # up and right
                if sourceCol < destCol and sourceRow < destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol + iterator)}{sourceRow + iterator}'):
                            collision = True
                            break

                # up and left
                elif sourceCol > destCol and sourceRow < destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol - iterator)}{sourceRow + iterator}'):
                            collision = True
                            break

                # down and right
                elif sourceCol < destCol and sourceRow > destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol + iterator)}{sourceRow - iterator}'):
                            collision = True
                            break

                # down and left
                elif sourceCol > destCol and sourceRow > destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol - iterator)}{sourceRow - iterator}'):
                            collision = True
                            break

                # valid move if no collisions found
                if not collision:
                    validMove = True

            # moving along row or column
            elif sourceCol == destCol or sourceRow == destRow:   

                # same column
                if sourceCol == destCol:

                    collision = False
                    iteratorList = list(range(abs(destRow - sourceRow)))
                    iteratorList = iteratorList[1:]

                    if sourceRow > destRow:
                        # check for occupied spaces between source and destination squares
                        for iterator in iteratorList:
                            if self.board.isOccupied(f'{chr(sourceCol)}{sourceRow - iterator}'):
                                collision = True
                                break
                    elif sourceRow < destRow:
                        # check for occupied spaces between source and destination squares
                        for iterator in iteratorList:
                            if self.board.isOccupied(f'{chr(sourceCol)}{sourceRow + iterator}'):
                                collision = True
                                break

                # same row
                elif sourceRow == destRow:

                    collision = False
                    iteratorList = list(range(abs(destCol - sourceCol)))
                    iteratorList = iteratorList[1:]

                    if sourceCol > destCol:
                        # check for occupied spaces between source and destination squares
                        for iterator in iteratorList:
                            if self.board.isOccupied(f'{chr(sourceCol - iterator)}{sourceRow }'):
                                collision = True
                                break
                    elif sourceRow < destRow:
                        # check for occupied spaces between source and destination squares
                        for iterator in iteratorList:
                            if self.board.isOccupied(f'{chr(sourceCol + iterator)}{sourceRow}'):
                                collision = True
                                break

                # valid move if no collisions found
                if not collision:
                    validMove = True

        # return result
        return validMove
        
    def checkMoveValidityKnight(self, piece, color, source, destination):
        """Check movement for knights"""

        # boolean for if  move is valid
        validMove = False

        sourceCol = ord(source[0:1])
        sourceRow = int(source[1:2])
        destCol = ord(destination[0:1])
        destRow = int(destination[1:2])

        # can move in L pattern
        if (not self.board.isOccupied(destination)) or (self.board.isOccupied(destination) and color != self.board.getColor(destination)):

            if (abs(sourceCol - destCol) == 1 and abs(sourceRow - destRow) == 2) \
            or (abs(sourceCol - destCol) == 2 and abs(sourceRow - destRow) == 1):
                validMove = True

        # return result
        return validMove
    
    def checkMoveValidityBishop(self, piece, color, source, destination):
        """Check movement for bishops"""

        # boolean for if  move is valid
        validMove = False

        sourceCol = ord(source[0:1])
        sourceRow = int(source[1:2])
        destCol = ord(destination[0:1])
        destRow = int(destination[1:2])

        # can move in straight lines on diagonals
        if (not self.board.isOccupied(destination)) or (self.board.isOccupied(destination) and color != self.board.getColor(destination)):

            # moving along diagonal
            if abs(sourceCol - destCol) == abs(sourceRow - destRow):

                collision = False
                iteratorList = list(range(abs(destCol - sourceCol)))
                iteratorList = iteratorList[1:]

                # up and right
                if sourceCol < destCol and sourceRow < destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol + iterator)}{sourceRow + iterator}'):
                            collision = True
                            break

                # up and left
                elif sourceCol > destCol and sourceRow < destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol - iterator)}{sourceRow + iterator}'):
                            collision = True
                            break

                # down and right
                elif sourceCol < destCol and sourceRow > destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol + iterator)}{sourceRow - iterator}'):
                            collision = True
                            break

                # down and left
                elif sourceCol > destCol and sourceRow > destRow:
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol - iterator)}{sourceRow - iterator}'):
                            collision = True
                            break

                # valid move if no collisions found
                if not collision:
                    validMove = True

        # return result
        return validMove

    def checkMoveValidityRook(self, piece, color, source, destination):
        """Check movement for rooks"""

        # boolean for if  move is valid
        validMove = False

        sourceCol = ord(source[0:1])
        sourceRow = int(source[1:2])
        destCol = ord(destination[0:1])
        destRow = int(destination[1:2])

        # can move in straight lines along rows or columns
        if (not self.board.isOccupied(destination)) or (self.board.isOccupied(destination) and color != self.board.getColor(destination)):

            collision = True
            # same column
            if sourceCol == destCol:

                collision = False
                iteratorList = list(range(abs(destRow - sourceRow)))
                iteratorList = iteratorList[1:]

                if sourceRow > destRow:
                    # check for occupied spaces between source and destination squares
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol)}{sourceRow - iterator}'):
                            collision = True
                            break
                elif sourceRow < destRow:
                    # check for occupied spaces between source and destination squares
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol)}{sourceRow + iterator}'):
                            collision = True
                            break

            # same row
            elif sourceRow == destRow:

                collision = False
                iteratorList = list(range(abs(destCol - sourceCol)))
                iteratorList = iteratorList[1:]

                if sourceCol > destCol:
                    # check for occupied spaces between source and destination squares
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol - iterator)}{sourceRow }'):
                            collision = True
                            break
                elif sourceRow < destRow:
                    # check for occupied spaces between source and destination squares
                    for iterator in iteratorList:
                        if self.board.isOccupied(f'{chr(sourceCol + iterator)}{sourceRow}'):
                            collision = True
                            break

            # valid move if no collisions found
            if not collision:
                validMove = True

        # return result
        return validMove

    def checkCastleValidity(self, whiteTurnFlag, sideFlag):
        """check to see if the given castle move is valid"""
        # parameters are whose turn it is (black = 0, white = 1) and which side to castle (queen = 0, king = 1)

        # boolean for if castle move is valid
        castleValid = False

        # black queenside
        if not whiteTurnFlag and not sideFlag:
            # check that neither rook nor king have moved
            if self.board.isOccupied('a8') and not self.board.get('a8').getHasMoved() and self.board.isOccupied('e8') and not self.board.get('e8').getHasMoved():
                # check that spaces between rook and king are not occupied
                if not self.board.isOccupied('b8') and not self.board.isOccupied('c8') and not self.board.isOccupied('d8'):
                    castleValid = True

        # black kingside
        if not whiteTurnFlag and sideFlag:
            # check that neither rook nor king have moved
            if self.board.isOccupied('h8') and not self.board.get('h8').getHasMoved() and self.board.isOccupied('e8') and not self.board.get('e8').getHasMoved():
                # check that spaces between rook and king are not occupied
                if not self.board.isOccupied('f8') and not self.board.isOccupied('g8'):
                    castleValid = True

        # white queenside
        if whiteTurnFlag and not sideFlag:
            # check that neither rook nor king have moved
            if self.board.isOccupied('a1') and not self.board.get('a1').getHasMoved() and self.board.isOccupied('e1') and not self.board.get('e1').getHasMoved():
                # check that spaces between rook and king are not occupied
                if not self.board.isOccupied('b1') and not self.board.isOccupied('c1') and not self.board.isOccupied('d1'):
                    castleValid = True

        # white kingside
        if whiteTurnFlag and sideFlag:
            # check that neither rook nor king have moved
            if self.board.isOccupied('h1') and not self.board.get('h1').getHasMoved() and self.board.isOccupied('e1') and not self.board.get('e1').getHasMoved():
                # check that spaces between rook and king are not occupied
                if not self.board.isOccupied('f1') and not self.board.isOccupied('g1'):
                    castleValid = True

        # return result
        return castleValid


    def isInCheck(self):
        # Checks if either player is in check. returns two booleans that are true if the white or black kings are
        # checked, respectively.
        whiteKing = ''
        blackKing = ''
        board = self.board.getBoard()
        # Identify the squares that each king are on.
        for coord, piece in board.items():
            if piece._type == 'king':
                if piece._is_white:
                    whiteKing = coord
                else:
                    blackKing = coord
        print(whiteKing)
        print(blackKing)
        whiteCheck = False
        blackCheck = False
        if whiteKing == '' or blackKing == '':
            return False, False
        for coord, piece in board.items():
            opposingKing = ''
            if piece._is_white:
                opposingKing = blackKing
            else:
                opposingKing = whiteKing

            if self.checkMoveValidity(piece,piece._is_white,coord,opposingKing):
                if piece._is_white:
                    blackCheck = True
                else:
                    whiteCheck = True


        return whiteCheck, blackCheck

    def isCheckmate(self):
        kingMoves = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                     'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                     'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                     'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                     'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                     'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                     'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                     'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
        whiteKingLoc = ''
        whiteKingPiece = None
        blackKingLoc = ''
        blackKingPiece = None

        board = self.board.getBoard()
        # Identify the squares that each king are on.
        for coord, piece in board.items():
            if piece._type == 'king':
                if piece._is_white:
                    whiteKingLoc = coord
                    whiteKingPiece = piece
                else:
                    blackKingLoc = coord
                    blackKingPiece = piece

        if self.white_to_play and self.white_in_check:
            whiteIsCheckmated = True
            for move in kingMoves:
                if self.checkMoveValidityKing(whiteKingPiece, True, whiteKingLoc,move):
                    whiteIsCheckmated = False
            return whiteIsCheckmated


        elif not self.white_to_play and self.black_in_check:
            blackIsCheckmated = True
            for move in kingMoves:
                if self.checkMoveValidityKing(blackKingPiece, True, blackKingLoc, move):
                    blackIsCheckmated = False

            return blackIsCheckmated

        return False