import pygame
import os
 
from pygame.sprite import Sprite
 
class MouseImage(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((50, 50), flags=pygame.SRCALPHA)
        self.fill_image()
        self.rect = self.image.get_rect()
 
    def fill_image(self):
        color = pygame.Color("gray90")
        color.a = 35
        self.image.fill(color)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
class Example:
    def __init__(self):
        # Center surface on screen. Must be done before creating main surface
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # Basic pygame setup
        pygame.display.set_caption("Mouse Hold Image")
        self.surface = pygame.display.set_mode((800, 600))
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.running = False
        self.delta = 0
        self.fps = 60
 
        self.mouse_image = MouseImage()
        self.mouse_image_show = False
 
    def mainloop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEMOTION:
                    if self.mouse_image_show is True:
                        self.mouse_image.rect.center = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left mouse button
                        self.mouse_image_show = True
                        self.mouse_image.rect.center = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.mouse_image_show = False
 
            self.surface.fill(pygame.Color("black"))
            if self.mouse_image_show:
                self.mouse_image.draw(self.surface)
 
            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)
 
if __name__ == "__main__":
    pygame.init()
    example = Example()
    example.mainloop()