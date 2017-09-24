import pygame
import utils

class Bike:

  def __init__(self, position):
    self.speed = 10
    self.colour = (255, 255, 255)
    self.trace_colour = (225, 228, 232)
    self.trace = [position]
    self.direction = (0, 0)

    position = (position[0] - 4, position[1] - 4)
    self.rect = pygame.Rect(position, (10, 10))


  def get_position(self):
    return (self.rect.x + 4, self.rect.y + 4)


  def set_position(self, position):
    self.rect.x = position[0] - 4
    self.rect.y = position[1] - 4


  def change_direction(self, direction):
    self.direction = direction
    self.trace.append(self.get_position())


  def next_position(self):
    self.rect.x = self.rect.x + self.direction[0] * self.speed
    self.rect.y = self.rect.y + self.direction[1] * self.speed


  def draw_bike(self, screen):
    pygame.draw.rect(screen, self.colour, self.rect, 0)


  def draw_trace(self, screen):
    trace = list(self.trace)
    trace.append(self.get_position())
    for i in range(len(trace) - 1):
      pygame.draw.line(screen, self.trace_colour, trace[i], trace[i + 1], 10)


  def is_on_trace(self, position):
    trace = list(self.trace)
    trace.append(self.get_position())
    for i in range(len(trace) - 2):
      if utils.is_on_line(position, trace[i], trace[i + 1]):
        return True

    return False


  def is_in_screen(self, dimensions):
    x = self.rect.x
    y = self.rect.y
    return x < 0 or y < 0 or x > (dimensions[0] - 10) or y > (dimensions[1] - 10)
