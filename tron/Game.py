import pygame
import json
from Bike import Bike
from GameSocket import GameSocket


class Game:
    GREY = (36, 39, 41)

    K_DICT = {
        pygame.K_UP: ((0, -1), pygame.K_DOWN),
        pygame.K_DOWN: ((0, 1), pygame.K_UP),
        pygame.K_LEFT: ((-1, 0), pygame.K_RIGHT),
        pygame.K_RIGHT: ((1, 0), pygame.K_LEFT),
    }

    def __init__(self):
        pygame.init()
        self.sock = None
        self.bikes = []
        self.done = False
        self.dimensions = (500, 500)
        self.last_key = None
        self.screen = pygame.display.set_mode(self.dimensions)

    def is_move_key(self, key):
        if key not in self.K_DICT:
            return False

        return key != self.last_key and self.last_key != self.K_DICT[key][1]

    def foo_bar(self, data):
        print(data)
        if len(data) == 0:
            return
        j = json.loads(data)
        self.bikes[1].speed = 10
        bike1.trace.append(j[0])
        bike1.set_position(j[0])
        bike1.direction = j[1]

    def start(self):
        self.sock.subscribe(self.foo_bar)
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    for bike in self.bikes:
                        bike.speed = 0
                elif event.type == pygame.KEYDOWN and self.is_move_key(event.key):
                    self.last_key = event.key
                    self.bikes[0].speed = 10
                    self.bikes[0].change_direction(self.K_DICT[event.key][0])
                    self.sock.send(self.bikes[0].get_position(), self.K_DICT[event.key][0])

            self.screen.fill(self.GREY)


            for bike in self.bikes:
                bike.draw_trace(self.screen)
                bike.draw_bike(self.screen)

            pygame.display.flip()

            for bike in self.bikes:
                bike.next_position()

            # p = bike.get_position()
            # if bike.is_on_trace(p) or bike.is_in_screen(self.dimensions):
            #     bike.speed = 0

            pygame.time.wait(75)


if __name__ == "__main__":
    sock = GameSocket()
    sock.connect("localhost", 8888)

    bike = Bike((250, 250))
    bike.direction = (0, -1)
    bike.colour = (244, 128, 36)
    bike.trace_colour = (82, 44, 14)
    bike.speed = 0

    bike1 = Bike((250, 250))
    bike1.direction = (0, -1)
    bike1.colour = (36, 128, 244)
    bike1.trace_colour = (14, 44, 82)
    bike1.speed = 0

    game = Game()
    game.sock = sock
    game.bikes.append(bike)
    game.bikes.append(bike1)
    game.start()
