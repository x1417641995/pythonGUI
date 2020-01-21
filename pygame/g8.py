
#finish
#滑鼠hold改變
import sys
import pygame



def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    FPS = 1
    # 設定視窗標題
    pygame.display.set_caption('圖片點擊')
    button = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
    button_pos = (100, 100)
    button2 = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
    button2_pos = (150, 150)
    mask = pygame.mask.from_surface(button)
    mask2 = pygame.mask.from_surface(button2)
    x = 0
    y = 0
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return False
            if e.type == pygame.MOUSEBUTTONDOWN:
                try:
                    if mask.get_at((e.pos[0]-button_pos[0], e.pos[1]-button_pos[1])):
                    #if mask.get_at((e.pos[0], e.pos[1])):
                        x += 1
                        print(x)        
                    
                except IndexError:
                    print("pass")
                    pass
            if e.type == pygame.MOUSEMOTION:#移動到上方 hold
            #if e.type == pygame.MOUSEBUTTONDOWN:    
                try:
                    if mask2.get_at((e.pos[0]-button2_pos[0], e.pos[1]-button2_pos[1])):
                        button2 = pygame.image.load('/ta-ju/png/5.png').convert_alpha()
                        y += 1
                        print("x2", y)
                except IndexError:
                    button2 = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
                    print("pass2")
                    pass

        screen.fill((80,80,80))
        screen.blit(button, button_pos)
        screen.blit(button2, button2_pos)
        pygame.display.flip()
    #pygame.quit()

main()