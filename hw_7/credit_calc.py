print("Кредитний калькулятор")
print()

a, b, c = "Місяць", "Сума до сплати", "B т.ч. нараховано %"
summ = input("Введіть цифрами сумму, яку хочете взяти під кредит: ")

if summ.isdigit():
    print(f"Ваша сума бажаного кредиту - {summ} грн.")
    year = input("Введіть цифрою кількість років, на які берете кредит (1 рік чи 5 років): ")
    if year.isdigit():
        # на 1 рік:
        if int(year) == 1:
            # шапка таблиці
            print("Кредитні умови на 1 рік:\n"
                  "Кредитна ставка на 1 рік - 2% місячних\n",
                  f"{a} | {b} | {c}", sep="")

            summ = int(summ)
            pl_1 = 0
            pl_2 = 0
            pl_3 = 0
            # обчислюю платежі та відсотки для 1 року
            for i in range(1, 13):
                print(f"{i:^6} | "
                      f"{(summ / 12 + (summ - pl_1) * 0.02):^14.2f} | "
                      f"{((summ - pl_1) * 0.02):^17.2f}", sep="")
                pl_2 += summ / 12 + (summ - pl_1) * 0.02
                pl_3 += (summ - pl_1) * 0.02
                pl_1 += summ / 12
            print(f"Разом: | ",
                  f"{pl_2:^14.2f} | "
                  f"{pl_3:^17.2f}", sep="")

        # на 5 років
        elif int(year) == 5:
            # шапка таблиці
            print("Кредитні умови на 5 років:\n"
                  "Кредитна ставка на 1й та 2й роки - 2% місячних\n",
                  "Кредитна ставка на 3й - 5й роки - 4% місячних\n",
                  f"{a} | {b} | {c}", sep="")

            summ = int(summ)
            pl_1 = 0
            pl_2 = 0
            pl_3 = 0
            # обчислюю платежі та відсотки для 5 років
            # для перших 2х років
            for i in range(1, 25):
                print(f"{i:^6} | "
                      f"{(summ / 60 + (summ - pl_1) * 0.02):^14.2f} | "
                      f"{((summ - pl_1) * 0.02):^17.2f}", sep="")
                pl_2 += summ / 60 + (summ - pl_1) * 0.02
                pl_3 += (summ - pl_1) * 0.02
                pl_1 += summ / 60
            # для останніх трьох років
            for i in range(25, 61):
                print(f"{i:^6} | "
                      f"{(summ / 60 + (summ - pl_1) * 0.04):^14.2f} | "
                      f"{((summ - pl_1) * 0.04):^17.2f}", sep="")
                pl_2 += summ / 60 + (summ - pl_1) * 0.04
                pl_3 += (summ - pl_1) * 0.04
                pl_1 += summ / 60
            print(f"Разом: | ",
                  f"{pl_2:^14.2f} | "
                  f"{pl_3:^17.2f}", sep="")
        else:
            print("На таких умовах кредит не надається.")
    else:
        print("Помилка, не правильно введений рік.")
else:
    print("Введена сума не відповідає вимогам")