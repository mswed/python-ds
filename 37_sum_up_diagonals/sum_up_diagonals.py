def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    tl_to_br = []
    cell = 0
    for row in matrix:
        tl_to_br.append(row[cell])
        cell += 1

    bl_to_tr = []
    matrix.reverse()
    cell = 0
    for row in matrix:
        bl_to_tr.append(row[cell])
        cell += 1

    return sum(tl_to_br) + sum(bl_to_tr)
