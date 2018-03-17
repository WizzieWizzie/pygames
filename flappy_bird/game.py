import pygame
from random import randint

# Colours
WHITE = pygame.Color(255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([300, 300])
frames_bird = []
for i in range(1, 4):
  img = pygame.image.load('img/bird/f{}.png'.format(i))
  frames_bird.append(img)

pipe = pygame.image.load('img/pipe.png')

i = 0
l = len(frames_bird)
y = 10
g = 5
n = 300
yy = randint(0, 10) - 5

done = False
while not done:

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      done = True

  keys = pygame.key.get_pressed()
  if len(keys) and keys[pygame.K_SPACE]:
      y = y - 15

  screen.fill(WHITE)

  screen.blit(pygame.transform.flip(pipe, False, True), (n, -210 + yy * 10))
  screen.blit(pipe, (n, 190 + yy * 10))

  a = -30 if g > 0 else 10
  screen.blit(frames_bird[i], (40, y))

  pygame.display.update()

  pygame.time.wait(50)

  i = 0 if i >= l -1 else (i + 1)
  y = y + g
  n = n - 5
  if n <= -52:
    n = 300
    yy = randint(0, 12) - 6

pygame.quit()
