import pygame

# Colour constants
BLACK = (0, 0, 0)
GREY = (75, 75, 75)
WHITE = (255, 255, 255)
GOLD = (251, 188, 5)
GREEN = (52, 168, 82)
BROWN = (166, 42, 42)

pygame.Color

pygame.init()
screen = pygame.display.set_mode([600, 600])

# Main character
h = 20
mario = pygame.Rect(20, 400, 10, h)
jumping = False
jump_y = 0

ground_y = 420

# Panels
panel = pygame.Rect(40, 380, 40, 2)

# Coins
coins = []
for n in range(10):
    coins.append(pygame.Rect(100 + n * 20, 410, 5, 5))

# Game status. False if game is not completed, False otherwise
done = False

# Start main game loop
while not done:
    # Iterate over all events
    for event in pygame.event.get():
        # Window quit button
        if event.type == pygame.QUIT:
            done = True

    # Get all pressed keys
    keys = pygame.key.get_pressed()
    mario.x += keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    mario.y += keys[pygame.K_DOWN] * 0 - keys[pygame.K_UP]

    if not jumping and keys[pygame.K_SPACE] and mario.y + h == ground_y:
        jumping = True
        jump_y = mario.y

    if jumping:
        d = jump_y - mario.y
        if d < 60:
            mario.y -= 1 if d >= 50 else 3
        else:
            jumping = False

    if not jumping and mario.y < 400 and not panel.colliderect(mario):
        mario.y += 4
        if mario.y > 400:
            mario.y = 400
        elif panel.colliderect(mario):
            mario.y = panel.y - h

    if not jumping and (mario.y == 400 or panel.y == mario.y + h):
        ground_y = mario.y + h

    for i in range(len(coins)):
        if coins[i] is not None and mario.colliderect(coins[i]):
            coins[i] = None

    # Fill screen with white colour
    screen.fill(WHITE)

    pygame.draw.line(screen, GREEN, (0, 424), (600, 424), 10)
    pygame.draw.line(screen, BROWN, (0, 444), (600, 444), 30)

    for coin in coins:
        if coin is not None:
            pygame.draw.rect(screen, GOLD, coin, 0)

    pygame.draw.rect(screen, BLACK, mario, 0)
    pygame.draw.rect(screen, GREY, panel, 0)

    # Update pixels on screen
    pygame.display.flip()
