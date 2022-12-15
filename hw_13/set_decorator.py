print("Декоратор функції, яка повертає множину чисел.")
print()


def decor_1(func):
    numbers = []

    def decor_2(*args):
        for i in func(*args):
            numbers.append(i)
        numbers.sort()
        for j, k in enumerate(numbers):
            if k % 2 == 0:
                if k % 3 == 0:
                    print(f"{(j + 1):>{len(str(len(numbers)))}}-й елемент  |  "
                          f"{k:{len(str(max(numbers)))}}  |  "
                          "парне число    |  "
                          "кратне 3")
                else:
                    print(f"{(j + 1):>{len(str(len(numbers)))}}-й елемент  |  "
                          f"{k:{len(str(max(numbers)))}}  |  "
                          "парне число    |  "
                          "не кратне 3")
            else:
                if k % 3 == 0:
                    print(f"{(j + 1):>{len(str(len(numbers)))}}-й елемент  |  "
                          f"{k:{len(str(max(numbers)))}}  |  "
                          "непарне число  |  "
                          "кратне 3")
                else:
                    print(f"{(j + 1):>{len(str(len(numbers)))}}-й елемент  |  "
                          f"{k:{len(str(max(numbers)))}}  |  "
                          "непарне число  |  "
                          "не кратне 3")

    return decor_2


@decor_1
def set_gen(number: int = 10):
    import random
    int_set = set()
    while len(int_set) < number:
        int_set.add(random.randrange(1000))
    return int_set


set_gen()
