A_CONST = 903  # int(input('1 число: '))
B_CONST = 1435  # int(input('2 число: '))


def euclid(a_1, b_2):
    """Осуществляет алгоритм Евклида для целых чисел"""

    if a_1 == 0:
        return b_2
    elif b_2 == 0:
        return a_1

    y = min(a_1, b_2)
    x = max(a_1, b_2)
    r_ost = 0
    p_ost = 0

    while x > 0:
        p_ost = r_ost
        r_ost = x % y
        if r_ost == 0:
            break
        x = (x // y) * y
        y = r_ost
    if p_ost == 0:
        return min(a_1, b_2)
    elif (a_1 % p_ost != 0) or (b_2 % p_ost != 0):
        p_ost = min(euclid(a_1, p_ost), euclid(b_2, p_ost))
        return(p_ost)
    else:
        return(p_ost)


def euclid_advanced(a_1, b_2):
    """Расширенный алгоритм Евклида для целых чисел"""
    p_ost = euclid(a_1, b_2)  # для начала выполним прямой алгоритм Евклида
    for i in range(1, a_1):
        for k in range(1, b_2):
            if p_ost == a_1 * i - b_2 * k:
                return(i, -k)
            elif p_ost == b_2 * k - a_1 * i:
                return(-i, k)


print(euclid_advanced(A_CONST, B_CONST))
