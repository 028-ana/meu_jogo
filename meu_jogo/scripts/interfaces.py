import pygame

class Texto:
    def __init__(self, tela, msg, tam, cor, x, y):
        self.tela = tela
        self.font = pygame.font.SysFont("Arial", tam)
        self.msg = msg
        self.cor = cor
        self.x = x
        self.y = y

    def desenhar(self):
        t = self.font.render(self.msg, True, self.cor)
        self.tela.blit(t, (self.x, self.y))


class Botao:
    def __init__(self, tela, texto, x, y):
        self.tela = tela
        self.font = pygame.font.SysFont("Arial", 40)
        self.texto = texto
        self.rect = pygame.Rect(x, y, 200, 70)

    def desenhar(self):
        pygame.draw.rect(self.tela, (200, 200, 200), self.rect)
        txt = self.font.render(self.texto, True, (0, 0, 0))
        self.tela.blit(txt, (self.rect.x + 40, self.rect.y + 20))

    def clicou(self):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False
