from module1 import foo


def test_foo():
    assert foo(1) == 1
    assert foo(2) == 4
    assert foo(3) == 9
