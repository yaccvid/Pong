#!/usr/bin/env python

import pygame
import sys
import random
import math as mth
from pygame import *

#Constants
WIDTH  = 600
HEIGHT = 400

	#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
BLUE  = (0,0,255)
GREEN = (0,255,0)
SLOPES = [-1,1]
#Create Player class
class Player:
	def __init__(self,surface,posx,posy,enemy):
		self.posx = 0
		self.posy = HEIGHT//2

		self.width = 10
		self.height = 50

		self.color = GREEN
		self.playerRect = pygame.Rect(self.posx,self.posy,self.width,self.height)
		self.rect  = pygame.draw.rect(surface,self.color, self.playerRect)

		self.speed = 3
		self.slope = 1
		self.enemy = enemy
		if enemy == True:
			self.posx = posx - self.width
			self.posy = posy

		self.oldloc = 0
	def update(self,surface,ball):
		if self.enemy == False:
			pressedKeys = pygame.key.get_pressed()
			if (self.posy + self.height) < HEIGHT:
				if pressedKeys[K_DOWN]:
					self.posy += self.speed

			if self.posy > 0:
				if pressedKeys[K_UP]:
					self.posy -= self.speed

			self.playerRect = pygame.Rect(self.posx,self.posy,self.width,self.height)		
			self.rect  = pygame.draw.rect(surface,self.color, self.playerRect)		
		else:
			self.AI(surface,ball)

	def predictBallLoc(self,dx,dy,ballx,bally):
		if self.slope != (dy/dx):
			self.slope = (dy/dx)
			newloc = (dy/dx)*(WIDTH - ballx) + bally
		#	print("Newloc: "+ str(newloc) + "ball.posy: " + str(ball.posy) + "b.posx= "+ str(ball.posx))
			if newloc >= 0 and newloc < HEIGHT:
				newloc = newloc - 10
				#dest = newloc - 10
				#self.oldloc = newloc
				return newloc
			else:
				return self.posy
		else:
			return self.posy

	def getSpeed(self,dest,src):
		if (abs(dest-src)/4) >= 2:
			return 100
		else:
			return 20
	def AI(self,surface,ball):
		#predict ball and update posx
		dest = 0
		#if self.slope != (ball.ydir/ball.xdir):
		#	self.slope = ball.ydir/ball.xdir
		#	newloc = self.predictBallLoc(ball.xdir,ball.ydir, ball.posx, ball.posy)
		#print("Newloc: "+ str(newloc) + "ball.posy: " + str(ball.posy) + "b.posx= "+ str(ball.posx))
		#	if newloc >=0 and newloc < HEIGHT:
		#		self.posy = newloc - 10
		#		#dest = newloc - 10
		#		self.oldloc = newloc
		targetLoc = self.predictBallLoc(ball.xdir, ball.ydir, ball.posx, ball.posy)
		speed = self.getSpeed(targetLoc,self.posy)
		if targetLoc == self.posy:
			self.posy = targetLoc
		elif targetLoc < self.posy:
			self.posy -= speed
		elif targetLoc > self.posy:
			self.posy += speed
		self.playerRect = pygame.Rect(self.posx,self.posy- 20,self.width,self.height)		
		self.rect  = pygame.draw.rect(surface,self.color, self.playerRect)

		#ballRect = pygame.draw.circle(surface,WHITE , (self.posx,self.posy), 7)
		
#Ball class
class Ball:
	def __init__(self,surface):
		self.color = GREEN
		self.center = (WIDTH//2,HEIGHT//2)
		self.radius = 7
		self.ballRect = pygame.draw.circle(surface,self.color, self.center, self.radius)

		self.posx = WIDTH//2
		self.posy = HEIGHT//2

		self.speed = 3

		self.xdir = random.choice(SLOPES)
		self.ydir = random.choice(SLOPES)

	def update(self,surface):
		if self.posx < 0 or self.posx > WIDTH:
			self.xdir *= -1
		if self.posy > HEIGHT or self.posy < 0:
			self.ydir *= -1

		self.posx += self.xdir*self.speed
		self.posy += self.ydir*self.speed
		self.ballRect = pygame.draw.circle(surface,self.color, (self.posx,self.posy), self.radius)
		
	def reverseX(self):
		self.xdir *= -1
		self.ydir = random.choice(SLOPES)
#Create Surface
DISPLAYSURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

#Create Player
P = Player(DISPLAYSURFACE,0,0,False)
E = Player(DISPLAYSURFACE,WIDTH,HEIGHT//2,True)
B = Ball(DISPLAYSURFACE)


#Initialise
pygame.init()

FPS = 60 #Limiting loop execution t0 60 times a second
FramesPerSecond = pygame.time.Clock()
#Game Loop
while True:
	#Create Window
	#Move player
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	if pygame.Rect.colliderect(P.playerRect, B.ballRect):
		B.reverseX()
	if pygame.Rect.colliderect(E.playerRect,B.ballRect):
		B.reverseX()

	DISPLAYSURFACE.fill(BLACK)
	#Draw Line in middle
	P.update(DISPLAYSURFACE,B)
	B.update(DISPLAYSURFACE)
	E.update(DISPLAYSURFACE,B)
	pygame.draw.line(DISPLAYSURFACE,GREEN, (WIDTH/2,0), (WIDTH/2,HEIGHT),2)
	pygame.display.update()
	FramesPerSecond.tick(FPS)