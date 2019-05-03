import random
import os
import time

from pygame import *
import pygame
import math

WIDTH = HEIGHT = 300
DISPLAY = (WIDTH, HEIGHT)
FPS = 30
RUNNING = True
FONT = "monospace"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

POINT_RADIUS = 5

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(DISPLAY)

pygame.display.set_caption("Monte Carlo Visualization")
clock = pygame.time.Clock()


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, color=BLACK):
        pygame.sprite.Sprite.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.image = pygame.Surface((1, 1))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def updete(self):
        pass


def rand_no_repit():
    already_returned = set()
    while True:
        i = random.randint(0, HEIGHT)
        if i not in already_returned:
            already_returned.add(i)
            return i


in_c = 0
out_c = 0
point_arr = []

point_group = pygame.sprite.Group()
m = 1
time.delay(100)
while RUNNING:
    clock.tick(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    res = in_c+out_c

    x = int(rand_no_repit())
    y = int(rand_no_repit())


    if x**2+(y - HEIGHT)**2 <= WIDTH**2:
        point_arr.append(Point(x, y, RED))
        in_c += 1
    else:
        point_arr.append(Point(x, y, BLUE))
        out_c += 1

    point_group.add(point_arr)
    point_group.update()

    screen.fill(WHITE)
    point_group.draw(screen)
    myfont = pygame.font.SysFont(FONT, 20)
    in_cd = myfont.render(str(in_c), 1, BLACK)
    screen.blit(in_cd, (WIDTH - 230, 20))
    pygame.draw.line(screen, BLACK, [WIDTH-170, 40], [WIDTH-230, 40])
    res_cd = myfont.render(str(res), 1, BLACK)
    screen.blit(res_cd, (WIDTH - 230, 38))
    fourx = myfont.render("4x ", 1, BLACK)
    screen.blit(fourx, (WIDTH - 265, 30))
    pygame.draw.line(screen, BLACK, [WIDTH-157, 38], [WIDTH-147, 38])
    pygame.draw.line(screen, BLACK, [WIDTH-157, 42], [WIDTH-147, 42])
    pi_cd = myfont.render(str(float(4*((in_c+1)/(res+1))))[:7], 1, BLACK)
    screen.blit(pi_cd, (WIDTH - 144, 29))
    pygame.display.flip()

    if res == 90000:#float(str(float(4 * ((in_c + 1) / (res + 1))))[:7]) == 3.14159:
        time.delay(100000)
        break

pygame.quit()
