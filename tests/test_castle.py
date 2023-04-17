from chess.model import Board, King, Rook, Bishop, Game

#tests if castle works under correct conditions
def test_castle_white():
    game = Game()
    game.board.set('e1', King(is_white=True,is_captured=False), True)
    game.board.set('a1', Rook(is_white=True,is_captured=False), True)
    print
    game.accept_move("castlequeen")
    assert game.board.get('c1') == King(is_white=True,is_captured=False)
    assert game.board.get('d1') == Rook(is_white=True,is_captured=False)

#tests if castle works when conditions are not satisfied and satisfied for black    
def test_castle_black():
    game = Game()
    game.board.set('e8', King(is_white=False,is_captured=False), True)
    game.board.set('h8', Rook(is_white=False,is_captured=False), True)
    game.board.set('f8', Bishop(is_white=False,is_captured=False), True)
    game.board.set('a1', Rook(is_white=True,is_captured=False), True)
    game.accept_move("a1a2") # white to move
    game.accept_move("castleking") # attemp castle
    assert game.board.get('e8') == King(is_white=False,is_captured=False)
    assert game.board.get('h8') == Rook(is_white=False,is_captured=False)
    assert game.board.get('f8') == Bishop(is_white=False,is_captured=False)
    game.accept_move("f8e7") #move rook out of row 8
    game.accept_move("a2a1") # white to move
    game.accept_move("castleking") #castle
    assert game.board.get('g8') == King(is_white=False,is_captured=False)
    assert game.board.get('f8') == Rook(is_white=False,is_captured=False)
    
#continue test to check if the King/Rook have moved prior to initiating castle
def test_castle_move():
    game = Game()
    game.board.set('e1', King(is_white=True,is_captured=False), False)
    game.board.set('a1', Rook(is_white=True,is_captured=False), False)
    game.accept_move("castlequeen")
    assert game.board.get('e1') == King(is_white=True,is_captured=False)
    assert game.board.get('a1') == Rook(is_white=True,is_captured=False)