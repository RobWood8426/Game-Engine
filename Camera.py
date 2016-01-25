import pygame
import Map
import math

class Camera(object):

    def __init__(self):
        pygame.init()

        pygame.mouse.set_visible(0)
        pygame.event.set_grab(1)

        self.drawDistance = 5
        self.mapSize = 40
        self.mapDensity = 1
        self.map = Map.Mapping(self.mapSize,self.mapDensity)



        self.gamemap = self.map.gamemap

        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.sideSpace = (self.width - self.height) / 2
        self.blockHeight = int(self.height/self.mapSize)


        self.font = pygame.font.SysFont("monospace", 15)


        self.displaySize = [self.width,self.height]
        self.white = [255, 255, 255]
        self.blue = [0, 0, 255]
        self.lightblue = [0, 0, 100]


        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self):
        self.screen.fill((0,0,0))


        self.label = self.font.render(str(self.map.player.direction[0]), 1, (255,255,0))
        self.screen.blit(self.label, (0, 0))

        self.label = self.font.render(str(self.map.player.direction[2]), 1, (255,255,0))
        self.screen.blit(self.label, (0, 20))




        self.playerX = self.map.player.position[0]*self.blockHeight*1.5+self.sideSpace
        self.playerY = self.map.player.position[2]*self.blockHeight*1.5

        for y in range(self.mapSize):
            for x in range(self.mapSize):


                playerXPlusDD = self.playerX+self.linewidth*self.drawDistance
                playerXMinusDD = self.playerX-self.linewidth*self.drawDistance
                playerZPlusDD = self.playerY+self.linewidth*self.drawDistance
                playerZMinusDD = self.playerY-self.linewidth*self.drawDistance
                blockXPos = self.sideSpace+(x+0.5)*self.linewidth
                blockZPos = (y+0.5)*self.linewidth

                if (self.gamemap[y][x] == 1):
                    if ( blockXPos < playerXPlusDD) and (blockXPos > playerXMinusDD) and ( blockZPos < playerZPlusDD) and (blockZPos > playerZMinusDD):
                        colour = self.lightblue
                    else :
                        colour = self.white

                    pygame.draw.line(self.screen,colour,(int(self.sideSpace+x*self.linewidth),int((0.5+y)*self.lineheight)),(int(self.sideSpace+(x+1)*self.linewidth),int((0.5+y)*self.lineheight)),int(self.lineheight))
                pygame.draw.circle(self.screen,self.blue,(int(self.playerX),int(self.playerY)),int(self.linewidth/4),0)
                pygame.draw.line(self.screen,self.white,(int(self.playerX),int(self.playerY)),(int(self.playerX+self.linewidth/4*self.map.player.direction[0]),int(self.playerY+self.linewidth/4*self.map.player.direction[2])),int(math.ceil(self.linewidth/20)))
        self.map.player.listen()
        pygame.display.update()


