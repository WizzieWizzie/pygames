import pygame

pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect_head = pygame.Rect(0, 0, 20, 20)

done = False
clock = pygame.time.Clock()

pygame.draw.rect(screen, BLACK, rect_head, 0)

l = 3
t = [None] * l
t[l - 1] = [0, 0]

_x = 1
_y = 0
k = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                _x = -1
                _y = 0

            if event.key == pygame.K_RIGHT:
                _x = 1
                _y = 0

            if event.key == pygame.K_UP:
                _x = 0
                _y = -1

            if event.key == pygame.K_DOWN:
                _x = 0
                _y = 1

        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    rect_head.move_ip(_x * 20, _y * 20)

    if rect_head.x >= 400:
        rect_head.move_ip(-400, 0)
    elif rect_head.x < 0:
        rect_head.move_ip(400, 0)

    if rect_head.y >= 300:
        rect_head.move_ip(0, -300)
    elif rect_head.y < 0:
        rect_head.move_ip(0, 300)

    pygame.draw.rect(screen, BLACK, rect_head, 0)

    t.append([rect_head.x, rect_head.y])

    if len(t) > l:
        t.pop(0)

    for i in range(l):
        if t[i] is None:
            continue

        r = pygame.Rect(t[i][0], t[i][1], 20, 20)
        pygame.draw.rect(screen, BLACK, r, 0)

    pygame.display.flip()

    if 500 - k * 5 > 0:
        pygame.time.wait(500 - k * 5)
        k += 1
