import pygame
import sys
import os

pygame.init()

font_path = "assets/font/pixel.ttf"

WIDTH, HEIGHT = 500, 500

BACKGROUND = (245, 204, 232)
test_color = (255, 255, 255)
white_color = (255, 255, 255)

font_dark_color = (74, 32, 64)
button_color_light = (236, 157, 237)
button_color_dark = (200, 128, 183)

button_width = 80
button_height = 30

current_page = "menu"

intro_text = "Hello Tamar! This is a game I made for you!"

visible_length = 0
typing_speed = 0.02
last_update = 0

text_font = pygame.font.Font(font_path, 16)
button_font = pygame.font.Font(font_path, 8)

button_continue = button_font.render("Continue", True, white_color)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Lessy Virtual Pet")

image_folder = "assets/faces"
idle_png = "idle.png"
full_path_idle = os.path.join(image_folder, idle_png)

try:
    game_icon = pygame.image.load(full_path_idle).convert_alpha()
    pygame.display.set_icon(game_icon)
except pygame.error:
    pass


def draw_text_box(surface, text, font, color, rect):
    words = text.split(' ')
    lines = []
    current = ""

    for word in words:
        test = current + word + " "
        if font.size(test)[0] < rect.width:
            current = test
        else:
            lines.append(current)
            current = word + " "
    lines.append(current)

    y = rect.y
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (rect.x, y))
        y += font.get_height()


running = True

while running:
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2-40 <= mouse[0] <= WIDTH/2+40 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+30:
                current_page = "continue"

    if current_page == "menu":
        current_time = pygame.time.get_ticks() / 1000

        if visible_length < len(intro_text):
            if current_time - last_update > typing_speed:
                visible_length += 1
                last_update = current_time

        display_text = intro_text[:visible_length]

        screen.fill(BACKGROUND)

        box = pygame.Rect(50, 50, 400, 120)
        pygame.draw.rect(screen, white_color, box, border_radius=8)

        inner_box = box.inflate(-20, -20)

        draw_text_box(screen, display_text, text_font, font_dark_color, inner_box)

        if WIDTH/2-40 <= mouse[0] <= WIDTH/2+40 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+30:
            pygame.draw.rect(screen, button_color_light, [WIDTH/2-40, HEIGHT/2, button_width, button_height])
        else:
            pygame.draw.rect(screen, button_color_dark, [WIDTH/2-40, HEIGHT/2, button_width, button_height])

        screen.blit(button_continue, (WIDTH/2-30, HEIGHT/2+8))

    elif current_page == "continue":
        screen.fill(test_color)

    pygame.display.update()
    clock.tick(60)

pygame.quit()