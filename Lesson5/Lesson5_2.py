"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""


with open('text5_2.txt') as s_a_w:

    my_count = s_a_w.readlines()
    for i, val in enumerate(my_count, 1):
        c_o_w = len(val.split())
        print(f'The string # {i} has {c_o_w} words')