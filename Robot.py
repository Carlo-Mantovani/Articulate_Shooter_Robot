from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from itertools import count
from dataclasses import dataclass, field
from Point import Point

@dataclass(slots=True)
class Robot:   
    id: int = field(init=False, default_factory=count().__next__)
    pos: Point = Point(0,0,10)
    escale: Point = field(init=False, default=Point(3,1,2))
    rotation: float = 180.0
    armEscale: int = field(init=False, default=Point(0.5,2,0.5))
    armRotation: float = 90.0
    speed: float = 0.25
    
    def move(self, direction: int): # direction should be 1 or -1
        vector = Point(1,0,0)
        vector.rotateY(self.rotation)
        self.pos = self.pos + vector * self.speed * direction    
        
    def rotateArm(self, direction: int): # direction should be 1 or -1
        newAngle = abs(self.armRotation + 3 * direction) 
        if (newAngle > 90 or newAngle < 15):
            return
        self.armRotation = newAngle
    
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
            self.pos.x,
            self.pos.y+0.75,
            self.pos.z
            )
        glRotatef(self.rotation,0,1,0)
        glRotatef(self.armRotation,0,0,1)
        
        glScalef(self.armEscale.x,self.armEscale.y,self.armEscale.z)
        
        glutSolidCube(1)
        glPopMatrix()