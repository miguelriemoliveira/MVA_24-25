

from functools import partial


def somar_e_multiplicar_por_x(p1, p2, x):
    return (p1 + p2) * x


def main():

    somar_e_multiplicar_por_x_2 = partial(somar_e_multiplicar_por_x, x=2)

    a = 8
    b = 5
    # c = somar_e_multiplicar_por_x(a, b, 2)
    c = somar_e_multiplicar_por_x_2(a, b)
    print('a=' + str(a))
    print('b=' + str(b))
    print('c=' + str(c))

    a = 3
    b = 1
    c = somar_e_multiplicar_por_x(a, b, 2)
    print('a=' + str(a))
    print('b=' + str(b))
    print('c=' + str(c))

    a = 1
    b = 0
    c = somar_e_multiplicar_por_x(a, b, 2)
    print('a=' + str(a))
    print('b=' + str(b))
    print('c=' + str(c))

    d = {'a': 1, 'b': 0, 'c': somar_e_multiplicar_por_x_2(a, b)}
    print(d)


if __name__ == "__main__":
    main()
