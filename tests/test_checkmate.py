from chess.model import Board, King, Queen, Rook, Game

#tests checkmate on black
def test_checkmate_black():
    game = Game()
    game.board.set('e8', King(is_white=False,is_captured=False))
    game.board.set('a7', Rook(is_white=True,is_captured=False))
    game.board.set('h6', Rook(is_white=True,is_captured=False))
    game.accept_move("h6h8")
    assert game.board.get('e8') == King(is_white=False,is_captured=True)

#tests checkmate on white
def test_checkmate_white():
    game = Game()
    game.board.set('d2', King(is_white=True,is_captured=False))
    game.board.set('a7', Queen(is_white=False,is_captured=False))
    game.board.set('a1', Rook(is_white=False,is_captured=False))
    game.board.set('g3', Rook(is_white=False,is_captured=False))
    game.accept_move("d2e2")
    game.accept_move("a7e7") #checkmate king
    assert game.board.get('e2') == King(is_white=True,is_captured=True)