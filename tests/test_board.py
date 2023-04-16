from chess.model import Board, Pawn, King, Queen, Bishop, Rook, Knight

def test_board_ctor():
    board = Board()
    board.set('e2', Pawn(is_white=True,is_captured=False))
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert board.get('e4') == None
    board.set('d2', King(is_white=True,is_captured=False))
    assert board.get('d2') == King(is_white=True,is_captured=False)
    board.set('f2', Queen(is_white=True,is_captured=False))
    assert board.get('f2') == Queen(is_white=True,is_captured=False)
    board.set('e7', Bishop(is_white=True,is_captured=False))
    assert board.get('e7') == Bishop(is_white=True,is_captured=False)
    board.set('a1', Rook(is_white=True,is_captured=False))
    assert board.get('a1') == Rook(is_white=True,is_captured=False)
    board.set('c8', Knight(is_white=True,is_captured=False))
    assert board.get('c8') == Knight(is_white=True,is_captured=False)