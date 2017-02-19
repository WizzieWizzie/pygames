import pygame

class Invader:
    def __init__(self, name, size, colour, screen):
        self.index = 0
        self.size = size
        self.colour = colour
        self.frames = []
        self.screen = screen
        self.read_frames(name)

    def read_frames(self, name):
        frame = []
        f = open('./data/' + name + '.dat', 'r')

        for line in f:
            line = line.strip()

            if len(line) == 0:
                continue

            if line == '-':
                self.frames.append(frame)
                frame = []
                continue

            frame.append(tuple(map(int, line.split())))

        self.frames.append(frame)
        f.close()

    def next_frame(self):
        self.index = self.index + 1
        if self.index >= len(self.frames):
            self.index = 0

    def draw_frame(self, x, y):
        for c in self.frames[self.index]:
            _x = c[0] * self.size + x
            _y = c[1] * self.size + y
            rect = pygame.Rect(_x, _y, c[2] * self.size, self.size)
            pygame.draw.rect(self.screen, self.colour, rect, 0)
