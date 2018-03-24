import pygame


class PipeObstacle:

    def __init__(self, img_file):
        self.image = pygame.image.load(img_file)

    def blit(self, surface, dest, width):
        w = width / 2
        a = pygame.transform.flip(self.image, False, True)
        surface.blit(a, (dest[0], dest[1] - 320 - w))
        b = self.image
        surface.blit(b, (dest[0], dest[1] + w))
