from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Point import Point

class Robot:
    def __init__(self) -> None:
        self.pos:             Point = Point(5, 0, 10)
        self.rotation:        float = 0.0
        self.escale:          Point = Point(3, 1, 2)
        self.speed:           float = 0.25
        self.cannonEscale:    int   = Point(3, 0.7, 0.7)
        self.cannonRotation:  float = 0.0
        self.cannonDirection: Point = Point(1, 0, 0)
        self.shotStrenght:    float = 10

    def move(self, direction: int) -> None:  # direction should be 1 or -1
        vector = Point(1, 0, 0)
        vector.rotateY(self.rotation)
        self.pos = self.pos + vector * self.speed * direction

    def rotateArm(self, direction: int) -> None:  # direction should be 1 or -1
        newAngle = self.cannonRotation + 3 * direction
        if (newAngle < 0 or newAngle > 90):
            return
        self.cannonRotation = newAngle

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
        # Move to the end of the cannon
        glPushMatrix()
        glTranslatef(1, 0.5, 0)
        self.rotateAroundPoint(self.cannonRotation, Point(-1, 0, 0))

    def drawShot(self) -> None:
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(self.cannonEscale.x/2 + self.shotStrenght/5, 0, 0)
        glEnd()

    def drawTank(self) -> None:
        self.defineCoordenates()
        # Draw aim helper
        self.drawShot()

        # Draw the arm
        glColor3f(0.0, 0.0, 0.5)
        
        glScalef(self.cannonEscale.x, self.cannonEscale.y, self.cannonEscale.z)
        glutSolidCube(1)
        glPopMatrix()
        # Draw the tank
        glColor3f(0.5, 0.0, 0.0)  # Vermelho
        
        glScalef(self.escale.x, self.escale.y, self.escale.z)
        glutSolidCube(1)
        glPopMatrix()
