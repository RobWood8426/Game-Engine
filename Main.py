import Camera
running = True
paused = False
Game = Camera.Camera()

while running:
    while not paused:
        Game.updateScreen()

