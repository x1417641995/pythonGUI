import os
import sys
import random
#import pygame as pygame
import pygame

from button import Button


#視窗置中
os.environ["SDL_VIDEO_CENTERED"] = '1'
icon = pygame.image.load('/ta-ju/png/6.png') 
pygame.init()
pygame.display.set_icon(icon)

#screen = pygame.display.set_mode((640, 480))
#bg = pygame.Surface(screen.get_size())
#bg = bg.convert()
# load and convert image


#設定視窗
width, height = 1000, 800                      
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Sean's game")        

#建立畫布bg
bg = pygame.Surface(screen.get_size()).convert()

bg.fill((255,255,255))           #白色


image = pygame.image.load("/ta-ju/png/1.png").convert()
bg.blit(image, (20,10))




RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)


#The button can be styled in a manner similar to CSS.
BUTTON1_STYLE = {"hover_color" : BLUE,
                "clicked_color" : GREEN,
                "clicked_font_color" : BLACK,
                "hover_font_color" : ORANGE,
                #"hover_sound" : pygame.mixer.Sound("blipshort1.wav")
                }


class Control(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((1300,600))
        #self.screen_rect = self.screen.get_rect()
        
        self.bg = pygame.Surface(self.screen.get_size()).convert()
        self.bg.fill((255,255,255))
        
        
        self.clock = pygame.time.Clock()
        self.done = False
        self.fps = 60.0
        self.color = GREEN
        message, message2, message3, message4, message5, message6, message7, message8 = ("Host", "SensorNode 1",
                                        "SensorNode 2","SensorNode 3",
                                        "Communication", "Alarm", "Battery", "Change password")
        #button style
        self.button = Button((0,0,150,100),RED, self.change_color,
                             text=message, **BUTTON1_STYLE)
        #button move
        #self.button.rect.center = (self.screen_rect.centerx,100)
        
        self.button2 = Button((0,100,150,100),RED, self.change_color2,
                             text=message2, **BUTTON1_STYLE)
        self.button3 = Button((0,200,150,100),RED, self.change_color3,
                             text=message3, **BUTTON1_STYLE)
        self.button4 = Button((0,300,150,100),RED, self.change_color,
                             text=message4, **BUTTON1_STYLE)
        self.button5 = Button((0,400,150,100),RED, self.change_color,
                             text=message5, **BUTTON1_STYLE)
        self.button6 = Button((0,500,150,100),RED, self.change_color,
                             text=message6, **BUTTON1_STYLE)
        self.button7 = Button((0,600,100,100),RED, self.change_color,
                             text=message7, **BUTTON1_STYLE)
        self.button8= Button((0,700,100,100),RED, self.change_color,
                             text=message8, **BUTTON1_STYLE)
        
        
        
    def change_color(self):
        #self.color = [random.randint(0,255) for _ in range(3)]
        print("click")
        self.color = BLACK#WHITE
        
        
        
        print("click5")
        
    def change_color2(self):
        #self.color = [random.randint(0,255) for _ in range(3)]
        print("click2")
        self.color = ORANGE
    def change_color3(self):
        #self.color = [random.randint(0,255) for _ in range(3)]
        print("click3")
        self.color = GREEN
        

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.button.check_event(event)
            
            self.button2.check_event(event)
            self.button3.check_event(event)
            

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
            image = pygame.image.load("/ta-ju/png/1.png").convert()
            self.bg.blit(image, (20,10))
            pygame.display.update()
            #self.button7.update(self.screen)
            #self.bg.update(self.screen)
            
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()