from typing import Optional

import chess.model as model

def board_to_text(board) ->str:
    ans = []
    ans.append('  a b c d e f g h')
    for i in range(8,0,-1):
        row = f'{i} '
        for col in 'abcdefgh':
            piece = board.get(f'{col}{i}')
            val = piece_to_char(piece)
            row += f'{val} '
        ans.append(row)
    return '\n'.join(ans) + '\n'

_PIECE_UNICODES = {
    'King': {True: "\u2654", False: "\u265A"},
    'Queen': {True: "\u2655", False: "\u265B"},
    'Rook': {True: "\u2656", False: "\u265C"},
    'Bishop': {True: "\u2657", False: "\u265D"},
    'Knight': {True: "\u2658", False: "\u265E"},
    'Pawn': {True: "\u2659", False: "\u265F"},
}

def piece_to_char(piece: Optional[model.Piece]) -> str:
    if piece is None:
        return '\u00B7'
    return _PIECE_UNICODES[type(piece).__name__][piece._is_white]

    