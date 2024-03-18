import pygame
from sys import exit
pygame.init()

display = pygame.display.set_mode((500,500))

pygame.display.set_caption("Ball")

clock = pygame.time.Clock()

vel = 20

x = 20
y = 20 

radius = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - vel >= 25:
        x -= vel
    
    if keys[pygame.K_RIGHT] and x + vel <= 500-25:
        x += vel

    if keys[pygame.K_UP] and y - vel >= 25:
        y -= vel

    if keys[pygame.K_DOWN] and y + vel <= 500-25:
        y += vel

    display.fill((255,255,255))

    pygame.draw.circle(display, (255, 0, 0), (x, y), radius)

    pygame.display.update()
    clock.tick(60)

    