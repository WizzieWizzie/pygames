import os.path
import random
import time

import pygame
import bird
import pipe

WHITE = pygame.Color(255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([300, 300])
bird_yellow = bird.Bird(os.path.join('img', 'bird'))
pipe = pipe.PipeObstacle(os.path.join('img', 'pipe.png'))

tb = round(1000 / 8)
t1 = round(time.time() * 1000)

i = 0
y = 10
g = 3
n = 300
yy = 0

done = False
while not done:

    t = round(time.time() * 1000)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if len(keys) and keys[pygame.K_SPACE]:
        y = y - 5

    screen.fill(WHITE)
    pipe.blit(screen, (n, 150 + yy * 10), 80)
    bird_yellow.blit(screen, (40, y), i)
    pygame.display.update()

    y = y + g
    n = n - 3
    if n <= -52:
        n = 300
        yy = random.randint(0, 12) - 6

    if tb <= (t - t1):
        i = 0 if i >= bird_yellow.length() - 1 else (i + 1)
        t1 = t

pygame.quit()
