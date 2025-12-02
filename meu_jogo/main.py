import pygame
from scripts.cenas import Menu, Partida, Vitoria, Transicao

pygame.init()

tamanho = (600, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Jogo - 3 Fases")

clock = pygame.time.Clock()
FPS = 60

# cena atual começa no menu
cenaAtual = "menu"
cena = Menu(tela)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    proxima = cena.atualizar()

    # se mudou de cena, cria do zero
    if proxima != cenaAtual:
        cenaAtual = proxima

        if proxima == "menu":
            cena = Menu(tela)
        if proxima == "fase1":
            cena = Partida(tela, fase=1)
        if proxima == "fase2":
            cena = Partida(tela, fase=2)
        if proxima == "fase3":
            cena = Partida(tela, fase=3)
        if proxima == "vitoria":
            cena = Vitoria(tela)
        if proxima == "transicao_1_2":
            cena = Transicao(tela, 1, 2)
        if proxima == "transicao_2_3":
            cena = Transicao(tela, 2, 3)

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
