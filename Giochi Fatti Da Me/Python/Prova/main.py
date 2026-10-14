import pygame
from sys import exit

pygame.init()

screen=pygame.display.set_mode((450,700))
clock=pygame.time.Clock()

sky=pygame.image.load("immagini/Sky.png")
ground=pygame.image.load("immagini/ground.png")


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky,(0,-50))
    screen.blit(ground,(0,625))
    pygame.display.update()