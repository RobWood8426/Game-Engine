import pygame
import Map

class Camera(object):

    def __init__(self):
        pygame.init()

        self.mapSize = 10
        self.mapDensity = 1
        self.map = Map.Mapping(self.mapSize,self.mapDensity)
        self.gamemap = self.map.gamemap

        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.sideSpace = (self.width - self.height) / 2
        self.lineheight = self.height/self.mapSize
        self.linewidth = self.lineheight

        self.playerX = self.map.player.playerX
        self.playerY = self.map.player.playerY

        self.displaySize = [self.width,self.height]
        self.white = [255, 255, 255]
        self.blue = [0, 0, 255]


        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self):

        for y in range(10):
            for x in range(10):
                #DrawMap
                if self.gamemap[y][x] == 1:
                    pygame.draw.line(self.screen,self.white,(self.sideSpace+x*self.linewidth,(0.5+y)*self.lineheight),(self.sideSpace+(x+1)*self.linewidth,(0.5+y)*self.lineheight),self.lineheight)
                if (x == self.playerX) & (y == self.playerY):
                    pygame.draw.circle(self.screen,self.blue,(self.linewidth/2 + self.sideSpace +x*self.linewidth, self.linewidth/2+y*self.linewidth),self.linewidth/4,0)
        pygame.display.update()