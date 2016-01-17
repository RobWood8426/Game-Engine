import pygame
import Map


class Camera(object):

    def __init__(self):
        self.gamemap = Map.Mapping().gamemap
        self.displaySize = [1600, 1000]
        self.white = [255, 255, 255]
        pygame.init()
        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self):
        for y in range(10):
            for x in range(16):
                if self.gamemap[y][x] == 1:
                    pygame.draw.line(self.screen,self.white,(x*100,(0.5+y)*100),((x+1)*100,(0.5+y)*100),100)
        pygame.display.update()