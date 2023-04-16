from chess.model import Board, King, Queen, Rook, Game

#tests checkmate on black
def test_checkmate_black():
    board = Board()
    game = Game()
    board.set('e8', King(is_white=False,is_captured=False))
    board.set('a7', Rook(is_white=True,is_captured=False))
    board.set('h6', Rook(is_white=True,is_captured=False))
    game.accept_move("h6h7")
    assert board.get('e8') == King(is_white=False,is_captured=True)

#tests checkmate on white
def test_checkmate_white():
    board = Board()
    game = Game()
    board.set('d2', King(is_white=True,is_captured=False))
    board.set('a7', Queen(is_white=False,is_captured=False))
    board.set('a1', Rook(is_white=False,is_captured=False))
    board.set('g3', Rook(is_white=False,is_captured=False))
    game.accept_move("d2e2")
    game.accept_move("a7e7") #checkmate king
    assert board.get('e8') == King(is_white=True,is_captured=True)