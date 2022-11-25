# ************************************************
#   Point.py
#   Autor: Márcio Sarroglia Pinho
#       pinho@pucrs.br
# ************************************************
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
            
    # Definicao de operadores
    # https://www.programiz.com/python-programming/operator-overloading
    def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)

    def __mul__(self, other: int):
            x = self.x * other
            y = self.y * other
            return Point(x, y)
