import pygame as pg
import game
import snake

def processKeys(keyStroke):
    if keyStroke == pg.K_LEFT:
        snake.direct(snake.Direction.Left)
    if keyStroke == pg.K_RIGHT:
        snake.direct(snake.Direction.Right)
    if keyStroke == pg.K_UP:
        snake.direct(snake.Direction.Up)
    if keyStroke == pg.K_DOWN:
        snake.direct(snake.Direction.Down)

snake.initOn(game.gameWidth // 2, game.gameHeight // 2)

game.addApple()

while True:
    # обрабатываем события игры
    game.processEvents(processKeys)

    # проверяем условия выхода
    if game.isTouchBorder(snake.getNextPos().x, snake.getNextPos().y):
        quit()

    # стёрли из игрового поля хвост
    game.clearPoint(snake.getTail().x, snake.getTail().y)

    # сдвинем змейку
    snake.move(game)

    # добавили на поле новую голову
    eatedPoint = game.setSnakePoint(snake.getHead().x, snake.getHead().y)

    # кушаем яблочко
    if game.isApple(eatedPoint):
        snake.eatApple()
        game.addApple()

    if game.isSnake(eatedPoint):
        quit()

    game.draw()

    pg.time.delay(150)
