from chess.model import Board, Pawn

def test_board_ctor():
    board = Board()
    board.set('e2', Pawn(is_white=True))
    assert board.get('e2') == Pawn(is_white=True)
    assert board.get('e4') == None
