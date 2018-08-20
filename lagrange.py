import math


def f(x):
    """
    Función que evalua una función.
    :param x: Punto en la función a evaluar.
    :return: Valor numérico de la función en el punto 'x'.
    """
    return x*math.exp(x)


table = ((1, f(1)), (2, f(2)), (3, f(3)))
inter = (table[0][0] - 1, table[1][0] - 1, table[2][0] - 1)
test = (1.5, 2.5, 3.5)
realev = []
aproev = []
errev = []


def lagrange(v):
    """
    Función que aproxima una serie de puntos, por medio de la interpolación de Lagrange.
    :param v: Punto a evaluar en la interpolación.
    :return: Valor aproximado del punto v, en la interpolación.
    """
    p = 0
    for r in inter:
        p = p + table[r][1]*li(r, v)
    return p


def li(r, v):
    """
    Función que devuelve 'li', perteneciente a la ecuación de interpolación de Lagrange.
    :param r: Valor actual.
    :param v: Punto a evaluar en la interpolación.
    :return: Valor de 'li' en base al punto 'r'.
    """
    fuc = 1
    for q in inter:
        if q != r:
            fuc = fuc*(v - table[q][0]) / (table[r][0] - table[q][0])
    return fuc


def err(vn, vl):
    """
    Función que calcula el error relativo.
    :param vn: Valor actual.
    :param vl: Valor anterior.
    :return: Error relativo en base a los dos valores.
    """
    return abs((vn-vl)/vn)


def testing():
    """
    Función que realiza la prueba de aproximación, en base a la tupla 'test'.
    :return: None
    """
    for q in test:
        realev.append(f(q))
        aproev.append(lagrange(q))
    for j in range(0, len(table)):
        errev.append(err(realev[j], aproev[j]))
    print(realev)
    print(errev)
