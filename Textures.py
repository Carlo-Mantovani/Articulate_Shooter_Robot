from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image

# **********************************************************************
# LoadTexture
# Retorna o id da textura lida
# **********************************************************************
def LoadTexture(nome) -> int:
    # carrega a imagem
    image = Image.open(nome)
    # converte para o formato de OpenGL
    img_data = np.array(list(image.getdata()), np.uint8)

    # Habilita o uso de textura
    glEnable(GL_TEXTURE_2D)

    # Cria um ID para texura
    texture = glGenTextures(1)
    errorCode = glGetError()
    if errorCode == GL_INVALID_OPERATION:
        print("Erro: glGenTextures chamada entre glBegin/glEnd.")
        return -1

    # Define a forma de armazenamento dos pixels na textura (1= alihamento por byte)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    # Define que tipo de textura ser usada
    # GL_TEXTURE_2D ==> define que ser· usada uma textura 2D (bitmaps)
    # e o nro dela
    glBindTexture(GL_TEXTURE_2D, texture)

    # texture wrapping params
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # texture filtering params
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    errorCode = glGetError()
    if errorCode != GL_NO_ERROR:
        print("Houve algum erro na criacao da textura.")
        return -1

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    # neste ponto, "texture" tem o nro da textura que foi carregada
    errorCode = glGetError()
    if errorCode == GL_INVALID_OPERATION:
        print("Erro: glTexImage2D chamada entre glBegin/glEnd.")
        return -1

    if errorCode != GL_NO_ERROR:
        print("Houve algum erro na criacao da textura.")
        return -1
    return texture

# **********************************************************************
#  Habilita o uso de textura 'NroDaTextura'
#  Se 'NroDaTextura' <0, desabilita o uso de texturas
#  Se 'NroDaTextura' for maior que a quantidade de texturas, gera
#  mensagem de erro e desabilita o uso de texturas
# **********************************************************************
def UseTexture(NroDaTextura: int, Texturas: list):
    if (NroDaTextura > len(Texturas)):
        print("Numero invalido da textura.")
        glDisable(GL_TEXTURE_2D)
        return
    if (NroDaTextura < 0):
        glDisable(GL_TEXTURE_2D)
    else:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, Texturas[NroDaTextura])