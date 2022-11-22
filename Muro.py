# ************************************************
#   Ponto.py
#   Define a classe Muro
# ************************************************

""" Classe Ponto """
class Muro:   
    def __init__(self, x=0,y=0,z=0, texIndex=0, on = True):
        self.x = x
        self.y = y
        self.z = z
        self.texIndex = texIndex
        self.on = on
