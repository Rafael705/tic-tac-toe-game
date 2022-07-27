import pygame
from pygame.draw import rect
from pygame.locals import *
from sys import exit

global VEZ

def desenhar_tabu():
    pygame.draw.line(tela, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 400), (600, 400), 10)

def draw_piece(pos):
    x, y = pos
    if VEZ == 'JOGADOR2':
        pygame.draw.circle(tela, (0, 0, 255), pos, 50)
    else:
        imagem = pygame.image.load('x.png').convert_alpha()
        imgR = pygame.transform.scale(imagem, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

def test_position():
    for p in rec:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                confimar(0, [100, 100])
            if p == rect2:
                confimar(1, [300, 100])
            if p == rect3:
                confimar(2, [500, 100])
            if p == rect4:
                confimar(3, [100, 300])
            if p == rect5:
                confimar(4, [300, 300])
            if p == rect6:
                confimar(5, [500, 300])
            if p == rect7:
                confimar(6, [100, 500])
            if p == rect8:
                confimar(7, [300, 500])
            if p == rect9:
                confimar(8, [500, 500])

def confimar(indice, pos):
    global ESCOLHA, VEZ, espaco
    if marca_tabu[indice] == 'X':
        print('X')
    elif marca_tabu[indice] == 'O':
        print('O')
    else:
        marca_tabu[indice] = ESCOLHA
        draw_piece(pos)
        print(marca_tabu)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
        else:
            VEZ = 'JOGADOR1'
        espaco +=1
       
def test_victory(l):
    return ((marca_tabu[0] == l and marca_tabu[1] == l and marca_tabu[2] == l) or
        (marca_tabu[3] == l and marca_tabu[4] == l and marca_tabu[5] == l) or
        (marca_tabu[6] == l and marca_tabu[7] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[3] == l and marca_tabu[6] == l) or
        (marca_tabu[1] == l and marca_tabu[4] == l and marca_tabu[7] == l) or
        (marca_tabu[2] == l and marca_tabu[5] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[4] == l and marca_tabu[8] == l) or
        (marca_tabu[2] == l and marca_tabu[4] == l and marca_tabu[6] == l))

def text_victory(v):
    ariel = pygame.font.SysFont('ariel', 35)
    message = 'JOGADOR {} VENCEU'.format(v)

    if v == 'EMPATE':
        mens_victory = ariel.render('DEU VELHA', True, (0, 255, 255), 0)
        tela.blit(mens_victory, (0, 265))
    else:
        mens_victory = ariel.render(message, True, (0, 255, 255), 0)
        tela.blit(mens_victory, (0, 265))

def reset():
    global ESCOLHA, ESTADO, VEZ, marca_tabu, espaco
    ESTADO = 'JOGANDO'
    VEZ = 'JOGADOR1'
    ESCOLHA = 'X'
    espaco = 0
    marca_tabu = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
    ]
    tela.fill(0)

def pontos(pontos1, pontos2):
    arial = pygame.font.SysFont('mingliuextbpmingliuextbmingliuhkscsextb', 25)
    jogador1 = 'Jogador1 = {}'.format(pontos1)
    jogador2 = 'Jogador2 = {}'.format(pontos2)

    jd1 = arial.render(jogador1, True, (189, 184, 185))
    jd2 = arial.render(jogador2, True, (189, 184, 185))
    tela.blit(jd1, (0, 0))
    tela.blit(jd2, (420, 0))

pygame.init()

tela = pygame.display.set_mode((600,600), 0, 32)
pygame.display.set_caption('tic-tac-toe game ')

ESTADO = 'JOGANDO'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
espaco = 0
marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200, 200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

rec =[
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9
]

pontos1, pontos2 = 0, 0

while True:
    mouse_pos = pygame.mouse.get_pos()
    if ESTADO == 'JOGANDO':
        desenhar_tabu()
        pontos(pontos1, pontos2)

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                if VEZ == 'JOGADOR1':
                    ESCOLHA = 'X'
                    test_position()
                else:
                    ESCOLHA = 'O'
                    test_position()

        if test_victory('X'):
            print('jogador1 VENCEU')
            text_victory('X')
            ESTADO = 'REST'
            pontos1 += 1

        elif test_victory('O'):
            print('Jogador2 VENCEU')
            text_victory('O')
            ESTADO = 'REST'
            pontos2 += 1
        elif espaco >= 9:
            print('EMPATE')
            text_victory('EMPATE')
            ESTADO = 'REST'

        
    else:
        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
                reset()
                desenhar_tabu()

    pygame.display.flip()
