from chess.model import Board, Pawn, Rook, Knight, Bishop, Queen, King, Game

#tests if setup peices function works correctly
def test_undo():
    game = Game()
    game.set_up_pieces()

    for col in 'abcdefgh':
        assert game.board.get(f'{col}2') == Pawn(is_white=True,is_captured=False)
        assert game.board.get(f'{col}7') == Pawn(is_white=False,is_captured=False)
        assert game.board.get(f'{col}3') == None
        assert game.board.get(f'{col}4') == None
        assert game.board.get(f'{col}5') == None
        assert game.board.get(f'{col}6') == None
    for col in 'e':    
        assert game.board.get(f'{col}1') == King(is_white=True,is_captured=False)
        assert game.board.get(f'{col}8') == King(is_white=False,is_captured=False)
    for col in 'd':    
        assert game.board.get(f'{col}1') == Queen(is_white=True,is_captured=False)
        assert game.board.get(f'{col}8') == Queen(is_white=False,is_captured=False)
    for col in 'cf':    
        assert game.board.get(f'{col}1') == Bishop(is_white=True,is_captured=False)
        assert game.board.get(f'{col}8') == Bishop(is_white=False,is_captured=False)
    for col in 'bg':    
        assert game.board.get(f'{col}1') == Knight(is_white=True,is_captured=False)
        assert game.board.get(f'{col}8') == Knight(is_white=False,is_captured=False)       
    for col in 'ah':    
        assert game.board.get(f'{col}1') == Rook(is_white=True,is_captured=False)
        assert game.board.get(f'{col}8') == Rook(is_white=False,is_captured=False)  