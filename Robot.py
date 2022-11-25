from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from itertools import count
from dataclasses import dataclass, field
from Point import Point

@dataclass(slots=True)
class Robot:   
    id: int = field(init=False, default_factory=count().__next__)
    pos: Point = Point(20,0,10)
    escale: Point = field(init=False, default=Point(3,1,2))
    rotation: float = 0.0
    armHeight: int = 2
    
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