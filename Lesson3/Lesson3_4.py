
def my_func(x, y):
    total = x**y
    if x <= 0:
        print("Ошибка ввода действительного числа - Х ")
    elif y >= 0:
        print("Ошибка ввода значения степени - Y ")
    else:
        print(float(f"{total:,.2f}"))

my_func(2, -3)

