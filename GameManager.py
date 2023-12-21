import pygame
import sys
import random

from pygame import *
from Player import *
from Ball import *

	#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
BLUE  = (0,0,255)
GREEN = (0,255,0)
class PongGameMgr:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # Initialise
        pygame.init()
        pygame.font.init()

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        # Create Surface
        self.DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")

        # Create Players
        self.P = Player(self.DISPLAYSURFACE, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.E = Enemy(self.DISPLAYSURFACE, SCREEN_WIDTH, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.B = Ball(self.DISPLAYSURFACE, SCREEN_WIDTH, SCREEN_HEIGHT)


        self.FPS = 60  # Limiting loop execution t0 60 times a second
        self.FramesPerSecond = pygame.time.Clock()

    def drawScore(self, surface):
        enemy_score = self.E.getScore()
        player_score = self.P.getScore()

        x = 0.25 * self.SCREEN_WIDTH
        y = 40
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(player_score), True, GREEN, BLACK)
        textRect = text.get_rect()
        textRect.center = (x, y)
        surface.blit(text, textRect)

        x = 0.75 * self.SCREEN_WIDTH
        y = 40
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(enemy_score), True, GREEN, BLACK)
        textRect = text.get_rect()
        textRect.center = (x, y)
        surface.blit(text, textRect)

    def resetGame(self):
        self.P.reset()
        self.B.reset()
        self.E.reset()
    def gameOver(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Game Over", True, GREEN, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
        surface.blit(text, textRect)
    def run_game(self):
        # Game Loop
        gameOvr = False
        gameRunning = True
        while True:
            # Create Window
            # Move player
            if gameRunning:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if not gameOvr:
                    if pygame.Rect.colliderect(self.P.playerRect, self.B.ballRect):
                        self.B.reverseX()
                        self.P.incrScore()
                    if pygame.Rect.colliderect(self.E.playerRect, self.B.ballRect):
                        self.B.reverseX()
                        self.E.incrScore()

                    self.DISPLAYSURFACE.fill(BLACK)
                    # Draw Line in middle
                    self.P.update(self.DISPLAYSURFACE, self.B)
                    self.B.update(self.DISPLAYSURFACE)
                    self.E.update(self.DISPLAYSURFACE, self.B)
                    self.drawScore(self.DISPLAYSURFACE)

                else:
                    self.gameOver(self.DISPLAYSURFACE)
                    pressedKeys = pygame.key.get_pressed()
                    if pressedKeys[K_y]:
                        self.resetGame()
                        gameRunning = True
                        gameOvr = False

                if self.B.isGameOver():
                    gameOvr = True
                else:
                    gameOvr = False
            pygame.draw.line(self.DISPLAYSURFACE, GREEN, (self.SCREEN_WIDTH / 2, 0), (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT), 2)
            pygame.display.update()
            self.FramesPerSecond.tick(self.FPS)