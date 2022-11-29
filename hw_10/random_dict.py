import random

print("Програма для перемноження значень словника.")

# створюю випадковий словник з 20 елементів
dict_1 = {a: random.randrange(1, 10) for a in range(20)}
print("Ваш словник:", dict_1)

# перемножую значення
mn = 1
for key in dict_1:
    mn *= dict_1.get(key)
print("Ваше значення:", mn)
