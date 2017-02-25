import pygame
import control
from Invader import Invader

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode([500, 500])

l = 10
invaders = []

for i in range(0, 5):
    invaders.append({
        'x': i * l * 9,
        'y': 0,
        'o': Invader('squid', l, BLACK, screen)
    })

for i in range(0, 4):
    invaders.append({
        'x': i * l * 12,
        'y': 10 * l,
        'o': Invader('crab', l, BLACK, screen)
    })

for i in range(0, 4):
    invaders.append({
        'x': i * l * 13,
        'y': 20 * l,
        'o': Invader('jellyfish', l, BLACK, screen)
    })

pos_beam = { 'x': 0, 'y': -1 }
pos_cannon = { 'x': 0, 'y': 200 }

done = False
while not done:
    pygame.time.wait(250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pos_beam['y'] < 0:
                pos_beam = { 'x': pos_cannon['x'] + 70, 'y': 190 }

    screen.fill(WHITE)

    #pos_cannon = control.cannon(pos_cannon, l)
    for invader in invaders:
        pos = {
            'x': 0 + invader['x'],
            'y': 0 + invader['y']
        }
        invader['o'].draw_frame(pos)
        invader['o'].next_frame()

    if pos_beam['y'] > -1:
        beam = pygame.Rect(pos_beam['x'], pos_beam['y'], l, 2 * l)
        pygame.draw.rect(screen, BLACK, beam, 0)
        pos_beam['y'] = pos_beam['y'] - l

    pygame.display.flip()
