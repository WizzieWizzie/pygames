import os

import pygame


class Bird:

    def __init__(self, img_dir):
        files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]
        self.images = list(map((lambda f: pygame.image.load(os.path.join(img_dir, f))), files))

    def blit(self, surface, dest, i=0):
        surface.blit(self.images[i], dest)

    def length(self):
        return len(self.images)
