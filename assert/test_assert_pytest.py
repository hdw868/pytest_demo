def test_assert_info():
    a = 1
    b = [2, 3, 4]
    assert a in b


def test_assert_with_approx():
    from pytest import approx
    assert 0.123456789 == approx(0.123456788)