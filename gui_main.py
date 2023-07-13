import pygame, time
from pygame.locals import *
import sys
from constantes import *
from gui.gui_form import Form
from gui.gui_form_menu_A import FormMenuA
from gui.gui_form_menu_B import FormMenuB
from gui.gui_form_menu_C import FormMenuC
from gui.gui_form_menu_game_l1 import FormGameLevel1
from gui.gui_form_menu_game_l2 import FormGameLevel2
from gui.gui_form_menu_game_l3 import FormGameLevel3

pygame.mixer.init()
BACKGROUND_MUSIC.play(-1)

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.display.set_caption("Vaquero vs Trollz")
pygame.init()
clock = pygame.time.Clock()

#coins_group = 
form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=800,h=400,color_background=(C_BLACK),color_border=(C_WHITE),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if(aux_form_active != None):
        aux_form_active.update(lista_eventos,keys,delta_ms)
        aux_form_active.draw()
        
    pygame.display.flip()
