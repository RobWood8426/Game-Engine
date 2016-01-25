import pygame
import sys
import random
import math

class PlayerOnMap(object):
    def __init__(self,map,mapsize):

        self.posFound = False
        self.position = [0, 0, 0]
        self.direction = [1, 0, 0]
        self.sensitivity = 0.05

        while not self.posFound:
            x = random.randint(0,mapsize-1)
            z = random.randint(0,mapsize-1)
            self.moving = False

            if (map[z][x] == 0) :
                self.posFound = True
                self.position[0] = x
                self.position[2] = z

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
        motion = [-self.sensitivity*i for i in pygame.mouse.get_rel()]
        cos = math.cos(motion[0])
        sin = math.sin(motion[0])

        x = self.direction[0]*cos + self.direction[2]*sin
        z = -self.direction[0]*sin + self.direction[2]*cos

        self.direction[0] = x
        self.direction[2] = z


        for t in range(len(self.pressedKeys)):
            if (self.pressedKeys[t] == 'Down'):
                self.position[0] -= 0.05*self.direction[0]
                self.position[2] -= 0.05*self.direction[2]
            elif (self.pressedKeys[t] == 'Up'):
                self.position[0] += 0.05*self.direction[0]
                self.position[2] += 0.05*self.direction[2]
            elif (self.pressedKeys[t] == 'Right'):
                self.position[0] += -0.05*(self.direction[2])
                self.position[2] += 0.05*(self.direction[0])
            elif (self.pressedKeys[t] == 'Left'):
                self.position[0] += 0.05*self.direction[2]
                self.position[2] += -0.05*self.direction[0]





        pygame.event.clear()





