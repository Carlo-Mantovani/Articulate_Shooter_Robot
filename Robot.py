from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from itertools import count
from dataclasses import dataclass, field
from Point import Point

@dataclass(slots=True)
class Robot:
    id: int = field(init=False, default_factory=count().__next__)
    pos: Point = Point(5, 0, 10)
    rotation: float = 0.0
    escale: Point = field(init=False, default=Point(3, 1, 2))
    armEscale: int = field(init=False, default=Point(3, 0.7, 0.7))
    armRotation: float = field(init=False, default=0.0)
    speed: float = field(init=False, default=0.25)  
    shotStrenght: float = field(init=False, default=10)
    cannonDirection: Point = field(init=False, default=Point(1, 0, 0))

    def move(self, direction: int) -> None:  # direction should be 1 or -1
        vector = Point(1, 0, 0)
        vector.rotateY(self.rotation)
        self.pos = self.pos + vector * self.speed * direction

    def rotateArm(self, direction: int) -> None:  # direction should be 1 or -1
        newAngle = self.armRotation + 3 * direction
        if (newAngle < 0 or newAngle > 90):
            return
        self.armRotation = newAngle

    def rotateAroundPoint(self, angle: float, p: Point) -> None:
        glTranslatef(p.x, p.y, p.z)
        glRotatef(angle, 0, 0, 1)
        glTranslatef(-p.x, -p.y, -p.z)

    # When calling this funct, must remeber to pop both matrix's
    def defineCoordenates(self) -> None:
        glPushMatrix()
        # Move to the position
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.rotation, 0, 1, 0)
        # Draw the arm
        glPushMatrix()
        glTranslatef(1, 0.5, 0)
        self.rotateAroundPoint(self.armRotation, Point(-1, 0, 0))

    def drawShot(self, modo) -> None:
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(self.armEscale.x/2 + self.shotStrenght/2, 0, 0)
        glEnd()

    def drawTank(self) -> None:
        self.defineCoordenates()
        # Draw aim helper
        self.drawShot(1)

        # Draw the arm
        glScalef(self.armEscale.x, self.armEscale.y, self.armEscale.z)
        glutSolidCube(1)
        glPopMatrix()
        # Draw the tank
        glScalef(self.escale.x, self.escale.y, self.escale.z)
        glutSolidCube(1)
        glPopMatrix()
