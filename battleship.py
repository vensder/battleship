#!/usr/bin/env bash python3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Field:

    def __init__(self, dimension=10):
        self.dimension = dimension

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        if dimension == 0:
            raise ValueError("No field -- no battle!")
        self.__dimension = abs(dimension)


class Ship:
    def __init__(self, size, position, is_vertical=True):
        self.size = size
        self.is_vertical = is_vertical
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def direction(self):
        return self.__direction

    @size.setter
    def size(self, size):
        if size == 0:
            raise ValueError("No ships -- no battle!")
        self.__size = abs(size)


map1 = Field(-11)
map2 = Field()
print(map1.dimension)
print(map2.dimension)

ship1 = Ship(1, Point(1, 1))
print(ship1.size)
print(ship1.position.x, ship1.position.y)
