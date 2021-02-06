"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

dict_of_numb = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text5_4_trans.txt', 'w', encoding='utf-8') as rus_numb:
    with open('text5_4.txt', 'r', encoding='utf-8') as eng_numb:
        rus_numb.writelines(string.replace(string.split()[0], dict_of_numb.get(string.split()[0])) for string in eng_numb)

