import pygame
from Invader import Invader

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode([500, 500])

l = 10
invader = Invader('ufo', l, BLACK, screen)
pos = { 'x': 0, 'y': 0 }

done = False
_x = 0
_y = -1
while not done:
    pygame.time.wait(250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and _y < 0:
                _x = pos['x'] + 70
                _y = 190

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        pos['y'] = pos['y'] - l
    if keys[pygame.K_DOWN]:
        pos['y'] = pos['y'] + l
    if keys[pygame.K_LEFT]:
        pos['x'] = pos['x'] - l
    if keys[pygame.K_RIGHT]:
        pos['x'] = pos['x'] + l

    screen.fill(WHITE)

    invader.draw_frame(pos['x'], pos['y'] + 200)
    invader.next_frame()

    if _y > -1:
        beam = pygame.Rect(_x, _y, l, 2 * l)
        pygame.draw.rect(screen, BLACK, beam, 0)
        _y = _y - l

    pygame.display.flip()
