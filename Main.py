import Camera, sys

paused = False
Game = Camera.Camera()
count = 0

while True:
    while not paused:
        count +=1
        Game.updateScreen()
        if count == 1000:

            sys.exit(0)