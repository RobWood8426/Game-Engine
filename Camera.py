import pygame
import Map

class Camera(object):

    def __init__(self):
        pygame.init()
        self.mapSize = 10
        self.mapDensity = 1
        self.gamemap = Map.Mapping(self.mapSize,self.mapDensity).gamemap
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.sideSpace = (self.width - self.height) / 2
        self.lineheight = self.height/self.mapSize
        self.linewidth = self.lineheight


        self.displaySize = [self.width,self.height]
        self.white = [255, 255, 255]


        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self):
        for y in range(10):
            for x in range(10):
                if self.gamemap[y][x] == 1:
                    pygame.draw.line(self.screen,self.white,(self.sideSpace+x*self.linewidth,(0.5+y)*self.lineheight),(self.sideSpace+(x+1)*self.linewidth,(0.5+y)*self.lineheight),self.lineheight)
        pygame.display.update()