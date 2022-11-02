print("Программа для перевернення слів.")

c = 0
while True:
    words = input("Введіть два слова через пробіл: ")
    if words.find(" ") == -1:
        print("Помилка. Ви ввели одне слово або не ввели пробіл.")
        continue
    elif words.find(" ") != words.rfind(" "):
        print("Помилка. Ви ввели більше двох слів.")
        continue
    else:
        c = words.find(" ")
    if not words.replace(" ", "j").isalpha():
        print("Помилка. Ви ввели не слова")
        continue
    else:
        break

print(words[c-1::-1].title(), words[:c:-1].title())
