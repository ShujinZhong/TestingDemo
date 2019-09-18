import pytest

@pytest.mark.parametrize("a,b,expected", [
                            (2,3,5),
                            (3,7,10),
                            (-2,5,3),
                            (2,10,12)
                            ])
def test_add(a,b, expected):
  from calculate import add
  result = add(a,b)
  assert result == expected

@pytest.mark.parametrize("a,b,expected", [
                            (5,3,3),
                            (7,7,0),
                            (7,5,3),
                            (14,2,12)
                            ])
def test_sub(a,b,expected):
    from calculate import sub
    result = sub(a,b)
    assert result == expected
