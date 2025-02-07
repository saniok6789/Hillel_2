import pytest

def divide(a: int, b: int) -> float:
    """Делит два числа, выбрасывает исключение при делении на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b

@pytest.mark.parametrize("a,b,result", [(10, 2, 5), (9, 3, 3), (100, 4, 25)])
def test_divide(a, b, result):
    assert divide(a, b) == result

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
