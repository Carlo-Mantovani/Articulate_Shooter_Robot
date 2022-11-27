# ***********************************************************************************
#   Autor: Marcio Sarroglia Pinho
#   pinho@pucrs.br
#
#   Para construir este programa, foi utilizada a biblioteca PyOpenGL, disponível em
#   http://pyopengl.sourceforge.net/documentation/index.html
#
#   Outro exemplo de código em Python, usando OpenGL3D pode ser obtido em
#   http://openglsamples.sourceforge.net/cube_py.html
#
#   Sugere-se consultar tambem as paginas listadas
#   a seguir:
#   http://bazaar.launchpad.net/~mcfletch/pyopengl-demo/trunk/view/head:/PyOpenGL-Demo/NeHe/lesson1.py
#   http://pyopengl.sourceforge.net/documentation/manual-3.0/index.html#GLUT
#
# ***********************************************************************************
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Robot import Robot
from Point import Point
import Textures

import time
import random

Texturas = []
Angulo = 0.0

tamX = 50
tamY = 15
tamZ = 25
MuroMatrix = [[True for _ in range(tamZ)]for _ in range(tamY)] # Matriz 15x25

robot = Robot()
# ***********************************************
#  Ponto calcula_ponto(Ponto p, Ponto &out)
#
#  Esta funcao calcula as coordenadas
#  de um ponto no sistema de referencia da
#  camera (SRC), ou seja, aplica as rotaçcoes,
#  escalas e translacoes a um ponto no sistema
#  de referencia do objeto SRO.
#  Para maiores detalhes, veja a pagina
#  https://www.inf.pucrs.br/pinho/CG/Aulas/OpenGL/Interseccao/ExerciciosDeInterseccao.html
def CalculaPonto(p: Point) -> Point:
    ponto_novo = [0, 0, 0, 0]

    mvmatrix = glGetDoublev(GL_MODELVIEW_MATRIX)
    for i in range(0, 4):
        ponto_novo[i] = mvmatrix[0][i] * p.x + \
            mvmatrix[1][i] * p.y + \
            mvmatrix[2][i] * p.z + \
            mvmatrix[3][i]

    x = ponto_novo[0]
    y = ponto_novo[1]
    z = -ponto_novo[2]
    
    return Point(x, y, z)           

# **********************************************************************
#  init()
#  Inicializa os parametros globais de OpenGL
# **********************************************************************
def init():
    # Define a cor do fundo da tela (BRANCO)
    glClearColor(0.5, 0.5, 0.5, 1.0)

    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    global Texturas
    Texturas += [Textures.LoadTexture("textures/grass.jpg")]
    Texturas += [Textures.LoadTexture("textures/bricks.jpg")]
# **********************************************************************
#
# **********************************************************************
def PosicUser():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, AspectRatio, 0.01, 50)  # Projecao perspectiva

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5, 4, 22, 5, 4, 10, 0, 1.0, 0)

# **********************************************************************
#  reshape( w: int, h: int )
#   trata o redimensionamento da janela OpenGL
# **********************************************************************
def reshape(w: int, h: int):
    global AspectRatio
    # Evita divisao por zero, no caso de uam janela com largura 0.
    if h == 0:
        h = 1
    # Ajusta a relacao entre largura e altura para evitar distorcao na imagem.
    # Veja funcao "PosicUser".
    AspectRatio = w / h
    # Reset the coordinate system before modifying
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Seta a viewport para ocupar toda a janela
    glViewport(0, 0, w, h)

    PosicUser()

# **********************************************************************
def DefineLuz():
    # Define cores para um objeto dourado
    LuzAmbiente = [0.4, 0.4, 0.4]
    LuzDifusa = [0.7, 0.7, 0.7]
    LuzEspecular = [0.9, 0.9, 0.9]
    PosicaoLuz0 = [2.0, 3.0, 0.0]  # Posicao da Luz
    Especularidade = [1.0, 1.0, 1.0]

    glEnable(GL_COLOR_MATERIAL)

    # Habilita o uso de iluminacao
    glEnable(GL_LIGHTING)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LuzAmbiente)
    # Define os parametros da luz numero Zero
    glLightfv(GL_LIGHT0, GL_AMBIENT, LuzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LuzDifusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LuzEspecular)
    glLightfv(GL_LIGHT0, GL_POSITION, PosicaoLuz0)
    glEnable(GL_LIGHT0)

    # Ativa o "Color Tracking"
    glEnable(GL_COLOR_MATERIAL)

    # Define a reflectancia do material
    glMaterialfv(GL_FRONT, GL_SPECULAR, Especularidade)

    # Define a concentracao do brilho.
    # Quanto maior o valor do Segundo parametro, mais
    # concentrado sera o brilho. (Valores validos: de 0 a 128)
    glMateriali(GL_FRONT, GL_SHININESS, 51)

# **********************************************************************
# DesenhaCubo()
#   Desenha o cenario
# **********************************************************************
def DesenhaCubo():

    glPushMatrix()
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glutSolidCube(1)
    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glPopMatrix()

# **********************************************************************
# void DesenhaPiso()
#   Desenha o piso como um unico grande ladrilho
# **********************************************************************
def DesenhaPiso():
    glPushMatrix()
    
    Textures.UseTexture(0, Texturas)
    glTranslatef(tamX/2,-1,tamZ/2-0.5)
    glScaled(tamX,0,tamZ+2.5)
    
    glColor3f(1, 1, 1)  # desenha QUAD em branco, pois vai usar textura
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glTexCoord(0, 0)
    glVertex3f(-0.5,  0.0, -0.5)
    glTexCoord(0, 1)
    glVertex3f(-0.5,  0.0,  0.5)
    glTexCoord(1, 1)
    glVertex3f(0.5,  0.0,  0.5)
    glTexCoord(1, 0)
    glVertex3f(0.5,  0.0, -0.5)
    glEnd()

    glColor3f(1, 1, 1)  # desenha a borda da QUAD
    glBegin(GL_LINE_STRIP)
    glNormal3f(0, 1, 0)
    glVertex3f(-0.5,  0.0, -0.5)
    glVertex3f(-0.5,  0.0,  0.5)
    glVertex3f(0.5,  0.0,  0.5)
    glVertex3f(0.5,  0.0, -0.5)
    glEnd()
    glPopMatrix()

# **********************************************************************
def DesenhaMuro():
    Textures.UseTexture(1, Texturas)
    for i in range (tamY):
        for j in range (tamZ):
            if MuroMatrix[i][j]:
                glPushMatrix()
                glTranslated(tamX/2, i, j)
                DesenhaCubo()
                glPopMatrix()

# **********************************************************************
# display()
#   Funcao que exibe os desenhos na tela
# **********************************************************************
def display():
    global Angulo
    # Limpa a tela com  a cor de fundo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    CalculaPonto(Point(0,0,0))

    DefineLuz()
    PosicUser()
    glMatrixMode(GL_MODELVIEW)

    DesenhaPiso()
    DesenhaMuro()
    
    glColor3f(0.5, 0.0, 0.0)  # Vermelho
    robot.drawTank()
    robot.shoot()

    print("")
    #print (robot.shotTrajectory[0].imprime())
    #print (robot.shotTrajectory[1].imprime())
    #print (robot.shotTrajectory[2].imprime())

    Angulo = Angulo + 1
    glutSwapBuffers()

# **********************************************************************
# animate()
#   Funcao chama enquanto o programa esta ocioso
#   Calcula o FPS e numero de interseccao detectadas, junto com outras informacoes
#
# **********************************************************************
# Variaveis Globais
nFrames, TempoTotal, AccumDeltaT = 0, 0, 0
oldTime = time.time()
def animate():
    global nFrames, TempoTotal, AccumDeltaT, oldTime

    nowTime = time.time()
    dt = nowTime - oldTime
    oldTime = nowTime

    AccumDeltaT += dt
    TempoTotal += dt
    nFrames += 1

    if AccumDeltaT > 1.0/30:  # fixa a atualizacao da tela em 30
        AccumDeltaT = 0
        glutPostRedisplay()


# **********************************************************************
#  keyboard ( key: int, x: int, y: int )
#
# **********************************************************************
ESCAPE = b'\x1b'
def keyboard(*args):
    global image, MuroMatrix
    # If escape is pressed, kill everything.
    if args[0] == b'a':
        if (robot.shotStrenght > 1.5):
            robot.shotStrenght -= 0.5
    if args[0] == b'd':
        if (robot.shotStrenght < 10):
            robot.shotStrenght += 0.5
    if args[0] == b'i':
        image.show()
    if args[0] == b's':
        robot.rotateArm(-1)
    if args[0] == b'w':
        robot.rotateArm(1)
    if args[0] == b' ':
        init()
    if args[0] == ESCAPE:   # Termina o programa qdo
        os._exit(0)         # a tecla ESC for pressionada

    # Forca o redesenho da tela
    glutPostRedisplay()

# **********************************************************************
#  arrow_keys ( a_keys: int, x: int, y: int )
# **********************************************************************
def arrow_keys(a_keys: int, x: int, y: int):
    if a_keys == GLUT_KEY_UP:         # Se pressionar UP
            robot.move(1)
            if(not isInside()):
                robot.move(-1)
    if a_keys == GLUT_KEY_DOWN:       # Se pressionar DOWN
            robot.move(-1)
            if (not isInside()):
                robot.move(1)
    if a_keys == GLUT_KEY_LEFT:       # Se pressionar LEFT
        robot.rotation += 3
    if a_keys == GLUT_KEY_RIGHT:      # Se pressionar RIGHT
        robot.rotation -= 3

    glutPostRedisplay()

def isInside():
    delta = robot.escale.x/2
    return robot.pos.x >= delta and \
           robot.pos.x < tamX-delta and \
           robot.pos.z >= 0 and \
           robot.pos.z < tamZ-1

def mouse(button: int, state: int, x: int, y: int):
    glutPostRedisplay()

def mouseMove(x: int, y: int):
    glutPostRedisplay()

# ***********************************************************************************
# Programa Principal
# ***********************************************************************************
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_RGB)
    glutInitWindowPosition(0, 0)

    # Define o tamanho inicial da janela grafica do programa
    glutInitWindowSize(650, 500)
    # Cria a janela na tela, definindo o nome da
    # que aparecera na barra de ti­tulo da janela.
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Articulate Shooter Robot")

    # executa algumas inicializacoes
    init()

    # Define que o tratador de evento para
    # o redesenho da tela. A funcao "display"
    # sera chamada automaticamente quando
    # for necessario redesenhar a janela
    glutDisplayFunc(display)
    glutIdleFunc(animate)

    # o redimensionamento da janela. A funcao "reshape"
    # Define que o tratador de evento para
    # sera chamada automaticamente quando
    # o usuario alterar o tamanho da janela
    glutReshapeFunc(reshape)

    # Define que o tratador de evento para
    # as teclas. A funcao "keyboard"
    # sera chamada automaticamente sempre
    # o usuario pressionar uma tecla comum
    glutKeyboardFunc(keyboard)

    # Define que o tratador de evento para
    # as teclas especiais(F1, F2,... ALT-A,
    # ALT-B, Teclas de Seta, ...).
    # A funcao "arrow_keys" sera chamada
    # automaticamente sempre o usuario
    # pressionar uma tecla especial
    glutSpecialFunc(arrow_keys)

    # glutMouseFunc(mouse)
    # glutMotionFunc(mouseMove)
    try:
        # inicia o tratamento dos eventos
        glutMainLoop()
    except SystemExit:
        pass

if __name__ == '__main__':
    main()
