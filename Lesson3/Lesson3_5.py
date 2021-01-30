
def my_sum():
    s = 0
    while True:
        my_list = input("Введите несколоко чисел через пробел, q для окончания расчёта: ").split()
        for i in range(len(my_list)):
            num_st = my_list[i]
            if num_st == 'q':
                return s
            else:
                int_list = list(map(int, my_list))
                sum_i = sum(int_list)
                try:
                    s = s + sum_i
                except ValueError:
                    print("Ошибка ввода числа")
                except TypeError:
                    print("Ошибка ввода числа")
        print(f"{sum_i} ({s})")

print(my_sum())
