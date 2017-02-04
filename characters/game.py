import pygame
import invader

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode([500, 500])

frames = invader.read_frames('invader')

def draw_frame(index, size):
    for c in frames[index]:
        rect = pygame.Rect(c[0] * 10, c[1] * 10, c[2] * size, size)
        pygame.draw.rect(screen, BLACK, rect, 0)

i = 0
done = False
while not done:
    pygame.time.wait(250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    screen.fill(WHITE)

    if i >= len(frames):
        i = 0

    draw_frame(i, 10)

    i = i + 1

    pygame.display.flip()
