import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 640
altura = 480
x = 0
y = 0
pygame.display.set_caption('ExemploJogo')
tela = pygame.display.set_mode((largura, altura))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.circle(tela, (0, 0, 255), (200, 45), 40)
    pygame.display.update()
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 480), 20)
