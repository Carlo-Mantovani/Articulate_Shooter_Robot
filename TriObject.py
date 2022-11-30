from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from dataclasses import dataclass, field
from Point import Point
from TriModel import TriModel

@dataclass(slots=True)
class TriObject:
    pos:    Point 
    escale: Point
    model:  TriModel
    min:    Point = field(init=False) 
    max:    Point = field(init=False)

    def __post_init__(self) -> None:
        self.min = (self.model.min + self.pos)
        self.max = (self.model.max + self.pos)

        self.min.x *= self.escale.x
        self.max.x *= self.escale.x
        self.min.y *= self.escale.y
        self.max.y *= self.escale.y
        self.min.z *= self.escale.z
        self.max.z *= self.escale.z

    def drawObject(self):
        glPushMatrix()
        glColor3f(
            self.model.color[0],
            self.model.color[1],
            self.model.color[2])

        glTranslatef(
            self.pos.x,
            self.pos.y,
            self.pos.z)

        glScalef(
            self.escale.x,
            self.escale.y,
            self.escale.z
        )   

        for i in range (len(self.model.vertices)):
            glBegin(GL_TRIANGLES)
            for j in range (len(self.model.vertices[i])):
                if j == 0:
                    glNormal3f(
                        self.model.vertices[i][3].x,
                        self.model.vertices[i][3].y,
                        self.model.vertices[i][3].z)
                if (j != 3):
                    glVertex3f(
                        self.model.vertices[i][j].x, 
                        self.model.vertices[i][j].y, 
                        self.model.vertices[i][j].z)
            glEnd()
        glPopMatrix()
