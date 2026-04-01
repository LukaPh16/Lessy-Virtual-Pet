import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 500, 500

#new_width = 100
#new_height = 100

BACKGROUND = (245, 204, 232)

font_color = (255, 255, 255)
button_color_light = (236, 157, 237)
button_color_dark = (200, 128, 183)

button_width = 50
button_height = 20

font = pygame.font.Font("assets/font/pixel.ttf", 8)

text = font.render('quit', True, font_color)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Lessy Virtual Pet")


image_folder = "assets/faces"
idle_png = "idle.png"

full_path_idle = os.path.join(image_folder, idle_png)


try:
    game_icon = pygame.image.load(full_path_idle).convert_alpha()

except pygame.error as e:
    print(f"Unable to load game icon: {e}")
    game_icon = None


if game_icon:
    pygame.display.set_icon(game_icon)

try:
    image = pygame.image.load(full_path_idle).convert_alpha()

except pygame.error as message:
    print(f"Cannot load image: idle.png - {message}")
    sys.exit()

#scaled_image = pygame.transform.scale(image, (new_width, new_height))

#scaled_rect = scaled_image.get_rect(center = (WIDTH // 2, HEIGHT // 2))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2-40 <= mouse[0] <= WIDTH/2+40 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                pygame.quit()

    mouse = pygame.mouse.get_pos()

    screen.fill(BACKGROUND)

    if WIDTH/2-40 <= mouse[0] <= WIDTH/2+40 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
        pygame.draw.rect(screen, button_color_light, [WIDTH/2-40, HEIGHT/2, button_width, button_height])

    else:
        pygame.draw.rect(screen, button_color_dark, [WIDTH/2-40, HEIGHT/2, button_width, button_height])


    screen.blit(text, (WIDTH/2-30, HEIGHT/2+5))



    #if image:
        #screen.blit(scaled_image, scaled_rect)

    
    pygame.display.update()

pygame.quit()