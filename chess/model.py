"""Chess Game model."""
from typing import Optional


class Board:
    """Class containing the state of the game board"""
    def __init__(self):
        self._squares = dict()
        self._lastState = dict()

    def get(self, location:str) -> Optional['Piece']:
        return self._squares.get(location, None)

    def set(self, location:str, piece: 'Piece'):
        self._squares[location] = piece

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

class Piece:
    """Abstract base class for chess pieces."""
    def __init__(self, is_white: bool, is_captured: bool, type:str) -> None:
        self._is_white = is_white
        self._is_captured = is_captured
        self.type = type

    def __hash__(self):
        return hash((type(self), self._is_white))

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)

    def getPieceColor(self):
        return self._is_white
    

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
            self.board.set(f'{col}2', Pawn(is_white=True,is_captured=False))
            self.board.set(f'{col}7', Pawn(is_white=False,is_captured=False))
        for col in 'e':    
            self.board.set(f'{col}1', King(is_white=True,is_captured=False))
            self.board.set(f'{col}8', King(is_white=False,is_captured=False))
        for col in 'd':    
            self.board.set(f'{col}1', Queen(is_white=True,is_captured=False))
            self.board.set(f'{col}8', Queen(is_white=False,is_captured=False))
        for col in 'cf':    
            self.board.set(f'{col}1', Bishop(is_white=True,is_captured=False))
            self.board.set(f'{col}8', Bishop(is_white=False,is_captured=False))
        for col in 'bg':    
            self.board.set(f'{col}1', Knight(is_white=True,is_captured=False))
            self.board.set(f'{col}8', Knight(is_white=False,is_captured=False))        
        for col in 'ah':    
            self.board.set(f'{col}1', Rook(is_white=True,is_captured=False))
            self.board.set(f'{col}8', Rook(is_white=False,is_captured=False))  

        # save last state of board
        self.board.saveBoardState()


    # TODO implement rules for how pieces can move
    def checkMoveValidity(self, piece, color, source, destination):

        validMove = False

        if piece.type == 'pawn':
            validMove = True

        elif piece.type == 'king':
            validMove = True

        elif piece.type == 'queen':
            validMove = True

        elif piece.type == 'knight':
            validMove = True

        elif piece.type == 'bishop':
            validMove = True

        elif piece.type == 'rook':
            validMove = True


        return validMove
