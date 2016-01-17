import random

class Mapping(object):
    def __init__(self):

        self.gamemap = [[random.randint(0,1) for i in range(16)] for j in range(10)]


