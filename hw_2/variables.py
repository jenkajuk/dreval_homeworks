print("""Завдання 1. Заміна значень 2х змінних використовючи 3-тю змінну.\n""")

variable1 = 10
variable2 = 50
print("""Змінна "1" -""", variable1, "\b,", """змінна "2" -""", variable2, "\b.")

variable3 = variable2
variable2 = variable1
variable1 = variable3
print("""Змінна "1" -""", variable1, "\b,", """змінна "2" -""", variable2, "\b.\n")

print("""Завдання 2. Заміна значень 2х змінних використовуючи властивості python.\n""")

variable_a = 100
variable_b = 20
print("""Змінна "a" -""", variable_a, "\b,", """змінна "b" -""", variable_b, "\b.")

variable_a, variable_b = variable_b, variable_a
print("""Змінна "a" -""", variable_a, "\b,", """змінна "b" -""", variable_b, "\b.\n")

print("""Завдання 3. Заміна значень 2 змінних не використівуючи 2х попредніх варіантів.\n""")

# мушу зауважити, спосіб підходить лише для числових змінних

var1 = 7
var2 = 8
print("""Змінна "1" -""", var1, "\b,", """змінна "2" -""", var2, "\b.")

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print("""Змінна "1" -""", var1, "\b,", """змінна "2" -""", var2, "\b.")
