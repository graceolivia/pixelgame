import pygame
import sys

# initialize pygame
pygame.init()

# screen settings
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Character Movement")

# colors
blue = (204,204,255)

# character settings
char_speed = 5

# load character image
char_image = pygame.image.load("girl.gif")
char_rect = char_image.get_rect()
char_rect.topleft = (width // 2, height // 2)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        char_rect.x -= char_speed
    if keys[pygame.K_RIGHT]:
        char_rect.x += char_speed
    if keys[pygame.K_UP]:
        char_rect.y -= char_speed
    if keys[pygame.K_DOWN]:
        char_rect.y += char_speed

    # fill screen with blue
    screen.fill(blue)

    # draw character
    screen.blit(char_image, char_rect.topleft)

    # update display
    pygame.display.flip()

    # cap the frame rate
    pygame.time.Clock().tick(60)
