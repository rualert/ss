from enum import Enum
from tkinter import RIGHT


class Point:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y


class Direction(Enum):
    Left = 0
    Right = 1
    Down = 2
    Up = 3


direction = Direction.Right

def initOn(x, y):
    global snake
    snake = [Point(x, y), Point(x-1, y)]


def getHead():
    return snake[0]


def getTail():
    return snake[len(snake) - 1]


def eatApple():
    snake.append(Point(0, 0))


def direct(newDirection):
    global direction

    if newDirection == Direction.Left and direction == Direction.Right:
        return

    if newDirection == Direction.Right and direction == Direction.Left:
        return

    if newDirection == Direction.Up and direction == Direction.Down:
        return

    if newDirection == Direction.Down and direction == Direction.Up:
        return

    direction = newDirection


def getNextPos():
    direct = 0, 0
    if direction == Direction.Right:
        direct = 1, 0

    if direction == Direction.Left:
        direct = -1, 0

    if direction == Direction.Down:
        direct = 0, 1

    if direction == Direction.Up:
        direct = 0, -1

    return Point(direct[0] + getHead().x, direct[1] + getHead().y)


def move(game):
    nextPos = getNextPos()
    # положим новое значение головы
    snake.insert(0, Point(nextPos.x, nextPos.y))
    # удалим жопку змеи
    snake.pop(-1)
