import pygame 
pygame.mixer.init()

# WINDOW
ANCHO_VENTANA = 1500
ALTO_VENTANA = 800
GROUND_LEVEL = 600
FPS = 60

DIRECTION_L = 0
DIRECTION_R = 1
GROUND_COLLIDE_H = 8 # Aprox Gravedad/2 + 1
DEBUG = False

# SOUNDS
BULLET_SOUND = pygame.mixer.Sound("sonidos\shoot.mp3")
MELEE_SOUND = pygame.mixer.Sound("sonidos\melee sound.mp3")
IMPACT_SOUND = pygame.mixer.Sound("sonidos\impact_bullet.mp3")
COLLET_COIN = pygame.mixer.Sound("sonidos\moneda sonido.mp3")
BACKGROUND_MUSIC = pygame.mixer.Sound("sonidos\musica vikingos nazi.mp3")
BULLET_SOUND.set_volume(0.4)
MELEE_SOUND.set_volume(0.5)
IMPACT_SOUND.set_volume(0.5)
COLLET_COIN.set_volume(0.5)
BACKGROUND_MUSIC.set_volume(0.25)

# COLOR CONSTANTS
C_RED = (255,0,0)
C_GREEN = (0,255,0)
C_BLUE = (0,0,255)
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_PINK = (255, 0, 160)
C_PEACH = (255, 118, 95)
C_BLUE_2 = (38, 0, 160)
C_YELLOW_2 = (255, 174, 0)
C_GREEEN_2 = (38, 137, 0)
C_ORANGE = (255, 81, 0)

# MOUSE CONSTANTS
M_STATE_NORMAL = 0
M_STATE_HOVER = 1
M_STATE_CLICK = 3
M_BRIGHT_HOVER = (32,32,32)
M_BRIGHT_CLICK = (32,32,32)
