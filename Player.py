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
            self.moving = False

            if (map[y][x] == 0) :
                self.posFound = True
                self.playerX = x
                self.playerY = y
            self.pressedKeys = []
            self.remove = ''

    def listen(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit(0)
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    sys.exit(0)
                elif (event.key == pygame.K_DOWN):
                    self.pressedKeys.append('Down')
                elif (event.key == pygame.K_UP):
                    self.pressedKeys.append('Up')
                elif (event.key == pygame.K_RIGHT):
                    self.pressedKeys.append('Right')
                elif (event.key == pygame.K_LEFT):
                    self.pressedKeys.append('Left')

            if (event.type== pygame.KEYUP):
                if (event.key == pygame.K_DOWN):
                    self.remove = 'Down'
                if (event.key == pygame.K_UP):
                    self.remove = 'Up'
                if (event.key == pygame.K_RIGHT):
                    self.remove = 'Right'
                if (event.key == pygame.K_LEFT):
                    self.remove = 'Left'

            if (self.remove <> '') and (len(self.pressedKeys) > 0):
                self.pressedKeys.remove(self.remove)
                self.remove = ''



        for t in range(len(self.pressedKeys)):
            if (self.pressedKeys[t] == 'Down'):
                self.playerY = self.playerY + 0.05
            elif (self.pressedKeys[t] == 'Up'):
                self.playerY = self.playerY - 0.05
            elif (self.pressedKeys[t] == 'Right'):
                self.playerX = self.playerX + 0.05
            elif (self.pressedKeys[t] == 'Left'):
                self.playerX = self.playerX - 0.05



