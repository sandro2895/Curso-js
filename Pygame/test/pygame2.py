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
relg = pygame.time.Clock()
while True:
    relg.tick(70)
    tela.fill((0, 0, 8))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.line(tela, (255, 255, 0), (0, 240), (largura, 240), 20)
    x = 200
    y += 1.5
    if y >= 186:
        y = 0


    pygame.display.update()

