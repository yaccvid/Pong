import pygame
import random
from pygame import *

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
BLUE  = (0,0,255)
GREEN = (0,255,0)
SLOPES = [-1,1]
# Ball class
class Ball:
    def __init__(self, surface,WIDTH,HEIGTH):
        self.SCREEN_WIDTH   = WIDTH
        self.SCREEN_HEIGHT  = HEIGTH
        self.color          = GREEN
        self.center         = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
        self.radius         = 7
        self.ballRect       = pygame.draw.circle(surface, self.color, self.center, self.radius)
        self.posx           = self.SCREEN_WIDTH // 2
        self.posy           = self.SCREEN_HEIGHT // 2
        self.speed          = 3
        self.xdir           = random.choice(SLOPES)
        self.ydir           = random.choice(SLOPES)

        self.gameOver       = False


    def isGameOver(self):
        return self.gameOver
    def update(self, surface):
        if self.posx < 0 or self.posx > self.SCREEN_WIDTH:
            self.xdir *= -1
        if self.posy > self.SCREEN_HEIGHT or self.posy < 0:
            self.ydir *= -1

        if self.posx <= 0:
            print("Player Lost")
            self.gameOver = True
        self.posx += self.xdir * self.speed
        self.posy += self.ydir * self.speed
        self.ballRect = pygame.draw.circle(surface, self.color, (self.posx, self.posy), self.radius)

    def reset(self):
        self.gameOver = False
        self.posx = self.SCREEN_WIDTH // 2
        self.posy = self.SCREEN_HEIGHT // 2

    def reverseX(self):
        self.xdir *= -1
        self.ydir = random.choice(SLOPES)
