print("Декоратор функції, який обробляє пароль.")
print()


def condit():
    print("Пароль має містити:\n"
          " - щонайменше 1 цифру,\n"
          " - щонайменше 1 букву,\n"
          " - щонайменше 1 спеціальний символ,\n"
          " - довжина пароля повинна бути не менше 8 символів,\n"
          " - пробіл та tab використовувати не дозволяється.")


def pass_checker(func):
    print("Будь ласка, створіть пароль.")
    condit()

    def analyser():
        while True:
            pass_analyser = func()
            # перевіряю та сповіщаю, якщо є пробіли чи табуляції
            if pass_analyser is None:
                print("\nУвага! Пробільні символи "
                      "і символи табуляції не дозволені!")
                condit()
                continue
            print(f"Ваш пароль: ' {pass_analyser} '")
            # перевіряю інші умови
            lit = 0
            numbs = 0
            err = 0
            for i in pass_analyser:
                if i.isalpha() is True:
                    lit += 1
                if i.isdigit() is True:
                    numbs += 1
            # якщо не виконані умови, друкую, які саме
            if lit == 0:
                print("Ваш пароль не містить літер.")
                err += 1
            if numbs == 0:
                print("Ваш пароль не містить цифр.")
                err += 1
            if pass_analyser.isalnum() is True:
                print("Ваш пароль не містить спеціальних символів.")
                err += 1
            if len(pass_analyser) < 8:
                print("Ваш пароль менше 8 символів.")
                err += 1
            # якщо є помилки, запитую пароль знову
            if err > 0:
                continue
            # якщо з паролем усе гаразд, сповіщаю про це та повертаю пароль
            print("Пароль прийнятний.")
            break

        return pass_analyser

    return analyser


@pass_checker
def pass_input():
    password = input("Введіть пароль: ")
    if " " in password or "\t" in password or len(password) == 0:
        return None
    else:
        return password


pass_input()
