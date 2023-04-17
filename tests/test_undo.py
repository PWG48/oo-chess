from chess.model import Board, Pawn, Game

#checks if undo/backup
def test_undo():
    game = Game()
    game.board.set('a2', Pawn(is_white=True,is_captured=False), True)
    game.accept_move("a2a3")
    assert game.board.get('a3') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('a2') == None
    game.accept_move("backup")
    assert game.board.get('a2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('a3') == None
    game.board.set('g7', Pawn(is_white=False,is_captured=False),True)
    game.accept_move("a2a3") #white to move
    game.accept_move("g7g5") #black moves pawn
    assert game.board.get('g5') == Pawn(is_white=False,is_captured=False)
    assert game.board.get('g7') == None
    game.accept_move("backup")
    assert game.board.get('g5') == None
    assert game.board.get('g7') == Pawn(is_white=False,is_captured=False)