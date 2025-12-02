import pygame
from scripts.interfaces import Texto, Botao
from scripts.obstaculo import Obstaculo
from scripts.jogador import Jogador
import random

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "JOGO - 3 FASES", 50, (255, 255, 255), 100, 100)
        self.botao = Botao(tela, "Jogar", 200, 300)

    def atualizar(self):
        self.tela.fill((30, 30, 30))
        self.titulo.desenhar()
        self.botao.desenhar()

        if self.botao.clicou():
            return "fase1"

        return "menu"


class Partida:
    def __init__(self, tela, fase):
        self.tela = tela
        self.fase = fase
        self.jogador = Jogador(tela)
        self.obstaculos = []
        self.tempo = 0
        self.dificuldade = 40 - fase*5  # menor = mais obstáculos

        self.txt = Texto(tela, f"FASE {fase}", 40, (255, 255, 0), 10, 10)

    def atualizar(self):
        self.tela.fill((0, 0, 0))
        self.txt.desenhar()

        self.jogador.mover()
        self.jogador.desenhar()

        self.tempo += 1

       # Spawn normal (mais frequente)
        if random.randint(1, self.dificuldade) == 1:
         self.obstaculos.append(Obstaculo(self.tela, self.fase))

# Spawn em ondas (às vezes)
        if random.randint(1, self.dificuldade * 2) == 1:
             for i in range(random.randint(1, 3)):
                 self.obstaculos.append(Obstaculo(self.tela, self.fase))



        for o in self.obstaculos[:]:
            o.mover()
            o.desenhar()

            if o.caixa().colliderect(self.jogador.caixa()):
                return "menu"

            if o.y > 650:
                self.obstaculos.remove(o)

        if self.tempo > 20 * 60:
            if self.fase == 1:
              return "transicao_1_2"
            if self.fase == 2:
             return "transicao_2_3"
            if self.fase == 3:
             return "vitoria"

        return f"fase{self.fase}"


class Vitoria:
    def __init__(self, tela):
        self.tela = tela
        self.txt = Texto(tela, "VOCÊ VENCEU!", 60, (0, 255, 0), 120, 200)
        self.botao = Botao(tela, "Menu", 200, 350)

    def atualizar(self):
        self.tela.fill((10, 10, 10))
        self.txt.desenhar()
        self.botao.desenhar()

        if self.botao.clicou():
            return "menu"

        return "vitoria"
    
class Transicao:
    def __init__(self, tela, fase_atual, fase_destino):
        self.tela = tela
        self.fase_atual = fase_atual
        self.fase_destino = fase_destino
        self.tempo = 0
        self.txt1 = Texto(tela, f"FASE {fase_atual} CONCLUÍDA", 50, (255, 255, 255), 60, 200)
        self.txt2 = Texto(tela, "PRÓXIMA FASE…", 40, (200, 200, 200), 150, 300)

    def atualizar(self):
        self.tela.fill((0, 0, 0))
        self.txt1.desenhar()
        self.txt2.desenhar()

        self.tempo += 1

        if self.tempo > 120:  # 2 segundos em 60 FPS
            return f"fase{self.fase_destino}"

        return f"transicao_{self.fase_atual}_{self.fase_destino}"

