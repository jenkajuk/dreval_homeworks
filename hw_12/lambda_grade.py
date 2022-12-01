print("Функція піднесення числа 'х' до степені 'у'.")
print()

print("Один список чисел для обробки у функції map:",
      list(map(lambda x, y=2: x ** y, (i for i in range(10)))))
print("Два списки чисел для обробки у функції map:",
      list(map(lambda x, y=1: x ** y, (i for i in range(10)),
               (j for j in range(10)))))
