print("Програма для створення квадратної матриці з парними/непарними строками")

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

# створюю ітерабельний об'єкт для генерації матриці
matrix = ([j for i in range(N)]
          if j % 2 == 0 else [k for k in range(-N, 0)] for j in range(N))

# виводжу на друк
for element in matrix:
    print("[", end="")
    for el_1 in element:
        print(f"{el_1:>{len(str(-N))}}, ", end="")
    print("\b\b]")
