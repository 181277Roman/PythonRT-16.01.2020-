
def my_func(x, y):
    total = pow(x, y)
    if x <= 0:
        print("Ошибка ввода действительного числа - Х ")
    elif y >= 0:
        print("Ошибка ввода значения степени - Y ")
    else:
        print(float(f"{total:,.3f}"))

my_func(2.5, -3)