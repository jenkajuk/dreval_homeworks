print("Програма для пошуку елементів одного списку в іншому списку.")
print()

# задаю списки
list_1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list_2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]

# видаляю повторювані елементи в першому списку та сортую його
list_1.sort()
for i in list_1:
    if list_1.index(i) != len(list_1) - 1 - list_1[::-1].index(i):
        list_1.remove(i)

# друкую таблицю значень
print("{0:^18}".format("Елемент"), "Кількість повторів")
all_count = 0
for j in list_1:
    print(f"{j:^18}", end="")
    count = 0
    if j in list_2:
        for k in list_2:
            if k == j:
                count += 1
        all_count += count
        print(f"{count:^20}")
    else:
        print(f"{count:^20}")
print("-"*37)
print("Всього повторів -", f"{all_count:^20}")
