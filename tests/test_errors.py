from chess.model import Board, Pawn, Bishop, Rook, Queen, Knight, King, Game

#tests bad syntax does not move the pieces
def test_syntax():
    game = Game()
    game.board.set('e2', Pawn(is_white=True,is_captured=False))
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('e4') == None
    game.accept_move("e4....e5")
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('e5') == None
    assert game.board.get('e4') == None
    game.accept_move("4e5e")
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('e5') == None
    assert game.board.get('e4') == None

# test moving a non-existance piece
def test_non_exist_piece():
    game = Game()
    game.board.set('e2', Pawn(is_white=True,is_captured=False))
    assert game.board.get('a1') == None
    assert game.board.get('a2') == None
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    game.accept_move("a1a2")
    assert game.board.get('a1') == None
    assert game.board.get('a2') == None
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)

# test white moving a black piece
def test_move_opponent_white():
    game = Game()
    game.board.set('f7', Pawn(is_white=False,is_captured=False))
    assert game.board.get('f6') == None
    assert game.board.get('f7') == Pawn(is_white=False,is_captured=False)
    game.accept_move("f7f6") #white to move
    assert game.board.get('f6') == None
    assert game.board.get('f7') == Pawn(is_white=False,is_captured=False)

# test black moving a white piece
def test_move_opponent_black():
    game = Game()
    game.board.set('c2', Pawn(is_white=True,is_captured=False))
    game.accept_move("c2c3") #white to move
    assert game.board.get('c4') == None
    assert game.board.get('c3') == Pawn(is_white=True,is_captured=False)
    game.accept_move("c3c4") #black to move
    assert game.board.get('c4') == None
    assert game.board.get('c3') == Pawn(is_white=True,is_captured=False)

# tests illegal and legal Bishop moves for white and black
def test_move_bishop_illegal():
    game = Game()
    game.board.set('c1', Bishop(is_white=True,is_captured=False))
    assert game.board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert game.board.get('c2') == None
    game.accept_move("c1c2")
    assert game.board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert game.board.get('c2') == None
    game.accept_move("c1g5")
    assert game.board.get('g5') == Bishop(is_white=True,is_captured=False)
    assert game.board.get('c1') == None

    game.board.set('f8', Bishop(is_white=False,is_captured=False))
    assert game.board.get('f8') == Bishop(is_white=False,is_captured=False)
    assert game.board.get('f7') == None
    game.accept_move("f8f7") #black to move
    assert game.board.get('f8') == Bishop(is_white=False,is_captured=False)
    assert game.board.get('f7') == None
    game.accept_move("f8b4") #black to move
    assert game.board.get('f8') == None
    assert game.board.get('b4') == Bishop(is_white=False,is_captured=False)

# tests illegal and legal Rook moves for white and black
def test_move_rook_illegal():
    game = Game()
    game.board.set('a1', Rook(is_white=True,is_captured=False))
    assert game.board.get('a1') == Rook(is_white=True,is_captured=False)
    assert game.board.get('b2') == None
    game.accept_move("a1b2")
    assert game.board.get('a1') == Rook(is_white=True,is_captured=False)
    assert game.board.get('b2') == None
    game.accept_move("a1a7")
    assert game.board.get('a7') == Rook(is_white=True,is_captured=False)
    assert game.board.get('a1') == None

    game.board.set('h8', Rook(is_white=False,is_captured=False))
    assert game.board.get('h8') == Rook(is_white=False,is_captured=False)
    assert game.board.get('c3') == None
    game.accept_move("h8c3") #black to move
    assert game.board.get('h8') == Rook(is_white=False,is_captured=False)
    assert game.board.get('c3') == None
    game.accept_move("h8d8") #black to move
    assert game.board.get('h8') == None
    assert game.board.get('d8') == Rook(is_white=False,is_captured=False)

    # tests illegal and legal queen moves for white and black
def test_move_queen_illegal():
    game = Game()
    game.board.set('d1', Queen(is_white=True,is_captured=False))
    assert game.board.get('d1') == Queen(is_white=True,is_captured=False)
    assert game.board.get('e3') == None
    game.accept_move("d1e3")
    assert game.board.get('d1') == Queen(is_white=True,is_captured=False)
    assert game.board.get('e3') == None
    game.accept_move("d1d6")
    assert game.board.get('d6') == Queen(is_white=True,is_captured=False)
    assert game.board.get('d1') == None

    game.board.set('d8', Queen(is_white=False,is_captured=False))
    assert game.board.get('d8') == Queen(is_white=False,is_captured=False)
    assert game.board.get('h1') == None
    game.accept_move("d8h1") #black to move
    assert game.board.get('d8') == Queen(is_white=False,is_captured=False)
    assert game.board.get('h1') == None
    game.accept_move("d8h8") #black to move
    assert game.board.get('d8') == None
    assert game.board.get('h8') == Queen(is_white=False,is_captured=False)

# tests illegal and legal knight moves for white and black
def test_move_knight_illegal():
    game = Game()
    game.board.set('b1', Knight(is_white=True,is_captured=False))
    assert game.board.get('b1') == Knight(is_white=True,is_captured=False)
    assert game.board.get('c4') == None
    game.accept_move("b1c4")
    assert game.board.get('b1') == Knight(is_white=True,is_captured=False)
    assert game.board.get('c4') == None
    game.accept_move("b1a3")
    assert game.board.get('a3') == Knight(is_white=True,is_captured=False)
    assert game.board.get('b1') == None

    game.board.set('g8', Knight(is_white=False,is_captured=False))
    assert game.board.get('g8') == Knight(is_white=False,is_captured=False)
    assert game.board.get('d5') == None
    game.accept_move("g8d5") #black to move
    assert game.board.get('g8') == Knight(is_white=False,is_captured=False)
    assert game.board.get('d5') == None
    game.accept_move("g8e7") #black to move
    assert game.board.get('g8') == None
    assert game.board.get('e7') == Knight(is_white=False,is_captured=False)

#test moving pieces over existing pieces
def test_move_over():
    game = Game()
    #Rook
    game.board.set('a1', Rook(is_white=True,is_captured=False))
    game.board.set('a2', Pawn(is_white=True,is_captured=False))
    game.accept_move("a1a3")
    assert game.board.get('a1') == Rook(is_white=True,is_captured=False)
    assert game.board.get('a2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('a3') == None

    #Bishop
    game.board.set('c1', Bishop(is_white=True,is_captured=False))
    game.board.set('d2', Pawn(is_white=True,is_captured=False))
    game.accept_move("c1e3")
    assert game.board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert game.board.get('d2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('e3') == None

    #Queen
    game.board.set('d1', Queen(is_white=True,is_captured=False))
    game.board.set('e2', Pawn(is_white=True,is_captured=False))
    game.accept_move("d1d4")
    assert game.board.get('d1') == Queen(is_white=True,is_captured=False)
    assert game.board.get('d2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('d4') == None
    game.accept_move("d1e3")
    assert game.board.get('d1') == Queen(is_white=True,is_captured=False)
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('e3') == None

#test moving to already occupied squares
def test_move_occupied():
    game = Game()
    game.board.set('a1', Rook(is_white=True,is_captured=False))
    game.board.set('c1', Bishop(is_white=True,is_captured=False))
    game.board.set('d1', Queen(is_white=True,is_captured=False))
    game.board.set('b2', Pawn(is_white=True,is_captured=False))
    game.accept_move("a1c1") #move rook to bishop
    assert game.board.get('a1') == Rook(is_white=True,is_captured=False)
    assert game.board.get('c1') == Bishop(is_white=True,is_captured=False)
    game.accept_move("c1b2") #move bishop to pawn
    assert game.board.get('c1') == Bishop(is_white=True,is_captured=False)
    assert game.board.get('b2') == Pawn(is_white=True,is_captured=False)
    game.accept_move("d1c1") #Queen to Bishop
    assert game.board.get('d1') == Queen(is_white=True,is_captured=False)
    assert game.board.get('c1') == Bishop(is_white=True,is_captured=False)
    game.board.set('b3', Pawn(is_white=True,is_captured=False))
    game.accept_move("b2b3") #Pawn to Pawn
    assert game.board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('b3') == Pawn(is_white=True,is_captured=False)

#test moving pawn illegaly
def test_move_pawn():
    game = Game()
    game.board.set('b2', Pawn(is_white=True,is_captured=False))
    game.accept_move("b2b1") #move pawn to back
    assert game.board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('b1') == None
    game.accept_move("b2c2") #move pawn right
    assert game.board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('c2') == None
    game.accept_move("b2a3") #move pawn diagonally
    assert game.board.get('b2') == Pawn(is_white=True,is_captured=False)
    assert game.board.get('a3') == None

#test moving king illegaly - includes King checking itself
def test_move_king():
    game = Game()
    game.board.set('e1', King(is_white=True,is_captured=False))
    game.board.set('e8', King(is_white=False,is_captured=False))
    game.board.set('d8', Queen(is_white=False,is_captured=False))
    game.accept_move("e1d1") #move king to check position
    assert game.board.get('d1') == None
    assert game.board.get('e1') == King(is_white=True,is_captured=False)
    
    game.accept_move("e1f3") #move king illegaly
    assert game.board.get('e1') == King(is_white=True,is_captured=False)
    assert game.board.get('f3') == None
    game.board.set('e2', Pawn(is_white=True,is_captured=False))
    game.accept_move("e1e2") #move king illegaly
    assert game.board.get('e1') == King(is_white=True,is_captured=False)
    assert game.board.get('e2') == Pawn(is_white=True,is_captured=False)
    
#test moving a piece blocking line of sight of an opponents piece on friednly king is allowed
def test_move_piece_to_check_friendly_king():
    game = Game()
    game.board.set('b2', King(is_white=True,is_captured=False))
    game.board.set('e8', King(is_white=False,is_captured=False))
    game.board.set('b7', Queen(is_white=False,is_captured=False))
    game.board.set('b3', Rook(is_white=True,is_captured=False))
    game.accept_move("b3c3") #move rook away from pinned position leaving its own king in check
    assert game.board.get('c3') == None
    assert game.board.get('b3') == Rook(is_white=True,is_captured=False)

#test white resigns
def test_white_resign():
    game = Game()
    game.board.set('d2', King(is_white=True,is_captured=False))
    game.board.set('f2', Pawn(is_white=True,is_captured=False))
    game.board.set('g3', Pawn(is_white=True,is_captured=False))
    game.board.set('a8', Rook(is_white=True,is_captured=False))
    game.board.set('e7', King(is_white=False,is_captured=False))
    game.board.set('h8', Pawn(is_white=False,is_captured=False))
    game.board.set('d4', Pawn(is_white=False,is_captured=False))
    game.accept_move("resign") #White resign
    assert game.game_over == True
    
    #test black resigns
def test_black_resign():
    game = Game()
    game.set_up_pieces()
    game.accept_move("e2e3") #White moves
    game.accept_move("resign") #Black resigns
    assert game.game_over == True