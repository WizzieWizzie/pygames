from math import pi, tan
from pygame import Color, Rect, draw


class Block:

    def __init__(self, x, y, d, c):
        self.d = d
        self.colour = c
        self.rect = Rect(x, y, self.d['w'], self.d['h'])

    def draw(self, surface):
        draw.rect(surface, self.colour, self.rect)


class Brick(Block):

    def __init__(self, x, y):
        Block.__init__(self, x, y, {'w': 60, 'h': 20}, Color(47, 79, 79))
        self.rect = Rect(x + 1, y + 1, self.d['w'] - 2, self.d['h'] - 2)
        self.o = 1


class Paddle(Block):

    def __init__(self, x, y):
        Block.__init__(self, x, y, {'w': 60, 'h': 20}, Color(47, 79, 79))

    def move_x(self, k):
        self.rect.x = self.rect.x + k


class Ball(Block):

    def __init__(self, x, y):
        Block.__init__(self, x, y, {'w': 10, 'h': 5}, Color(0, 0, 0))
        self.a = pi / 12
        self.k = -1
        self.i = 0
        self.p = {'x': self.rect.x, 'y': self.rect.y}

    def move(self, k):
        self.rect.y = self.p['y'] + self.i * self.k
        self.rect.x = self.p['x'] + tan(self.a) * self.i
        self.i = self.i + k

    def bounce_x(self, k):
        self.i = 0
        self.a = -self.a
        self.rect.x = self.rect.x + k
        self.p = {'x': self.rect.x, 'y': self.rect.y}

    def bounce_y(self):
        self.i = 0
        self.k = -self.k
        self.p = {'x': self.rect.x, 'y': self.rect.y}
