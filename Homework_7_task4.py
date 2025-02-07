def is_even(n: int) -> bool:
    """
    Проверяет, является ли число четным.
    
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return n % 2 == 0

def factorial(n: int) -> int:
    """
    Вычисляет факториал числа.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
