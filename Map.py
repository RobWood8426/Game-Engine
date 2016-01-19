import random
import Player

class Mapping(object):
    def __init__(self,mapSize,mapDensity):
        self.mapSize = mapSize
        self.mapDensity = mapDensity
        self.gamemap = [[round(random.uniform(0,self.mapDensity)) for i in range(self.mapSize)] for j in range(self.mapSize)]
        self.player = Player.PlayerOnMap(self.gamemap,self.mapSize)




