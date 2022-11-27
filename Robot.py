from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from itertools import count
from dataclasses import dataclass, field
from Point import Point

@dataclass(slots=True)
class Robot:   
    id: int = field(init=False, default_factory=count().__next__)
    pos: Point = Point(5,0,10)
    rotation: float = 0.0
    escale: Point = field(init=False, default=Point(3,1,2))
    armEscale: int = field(init=False, default=Point(3,0.7,0.7))
    armRotation: float = field(init=False, default=0.0)
    speed: float = field(init=False, default=0.25) # como deixar em 2.5m/s?
    shotStrenght: float = field(init=False, default=2)
    
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
        
    def defineCoordenates(self): # When calling this funct, must remeber to pop both matrix's
        glPushMatrix()
        # Move to the position
        glTranslatef(self.pos.x,self.pos.y,self.pos.z)
        glRotatef(self.rotation,0,1,0)
        # Draw the arm
        glPushMatrix()
        glTranslatef(1,0.5,0)
        self.rotateAroundPoint(self.armRotation, Point(-1,0,0))
        
    def shoot(self):
        self.defineCoordenates()
        glTranslatef(self.armEscale.x/2+self.shotStrenght,0,0)
        angle = -1 * (90 - self.armRotation)
        glRotatef(angle,0,0,1)
        self.drawShot()
        glPopMatrix()
        glPopMatrix()
        
    def drawShot(self):
        glBegin(GL_LINES)
        glVertex3f(0,0,0)
        glVertex3f(self.armEscale.x/2+self.shotStrenght,0,0)
        glEnd()
    
    def drawTank(self):
        self.defineCoordenates()
        # Draw aim helper
        self.drawShot()
        # Draw the arm
        glScalef(self.armEscale.x,self.armEscale.y,self.armEscale.z)
        glutSolidCube(1)
        glPopMatrix()
        # Draw the tank
        glScalef(self.escale.x,self.escale.y,self.escale.z)
        glutSolidCube(1)
        glPopMatrix()
        