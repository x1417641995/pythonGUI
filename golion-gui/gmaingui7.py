
#v2.1
#button, text label, text iuput FINISH
#MESK expect

import os
import sys
import random
import time
#import pygame as pygame
import pygame
#-*-conding:utf-8-*-
from textbox import TextBox

from button import Button


#視窗置中
os.environ["SDL_VIDEO_CENTERED"] = '1'
icon = pygame.image.load('/ta-ju/png/6.png') 
pygame.init()
pygame.display.set_icon(icon)

#設定視窗
width, height = 1000, 800                      
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Sean's game")        




RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)
font = pygame.font.SysFont("simhei", 40)

#The button can be styled in a manner similar to CSS.
BUTTON1_STYLE = {"hover_color" : BLUE,
                "clicked_color" : GREEN,
                "clicked_font_color" : BLACK,
                "hover_font_color" : ORANGE,
                #"hover_sound" : pygame.mixer.Sound("blipshort1.wav")
                }

KEY_REPEAT_SETTING = (200,70)

class Control(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((1300,600))
        #self.screen_rect = self.screen.get_rect()
        self.bnum = 0
        
        self.clock = pygame.time.Clock()
        self.done = False
        self.fps = 60.0
        self.color = GREEN
        message, message2, message3, message4, message5, message6, message7, message8 = ("Host", "SensorNode 1",
                                        "SensorNode 2","SensorNode 3",
                                        "Communication", "Alarm", "Battery", "Change password")
        #button style
        self.button = Button((0,0,150,100),RED, self.button_click,
                             text=message, **BUTTON1_STYLE)
        #button move
        #self.button.rect.center = (self.screen_rect.centerx,100)
        
        self.button2 = Button((0,100,150,100),RED, self.button_click2,
                             text=message2, **BUTTON1_STYLE)
        self.button3 = Button((0,200,150,100),RED, self.button_click3,
                             text=message3, **BUTTON1_STYLE)
        self.button4 = Button((0,300,150,100),RED, self.button_click4,
                             text=message4, **BUTTON1_STYLE)
        self.button5 = Button((0,400,150,100),RED, self.button_click5,
                             text=message5, **BUTTON1_STYLE)
        self.button6 = Button((0,500,150,100),RED, self.button_click6,
                             text=message6, **BUTTON1_STYLE)
        self.button7 = Button((0,600,100,100),RED, self.button_click,
                             text=message7, **BUTTON1_STYLE)
        self.button8= Button((0,700,100,100),RED, self.button_click,
                             text=message8, **BUTTON1_STYLE)
        #input
        
        self.b2_input = TextBox((450,270,150,25),command=self.change_color2,
                              clear_on_enter=True,inactive_on_enter=False)
        
        pygame.key.set_repeat(*KEY_REPEAT_SETTING)
        
        #mesk
        
        self.pnum, self.pnum2, self.pnum3 = 0,0,0
        
        self.photo = pygame.image.load('p1.1.png').convert_alpha()
        self.photo_pos = (550, 55)
        self.mask = pygame.mask.from_surface(self.photo)
        
        self.photo2 = pygame.image.load('p1.3.png').convert_alpha()
        self.photo2_pos = (400, 200)
        self.mask2 = pygame.mask.from_surface(self.photo2)
        
        self.photo3 = pygame.image.load('p2.1.png').convert_alpha()
        self.photo3_pos = (410, 345)
        self.mask3 = pygame.mask.from_surface(self.photo3)
        
    #left button click    
    def button_click(self):
        self.bnum = 1
        print("click")
        self.color = BLACK#WHITE
        
    def button_click2(self):
        print("click2")
        #self.color = ORANGE
        self.bnum = 2
    def button_click3(self):
        self.bnum = 3
        print("click3")
        self.color = GREEN
    def button_click4(self):
        self.bnum = 4
        print("click3")
        self.color = GREEN
    def button_click5(self):       
        self.bnum = 5
        self.color = WHITE
        print("click5")
    def button_click6(self):
        self.bnum = 6
        self.color = ORANGE
        print("click6")
        
    #text input function
    def change_color(self,id,color):
        try:
            self.color = pygame.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")
    def change_color2(self,id,color):
        try:
            self.color = pygame.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")  
    #event
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.button.check_event(event)
            
            self.button2.check_event(event)
            self.button3.check_event(event)
            self.button4.check_event(event)
            self.button5.check_event(event)
            self.button6.check_event(event)           
            #self.input.get_event(event)
            self.b2_input.get_event(event)
            
            #mesk
            x, y=0,0
            #進入第一頁才偵測
            if(self.bnum == 1):
                if event.type == pygame.MOUSEBUTTONDOWN:#click to change pages
                    #1
                    try:
                        if self.mask.get_at((event.pos[0]-self.photo_pos[0], event.pos[1]-self.photo_pos[1])):
                            self.button_click3()
                    except IndexError:
                        pass
                    #2
                    try:
                        if self.mask2.get_at((event.pos[0]-self.photo2_pos[0], event.pos[1]-self.photo2_pos[1])):                            
                            self.button_click2()                   
                    except IndexError:
                        pass
                    #3
                    try:
                        if self.mask3.get_at((event.pos[0]-self.photo3_pos[0], event.pos[1]-self.photo3_pos[1])):
                            self.button_click6()                      
                    except IndexError:
                        pass
                if event.type == pygame.MOUSEMOTION:#移動到上方 hold
                    ###1
                    try:
                        if self.mask.get_at((event.pos[0]-self.photo_pos[0], event.pos[1]-self.photo_pos[1])):
                            #self.photo2 = pygame.image.load('p1.3.png').convert_alpha()
                            self.pnum = 1
                            print(self.pnum) 
                        else:
                            self.pnum = 2
                            print(self.pnum, "out")
                            
                    except IndexError:
                        #photo2 = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
                        self.pnum = 2
                        pass
                        
                    ###2
                    try:
                        if self.mask2.get_at((event.pos[0]-self.photo2_pos[0], event.pos[1]-self.photo2_pos[1])):
                            self.pnum2 = 1
                            print(self.pnum)
                        else:
                            self.pnum2 = 2
                            print(self.pnum, "out")                           
                    except IndexError:
                        #photo2 = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
                        self.pnum2 = 2
                        print(self.pnum)
                        pass
                    ###3
                    try:
                        if self.mask3.get_at((event.pos[0]-self.photo3_pos[0], event.pos[1]-self.photo3_pos[1])):                           
                            self.pnum3 = 1
                            print(self.pnum)
                        else:
                            self.pnum3 = 2
                    except IndexError:
                        #photo2 = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
                        self.pnum3 = 2
                        print(self.pnum)
                        pass
                    
    #main interface            
    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            self.button.update(self.screen)
            
            self.button2.update(self.screen)
            self.button3.update(self.screen)
            self.button4.update(self.screen)
            self.button5.update(self.screen)
            self.button6.update(self.screen)
            #self.input.update()
            self.b2_input.update()
            #self.input.draw(self.screen)
            if(self.bnum == 1):
                
                #self.input.update()
                #self.input.draw(self.screen)
                self.screen.blit(self.photo, self.photo_pos)
                self.screen.blit(self.photo2, self.photo2_pos)
                self.screen.blit(self.photo3, self.photo3_pos)
                if(self.pnum == 1):
                    self.photo = pygame.image.load('p1.2.png').convert_alpha()
                    #print(self.pnum, "photo")
                    #self.photo2 = pygame.image.load('p1.3.png').convert_alpha()
                    #self.photo3 = pygame.image.load('p2.1.png').convert_alpha()
                if(self.pnum == 2):
                    self.photo = pygame.image.load('p1.1.png').convert_alpha()
                    #print(self.pnum, "photo")
                if(self.pnum2 == 1):
                    self.photo2 = pygame.image.load('p1.4.png').convert_alpha()
                    #print(self.pnum, "photo")
                if(self.pnum2 == 2):
                    self.photo2 = pygame.image.load('p1.3.png').convert_alpha()
                if(self.pnum3 == 1):
                    self.photo3 = pygame.image.load('p2.2.png').convert_alpha()
                    #print(self.pnum, "photo")
                if(self.pnum3 == 2):
                    self.photo3 = pygame.image.load('p2.1.png').convert_alpha()
                    #self.photo3 = pygame.image.load('p2.4.png').convert_alpha()
            elif(self.bnum == 2):
                self.screen.blit(pygame.image.load("/ta-ju/png/2.png").convert(), (150,0))
                h_text = font.render("Model Name", True, (0,0,0))
                h_text2 = font.render("Serial Number", True, (0,0,0))
                
                
                self.b2_input.draw(self.screen)
                h_text3 = font.render("Firmware( show Version / upgrade)", True, (0,0,0))
                h_text4 = font.render("Upload Interval (System Check): days & hours ", True, (0,0,0))
                h_text5 = font.render("Sleep Period ", True, (0,0,0))
                self.screen.blit(h_text, (200,240))
                self.screen.blit(h_text2, (200,270))
                self.screen.blit(h_text3, (200,300))
                self.screen.blit(h_text4, (200,330))
                self.screen.blit(h_text5, (200,360))
            elif(self.bnum == 3):
                b3_text = font.render("Type", True, (0,0,0))
                b3_text2 = font.render("Upload Thresholds Ratio: Concentration", True, (0,0,0))
                self.screen.blit(b3_text, (200,240))
                self.screen.blit(b3_text2, (200,270))
            elif(self.bnum == 4):
                b3_text = font.render("Type B", True, (0,0,0))
                b3_text2 = font.render("Upload Thresholds Ratio: Concentration", True, (0,0,0))
                self.screen.blit(b3_text, (200,240))
                self.screen.blit(b3_text2, (200,270))
            elif(self.bnum == 5):
                b5_text = font.render("Type: LoRa", True, (0,0,0))
                b5_text2 = font.render("FSB", True, (0,0,0))
                b5_text3 = font.render("Channel", True, (0,0,0))
                b5_text4 = font.render("App name", True, (0,0,0))
                b5_text5 = font.render("App Key", True, (0,0,0))
                self.screen.blit(b5_text, (200,240))
                self.screen.blit(b5_text2, (200,270))
                self.screen.blit(b5_text3, (200,300))
                self.screen.blit(b5_text4, (200,330))
                self.screen.blit(b5_text5, (200,360))
            elif(self.bnum == 6):
                b6_text = font.render("Type: ", True, (0,0,0))
                b6_text2 = font.render("NH3", True, (0,0,0))
                b6_text3 = font.render("CO2", True, (0,0,0))
                b6_text4 = font.render("Humidity", True, (0,0,0))
                self.screen.blit(b6_text, (200,240))
                self.screen.blit(b6_text2, (200,270))
                self.screen.blit(b6_text3, (200,300))
                self.screen.blit(b6_text4, (200,330))
                
                
            #image = pygame.image.load("/ta-ju/png/1.png").convert()
            #self.screen.blit(image, (150,0))
            
            #self.button7.update(self.screen)
            #self.bg.update(self.screen)
            #gameDisplay.blit(TextSurf, TextRect)
            
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()