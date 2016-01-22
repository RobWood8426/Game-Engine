import pygame
import sys
import random
import math

class PlayerOnMap(object):
    def __init__(self,map,mapsize):
        pygame.init()

        self.sin = 0
        self.cos = 0
        self.hyp = 0
        self.directionX = 0
        self.directionY = 0
        self.posFound = False
        self.basicX = 0
        self.basicY = 0
        self.angle = 0
        self.mouseX , self.mouseY = pygame.mouse.get_rel()
        self.direction = 0


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
                elif (event.key == pygame.K_s):
                    self.pressedKeys.append('Down')
                elif (event.key == pygame.K_w):
                    self.pressedKeys.append('Up')
                elif (event.key == pygame.K_d):
                    self.pressedKeys.append('Right')
                elif (event.key == pygame.K_a):
                    self.pressedKeys.append('Left')

            if (event.type== pygame.KEYUP):
                if (event.key == pygame.K_s):
                    self.remove = 'Down'
                if (event.key == pygame.K_w):
                    self.remove = 'Up'
                if (event.key == pygame.K_d):
                    self.remove = 'Right'
                if (event.key == pygame.K_a):
                    self.remove = 'Left'

                if (self.remove != '') & (self.remove in self.pressedKeys):
                    self.pressedKeys.remove(self.remove)
                    self.remove = ''



        for t in range(len(self.pressedKeys)):
            if (self.pressedKeys[t] == 'Down'):
                self.basicY = self.basicY + 0.05
            elif (self.pressedKeys[t] == 'Up'):
                self.basicY = self.basicY - 0.05
            elif (self.pressedKeys[t] == 'Right'):
                self.basicX = self.basicX + 0.05
            elif (self.pressedKeys[t] == 'Left'):
                self.basicX = self.basicX - 0.05

        self.mouseX , self.mouseY = pygame.mouse.get_rel()
        self.hyp = math.sqrt((self.mouseX*self.mouseX+self.mouseY*self.mouseY))

        if self.hyp != 0 :
            self.sin = self.sin + self.mouseY/self.hyp
            self.cos = self.cos + self.mouseX/self.hyp


        self.playerY = self.playerY + self.cos * self.basicX - self.sin * self.basicY
        self.playerX = self.playerX + self.sin * self.basicX - self.cos * self.basicY

        self.basicX = 0
        self.basicY = 0
        self.hype = 0


        pygame.event.clear()





