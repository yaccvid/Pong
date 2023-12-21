# Create Player class
import pygame
from pygame import *
	#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
BLUE  = (0,0,255)
GREEN = (0,255,0)
class Player:
    def __init__(self, surface, posx, posy, WIDTH,HEIGHT):
        self.SCREEN_WIDTH      = WIDTH
        self.SCREEN_HEIGHT     = HEIGHT
        self.posx       = 0
        self.posy       = self.SCREEN_HEIGHT // 2
        self.width      = 10
        self.height     = 50
        self.color      = GREEN
        self.playerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.rect       = pygame.draw.rect(surface, self.color, self.playerRect)
        self.speed      = 3
        self.slope      = 1
        self.score      = 0



    def update(self, surface, ball):
        pressedKeys = pygame.key.get_pressed()
        if (self.posy + self.height) < self.SCREEN_HEIGHT:
            if pressedKeys[K_DOWN]:
                self.posy += self.speed

        if self.posy > 0:
            if pressedKeys[K_UP]:
                self.posy -= self.speed

        self.playerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.rect = pygame.draw.rect(surface, self.color, self.playerRect)


    def incrScore(self):
        self.score += 1

    def getScore(self):
        return self.score

    def reset(self):
        self.score = 0
        self.posx = 0
        self.posy = self.SCREEN_HEIGHT // 2


#Enemy class inheriting from Player
class Enemy(Player):
    def __init__(self, surface, posx, posy, WIDTH, HEIGHT):
        super().__init__(surface,posx, posy,  WIDTH,HEIGHT)
        self.posx = posx - self.width
        self.posy = posy
        self.oldloc = 0

    def predictBallLoc(self, dx, dy, ballx, bally):
        if self.slope != (dy / dx):
            self.slope = (dy / dx)
            newloc = (dy / dx) * (self.SCREEN_WIDTH - ballx) + bally
            #	print("Newloc: "+ str(newloc) + "ball.posy: " + str(ball.posy) + "b.posx= "+ str(ball.posx))
            if newloc >= 0 and newloc < self.SCREEN_HEIGHT:
                newloc = newloc - 10
                # dest = newloc - 10
                # self.oldloc = newloc
                return newloc
            else:
                return self.posy
        else:
            return self.posy

    def getSpeed(self, dest, src):
        return (abs(dest - src) // 3)

    def update(self, surface, ball):
        # predict ball and update posx
        targetLoc = self.predictBallLoc(ball.xdir, ball.ydir, ball.posx, ball.posy)
        speed = self.getSpeed(targetLoc, self.posy)
        self.posy = targetLoc
        if targetLoc == self.posy:
            self.posy = targetLoc
        elif targetLoc < self.posy:
            self.posy -= speed
        elif targetLoc > self.posy:
            self.posy += speed

        #For a natural movement
        self.posy = ball.posy
        if (self.posy + self.height) >= self.SCREEN_HEIGHT:
            self.posy = self.SCREEN_HEIGHT - self.height
        self.playerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.rect = pygame.draw.rect(surface, self.color, self.playerRect)

    def reset(self):
        super().reset()
        self.posx = self.SCREEN_WIDTH - self.width
        self.posy = self.posy

