from chess.model import Board, Pawn, Bishop, Rook, Queen, Knight, King, Game

#tests bad syntax does not move the pieces
def test_syntax():
    board = Board()
    game = Game()
    board.set('e2', Pawn(is_white=True,is_captured=False))
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert board.get('e4') == None
    game.accept_move("e4....e5")
    assert board.get('e4') == Pawn(is_white=True,is_captured=False)
    assert board.get('e5') == None
    game.accept_move("4e5e")
    assert board.get('e4') == Pawn(is_white=True,is_captured=False)
    assert board.get('e5') == None

# test moving a non-existance piece
def test_non_exist_piece():
    board = Board()
    game = Game()
    board.set('e2', Pawn(is_white=True,is_captured=False))
    assert board.get('a1') == None
    assert board.get('a2') == None
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)
    game.accept_move("a1a2")
    assert board.get('a1') == None
    assert board.get('a2') == None
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)

# test white moving a black piece
def test_move_opponent_white():
    board = Board()
    game = Game()
    board.set('f7', Pawn(is_white=False,is_captured=False))
    assert board.get('f6') == None
    assert board.get('f7') == Pawn(is_white=False,is_captured=False)
    game.accept_move("f7f6") #white to move
    assert board.get('f6') == None
    assert board.get('f7') == Pawn(is_white=False,is_captured=False)

# test black moving a white piece
def test_move_opponent_black():
    board = Board()
    game = Game()
    board.set('c2', Pawn(is_white=True,is_captured=False))
    game.accept_move("c2c3") #white to move
    assert board.get('c4') == None
    assert board.get('c3') == Pawn(is_white=True,is_captured=False)
    game.accept_move("c3c4") #black to move
    assert board.get('c4') == None
    assert board.get('c3') == Pawn(is_white=True,is_captured=False)

# tests illegal and legal Bishop moves for white and black
def test_move_bishop_illegal():
    board = Board()
    game = Game()
    board.set('c1', Bishop(is_white=True,is_captured=False))
    assert board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert board.get('c2') == None
    game.accept_move("c1c2")
    assert board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert board.get('c2') == None
    game.accept_move("c1g5")
    assert board.get('g5') == Bishop(is_white=True,is_captured=False)
    assert board.get('c1') == None

    board.set('f8', Bishop(is_white=False,is_captured=False))
    assert board.get('f8') == Bishop(is_white=False,is_captured=False)
    assert board.get('f7') == None
    game.accept_move("f8f7") #black to move
    assert board.get('f8') == Bishop(is_white=False,is_captured=False)
    assert board.get('f7') == None
    game.accept_move("f8b4") #black to move
    assert board.get('f8') == None
    assert board.get('b4') == Bishop(is_white=False,is_captured=False)

# tests illegal and legal Rook moves for white and black
def test_move_rook_illegal():
    board = Board()
    game = Game()
    board.set('a1', Rook(is_white=True,is_captured=False))
    assert board.get('a1') == Rook(is_white=True,is_captured=False)
    assert board.get('b2') == None
    game.accept_move("a1b2")
    assert board.get('a1') == Rook(is_white=True,is_captured=False)
    assert board.get('b2') == None
    game.accept_move("a1a7")
    assert board.get('a7') == Rook(is_white=True,is_captured=False)
    assert board.get('a1') == None

    board.set('h8', Rook(is_white=False,is_captured=False))
    assert board.get('h8') == Rook(is_white=False,is_captured=False)
    assert board.get('c3') == None
    game.accept_move("h8c3") #black to move
    assert board.get('h8') == Rook(is_white=False,is_captured=False)
    assert board.get('c3') == None
    game.accept_move("h8d8") #black to move
    assert board.get('h8') == None
    assert board.get('d8') == Rook(is_white=False,is_captured=False)

    # tests illegal and legal queen moves for white and black
def test_move_queen_illegal():
    board = Board()
    game = Game()
    board.set('d1', Queen(is_white=True,is_captured=False))
    assert board.get('d1') == Queen(is_white=True,is_captured=False)
    assert board.get('e3') == None
    game.accept_move("d1e3")
    assert board.get('d1') == Queen(is_white=True,is_captured=False)
    assert board.get('e3') == None
    game.accept_move("d1d6")
    assert board.get('d6') == Queen(is_white=True,is_captured=False)
    assert board.get('d1') == None

    board.set('h8', Queen(is_white=False,is_captured=False))
    assert board.get('d8') == Queen(is_white=False,is_captured=False)
    assert board.get('h1') == None
    game.accept_move("d8h1") #black to move
    assert board.get('d8') == Queen(is_white=False,is_captured=False)
    assert board.get('h1') == None
    game.accept_move("d8h8") #black to move
    assert board.get('d8') == None
    assert board.get('h8') == Queen(is_white=False,is_captured=False)

# tests illegal and legal knight moves for white and black
def test_move_queen_illegal():
    board = Board()
    game = Game()
    board.set('b1', Knight(is_white=True,is_captured=False))
    assert board.get('b1') == Knight(is_white=True,is_captured=False)
    assert board.get('c4') == None
    game.accept_move("b1c4")
    assert board.get('b1') == Knight(is_white=True,is_captured=False)
    assert board.get('c4') == None
    game.accept_move("b1a3")
    assert board.get('a3') == Knight(is_white=True,is_captured=False)
    assert board.get('b1') == None

    board.set('g8', Knight(is_white=False,is_captured=False))
    assert board.get('g8') == Knight(is_white=False,is_captured=False)
    assert board.get('d5') == None
    game.accept_move("g8d5") #black to move
    assert board.get('g8') == Knight(is_white=False,is_captured=False)
    assert board.get('d5') == None
    game.accept_move("g8e7") #black to move
    assert board.get('g8') == None
    assert board.get('e7') == Knight(is_white=False,is_captured=False)

#test moving pieces over existing pieces
def test_move_over():
    board = Board()
    game = Game()
    #Rook
    board.set('a1', Rook(is_white=True,is_captured=False))
    board.set('a2', Pawn(is_white=True,is_captured=False))
    game.accept_move("a1a3")
    assert board.get('a1') == Rook(is_white=True,is_captured=False)
    assert board.get('a2') == Pawn(is_white=True,is_captured=False)
    assert board.get('a3') == None

    #Bishop
    board.set('c1', Bishop(is_white=True,is_captured=False))
    board.set('d2', Pawn(is_white=True,is_captured=False))
    game.accept_move("c1e3")
    assert board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert board.get('d2') == Pawn(is_white=True,is_captured=False)
    assert board.get('e3') == None

    #Queen
    board.set('d1', Queen(is_white=True,is_captured=False))
    board.set('e2', Pawn(is_white=True,is_captured=False))
    game.accept_move("d1d4")
    assert board.get('d1') == Queen(is_white=True,is_captured=False)
    assert board.get('d2') == Pawn(is_white=True,is_captured=False)
    assert board.get('d4') == None
    game.accept_move("d1e3")
    assert board.get('d1') == Queen(is_white=True,is_captured=False)
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert board.get('e3') == None

#test moving to already occupied squares
def test_move_occupied():
    board = Board()
    game = Game()
    board.set('a1', Rook(is_white=True,is_captured=False))
    board.set('c1', Bishop(is_white=True,is_captured=False))
    board.set('d1', Queen(is_white=True,is_captured=False))
    board.set('b2', Pawn(is_white=True,is_captured=False))
    game.accept_move("a1c1") #move rook to bishop
    assert board.get('a1') == Rook(is_white=True,is_captured=False)
    assert board.get('c1') == Bishop(is_white=True,is_captured=False)
    game.accept_move("c1b2") #move bishop to pawn
    assert board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert board.get('b2') == Pawn(is_white=True,is_captured=False)
    game.accept_move("d1c1") #Queen to Bishop
    assert board.get('d1') == Queen(is_white=True,is_captured=False)
    assert board.get('c1') == Bishop(is_white=True,is_captured=False)
    board.set('b3', Pawn(is_white=True,is_captured=False))
    game.accept_move("b2b3") #Pawn to Pawn
    assert board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert board.get('b3') == Pawn(is_white=True,is_captured=False)

#test moving pawn illegaly
def test_move_pawn():
    board = Board()
    game = Game()
    board.set('b2', Pawn(is_white=True,is_captured=False))
    game.accept_move("b2b1") #move pawn to back
    assert board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert board.get('b1') == None
    game.accept_move("b2c2") #move pawn right
    assert board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert board.get('c2') == None
    game.accept_move("b2a3") #move pawn diagonally
    assert board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert board.get('a3') == None

#test moving king illegaly - includes King checking itself
def test_move_king():
    board = Board()
    game = Game()
    board.set('e1', King(is_white=True,is_captured=False))
    board.set('d8', Queen(is_white=False,is_captured=False))
    game.accept_move("e1d1") #move king to check position
    assert board.get('e1') == King(is_white=True,is_captured=False)
    assert board.get('d1') == None
    game.accept_move("e1f3") #move king illegaly
    assert board.get('e1') == King(is_white=True,is_captured=False)
    assert board.get('f3') == None
    board.set('e2', Pawn(is_white=True,is_captured=False))
    game.accept_move("e1e2") #move king illegaly
    assert board.get('e1') == King(is_white=True,is_captured=False)
    assert board.get('e2') == Pawn(is_white=True,is_captured=False)
    
    