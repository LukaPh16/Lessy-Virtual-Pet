import pygame
import sys
import os
import time

pygame.init()

font_path = "assets/font/pixel.ttf"

WIDTH, HEIGHT = 500, 500

BACKGROUND = (245, 204, 232)
test_color = (255, 0, 0)
white = (255, 255, 255)

font_dark_color = (74, 32, 64)
button_color_light = (236, 157, 237)
button_color_dark = (200, 128, 183)

button_width = 80
button_height = 30

current_page = 0

page1_text = "Hello Tamar! This is a game I made for you!"
page2_text = "In this game I brought someone closer to you!"
page3_text = "Can you guess who it is?"
page4_text = "It is your dog! Lessy!"

pages_text = [
    page1_text,
    page2_text,
    page3_text,
    page4_text
]

visible_length = 0
typing_speed = 0.05
last_update = 0

text_font = pygame.font.Font(font_path, 16)
button_font = pygame.font.Font(font_path, 8)

continue_text = button_font.render("Continue", True, white)
continue_text_x = WIDTH/2-31
continue_text_y = HEIGHT/2+160

button_continue_x = WIDTH/2-40
button_continue_y = HEIGHT/2 + 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Lessy Virtual Pet")

image_folder = "assets/faces"
idle_png = "idle.png"
full_path_idle = os.path.join(image_folder, idle_png)

running = True

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

def button_continue():
    if button_continue_x <= mouse[0] <= button_continue_x+80 and button_continue_y <= mouse[1] <= button_continue_y+30:
        pygame.draw.rect(screen, button_color_light, [button_continue_x, button_continue_y, button_width, button_height], border_radius=4)
    else:
        pygame.draw.rect(screen, button_color_dark, [button_continue_x, button_continue_y, button_width, button_height], border_radius=4)

    screen.blit(continue_text, (continue_text_x, continue_text_y))

def pages(page_text):
    global visible_length, typing_speed, last_update
    current_time = pygame.time.get_ticks() / 1000

    if visible_length < len(page_text):
        if current_time - last_update > typing_speed:
            visible_length += 1
            last_update = current_time

    display_text = page_text[:visible_length]

    screen.fill(BACKGROUND)

    box = pygame.Rect(50, 200, 400, 60)
    pygame.draw.rect(screen, white, box, border_radius=4)

    inner_box = box.inflate(-20, -20)

    draw_text_box(screen, display_text, text_font, font_dark_color, inner_box)

    if visible_length == len(page_text):
        button_continue()

while running:
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if visible_length == len(pages_text[current_page]):
                if button_continue_x <= mouse[0] <= button_continue_x+80 and button_continue_y <= mouse[1] <= button_continue_y+30:
                    if current_page < len(pages_text) - 1:
                        current_page += 1
                        visible_length = 0
                        last_update = 0

    pages(pages_text[current_page])

    pygame.display.update()
    clock.tick(60)

pygame.quit()