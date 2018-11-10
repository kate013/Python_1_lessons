# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimeter(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def sq(self):
        self.perimetr /=2
        self.sq=  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.sq)

    def hgt(self):
        self.sq *=2
        self.hgt =  round((self.sq / self.CA),2)
        return (self.hgt)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

my_tri = Triangle(4,4,7,6,3,8)


print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC,my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimeter()))
print('Площадь треугольника АВС равна {}'.format(my_tri.sq()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.hgt()))


