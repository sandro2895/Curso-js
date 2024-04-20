import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 720
altura = 640
y = altura/2
x = largura/2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo2')
rell = pygame.time.Clock()

while True:
    rell.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

     #   if event.type == KEYDOWN:
       #     if event.key == K_a or event.key == K_LEFT:
               # x -= 15
        #    if event.key == K_d or event.key == K_RIGHT:
                #x += 15
        #    if event.key == K_w or event.key == K_UP:
               # y -= 15
        #    if event.key == K_s or event.key == K_DOWN:
         #       #y += 15


    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x -= 5
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x += 5
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y -= 5
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y += 5
    pygame.draw.rect(tela, (0, 255, 0), (x, y, 100, 15))
    pygame.display.update()


