import thorpy, pygame

application = thorpy.Application((500,500), "Launching alerts")

#normal, pressed, hover = "normal.png", "pressed.png", "hover.png"
normal, pressed, hover = "normal.png", "pressed.png", "/ta-ju/png/4.png"

button1 = thorpy.make_image_button(normal, pressed, hover,
                                    alpha=255, #opaque
                                    colorkey=(255,255,255)) #white=transparent
#mask = pygame.mask.from_surface(button1)

#this time a very simple button, with a text (only 1 image)
button2 = thorpy.make_image_button(normal, colorkey=False, text="Hello")


background = thorpy.Background(image=thorpy.style.EXAMPLE_IMG,
                                    elements=[button1, button2])
thorpy.store(background)

menu = thorpy.Menu(background)
menu.play()

application.quit()