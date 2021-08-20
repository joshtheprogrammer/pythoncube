from win32api import GetSystemMetrics

import pygame
from pygame.locals import *

import threading
import time

import math
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.constants import OPENGL

class Render(object):
    def __init__(self, W, H):
        self.W, self.H = W, H

        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )

        self.edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )

    def Cube(self, col, pos, rot):
        glPushMatrix()
        glLoadIdentity()
    
        glColor(col[0], col[1], col[2])

        gluPerspective(45, self.W/self.H, 0.1, 50.0)
        glTranslatef(pos[0], pos[1], pos[2])
        glRotatef(rot[0], rot[1],rot[2],rot[3])

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                c1 = self.vertices[vertex]
                glVertex3fv(c1)
        glEnd()

        glPopMatrix()        

def randomcolor():
    while True:
        for color in range(3):
            c[color] = random.random()
        time.sleep(1)

if __name__ == "__main__":
    c = [0,0,0]
    threading.Thread(target=randomcolor).start()

    W, H = GetSystemMetrics(0),GetSystemMetrics(1)
    r = Render(W, H)

    pygame.init()
    pygame.display.set_caption("mongus 1.0")
    pygame.display.set_mode((W, H), DOUBLEBUF|OPENGL)

    glClearColor(0.1, 0.1, 0.1, 1.0)

    arch = False

    mag = 2

    count = 0
    count2 = 0
    count3 = 0

    while 1:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

        if count > mag*3.14:
            arch = True
        if count2 > mag*3.14:
            count = 0
            count2 = 0
            count3 = 0
            mag = 2
            arch = False
        
        if arch == False:
            r.Cube(c,[count,0,-10], [1,1,3,1])
            count += .08
            
        else:
            r.Cube(c,[count-count2, math.sin(count2/mag), -10], [count3*6,1,1,count*3])
            count2 += .08
            count3 += 1

        pygame.display.flip()
        pygame.time.wait(10)

        

        
        


        