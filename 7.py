
import sys
import pygame



def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    button = pygame.image.load('/ta-ju/png/4.png').convert_alpha()
    button_pos = (100, 100)
    mask = pygame.mask.from_surface(button)
    x = 0
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
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

        screen.fill((80,80,80))
        screen.blit(button, button_pos)
        pygame.display.flip()
    pygame.quit()

main()