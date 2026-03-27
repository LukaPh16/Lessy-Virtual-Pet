import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND = (160, 0, 255)

new_width = 100
new_height = 100

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
    print(f"Cannot load image: face.png - {message}")
    sys.exit()

scaled_image = pygame.transform.scale(image, (new_width, new_height))

scaled_rect = scaled_image.get_rect(center = (WIDTH // 2, HEIGHT // 2))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(BACKGROUND)

        pygame.display.flip()

    if image:
        screen.blit(scaled_image, scaled_rect)
    
    pygame.display.flip()

pygame.quit()