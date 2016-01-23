import pygame
import sys
import random
import math

class PlayerOnMap(object):
    def __init__(self,map,mapsize):
        pygame.init()
        self.mouseHyp = 0
        self.mouseSin = 0
        self.sin = 1
        self.cos = 0
        self.hyp = 0
        self.directionX = 1
        self.directionY = 1
        self.posFound = False
        self.basicX = 0
        self.basicY = 0
        self.angle = 0
        self.mouseX , self.mouseY = pygame.mouse.get_rel()
        self.direction = 10
        self.sensitivity = 1

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

        # relative movement of the mouse from last call
        self.mouseX , self.mouseY = pygame.mouse.get_rel()


        #if there has been mouse movement

        if self.mouseX != 0 :

            self.mouseSin = math.sin(self.mouseX)
            self.directionY = self.directionY + self.mouseSin
            self.directionX = self.directionX + 1/self.mouseSin

        #the length of the hypotenuse of the directional triangle
        self.hyp = math.sqrt((self.directionX*self.directionX+self.directionY*self.directionY))


        if self.hyp != 0 :
            self.sin = self.directionY/self.hyp
            self.cos = self.directionX/self.hyp



        self.direction = self.directionX

        self.playerY = self.playerY + (self.cos * self.basicX) - (self.sin * self.basicY)
        self.playerX = self.playerX + (self.sin * self.basicX) - (self.cos * self.basicY)

        self.sin = 0
        self.cos = 0
        self.basicX = 0
        self.basicY = 0
        self.hyp = 0


        pygame.event.clear()





