import pygame
import random

class Obstaculo:
    def __init__(self, tela, fase):
        self.tela = tela
        self.larg = 60
        self.alt = 40
        self.x = random.randint(0, 540)
        self.y = -50
        self.vel = 4 + fase * 2

    def mover(self):
        self.y += self.vel

    def desenhar(self):
        pygame.draw.rect(self.tela, (255, 50, 50), (self.x, self.y, self.larg, self.alt))

    def caixa(self):
        return pygame.Rect(self.x, self.y, self.larg, self.alt)
