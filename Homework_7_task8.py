def transpose_matrix(matrix):
    """
    Транспонирует матрицу.
    
    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    return list(map(list, zip(*matrix)))

def matrix_multiply(matrix1, matrix2):
    """
    Умножает две матрицы.
    
    >>> matrix_multiply([[1, 2]], [[3], [4]])
    [[11]]
    """
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
