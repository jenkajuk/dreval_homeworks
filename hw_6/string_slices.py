print("Программа для обробки рядка.")

while True:
    string = input("Введіть рядок довжиною від 15 символів: ")
    if len(string) >= 15:
        break
    else:
        print("Введений рядок коротший за 15 символів.")

print("a. Третій символ рядка:", string[2])
print("b. Передостанній символ цього рядка:", string[-2])
print("c. Перші п'ять символів цього рядка:", string[:5])
print("d. Весь рядок, крім двох останніх символів:", string[:-2])
print("e. Усі символи з парними індексами:", string[::2])
print("f. Усі символи з непарними індексами:", string[1::2])
print("g. Усі символи у зворотному порядку:", string[::-1])
print("h. Усі символи рядка через один у зворотному порядку, починаючи з останнього:", string[::-2])
print("i. Довжина цього рядка:", len(string))
