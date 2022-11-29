print("Програма для друку максимуму та мінімуму входжень слів у вірш.")

str_1 = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами."""

# видаляю зайві символи
symbs = ".,—"
for el in symbs:
    str_1 = str_1.replace(el, "")

# створюю список зі слів
list_1 = str_1.lower().split()

# створюю словник з ключами-словами та значеннями-вживаностями
dict_1 = {}
for word in list_1:
    if word in dict_1:
        dict_1[word] += 1
    if word not in dict_1:
        dict_1.setdefault(word, 1)

# визначаю найбільш і найменш вживані слова
max_dict = {k: v for k, v in dict_1.items() if v == max(dict_1.values())}
min_dict = {k: v for k, v in dict_1.items() if v == min(dict_1.values())}
if len(max_dict) > 1:
    print("Найбільш вживані слова: ")
elif len(max_dict) == 1:
    print("Найбільш вживане слово: ")
for el in max_dict:
    print(" " * 23, f"'{el}', зустрічається у вірші разів - {max_dict[el]}")
if len(min_dict) > 1:
    print("Найменш вживані слова: ")
elif len(min_dict) == 1:
    print("Найбільш вживане слово: ")
for el in min_dict:
    print(" " * 23, f"'{el}', зустрічається у вірші разів - {min_dict[el]}")
