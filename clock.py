# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:38:32 2013

@author: Nick Walker
"""

if __name__ == '__build__':
	raise Exception

import sys
from math import *
from time import *
from datetime import datetime

circleV = 360
angle = 0.0
da = pi/180
h = (localtime()[3] + localtime()[4]/60 + localtime()[5]/360)/12.*2*pi
m = (localtime()[4] + localtime()[5]/60)/60.*2*pi
s = (localtime()[5])/60.*2*pi

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''
  sys.exit()

def init():
   glClearColor(0.0, 0.0, 0.0, 0.0)
   glShadeModel(GL_FLAT)   

def display():
   global circleV 
   global angle
   global da
   global s
   global m
   global h
   
   glClear(GL_COLOR_BUFFER_BIT)
   glPushMatrix()
   
   glColor3f(1.0, 1.0, 1.0)
   glBegin(GL_POLYGON)
   glVertex2d(50*cos(angle), 50*sin(angle))
   for n in range(circleV):
      glVertex2d(50*cos(angle), 50*sin(angle)) 
      angle = angle + da
   glEnd()   
   
   glColor(1.0, 0.0, 0.0)
   glLineWidth(1.0)
   glBegin(GL_LINES)
   glVertex2d(0.0, 0.0)
   glVertex2d(30.0*sin(s), 30.0*cos(s))
   glEnd()
   
   glColor(1.0, 0.0, 0.0)
   glLineWidth(2.0)
   glBegin(GL_LINES)
   glVertex2d(0.0, 0.0)
   glVertex2d(20.0*sin(m), 20.0*cos(m))
   glEnd()
   
   glColor(1.0, 0.0, 0.0)
   glLineWidth(4.0)
   glBegin(GL_LINES)
   glVertex2d(0.0, 0.0)
   glVertex2d(10*sin(h), 10*cos(h))
   glEnd()
   
   glColor3f(1.0, 1.0, 1.0)
   glBegin(GL_POLYGON)
   glVertex2d(4*sin(angle), 4*cos(angle))
   for n in range(circleV):
      glVertex2d(4*cos(angle), 4*sin(angle))
      angle = angle + da
   glEnd()

   glColor3f(1.0, 0.0, 0.0)
   glBegin(GL_POLYGON)
   glVertex2d(2*sin(angle), 2*cos(angle))
   for n in range(circleV):
      glVertex2d(2*cos(angle), 2*sin(angle))
      angle = angle + da
   glEnd()      
   
   glPopMatrix()
   glutSwapBuffers()
   
def time():
   global s
   global m
   global h
   h = (localtime()[3] + localtime()[4]/60. + localtime()[5]/360.)/12.*2*pi
   m = (localtime()[4] + localtime()[5]/60.)/60.*2*pi
   s = ((localtime()[5])/60.)*2*pi
   glutPostRedisplay()
   
def reshape(w, h):
   glViewport(0, 0, w, h)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(512, 512)
glutInitWindowPosition(100, 100)
glutCreateWindow('Clock')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutIdleFunc(time)
glutMainLoop()