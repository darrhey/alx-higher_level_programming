#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        string = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError("{} must be a list".format(string))
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0] == 0)):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0] == 0)):
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if not type(j) in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if not type(j) in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])

    for i in m_a:
        if len_m_a != len(i):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if len_m_b != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if len_m_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new = [[0 for a in m_b[0]] for b in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new[i][j] += m_a[i][k] * m_b[k][j]
    return new
