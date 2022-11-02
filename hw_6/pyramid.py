print("Программа для друку піраміди.")

blocks = "123456789"
number = input("Введіть число від 3 до 9 цифрою: ")

if number.isdigit():
    if 3 <= int(number) <= 9:
        # без вирівнювання
        i = 0
        while i < int(number):
            print(blocks[:i], blocks[i::-1], sep="")
            i += 1

        # вирівнювання по центру (1й спосіб)
        i = 0
        while i < int(number):
            print((blocks[:i] + blocks[i::-1]).center(2 * int(number) - 1))
            i += 1

        # вирівнювання по центру (2й спосіб)
        i = 0
        while i < int(number):
            print(blocks[:i].rjust(int(number) - 1), blocks[i::-1], sep="")
            i += 1

        # вирівнювання за правим краєм
        i = 0
        while i < int(number):
            print(blocks[:i].rjust(2 * (int(number) - 1) - i), blocks[i::-1], sep="")
            i += 1
    else:
        print("Ви ввели число поза можливим діапазоном.")
else:
    print("Неправильно введене число.")
