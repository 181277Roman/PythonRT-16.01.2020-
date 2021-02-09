
"""
Реализовать базовый класс Worker (работник).
● определить атрибуты: name , surname , position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker ;
● в классе Position реализовать методы получения полного имени сотрудника
( get_full_name ) и дохода с учётом премии ( get_total_income );
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return  f'{self.name} {self.surname}'
    def get_full_profit(self):
        return f'{sum(self._income.values())}'
employee = Position('Mr. Gomer', 'Simpson', 'Safety inspector', 13000, 2000)
print(employee.get_full_name())
print(employee.position)
print(employee.get_full_profit())



