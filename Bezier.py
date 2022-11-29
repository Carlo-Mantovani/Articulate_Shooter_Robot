from Point import Point
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Bezier:
    def __init__NEW(self, p0:Point, p1:Point, p2:Point, conexoes):
        print ("Construtora da Bezier")
        self.ComprimentoTotalDaCurva = 0.0
        self.Coords = []
        self.Coords += [p0]
        self.Coords += [p1]
        self.Coords += [p2]
        conexoes = [[Bezier]]

    def __init__(self, *args:Point):
        self.ComprimentoTotalDaCurva = 0.0
        self.Coords = []
        self.conexoes = [[]]
        self.indice = 0

        for i in args:
            self.Coords.append(i)

    def Calcula(self, t):
        UmMenosT = 1-t
        P = Point()
        P = self.Coords[0] * UmMenosT * UmMenosT + self.Coords[1] * 2 * UmMenosT * t + self.Coords[2] * t*t
        return P
   
    def Traca(self) -> None:     
        t=0.0
        DeltaT = 1.0/50
        P = Point
        glBegin(GL_LINE_STRIP)
        
        while(t<1.0):
            P = self.Calcula(t)
            glVertex3f(P.x, P.y,P.z)
            t += DeltaT
        P = self.Calcula(1.0) #faz o acabamento da curva
        glVertex3f(P.x, P.y,P.z)
        
        glEnd()

    def CalculaComprimento(self) -> float:
        DeltaT = 1.0/50
        t = DeltaT
        P1,P2 = Point,Point
        self.ComprimentoTotalDaCurva = 0.0
        P1 = self.Calcula(0.0)
        while(t<1.0):
            P2 = self.Calcula(t)
            self.ComprimentoTotalDaCurva += distancia(P1,P2)
            P1 = P2
            t+=DeltaT
        P2 = self.Calcula(1.0)
        self.ComprimentoTotalDaCurva += distancia(P1,P2)
        return self.ComprimentoTotalDaCurva

def distancia(p1:Point, p2:Point) -> Point:
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
           
            