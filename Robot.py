
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
        self.shotStrength:    float = 15
        self.min:             Point = Point(3.5, 0, 9)
        self.max:             Point = Point(6.5, 1, 11)

    def updateMinMax(self) -> None:
        position = Point(self.pos.x, self.pos.y, self.pos.z)
        position.rotateY(self.rotation)
    
        self.min.x = position.x - self.escale.x/2
        self.max.x = position.x + self.escale.x/2
        self.min.y = 0
        self.max.y = 1
        self.min.z = position.z - self.escale.z/2
        self.max.z = position.z + self.escale.z/2

    
    def move(self, direction: int) -> None:  # direction should be 1 or -1
        vector = Point(1, 0, 0)
        vector.rotateY(self.rotation)
        self.pos = self.pos + vector * self.speed * direction
        self.updateMinMax()

    def rotateArm(self, direction: int) -> None:  # direction should be 1 or -1
        newAngle = self.cannonRotation + 5 * direction
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
        glColor3f(0.0, 0.0, 0.5)
        
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(self.cannonEscale.x/2 + self.shotStrength/5, 0, 0)
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
