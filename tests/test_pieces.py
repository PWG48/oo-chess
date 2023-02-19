from chess.model import Pawn

def test_identity():
    pawn1 = Pawn(is_white=True)
    pawn2 = Pawn(is_white=True)
    pawn3 = Pawn(is_white=False)
    assert pawn1 == pawn2
    assert not pawn1 == pawn3
