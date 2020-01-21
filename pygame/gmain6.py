

import pygame as pg
import pygame
#pygame初始化
pg.init()

#設定視窗
width, height = 1000, 800                      
screen = pg.display.set_mode((width, height)) 
pg.display.set_caption("Sean's game")        

#建立畫布bg
bg = pg.Surface(screen.get_size()).convert()

bg.fill((255,255,255))           #白色


image = pygame.image.load("/ta-ju/png/1.png").convert()
bg.blit(image, (20,10))

#改字體、大小
#字體變數 = pygame.font.SysFont(字體名稱, 字體尺寸)
#繪製
#文字變數 = 字體變數.render(文字, 平滑值, 文字顏色, 背景顏色)
font = pg.font.SysFont("simhei", 40)
text = font.render("Hello", True, (0,0,255), (255,255,255))
text2 = font.render("djfkjkj", True, (0,0,0))
bg.blit(text, (320,240))
bg.blit(text2, (320,300))


#顯示
screen.blit(bg, (0,0))
pg.display.update()

#關閉程式的程式碼
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit() 