import pygame
from player import Player
from auxiliar import Auxiliar
from constantes import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, path, x, y, valor, width = 30, height = 30 ):
        super().__init__()

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.frame = 0
        self.rect.x = x
        self.rect.y = y
        self.valor = valor

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen,color=(C_WHITE),rect=self.rect)
        screen.blit(self.image,self.rect)