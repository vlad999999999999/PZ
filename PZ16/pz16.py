# Практическое занятие №16 — Вариант 18
# Блок 1: Класс Круг с методами
# Блок 2: ООП-наследование — Транспорт -> Авто и Мото
# Блок 3: Сохраняем и загружаем 3 круга через pickle

import math
import pickle

# БЛОК 1

class Krug:
    def __init__(self, r):
        self.r = r  # кароч радиус круга

    def ploshad(self):
        return math.pi * self.r ** 2  # площадь круга

    def dlina(self):
        return 2 * math.pi * self.r  # длина окружности

    def diametr(self):
        return 2 * self.r  # диаметр 

    def __str__(self):
        return f'Круг: радиус={self.r}, площадь={self.ploshad():.2f}, длина={self.dlina():.2f}'

# БЛОК 2

class Transport:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

    def info(self):
        return f'Скорость: {self.max_speed}, колёс: {self.wheels}'

class Avto(Transport):
    def __init__(self, max_speed, wheels, marka):
        super().__init__(max_speed, wheels)
        self.marka = marka

    def info(self):
        return f'Авто {self.marka} — {super().info()}'

class Moto(Transport):
    def __init__(self, max_speed, wheels, obem):
        super().__init__(max_speed, wheels)
        self.obem = obem

    def info(self):
        return f'Мото {self.obem}cc — {super().info()}'

# БЛОК 3 

def save_def(obj_list, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj_list, f)  # сериализуем всё как есть
        print(f'в {file_name}')

def load_def(file_name):
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
        print(f'из {file_name}')
        return data

# ТЕСТЫ в общем 

if __name__ == '__main__':
    print(' 1')
    k1 = Krug(3)
    k2 = Krug(5)
    k3 = Krug(10)
    print(k1)
    print(k2)
    print(k3)

    print(' 2')
    a = Avto(220, 4, 'Lada')
    m = Moto(180, 2, 600)
    print(a.info())
    print(m.info())

    print(' 3')
    save_def([k1, k2, k3], 'krugi.dat')
    krugi = load_def('krugi.dat')
    for k in krugi:
        print(k)
