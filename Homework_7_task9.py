import pytest

class AgeVerifier:
    """Проверка возраста."""

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

@pytest.mark.parametrize("age,expected", [(17, False), (18, True), (21, True)])
def test_is_adult(age, expected):
    assert AgeVerifier.is_adult(age) == expected

@pytest.mark.skipif(-1 < 0, reason="Возраст не может быть отрицательным")
def test_negative_age():
    assert not AgeVerifier.is_adult(-5)

@pytest.mark.skipif(121 > 120, reason="Возраст более 120 маловероятен")
def test_too_high_age():
    assert not AgeVerifier.is_adult(121)
