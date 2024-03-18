import pygame 
import time
from sys import exit

pygame.init()

width, height = 800,600

screen  = pygame.display.set_mode((width, height))

pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

back_img = pygame.image.load("mainclock.png")
min_arm = pygame.image.load("rightarm.png")
sec_arm = pygame.image.load("leftarm.png")

back_img = pygame.transform.scale(back_img, (width, height))
min_arm = pygame.transform.scale(min_arm, (back_img.get_width(), back_img.get_height()))
sec_arm = pygame.transform.scale(sec_arm, (back_img.get_width()*0.06, back_img.get_height()))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mytime = time.localtime()

    min_ang = -(360*mytime.tm_min)/60 - 54
    sec_ang = -(360*mytime.tm_sec)/60 - 12 

    rotated_min = pygame.transform.rotate(min_arm, min_ang)
    rotated_sec = pygame.transform.rotate(sec_arm, sec_ang)

    screen.blit(back_img, (0, 0))
    screen.blit(rotated_min, (width // 2 - rotated_min.get_width() // 2, 
                                    height // 2 - rotated_min.get_height() // 2))
    screen.blit(rotated_sec, (width // 2 - rotated_sec.get_width() // 2, 
                                    height // 2 - rotated_sec.get_height() // 2))
    pygame.display.update()
    clock.tick(30)
