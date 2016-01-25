import Camera
from pygame.time import Clock

running = True
paused = False
Game = Camera.Camera()
gameClock = Clock()

while running:
    while not paused:
        gameClock.tick(60)
        fps = gameClock.get_fps()

        Game.updateScreen(fps)
