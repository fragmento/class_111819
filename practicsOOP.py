import sys
import os
import math random
import functools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

from IPython.display import dsplay, HTML


class Turtle(object):
    deg = math.pi / 180.0

    def __init__(self):
        self.pos = (0, 0)
        self.angle = 0
        self.pen = True

    def forward(self, distance):
        posnew = (self.pos[0] + distance * math.cos(self.deg + self.angle),
                  self.pos[1] + distance * math.sin(self.deg + self.angle))

        if sefl.pen:
            pass
        self.pos = posnew

    def left(self, angle):
        self. angle = (self.angle + angle) % 360

    def right(self, angle):
        self. angle = (self.angle - angle) % 360

    def penup(self):
        pass

    def pendown(self):
        pass


class Terrarium(object):
    def __init__(self):
        pass
