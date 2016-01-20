import pygame
import sys
import random
import math

class PlayerOnMap(object):
    def __init__(self,map,mapsize):
        pygame.init()
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
        self.angle = math.atan2(self.mouseY,self.mouseX)*180/math.pi

        if self.angle != 0 :
            self.direction = self.direction + self.mouseX/5



        self.playerY = self.playerY + math.cos(math.radians(self.direction)) * self.basicX - math.sin(math.radians(self.direction)) * self.basicY
        self.playerX = self.playerX + math.sin(math.radians(self.direction)) * self.basicX - math.cos(math.radians(self.direction)) * self.basicY

        self.basicX = 0
        self.basicY = 0


        pygame.event.clear()





