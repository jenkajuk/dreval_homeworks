print('''Вас вітає програма "Домашня робота 4.3"''')

# задаю словник для паролів та їх власників
passwords = {"мій_пароль": "Євген Древаль", "qwerty1234": "Тетяна Супрун", "25011991": "Михайло Білий"}

# вводимо пароль та перевіряємо його присутність у словнику
i = 0
while i < 3:
    b = input("Будь ласка, введіть пароль: ")
    if b in passwords:
        print("Пароль прийнято. Вітаю,", passwords.get(b), "\b.")
        break
    else:
        print("Не вірний пароль.")
        i += 1
        if i >= 3:
            print("В доступі відмовлено. Зверніться до master33life@ukr.net для відновлення пароля.")
