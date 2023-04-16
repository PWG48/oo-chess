from chess.model import Pawn, King, Queen, Bishop, Rook, Knight

def test_identity():
    pawn1 = Pawn(is_white=True,is_captured=False)
    pawn2 = Pawn(is_white=True,is_captured=False)
    pawn3 = Pawn(is_white=False,is_captured=False)
    assert pawn1 == pawn2
    assert not pawn1 == pawn3
    
    king1 = King(is_white=True,is_captured=False)
    king2 = King(is_white=True,is_captured=False)
    king3 = King(is_white=False,is_captured=False)
    assert king1 == king2
    assert not king2 == king3

    queen1 = Queen(is_white=True,is_captured=False)
    queen2 = Queen(is_white=True,is_captured=False)
    queen3 = Queen(is_white=False,is_captured=False)
    assert queen1 == queen2
    assert not queen2 == queen3

    bishop1 = Bishop(is_white=True,is_captured=False)
    bishop2 = Bishop(is_white=True,is_captured=False)
    bishop3 = Bishop(is_white=False,is_captured=False)
    assert bishop1 == bishop2
    assert not bishop2 == bishop3

    rook1 = Rook(is_white=True,is_captured=False)
    rook2 = Rook(is_white=True,is_captured=False)
    rook3 = Rook(is_white=False,is_captured=False)
    assert rook1 == rook2
    assert not bishop2 == rook3

    knight1 = Knight(is_white=True,is_captured=False)
    knight2 = Knight(is_white=True,is_captured=False)
    knight3 = Knight(is_white=False,is_captured=False)
    assert knight1 == knight2
    assert not knight2 == knight3