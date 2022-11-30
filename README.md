# Robô Articulado Atirador

Trabalho 3 da disciplina de Computação Gráfica desenvolvido por Márcio Pinho e alterado por Pedro Gaspary e Carlo Mantovani. O código foi desenvolvido em Python e utiliza a biblioteca PyOpenGL.

O programa simula um jogo, em que o jogador controla um tanque que atira projéteis em um cenário com diversos objetos. Há um grande muro no centro do cenário que pode ser destruído, além de aliados e inimigos. Os aliados são objetos verdes e os inimigos são objetos vermelhos.

O jogo tem um sistema de pontuação dependendo do que for atingido pelo projétil:

| Alvo           	| Pontuação   	|
|----------------	|-------------	|
| Objeto Inimigo 	| +10         	|
| Objeto Aliado  	| -10         	|
| Piso           	| -5          	|
| Muro           	| +5          	|
| Tanque         	| Fim de Jogo 	|

Caso o jogador acerte o próprio tanque, o jogo é encerrado.

## Como executar

Para executar o programa, basta executar, na pasta raíz do projeto, o comando:

    $ python Main.py

O programa será executado automaticamente.  

## Comandos do Programa

### Movimento e Controle do Robô 


O robô pode se mover para frente e para trás, além de rotacionar no eixo Y. O canhão pode ser rotacionado, mirando para cima e para baixo. Por último, uma mira saindo do canhão indica uma estimação da força que será usada no disparo. Essa força também pode ser alterada.
  

`up` - Movimenta o robô para frente

  
`down` - Movimenta o robô para trás

  
`left` - Rotaciona o robô para esquerda

  
`right` - Rotaciona o robô para direita
  

`w` - Rotaciona o canhão para cima

`s` - Rotaciona o canhão para baixo

> O ângulo padrão do canhão é 0°. Tanto o aumento quanto o decremento são  de 5°, até um máximo de 90° e um mínimo de 0°.

`d` - Aumenta a força do disparo

`a` - Diminui a força do disparo

> A força padrão do disparo é uma constante de valor 15. Tanto o aumento quanto o decremento são  de valor 1, até um máximo de 50 e um mínimo de 5.
    
`backspace` - Dispara o projétil

> Um próximo disparo só pode ser dado assim que o anterior atingir seu alvo.

`esc` - Termina o programa
