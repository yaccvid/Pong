#!/usr/bin/env python
# import pygame
# import sys
# import random
#
# from pygame import *
# from Player import *
# from Ball import *

from GameManager import *
#Constants
WIDTH  = 600
HEIGHT = 400

Mgr = PongGameMgr(WIDTH,HEIGHT)

Mgr.run_game()
	#Colors
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED   = (255,0,0)
# BLUE  = (0,0,255)
# GREEN = (0,255,0)






#
# #Create Surface
# DISPLAYSURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("Pong")
#
# #Create Player
# P = Player(DISPLAYSURFACE,0,0, WIDTH, HEIGHT)
# E = Enemy(DISPLAYSURFACE,WIDTH,HEIGHT//2, WIDTH,HEIGHT)
# B = Ball(DISPLAYSURFACE,WIDTH, HEIGHT)
#
#
# #Initialise
# pygame.init()
# pygame.font.init()
#
# FPS = 60 #Limiting loop execution t0 60 times a second
# FramesPerSecond = pygame.time.Clock()
# #Game Loop
# gameRunning = True
# while True:
# 	#Create Window
# 	#Move player
# 	if gameRunning:
# 		for event in pygame.event.get():
# 			if event.type == QUIT:
# 				pygame.quit()
# 				sys.exit()
# 		if pygame.Rect.colliderect(P.playerRect, B.ballRect):
# 			B.reverseX()
# 			P.incrScore()
# 		if pygame.Rect.colliderect(E.playerRect,B.ballRect):
# 			B.reverseX()
# 			E.incrScore()
#
# 		DISPLAYSURFACE.fill(BLACK)
# 		#Draw Line in middle
# 		P.update(DISPLAYSURFACE,B)
# 		B.update(DISPLAYSURFACE)
# 		E.update(DISPLAYSURFACE,B)
# 		P.drawScore(DISPLAYSURFACE)
# 		E.drawScore(DISPLAYSURFACE)
# 		pygame.draw.line(DISPLAYSURFACE,GREEN, (WIDTH/2,0), (WIDTH/2,HEIGHT),2)
# 		pygame.display.update()
# 		FramesPerSecond.tick(FPS)

