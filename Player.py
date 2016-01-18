import pygame
import sys

class PlayerOnMap(object):
    def __init__(self,map):
        pygame.init()
        self.posFound = False
        for y in range(10):
            for x in range(10):
                if (not self.posFound) & (map[y][x] == 0) :
                    self.posFound = True
                    self.playerX = x
                    self.playerY = y

    def listen(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit(0)
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    sys.exit(0)
                elif (event.key == pygame.K_DOWN):
                    self.playerY =+1
                elif (event.key == pygame.K_UP):
                    self.playerY =-1
                elif (event.key == pygame.K_RIGHT):
                    self.playerX =+1
                elif (event.key == pygame.K_LEFT):
                    self.playerX =-1


