from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Point import Point

class Robot:
    Length=3
    Height=1
    Width=2    
    armHeight=2
    def __init__(self,tank: Point):
        self.tankPos = tank
        
    def draw(self):
        glPushMatrix()
        # Draw the tank
        glTranslatef(self.tankPos.x,self.tankPos.y,self.tankPos.z)
        glScalef(self.Length,self.Height,self.Width)
        glutSolidCube(1)
        
        glPopMatrix()
        
        glPushMatrix()
        # Draw the first arm
        glTranslatef(self.tankPos.x-1,self.tankPos.y+self.Height,self.tankPos.z)
        glScalef(1,self.armHeight,1)
        glutSolidCube(0.5)
        
        glPopMatrix()
        
        glPushMatrix()
        # Draw the second arm
        glTranslatef(self.tankPos.x-1,self.tankPos.y+self.Height+0.80,self.tankPos.z)
        glScalef(1,self.armHeight,1)
        glutSolidCube(0.25)
        
        glPopMatrix()