# ************************************************
#   Point.py
#   Autor: Márcio Sarroglia Pinho
#       pinho@pucrs.br
# ************************************************
import math

class Point:   
    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    """ Imprime os valores de cada eixo do ponto """
    # Faz a impressao usando sobrecarga de funcao
    # https://www.educative.io/edpresso/what-is-method-overloading-in-python
    def imprime(self, msg=None):
        if msg is not None:
            print (msg, self.x, self.y, self.z)
        else:
            print (self.x, self.y, self.z)

    """ Define os valores dos eixos do ponto """
    def set(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def rotateX(self, angle: float):
        radAngle = math.radians(angle)
        y = self.y * math.cos(radAngle) + self.z * math.sin(radAngle)
        z = -self.y * math.sin(radAngle) + self.z * math.cos(radAngle)
        self.y = y
        self.z = z
        
    def rotateY(self, angle: float):
        radAngle = math.radians(angle)
        x = self.x * math.cos(radAngle) + self.z * math.sin(radAngle)
        z = -self.x * math.sin(radAngle) + self.z * math.cos(radAngle)
        self.x = x
        self.z = z
        
    def rotateZ(self, angle: float):
        radAngle = math.radians(angle)
        x = self.x * math.cos(radAngle) - self.y * math.sin(radAngle)
        y = self.x * math.sin(radAngle) + self.y * math.cos(radAngle)
        self.x = x
        self.y = y
                 
    # Definicao de operadores
    # https://www.programiz.com/python-programming/operator-overloading
    def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Point(x, y, z)

    def __mul__(self, other: int):
            x = self.x * other
            y = self.y * other
            z = self.z * other
            return Point(x, y, z)

