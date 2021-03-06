import pygame
import Map
import math

class Camera(object):

    def __init__(self):
        pygame.init()

        pygame.mouse.set_visible(0)
        pygame.event.set_grab(1)


        self.FOV = math.tan(math.pi/4)
        self.drawDistance = 5
        self.mapSize = 40
        self.mapDensity = 1
        self.map = Map.Mapping(self.mapSize,self.mapDensity)



        self.gamemap = self.map.gamemap

        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.sideSpace = (self.width - self.height) / 2
        self.blockHeight = self.height/self.mapSize


        self.font = pygame.font.SysFont("monospace", 15)


        self.displaySize = [self.width,self.height]
        self.white = [255, 255, 255]
        self.blue = [0, 0, 255]
        self.lightblue = [0, 0, 100]


        self.screen = pygame.display.set_mode(self.displaySize, pygame.FULLSCREEN)

    def updateScreen(self,fps):
        self.screen.fill((0,0,0))


        self.label = self.font.render(str(self.map.player.direction[0]), 1, (255,255,0))
        self.screen.blit(self.label, (0, 0))

        self.label = self.font.render(str(self.map.player.direction[2]), 1, (255,255,0))
        self.screen.blit(self.label, (0, 20))

        self.label = self.font.render(str(fps), 1, (255,255,0))
        self.screen.blit(self.label, (0, 40))


        self.playerX = self.map.player.position[0]*self.blockHeight+self.blockHeight/2+self.sideSpace
        self.playerY = self.map.player.position[2]*self.blockHeight+self.blockHeight/2

        for y in range(self.mapSize):
            for x in range(self.mapSize):


                playerXPlusDD = self.playerX+self.blockHeight*self.drawDistance
                playerXMinusDD = self.playerX-self.blockHeight*self.drawDistance
                playerZPlusDD = self.playerY+self.blockHeight*self.drawDistance
                playerZMinusDD = self.playerY-self.blockHeight*self.drawDistance
                blockXPos = self.sideSpace+(x+0.5)*self.blockHeight
                blockZPos = (y+0.5)*self.blockHeight

                if (self.gamemap[y][x] == 1):
                    if ( blockXPos < playerXPlusDD) and (blockXPos > playerXMinusDD) and ( blockZPos < playerZPlusDD) and (blockZPos > playerZMinusDD):
                        colour = self.lightblue
                    else :
                        colour = self.white

                    pygame.draw.line(self.screen,colour,(int(self.sideSpace+x*self.blockHeight),int((0.5+y)*self.blockHeight)),(int(self.sideSpace+(x+1)*self.blockHeight),int((0.5+y)*self.blockHeight)),int(self.blockHeight))
                pygame.draw.circle(self.screen,self.blue,(int(self.playerX),int(self.playerY)),int(self.blockHeight/4),0)
                pygame.draw.line(self.screen,self.white,(int(self.playerX),int(self.playerY)),(int(self.playerX+self.blockHeight/4*self.map.player.direction[0]),int(self.playerY+self.blockHeight/4*self.map.player.direction[2])),int(math.ceil(self.blockHeight/20)))
        self.map.player.listen()
        pygame.display.update()


