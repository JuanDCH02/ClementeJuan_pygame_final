import pygame
from constantes import *
from pygame.locals import *
from constantes import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def draw_txt(self, surface, txt, size, x, y ):
        font = pygame.font.SysFont("serif", size)
        txt_surface =  font.render(txt, True, C_PEACH)
        txt_rect = txt_surface.get_rect()
        txt_rect.midtop = (x, y)
        surface.blit(txt_surface, txt_rect)

    @staticmethod
    def valide_game_over(self, game_over, lvl):
        if game_over:
            self.surface.fill(C_BLACK)
            txt = "GAME OVER, CLICK TO RESTART"
            Auxiliar.draw_txt(self,self.surface, txt , 70, ANCHO_VENTANA // 2,ALTO_VENTANA // 2)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if lvl == 1:
                        self.__init__(name="form_game_L1",master_surface = self.master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=True)
                    if lvl == 2:
                        self.__init__(name="form_game_L2",master_surface = self.master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=True)
                    if lvl == 3:
                        self.__init__(name="form_game_L3",master_surface = self.master_surface,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=True)

    @staticmethod       
    def show_game_won(self, game_won):
        if game_won:
            self.surface.fill(C_BLACK)
            txt = "YOU WIN, CLICK TO CONTINUE"
            Auxiliar.draw_txt(self,self.surface, txt , 70, ANCHO_VENTANA // 2,ALTO_VENTANA // 2)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.set_active("form_menu_A")
                    game_won = False