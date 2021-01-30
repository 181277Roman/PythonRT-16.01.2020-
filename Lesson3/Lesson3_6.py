"""
Реализовать функцию i nt_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func() .

"""

def int_func():
    """с исключением кириллицы, но с числами"""
    in_list = input("Enter a few words in English letters separated by a space: ").split()
    for word in in_list:
        test_word = ascii(word)
        print(test_word)
        rl = 'u04'
        if rl not in test_word:
            new_list = word.title()
            print(new_list)
        else:
            print("Error input words")

int_func()




