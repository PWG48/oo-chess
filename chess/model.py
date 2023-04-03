"""Chess Game model."""
from typing import Optional


class Board:
    def __init__(self):
        self._squares = dict()

    def get(self, location:str) -> Optional['Piece']:
        return self._squares.get(location, None)

    def set(self, location:str, piece: 'Piece'):
        self._squares[location] = piece

class Piece:
    """Abstract base class for chess pieces."""
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        self._is_white = is_white
        self._is_captured = is_captured

    def __hash__(self):
        return hash((type(self), self._is_white))

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)


class Pawn(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured)

class King(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured)
        has_castled = False

class Queen(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured)
        
class Knight(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured)

class Bishop(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured)

class Rook(Piece):
    def __init__(self, is_white: bool, is_captured: bool) -> None:
        super().__init__(is_white, is_captured)

class Game:
    def __init__(self):
        self.board = Board()
        self.white_to_play = True
        self.game_over = False

    def accept_move(self, move):
        # TODO: Implement updating the board with the give move
        self.white_to_play = not self.white_to_play

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