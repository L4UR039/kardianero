import pygame
from pygame.locals import *
from sys import exit

image_bg = 'background.png'

pygame.init()

global SCREEN_SIZE
global screen

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
pygame.display.set_caption("Kardiá Neró")

background = pygame.image.load(image_bg).convert()
background = pygame.transform.scale(background, SCREEN_SIZE)

# Cores
branco = (56, 142, 165)
azul_normal = (0, 128, 255)
azul_hover = (0, 0, 255)
texto_cor = (13, 59, 72) 

fonte = pygame.font.Font(None, 36)

imagem_fundo_jogar = pygame.image.load('imagem_jogar.png')
imagem_fundo_historia = pygame.image.load('imagem_historia.png')

def desenhar_botao(texto, x, y, largura, altura, cor_normal, cor_hover, acao, imagem_fundo=None):
    global SCREEN_SIZE
    global screen
    retangulo = pygame.Rect(x, y, largura, altura)
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if retangulo.collidepoint(mouse_pos):
        pygame.draw.rect(screen, cor_hover, retangulo, border_radius=15)
        if click[0] == 1:
            if imagem_fundo is not None:
                imagem_fundo = pygame.transform.scale(imagem_fundo, SCREEN_SIZE)
                screen.blit(imagem_fundo, (0, 0))
            acao()
    else:
        pygame.draw.rect(screen, cor_normal, retangulo, border_radius=15)

    texto_botao = fonte.render(texto, True, texto_cor)
    texto_retangulo = texto_botao.get_rect()
    texto_retangulo.center = retangulo.center
    screen.blit(texto_botao, texto_retangulo)

def botao_voltar():
    global SCREEN_SIZE
    global screen
    menu_principal()

def iniciar_jogo():
    tela_jogo()

def tela_jogo():
    global SCREEN_SIZE
    global screen
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        desenhar_botao("Voltar", 250, SCREEN_SIZE[1] -75, 100, 50, branco, azul_normal, botao_voltar)
        pygame.display.update()

def iniciar_historia():
    tela_historia()

def tela_historia():
    global SCREEN_SIZE
    global screen
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        desenhar_botao("Voltar", 250, SCREEN_SIZE[1] -75, 100, 50, branco, azul_normal, botao_voltar)
        pygame.display.update()

def menu_principal():
    global SCREEN_SIZE
    global screen
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == VIDEORESIZE:
                SCREEN_SIZE = event.size
                screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
                pygame.display.set_caption(f"Dimensões atuais: {str(event.size)}")

        screen_width, screen_height = SCREEN_SIZE
        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x, y))

        desenhar_botao("Jogar", 200, 200, 200, 50, branco, azul_hover, iniciar_jogo, imagem_fundo_jogar)
        desenhar_botao("História", 200, 300, 200, 50, branco, azul_hover, iniciar_historia, imagem_fundo_historia)
        pygame.display.update()

if __name__ == "__main__":
    menu_principal()