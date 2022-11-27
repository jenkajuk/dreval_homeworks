import random

print("Програма для створення квадратної матриці з випадковими значеннями")

# отримую значення розміру матриці від користувача на вхід
N = 0
while N == 0:
    N = input("Введіть розмір матриці (ціле число цифрами): ")
    if N.isdigit() is True:
        N = int(N)
        if N < 1:
            print("Помилка. Немає даних для виводу.")
    else:
        print("Помилка. Ви ввели не число,",
              "використали літери чи інші символи.")
        N = 0

# створюю список-матрицю
matrix = [[random.randrange(-1101, 1101) for i in range(N)]for j in range(N)]

# визначаю символьний розмір елементів матриці
max_el = len(str(max(max(element) for element in matrix)))
min_el = len(str(min(min(element) for element in matrix)))
if max_el > min_el:
    length = max_el
else:
    length = min_el

# друкую матрицю
for element in matrix:
    print("[", end="")
    for el_1 in element:
        print(f"{el_1:>{length}}, ", end="")
    print("\b\b]")

# визначаю сумму чисел по діагоналі зліва/верх - вправо/вниз
diag_summ = sum(element[par] for par, element in enumerate(matrix))
print("Сума чисел по діагоналі зліва:", diag_summ)

# визначаю сумму чисел по діагоналі зправа/верх - вліво/вниз
diag_summ = sum(element[-1 - par] for par, element in enumerate(matrix))
print("Сума чисел по діагоналі справа:", diag_summ)

# визначаю сумму чисел в останньому стовбчику
col_summ = sum(element[-1] for element in matrix)
print("Сума чисел останнього стовпчика матриці:", col_summ)
