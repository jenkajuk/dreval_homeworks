print("Програма для створення словника з двох списків.")

# задаю списки
list_1 = [a for a in "abcdefg"]
print("Перший список:", list_1)
list_2 = [a for a in range(1, 8)]
print("Другий список:", list_2)

# створюю словник
dict_1 = dict(zip(list_1, list_2))
print("Ваш словник:", dict_1)
