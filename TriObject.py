from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Point import Point
from Tri import Tri

class TriObject:
    def __init__(self, pos: Point, 
                 escale: Point, 
                 model: Tri
                ) -> None:
        self.pos = pos 
        self.escale = escale
        self.model = model

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
              if (j != 3):
                    glVertex3f(
                        self.model.vertices[i][j].x, 
                        self.model.vertices[i][j].y, 
                        self.model.vertices[i][j].z)
            glEnd()
        glPopMatrix()
