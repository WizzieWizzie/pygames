from random import randrange
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

direction_dictionary = {
    pygame.K_LEFT: {"x": -1, "y": 0},
    pygame.K_RIGHT: {"x": 1, "y": 0},
    pygame.K_UP: {"x": 0, "y": -1},
    pygame.K_DOWN: {"x": 0, "y": 1},
}

size = [400, 300]

pygame.init()

screen = pygame.display.set_mode(size)

direction = {"x": 1, "y": 0}

snake = []

for n in range(3):
    rect = pygame.Rect(n * 20 * (-1), 0, 20, 20)
    snake.append(rect)


def position(p, d, m):
    v = p + 20 * d

    if v > m:
        return 0

    if v < 0:
        return m

    return v


mouse = pygame.Rect(randrange(0, size[0], 20), randrange(0, size[1], 20), 20, 20)

score = 0
font = pygame.font.Font(None, 21)
text = font.render("Score: " + str(score), 1, BLACK)


done = False
while not done:
    pygame.time.wait(250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in direction_dictionary:
            direction = direction_dictionary[event.key]

        elif event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    if snake[0].colliderect(mouse):
        snake.append(pygame.Rect(0, 0, 20, 20))
        score += 1
        text = font.render("Score: " + str(score), 1, BLACK)
        mouse.x = randrange(0, size[0], 20)
        mouse.y = randrange(0, size[1], 20)

    for i in reversed(range(1, len(snake))):
        snake[i].x = snake[i - 1].x
        snake[i].y = snake[i - 1].y

    snake[0].x = position(snake[0].x, direction["x"], size[0])
    snake[0].y = position(snake[0].y, direction["y"], size[1])

    for i in range(len(snake)):
        pygame.draw.rect(screen, BLACK, snake[i], 0)
        if i != 0 and snake[0].colliderect(snake[i]):
            done = True

    pygame.draw.rect(screen, BLACK, mouse, 1)

    screen.blit(text, (10, 10))

    pygame.display.flip()
