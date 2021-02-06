"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.

"""

import random

with open('text5_5.txt', 'w', encoding='utf-8') as list_number_f:
    list_number = [random.randint(1, 51) for i in range(51)]
    list_number_f.write(' '.join(map(str, list_number)))
print(f'Сумма набора чисел - {sum(list_number)}')

