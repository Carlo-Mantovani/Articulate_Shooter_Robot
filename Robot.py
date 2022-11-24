from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Point import Point

class Robot:   
    armHeight=2
    def __init__(self):
        self.pos = Point(20,0,10)
        self.escale = Point(3,1,2)
        self.rotation:float = 0.0 
        
    def draw(self):
        glPushMatrix()
        # Draw the tank
        glTranslatef(self.pos.x,self.pos.y,self.pos.z)
        glRotatef(self.rotation,0,1,0)
        glScalef(self.escale.x,self.escale.y,self.escale.z)
        
        glutSolidCube(1)
        glPopMatrix()
        
        glPushMatrix()
        # Draw the first arm
        glTranslatef(
            self.pos.x-1,
            self.pos.y+self.escale.y,
            self.pos.z
            )
        glRotatef(self.rotation,0,1,0)
        glScalef(1,self.armHeight,1)
        
        glutSolidCube(0.5)
        glPopMatrix()
        
        glPushMatrix()
        # Draw the second arm
        glTranslatef(
            self.pos.x-1,
            self.pos.y+self.escale.y+0.70,
            self.pos.z
            )
        glRotatef(self.rotation,0,1,0)
        glScalef(1,self.armHeight,1)
        
        glutSolidCube(0.25)
        glPopMatrix()