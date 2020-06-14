def foo():
    return 1


def simple_case():
    b = [2, 3, 4]
    assert foo() in b


if __name__ == '__main__':
    simple_case()
