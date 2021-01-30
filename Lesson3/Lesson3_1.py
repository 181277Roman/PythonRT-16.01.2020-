
def div_calc(f_number, s_number):
    try:
        sub = f_number / s_number
    except ZeroDivisionError:
        return print("Вы не можете разделить на '0'")
    print(f"Результат деления: {sub:,.2f}")
div_calc(f_number=(float(input("Задайте первое значение: "))), s_number=(float(input("Задайте второе значение: "))))

