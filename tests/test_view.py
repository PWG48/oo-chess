import chess.view as view
import chess.model as model

def test_piece_to_char():
    assert ' ' == view.piece_to_char(None)
    assert 'P' == view.piece_to_char(model.Pawn(is_white=True))
    assert 'p' == view.piece_to_char(model.Pawn(is_white=False))
