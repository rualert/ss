import random
import pygame as pg

# создадим константы
ratio = 40
size = width, height = 600, 400
gameSize = gameWidth, gameHeight = width // ratio, height // ratio
emptyPoint = 0
snakePoint = 1
applePoint = 2


# инициализируем графику
pg.init()
screen = pg.display.set_mode(size)
pg.display.set_caption("Змейка на питоне")
pg.display.update()

# цвет
green = (0, 180, 0)
black = (0, 0, 0)
red = (180, 0, 0)

gameField = [[emptyPoint] * (gameHeight) for i in range(gameWidth)]


def draw():
    for i in range(gameWidth):
        for j in range(gameHeight):
            if gameField[i][j] == 0:
                pg.draw.rect(screen, black, (i * ratio, j * ratio, ratio, ratio))
            if gameField[i][j] == 1:
                pg.draw.rect(screen, green, (i * ratio, j * ratio, ratio, ratio))
            if gameField[i][j] == 2:
                pg.draw.rect(screen, red, (i * ratio, j * ratio, ratio, ratio))
    pg.display.update()


def isTouchBorder(x, y):
    return x <= -1 or x >= gameWidth or y <= -1 or y >= gameHeight

def isApple(val):
    return val == applePoint

def isSnake(val):
    return val == snakePoint

def addApple():
    x = random.randrange(0, gameWidth)
    y = random.randrange(0, gameHeight)
    while gameField[x][y] != 0:
        x = random.randrange(0, gameWidth)
        y = random.randrange(0, gameHeight)    
    gameField[x][y] = applePoint


def clearPoint(x, y):
    gameField[x][y] = emptyPoint


def setSnakePoint(x, y):
    if isTouchBorder(x, y):
        return

    oldValue = gameField[x][y]
    gameField[x][y] = snakePoint
    return oldValue

def processEvents(processKeys):
     for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            processKeys(event.key)