import random

print("Програма аналізу списку з 15 випадкових чисел")

# створюю список з 15 випадкових чисел
an_list = [random.randrange(-1001, 1001) for i in range(15)]
print("Ваш список має вигляд:", an_list)

# виконую аналіз за умовою
# вважаю, що список починається з парного числа (нульового)
print("Чи більша сумма непарних чисел у списку за суму парних чисел? - ", end="")
if sum(j for i, j in enumerate(an_list) if i % 2 != 0) > sum(j for i, j in enumerate(an_list) if i % 2 == 0):
    print("Так.")
else:
    print("Ні.")
