from TP_Calculatrice import tp

def test_DeuxNombre():
    """test func 1"""
    assert tp.DeuxNombre(2,3)== 5


def test_MultipNombre():
    """Test multiplication"""
    assert tp.MultipNombre(2,3) == 6

print("All tests pass")