def foo():
    return 1


def test_simple_case():
    """straight forward in pytest"""
    b = [2, 3, 4]
    assert foo() in b
