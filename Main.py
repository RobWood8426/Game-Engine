import Camera
import pygame
from pygame.time import Clock
running = True
paused = False
Game = Camera.Camera()
clock = Clock()
while running:
    while not paused:
        clock.tick(60)
        Game.updateScreen()
        pygame.event.clear()

