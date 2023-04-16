import chess.view as view
import chess.model as model

def test_piece_to_char():
    assert '·' == view.piece_to_char(None)
    assert '♙' == view.piece_to_char(model.Pawn(is_white=True,is_captured=False))
    assert '♟' == view.piece_to_char(model.Pawn(is_white=False,is_captured=False))
    assert '♔' == view.piece_to_char(model.King(is_white=True,is_captured=False))
    assert '♚' == view.piece_to_char(model.King(is_white=False,is_captured=False))
    assert '♕' == view.piece_to_char(model.Queen(is_white=True,is_captured=False))
    assert '♛' == view.piece_to_char(model.Queen(is_white=False,is_captured=False))
    assert '♖' == view.piece_to_char(model.Rook(is_white=True,is_captured=False))
    assert '♜' == view.piece_to_char(model.Rook(is_white=False,is_captured=False))
    assert '♗' == view.piece_to_char(model.Bishop(is_white=True,is_captured=False))
    assert '♝' == view.piece_to_char(model.Bishop(is_white=False,is_captured=False))
    assert '♘' == view.piece_to_char(model.Knight(is_white=True,is_captured=False))
    assert '♞' == view.piece_to_char(model.Knight(is_white=False,is_captured=False))