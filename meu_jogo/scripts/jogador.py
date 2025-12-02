import pygame

class Jogador:
    def __init__(self, tela):
        self.tela = tela
        self.x = 300
        self.y = 500
        self.vel = 6
        self.tam = 40

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT] and self.x < 600 - self.tam:
            self.x += self.vel

    def desenhar(self):
        pygame.draw.rect(self.tela, (0, 150, 255), (self.x, self.y, self.tam, self.tam))

    def caixa(self):
        return pygame.Rect(self.x, self.y, self.tam, self.tam)
