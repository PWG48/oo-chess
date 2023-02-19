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
    def __init__(self, is_white: bool) -> None:
        self._is_white = is_white

    def __hash__(self):
        return hash((type(self), self._is_white))

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)


class Pawn(Piece):
    pass


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
            self.board.set(f'{col}2', Pawn(is_white=True))
            self.board.set(f'{col}7', Pawn(is_white=False))
