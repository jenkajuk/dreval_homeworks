print("Програма виконує пошук антропоморфних чисел, не більших за задане.")

number = 1 + int(input("Введіть ваше число цифрами: "))
for i in range(1, number):
    a = i ** 2
    if str(i) in str(a):
        k = 1
        for j in str(i):
            k *= 10
            if a - a // k * k == i:
                print(i, "x", i, "=", a)
