print("Програма для об'єднання двох словників різними методами.")

# задаю словники
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}

# об'єдную словники:
# спосіб 1:
dictionary_3 = dictionary_1 | dictionary_2
print(dictionary_3)

# спосіб 2:
dictionary_3.clear()
dictionary_3 = {**dictionary_1, **dictionary_2}
print(dictionary_3)

# спосіб 3:
while len(dictionary_2) != 0:
    a = dictionary_2.popitem()
    dictionary_1.update([a])
print(dictionary_1)

# спосіб 4:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)
