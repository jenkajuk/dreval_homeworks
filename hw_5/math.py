print("""Програма виконує аналіз заданих цілих чисел.
Введіть потрібні числа цифрами.
Щоб закінчити введення чисел, введіть: 0""")

summing = 0
aver = 0
k_aver = 0
max_n = 0
min_n = 0
even = 0
odd = 0

while True:
    number = int(input("Введіть ваше число: "))
    if number != 0:
        summing += number
        k_aver += 1
        if max_n == 0:
            max_n += number
        if number > max_n:
            max_n = number
        if min_n == 0:
            min_n += number
        if number < min_n:
            min_n = number
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        break

aver = summing / k_aver

print("Сума введених чисел:", summing)
print("Середнє значення:", aver)
print("Максимальне значення:", max_n)
print("Мінімальне значення:", min_n)
print("Кількість парних чисел:", even)
print("Кількість непарних чисел:", odd)
