import pygame
import sys
import time
import math
import random
from utils import *
from path_tracking import *


street = pygame.image.load("imgs/street.png")
width, height = street.get_width(), street.get_height()
gameDisplay = pygame.display.set_mode((width, height))

car = scale_image(pygame.image.load("imgs/car.png"), 0.45)
# car_up = scale_image(pygame.image.load("imgs/car_up.png"), 0.45)
# car_down = scale_image(pygame.image.load("imgs/car_down.png"), 0.45)
# car_left = scale_image(pygame.image.load("imgs/car_left.png"), 0.45)
# car_right = scale_image(pygame.image.load("imgs/car_right.png"), 0.45)

# car_down = car_up
# car_down = pygame.transform.rotate(car_down, 180)
# car_left = car_up
# car_left = pygame.transform.rotate(car_left, 90)
# car_right = car_up
# car_right = pygame.transform.rotate(car_right, -90)

poss_start = [(279,413), (159,8), (414, 159), (8, 279)]
# car_start = [(car_up, poss_start[0]), (car_down, poss_start[1]), (car_left, poss_start[2]), (car_right, poss_start[3])]

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.img
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.start_pos
        self.acceleration = 0.01

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, gameDisplay):
        blit_rotate_center(gameDisplay, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    
    
class Car(AbstractCar):
    # car_new = random.choice(car_start)
    # img = car_new[0]
    # start_pos = car_new[1]
    
    img = car
    # blit_rotate_center(gameDisplay, img, (415, 175), 90)
    start_pos = poss_start[2]
    
    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(gameDisplay, (255, 0, 0), point, 5)
            
    def draw(self, gameDisplay):
        super().draw(gameDisplay)
        # self.draw_points(gameDisplay)
            
    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            final_angle = math.pi / 2
        else:
            final_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            final_angle += math.pi

        angle_diff = self.angle - math.degrees(final_angle)
        if angle_diff >= 180:
            angle_diff -= 360

        if angle_diff > 0:
            self.angle -= min(self.rotation_vel, abs(angle_diff))
        else:
            self.angle += min(self.rotation_vel, abs(angle_diff))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()
        
    def distance(self, cur_pos, prev_pos, d):
        if cur_pos.x == prev_pos.x:
            d = d + abs(cur_pos.y - prev_pos.y)
        elif cur_pos.x == prev_pos.x:
            d = d + abs(cur_pos.x - prev_pos.x)
        else:
            d = d + math.sqrt((cur_pos.x - prev_pos.x)**2 + (cur_pos.y - prev_pos.y)**2)
        return d