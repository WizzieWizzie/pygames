import pygame

def cannon(position, step):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        position['x'] = position['x'] - step
    if keys[pygame.K_RIGHT]:
        position['x'] = position['x'] + step

    return position
