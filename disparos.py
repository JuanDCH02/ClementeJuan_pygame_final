
from player import *
from constantes import *
from auxiliar import Auxiliar
import math
pygame.mixer.init()



class Disparar(pygame.sprite.Sprite):
    def __init__(self,path, x, y) -> None:
        super().__init__()

        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(6,5))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x += 20
        if self.rect < 0 or self.rect > 1500:
            self.kill()