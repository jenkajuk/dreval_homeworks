print("Програма для створення списка чисел, не кратних 20")
print()

# створюю список чисел від 10 до 250
my_list = list(range(10, 251))

# присвоюю новий список
for i in my_list:
    if i % 20 == 0:
        my_list.remove(i)

# виводжу список на екран
print("Наш список має вигляд:")

for i, b in enumerate(my_list):
    print(f"{str(b):5}", end="")
    if (i + 1) % 11 == 0:
        print("")
print()
