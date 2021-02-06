"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""

def fortune():
    salary = {}
    try:
        with open('text5_3.txt', 'r', encoding='utf-8') as file:
            for string in file:
                salary[string.split()[0]] = float(string.split()[1])
        print('Менее 20000 руб. зарабатывают: ')
        for name, wage in salary.items():
            if wage < 20000:
                print(name)
        print(f'Средняя ЗП равна {round(sum(salary.values()) / len(salary), 2)} руб.')
        for name, wage in salary.items():
            if wage == max(salary.values()):
                print(f'Самая большая ЗП у {name}a - {wage} руб.')
    except IOError:
        print('Туже пояса!')
    except:
        print('неизвестная ошибка')
fortune()