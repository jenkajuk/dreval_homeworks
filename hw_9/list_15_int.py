import random

print("Програма аналізу списку з 15 випадкових чисел")

# створюю список з 15 випадкових чисел
an_list = [random.randrange(-1001, 1001) for i in range(15)]
print("Ваш список має вигляд:", an_list)

# виконую аналіз за умовою
print("Чи більша сума непарних чисел у списку",
      "за суму парних чисел? - ", end="")
even = sum(i for i in an_list if i % 2 == 0)
odd = sum(j for j in an_list if j % 2 != 0)
if even < odd:
    print("Так.")
else:
    print("Ні.")
