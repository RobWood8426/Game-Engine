import pygame
from pygame.locals import *
import random
displaySize = [1600, 1000]
white = [255, 255, 255]

gameMap = [[random.randint(0,1) for i in range(16)] for j in range(10)]
height = 100
width = 160

pygame.init()
screen = pygame.display.set_mode(displaySize, pygame.FULLSCREEN)

def displayMap(gameMap):
    for y in range(10):
        for x in range(16):
            if gameMap[y][x] == 1:
                pygame.draw.line(screen,white,(x*100,(0.5+y)*100),((x+1)*100,(0.5+y)*100),100)
    pygame.display.update()
displayMap(gameMap)

pygame.time.wait(5000)
pygame.quit()