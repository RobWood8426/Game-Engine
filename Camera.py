import pygame
import Map
import ctypes

class Camera(object):

    def __init__(self):

        self.gamemap = Map.Mapping().gamemap
        self.screensize = ctypes.windll.user32
        self.width = self.screensize.GetSystemMetrics(0)
        self.height = self.screensize.GetSystemMetrics(1)

        self.lineheight = self.height/10
        self.linewidth = self.width/16

        self.displaySize = [self.width,self.height]
        self.white = [255, 255, 255]

        pygame.init()
        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self):
        for y in range(10):
            for x in range(16):
                if self.gamemap[y][x] == 1:
                    pygame.draw.line(self.screen,self.white,(x*self.linewidth,(0.5+y)*self.lineheight),((x+1)*self.linewidth,(0.5+y)*self.lineheight),self.lineheight)
        pygame.display.update()