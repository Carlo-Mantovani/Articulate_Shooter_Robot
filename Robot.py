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
    rotation: float = 0.0
    armEscale: int = field(init=False, default=Point(3,0.7,0.7))
    armRotation: float = 0.0
    speed: float = 0.25
    
    def move(self, direction: int): # direction should be 1 or -1
        vector = Point(1,0,0)
        vector.rotateY(self.rotation)
        self.pos = self.pos + vector * self.speed * direction    
        
    def rotateArm(self, direction: int): # direction should be 1 or -1
        newAngle = self.armRotation + 3 * direction
        if (newAngle < 0 or newAngle > 75):
            return
        self.armRotation = newAngle
        
    def rotateAroundPoint(self, angle: float, p: Point):
        glTranslatef(p.x, p.y, p.z)
        glRotatef(angle, 0,0,1)
        glTranslatef(-p.x, -p.y, -p.z)
    
    def draw(self):
        glPushMatrix()
        # Move to the position
        glTranslatef(self.pos.x,self.pos.y,self.pos.z)
        glRotatef(self.rotation,0,1,0)
        # Draw the arm
        glPushMatrix()
        glTranslatef(1,0.5,0)
        self.rotateAroundPoint(self.armRotation, Point(-1,0,0))
        glScalef(self.armEscale.x,self.armEscale.y,self.armEscale.z)
        
        glutSolidCube(1)
        glPopMatrix()
        # Draw the tank
        glScalef(self.escale.x,self.escale.y,self.escale.z)
        glutSolidCube(1)
        glPopMatrix()
        