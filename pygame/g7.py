import pygame
import os
 
pygame.init()
screen = pygame.display.set_mode((600, 400))
done = False
clock = pygame.time.Clock()
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
buttonText = pygame.font.SysFont('Comic Sans MS', 20)
 
class Button:
    def __init__ (self, colour, x, y, width, height, label):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
 
    def getColour(self):
        return(self.colour)
 
    def getX(self):
        return(self.x)
 
    def getY(self):
        return(self.y)
 
    def getWidth(self):
        return(self.getWidth)
 
    def getHeight(self):
        return(self.getHeight)
 
    def getLabel(self):
        return(self.getHeight)
 
teacher = Button([255, 0, 0], 450, 100, 100, 50, "Teacher")
student = Button([255, 0, 0], 450, 200, 100, 50, "Student")
 
def initialiseText(buttonText, i):
    text = i.getLabel()
    textSurface = buttonText.render(text)
 
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)  
 
    #teacher = pygame.draw.rect(screen, teacher.getColour, [teacher.getX, teacher.getY, teacher.getWidth, teacher.getHeight])
    teacher = pygame.draw.rect(screen, RED, [200, 200, 100, 100]) 
    initialiseText(buttonText, teacher)
    screen.blit(textSurface, teacher.center)
     
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if button.collidepoint(mouse):
            print("hi")