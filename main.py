import pygame
from scripts.cenas import Menu, Partida, Transicao, Morte, Vitoria

pygame.init()

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Desafio Triplo")

clock = pygame.time.Clock()
FPS = 60

cena_atual = "menu"
cena = Menu(tela)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    proxima = cena.atualizar()

    if proxima != cena_atual:
        cena_atual = proxima

        if proxima == "menu":
            cena = Menu(tela)

        elif proxima.startswith("fase"):
            partes = proxima.replace("fase", "").split("_")
            fase = int(partes[0])
            dificuldade = partes[1]
            cena = Partida(tela, fase, dificuldade)

        elif proxima.startswith("transicao"):
            partes = proxima.split("_")
            atual = int(partes[1])
            prox = int(partes[2])
            dificuldade = partes[3]
            cena = Transicao(tela, atual, prox, dificuldade)

        elif proxima == "morte":
            cena = Morte(tela)

        elif proxima == "vitoria":
            cena = Vitoria(tela)

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
