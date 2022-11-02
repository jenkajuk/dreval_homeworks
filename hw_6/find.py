print("Программа для пошуку символів.")

string = input("Введіть рядок для пошуку: ")
char = input("Введіть символ, який потрібно знайти: ")

count = 0
a = 0

while string.find(char, a) > -1:
    if string.find(char, a) > -1:
        # для наглядності позицію символа на виводі іменую не з нульового, а з першого
        print("Cимвол '", char, "' знаходиться на ", string.find(char, a) + 1, " місці", sep="")
        count += 1
        a = string.find(char, a) + 1

print("Знайдено символів:", count)
