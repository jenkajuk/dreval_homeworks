print("Функція перевірки еквівалентності чисел у списку заданому числу.")


def func_1(a, b):
    """
    Функція отримує на вхід список чисел і окремо число та перевіряє,
    чи є в списку пара чисел, сума яких дорівнює окремому числу.

    :param a: список чисел для перевірки
    :param b: число для перевірки
    :return: False або True
    """
    a = list(a)
    result = False
    for i in a:
        if b - i in a:
            result = True
            break
    return result


print(func_1([1, 2, 3, 4, 5, 6, 7], 9))
print(func_1((i for i in range(0, 15, 3)), 4))
