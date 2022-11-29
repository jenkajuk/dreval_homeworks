print("Програма для створення словника з рядка.")

# задаю рядок
str_1 = 'python is good language to code'
print("Ваш рядок:", str_1)

# видаляю пробіли з рядка
str_1 = str_1.replace(" ", "")

# створюю словник
dict_1 = {}
for a in str_1:
    if a in dict_1:
        dict_1[a] += 1
    if a not in dict_1:
        dict_1.setdefault(a, 1)
print("Ваш словник:", dict_1)
