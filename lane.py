import pygame
import sys
import time
import math
# from utils import *

pygame.font.init()

black = (0,0,0)
white = (255,255,255)

# street = scale_image(pygame.image.load("bg.png"), 0.9)
street = pygame.image.load("bg.png")
width, height = street.get_width(), street.get_height()
gameDisplay = pygame.display.set_mode((width, height))

pygame.display.set_caption("Simulation")
font = pygame.font.SysFont("comicsans", 44)

clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.blit(street, (0,0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()