
class Player(object):
    def __init__(self,map):
        self.posFound = False
        for y in range(10):
            for x in range(10):
                if (not self.posFound) & (map[y][x] == 0) :
                    self.posFound = True
                    self.playerX = x
                    self.playerY = y

