import pygame
import sys

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Character Movement")

blue = (204,204,255)

char_speed = 5

char_image = pygame.image.load("girl.gif")
char_rect = char_image.get_rect()
char_rect.topleft = (width // 2, height // 2)

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


    if char_rect.left < 0:
        char_rect.left = 0
    if char_rect.right > width:
        char_rect.right = width
    if char_rect.top < 0:
        char_rect.top = 0
    if char_rect.bottom > height:
        char_rect.bottom = height

    screen.fill(blue)

    screen.blit(char_image, char_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
