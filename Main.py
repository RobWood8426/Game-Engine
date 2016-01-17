import pygame
from pygame.locals import *

white = [255, 255, 255]
displaySize = [1200, 750]
lineSize = 3
start = [600, 375]
end = [650, 425]

pygame.init()

screen = pygame.display.set_mode(displaySize)



paused = False

while True:
    while not paused:

        pygame.draw.line(screen, white, start, end, lineSize)
        pygame.display.update()

        start = end

        end[0] = end[0]+50
        end[1] = end[1]+50



    if paused:
        'Show Menu'
