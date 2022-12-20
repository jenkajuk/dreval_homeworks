import random
print("Програма для сортування елементів матриці.")
print()


def sorting(mtrx: list):
    m = len(mtrx)
    for i in range(m):
        for j in range(-1, -m + i, -1):
            if sum(mtrx[j]) < sum(mtrx[j - 1]):
                mtrx[j], mtrx[j - 1] = mtrx[j - 1], mtrx[j]

    for i in range(m):
        if i % 2 == 0:
            for j in range(m):
                for k in range(m - 1):
                    if mtrx[i][k] < mtrx[i][k + 1]:
                        mtrx[i][k], mtrx[i][k + 1] = mtrx[i][k + 1], mtrx[i][k]
        else:
            for j in range(m):
                for k in range(-1, -m + j, -1):
                    if mtrx[i][k] < mtrx[i][k - 1]:
                        mtrx[i][k], mtrx[i][k - 1] = mtrx[i][k - 1], mtrx[i][k]

    return mtrx


def printing(mtrx: list):
    m = len(mtrx)
    for i in range(m):
        for j in range(m):
            print(f"{mtrx[j][i]:>{len(str(sum(mtrx[j]))) + 1}} |", end="")
        print()

    for i in range(m):
        print("-" * (3 + len(str(sum(mtrx[i])))), end="")
    print()

    for i in range(m):
        print(f"{sum(mtrx[i]):>{len(str(sum(mtrx[i]))) + 1}} |", end="")
    print()


if __name__ == "__main__":
    M = 0
    while M < 5:
        M = input("Введіть 'М' для створення матриці 'МхМ'.\n"
                  "'М' повинно бути додатним цілим числом, більшим за 5: ")
        if M.isdigit() is False:
            print("Помилка. Введене значення не відповідає вимогам.")
            M = 0
            continue
        else:
            M = int(M)

    matrix = [[random.randint(1, 50) for j in range(M)] for i in range(M)]

    print("До сортування:")
    printing(matrix)
    print("Після сортування:")
    printing(sorting(matrix))
