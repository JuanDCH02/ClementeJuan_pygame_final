import pygame, random, time
from pygame.locals import *
from constantes import *
from gui.gui_form import Form
from gui.gui_button import Button
from gui.gui_textbox import TextBox
from gui.gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy, Enemy_Boss
from plataforma import Plataform
from background import Background
from bullet import Bullet
from coins import Coin
from auxiliar import Auxiliar
pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.game_over =  False
        self.game_won = False
        self.time_between_shoots = 1000
        self.time_between_shoots_enemy = 2500
        self.last_shoot = pygame.time.get_ticks()

        # --- GUI WIDGET --- 
        self.current_time = 0
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        
       
        self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/set_bg_01/forest/all.png")

         # --- ENEMIES ---
        self.enemies_sprites = pygame.sprite.Group()
        self.enemies_sprites.add(Enemy_Boss(x=550,y=400,speed_walk=7,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300))
        self.enemies_sprites.add(Enemy_Boss(x=1200,y=200,speed_walk=7,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300))

        # --- PLAYER ---
        self.player_sprite = pygame.sprite.Group()
        self.player_1 = Player(x=10,y=400,speed_walk=13,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300,)
        self.player_sprite.add(self.player_1)

        # --- CREATE PALTFORMS ---
        self.plataform_list = []
        
        self.plataform_list.append(Plataform(x=150,y=360,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=200,y=360,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=350,y=290,width=50,height=50,type=14))
        self.plataform_list.append(Plataform(x=300,y=290,width=50,height=50,type=12))

        self.plataform_list.append(Plataform(x=250,y=500,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=300,y=500,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=350,y=500,width=50,height=50,type=13))   
        self.plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=520,y=350,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=570,y=350,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=620,y=350,width=50,height=50,type=13))   
        self.plataform_list.append(Plataform(x=670,y=350,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=750,y=270,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=800,y=270,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=850,y=270,width=50,height=50,type=13))   
        self.plataform_list.append(Plataform(x=900,y=270,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=1050,y=350,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=1100,y=350,width=50,height=50,type=14))


        

        self.bullet_list = []

        # --- CEATE COINS ---
        self.coins_sprites = pygame.sprite.Group()
        self.coins_sprites.add(Coin("images\caracters\players\cowgirl\heart.png", 430, 420, 150))
        self.coins_sprites.add(Coin("images\caracters\players\cowgirl\heart.png",620, 200, 350))
        self.coins_sprites.add(Coin("images\caracters\players\cowgirl\heart.png",750, 300, 250))
        self.coins_sprites.add(Coin("images\caracters\players\cowgirl\heart.png",1090, 300, 400))
        self.coins_sprites.add(Coin("images\caracters\players\cowgirl\heart.png",230, 200, 400))


    #--- METHODS ---
    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def shoot_enemy(self):
        ahora = pygame.time.get_ticks()
        for enemy_element in self.enemies_sprites:   
            if ahora - self.last_shoot > self.time_between_shoots_enemy:
                self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,10,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment01.png",frame_rate_ms=100,move_rate_ms=20,width=6,height=5))
                BULLET_SOUND.play()
                self.last_shoot = ahora 

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))

    def enemy_collide(self):
        collision = pygame.sprite.spritecollide(self.player_1,self.enemies_sprites,False)
        ahora = pygame.time.get_ticks()
        if collision:
            if ahora - self.last_shoot > self.time_between_shoots:
                self.player_1.receive_shoot()

    def coin_collide(self):
        for aux_coin in self.coins_sprites:
            collision = pygame.sprite.spritecollide(self.player_1, self.coins_sprites, True)
            if collision:
                self.player_1.score += aux_coin.valor
                COLLET_COIN.play()
                if self.player_1.lives < 5:
                    self.player_1.lives += 1
                    
    def shoot_player(self, keys):
        if keys[pygame.K_e]:
            ahora = pygame.time.get_ticks() 
            for enemy_element in self.enemies_sprites:
                if ahora - self.last_shoot > self.time_between_shoots:
                    self.bullet_list.append(Bullet(self.player_1,self.player_1.rect.centerx,self.player_1.rect.centery,enemy_element.rect.centerx,enemy_element.rect.centery,15,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment01.png",frame_rate_ms=100,move_rate_ms=20))
                    self.last_shoot = ahora



    # --- LOOP --- 
    def update(self, lista_eventos,keys,delta_ms):
        if self.player_1.lives == 0:
            self.game_over = True
        if len(self.coins_sprites) == 0 and len(self.enemies_sprites) == 0:
            self.game_won = True
            # self.set_active("form_menu_A")
            Auxiliar.show_game_won(self, self.game_won)

        Auxiliar.valide_game_over(self, self.game_over, 3)
    
            
        self.shoot_player(keys)
        #self.enemy_collide()
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemies_sprites,self.player_1)

        for enemy_element in self.enemies_sprites:
            if enemy_element.lives <= 0:
                enemy_element.kill()
            enemy_element.update(delta_ms,self.plataform_list)

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list)
        #self.shoot_enemy()

        self.pb_lives.value = self.player_1.lives 
        self.coins_sprites.update()
        self.coin_collide()

        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        Auxiliar.draw_txt(self, self.surface, str(self.player_1.score), 35, ANCHO_VENTANA-100, ALTO_VENTANA-50)
        Auxiliar.draw_txt(self, self.surface, "SCORE:", 35, ANCHO_VENTANA-210, ALTO_VENTANA-50)

        for aux_widget in self.widget_list:    
            aux_widget.draw()
    
        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemies_sprites:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)

        for aux_coin in self.coins_sprites:
            aux_coin.draw(self.surface)