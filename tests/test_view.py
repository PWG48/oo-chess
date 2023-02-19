import chess.view as view
import chess.model as model

def test_piece_to_char():
    assert '·' == view.piece_to_char(None)
    assert '♙' == view.piece_to_char(model.Pawn(is_white=True))
    assert '♟' == view.piece_to_char(model.Pawn(is_white=False))
