"""test func 1"""
def test_DeuxNombre():
     """Test addition"""
    assert DeuxNombre(2, 3) == 5
    assert DeuxNombre(-2, 3) == 1
    assert DeuxNombre(0, 0) == 0

def test_MultipNombre():
    """Test multiplication"""
    assert DeuxNombre(2, 3) == 6
    assert DeuxNombre(-2, 3) == -6
    assert DeuxNombre(0, 0) == 0

    print("All tests pass")