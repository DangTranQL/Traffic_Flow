import pygame
import sys
import time
import math
import random
from utils import *
from car import *
from path_tracking import *

pygame.font.init()

street = pygame.image.load("imgs/street.png")
width, height = street.get_width(), street.get_height()
gameDisplay = pygame.display.set_mode((width, height))

pygame.display.set_caption("Simulation")
font = pygame.font.SysFont("comicsans", 44)


class GameInfo:
    def __init__(self):
        self.started = False
        self.start_time = 0

    def reset(self):
        self.started = False
        self.start_time = 0

    def game_finished(self):
        return False

    def start_run(self):
        self.started = True
        self.start_time = time.time()

def draw(display, images, car, game_info):
    for img, pos in images:
        display.blit(img, pos)

    car.draw(display)
    pygame.display.update()
    
fps = 60
clock = pygame.time.Clock()
run = True

images = [(street, (0,0))]
game_info = GameInfo()
path = State('straight')[0]
car = Car(0.05,0.1,path)

while run:
    clock.tick(fps)
    
    draw(gameDisplay, images, car, game_info)
    
    while not game_info.started:
        blit_text_center(gameDisplay, font, f"Press any key to start")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                game_info.start_run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        car.move()
        
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     car.path.append(pos)

# print(car.path)
pygame.quit()