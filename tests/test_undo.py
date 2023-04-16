from chess.model import Board, Pawn, Game

#checks if undo/backup
def test_undo():
    board = Board()
    board.set('a2', Pawn(is_white=True,is_captured=False))
    game = Game()
    game.accept_move("a2a3")
    assert board.get('a3') == Pawn(is_white=True,is_captured=False)
    assert board.get('a2') == None
    game.accept_move("backup")
    assert board.get('a2') == Pawn(is_white=True,is_captured=False)
    assert board.get('a3') == None

    board.set('g7', Pawn(is_white=False,is_captured=False))
    game.accept_move("a2a4") #white to move
    game.accept_move("g7g5")
    assert board.get('g5') == Pawn(is_white=False,is_captured=False)
    assert board.get('g7') == None
    game.accept_move("backup")
    assert board.get('g5') == None
    assert board.get('g7') == Pawn(is_white=False,is_captured=False)