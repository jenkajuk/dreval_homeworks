print("Програма перевіряє, чи присутні у вашому числі однакові цифри.")

c = 0  # лічильник співпадінь чисел
number = input("Введіть ваше число цифрами: ")

for i in number:
    for b in number:
        if b == i:
            c += 1
    if c >= 2:
        break
    else:
        c = 0
print("Так, присутні однакові числа.") if c >= 2 else print("Ні, відсутні однакові числа.")
