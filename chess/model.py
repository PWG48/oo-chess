"""Chess Game model."""
from typing import Optional


class Board:
    """Class containing the state of the game board"""
    def __init__(self):
        self._squares = dict()
        self._lastState = dict()

    def get(self, location:str) -> Optional['Piece']:
        return self._squares.get(location, None)

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

    def accept_move(self, move):

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

        # toggle play turn after a valid move
        self.white_to_play = not self.white_to_play

        # update the total number of moves made
        self.number_of_moves += 1

        # allow backup again after a move
        self.has_backedup = False

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


    # TODO implement rules for how pieces can move
    def checkMoveValidity(self, piece, color, source, destination):
        """Check if the given move follows the movement rules"""

        validMove = False

        if piece.getType() == 'pawn':
            validMove = self.checkMoveValidityPawn(piece, color, source, destination)

        elif piece.getType() == 'king':
            validMove = True

        elif piece.getType() == 'queen':
            validMove = True

        elif piece.getType() == 'knight':
            validMove = True

        elif piece.getType() == 'bishop':
            validMove = True

        elif piece.getType() == 'rook':
            validMove = True


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
            elif self.board.isOccupied(destination) and not self.board.getColor(destination):
                if destRow - sourceRow == -1 and (abs(sourceCol - destCol) == 1):
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