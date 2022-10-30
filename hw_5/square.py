print("""Програма знаходження чисел, які менші за задане, та їх квадрати менші за задане число.""")

number = int(input("Введіть ваше число цифрами: "))
print(number, "\b:  ", end="")
for i in range(0, number):
    if i ** 2 < number:
        print(i ** 2, end=" ")
    else:
        break
