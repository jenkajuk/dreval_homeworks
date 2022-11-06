print("Програма для виведення трикутника")
print()

number = input("Введіть кількість рядків числом: ")

if number.isdigit():
    number = int(number)
    if number > 0:
        for i in range(number):
            print(f"{i:>{len(str(number - 1))}} "
                  f"{10 ** i:>{number}}")
    else:
        print("Немає що друкувати")
else:
    print("Помилка, введені дані не відповідають умовам")
