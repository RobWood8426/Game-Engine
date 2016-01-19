import pygame
import sys
import random

class PlayerOnMap(object):
    def __init__(self,map,mapsize):
        pygame.init()
        self.posFound = False
        while not self.posFound:
            x = random.randint(0,mapsize-1)
            y = random.randint(0,mapsize-1)
            if (map[y][x] == 0) :
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
                    self.playerY = self.playerY + 1
                elif (event.key == pygame.K_UP):
                    self.playerY = self.playerY - 1
                elif (event.key == pygame.K_RIGHT):
                    self.playerX = self.playerX + 1
                elif (event.key == pygame.K_LEFT):
                    self.playerX = self.playerX - 1


