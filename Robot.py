from Point import Point

class Robot:
    tamX=3
    tamY=1
    def __init__(self,x,y,z):
        self.pos = Point(x,y,z)
        
    def imprime(self):
        self.pos.imprime()