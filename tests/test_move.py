from chess.model import Board, Pawn, Game
def test_move():
    board = Board()
    board.set('e2', Pawn(is_white=True,is_captured=False))
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert board.get('e4') == None
    game = Game()
    game.accept_move("e2e4")
    assert board.get('e4') == Pawn(is_white=True,is_captured=False)
    game.accept_move("e4....e5")
    assert board.get('e4') == Pawn(is_white=True,is_captured=False)
    assert board.get('e5') == None