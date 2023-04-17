from chess.model import Board, Pawn, Game

#checks if a correctly entered move moves pieces of the board
def test_move():
    game = Game()
    game.board.set('e2', Pawn(is_white=True,is_captured=False), True)
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('e4') == None
    game.accept_move("e2e4")
    assert game.board.get('e4') == Pawn(is_white=True,is_captured=False)
    