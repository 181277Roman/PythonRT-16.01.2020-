
"""
1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
© geekbrains.ru 18
# класс Bus, наследующий Transport
class Bus (Transport):
def show_info (self):
print( "Родительский метод класса Bus" )
t = Transport()
t.show_info()
a = Auto()
a.show_info()
b = Bus()
b.show_info()
Родительский метод класса Transport
Родительский метод класса Auto
Родительский метод класса Bus
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.

"""
import time

class Trafficlight:
    __color = 'Black'

    def running(self):
        while True:
            print(f"\033[41m Красный свет светофора", end='')
            time.sleep(5)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[41m Красный свет светофора", end='')
            time.sleep(1)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[41m Красный свет светофора", end='')
            time.sleep(1)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[43m Жёлтый свет светофора", end='')
            time.sleep(5)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[42m Зелёный свет светофора", end='')
            time.sleep(5)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[42m Зелёный свет светофора", end='')
            time.sleep(1)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[42m Зелёный свет светофора", end='')
            time.sleep(1)
            print(f'', end=" \r")
            time.sleep(1)
            print(f"\033[41m Красный свет светофора", end='')
            time.sleep(1)
            print(f'', end=" \r")

trafficlight = Trafficlight()
trafficlight.running()
