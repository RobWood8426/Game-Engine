import pygame
import Map

class Camera(object):

    def __init__(self):
        pygame.init()

        pygame.mouse.set_visible(0)
        pygame.event.set_grab(1)

        self.mapSize = 10
        self.mapDensity = 1
        self.map = Map.Mapping(self.mapSize,self.mapDensity)
        self.gamemap = self.map.gamemap

        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.sideSpace = (self.width - self.height) / 2
        self.lineheight = int(self.height/self.mapSize)
        self.linewidth = self.lineheight

        self.font = pygame.font.SysFont("monospace", 15)


        self.displaySize = [self.width,self.height]
        self.white = [255, 255, 255]
        self.blue = [0, 0, 255]


        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self):
        self.screen.fill((0,0,0))


        self.label = self.font.render(str(self.map.player.direction[0]), 1, (255,255,0))
        self.screen.blit(self.label, (0, 0))

        self.label = self.font.render(str(self.map.player.direction[2]), 1, (255,255,0))
        self.screen.blit(self.label, (0, 20))







        self.playerX = self.map.player.position[0]*self.linewidth+self.linewidth/2+self.sideSpace
        self.playerY = self.map.player.position[2]*self.linewidth+self.linewidth/2

        for y in range(10):
            for x in range(10):
                #DrawMap
                if (self.gamemap[y][x] == 1):
                    pygame.draw.line(self.screen,self.white,(int(self.sideSpace+x*self.linewidth),int((0.5+y)*self.lineheight)),(int(self.sideSpace+(x+1)*self.linewidth),int((0.5+y)*self.lineheight)),int(self.lineheight))
                pygame.draw.circle(self.screen,self.blue,(int(self.playerX),int(self.playerY)),int(self.linewidth/4),0)
        self.map.player.listen()
        pygame.display.update()


