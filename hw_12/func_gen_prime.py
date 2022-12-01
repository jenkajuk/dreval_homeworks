import random

print("Функція-генератор простих чисел у заданому діапазоні.")
print()


def func_gen_prime(start_diap, final_diap):
    """
    Функція отримує на вхід два числа, які визначають межі діапазону,
    та генерує в цьому діапазоні усі прості числа.
    Функція працює як в прямому (від меншого числа до більшого),
    так і у зворотному напрямку (від більшого числа до меншого).

    :param start_diap: початкова межа діапазону, входить у діапазон
    :param final_diap: кінцева межа діапазону, не входить у діапазон
    """
    step = 1
    if start_diap > final_diap:
        step = -1
    for element in range(start_diap, final_diap, step):
        trigger = 0
        for j in range(1, element):
            if element % j == 0 and j != 1:
                trigger = 0
                break
            trigger = 1
        if trigger == 1:
            yield element


n = random.randint(0, 100)
z = random.randint(0, 100)
print(f"Початок діапазону - {n}, кінець діапазону - {z}.")
for i in func_gen_prime(n, z):
    print(i, end=" ")
print()
print()
n = random.randint(0, 100)
z = random.randint(0, 100)
print(f"Початок діапазону - {n}, кінець діапазону - {z}.")
for i in func_gen_prime(n, z):
    print(i, end=" ")
print()
