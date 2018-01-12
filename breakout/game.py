from math import floor, pi

from pygame import K_LEFT, K_RIGHT, QUIT, init, display, event, time, key, Color

from blocks import Brick, Ball, Paddle

WHITE = Color(255, 255, 255)

size = [420, 300]
init()
screen = display.set_mode(size)
screen.set_alpha(None)
paddle = Paddle(0, 280)
ball = Ball(225, 275)
ball.a = pi / 4
bricks = [Brick((i % 7) * 60, floor(i / 7) * 20) for i in range(35)]

done = False
while not done:
    time.wait(0)

    screen.fill(WHITE)

    for e in event.get():
        if e.type == QUIT:
            done = True

    keys = key.get_pressed()
    if len(keys) and (keys[K_LEFT] or keys[K_RIGHT]):
        paddle.move_x(5 if keys[K_RIGHT] else -5)

    paddle.draw(screen)
    ball.draw(screen)

    if paddle.rect.y == ball.rect.y + 5 and ball.k == 1 and paddle.rect.x < ball.rect.x < paddle.rect.x + 60:
        ball.bounce_y()

    if size[0] <= ball.rect.x + 10:
        ball.bounce_x(-5)

    if 0 >= ball.rect.x:
        ball.bounce_x(5)

    for brick in bricks:

        if brick.o is not 0 and ball.k == -1 and brick.rect.y + 19 == ball.rect.y and (brick.rect.x < ball.rect.x < brick.rect.x + 60 or brick.rect.x < ball.rect.x + 10 < brick.rect.x + 60):
            ball.bounce_y()
            brick.o = 0

        if brick.o is not 0:
            brick.draw(screen)

    display.flip()
    ball.move(1)
