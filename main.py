import pygame
import sys
import os
import time
import json

pygame.init()

font_path = "assets/font/pixel.ttf"
idle = pygame.image.load("assets/faces/idle.png")

new_size = (200, 200)
idle_face = pygame.transform.scale(idle, new_size)

WIDTH, HEIGHT = 500, 500

BACKGROUND = (245, 204, 232)
test_color = (255, 0, 0)
white = (255, 255, 255)

color1 = (245, 204, 232)
color2 = (236, 157, 237)
color3 = (200, 128, 183)
color4 = (159, 107, 160)
color5 = (74, 32, 64)

page0 = "Hello Tamar! This is a game I made for you!"
page1 = "In this game I brought someone closer to you!"
page2 = "Can you guess who it is?"
page3 = "It is your dog! Lessy!"
page4 = ""
page5 = ""

pages_text = [
    page0,
    page1,
    page2,
    page3,
    page4,
    page5
]

visible_length = 0
typing_speed = 0.05
last_update = 0

text_font = pygame.font.Font(font_path, 16)
button_font = pygame.font.Font(font_path, 8)

back_text = button_font.render("Back", True, white)
back_text_x = 39
back_text_y = 40

button_back_width = 50
button_back_height = 30
button_back_x = 30
button_back_y = 30

continue_text = button_font.render("Continue", True, white)
continue_text_x = WIDTH/2-31
continue_text_y = HEIGHT/2+160

button_continue_width = 80
button_continue_height = 30
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

def save_progress(page):
    data = {
        "page": page
    }

    with open("assets/memory.json", "w") as f:
        json.dump(data, f)

def load_progress():
    try:
        with open("assets/memory.json", "r") as f:
            data = json.load(f)
            return data.get("page", 0)
    except:
        return 0
    
current_page = load_progress()

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

def button_back():
    if button_back_x <= mouse[0] <= button_back_x+80 and button_back_x <= mouse[1] <= button_back_y+30:
        pygame.draw.rect(screen, color2, [button_back_x,button_back_y, button_back_width, button_back_height], border_radius = 4)
    else:
        pygame.draw.rect(screen, color3, [button_back_x, button_back_y, button_back_width, button_back_height], border_radius = 4)
    
    screen.blit(back_text, (back_text_x, back_text_y))
def button_continue():
    if button_continue_x <= mouse[0] <= button_continue_x+80 and button_continue_y <= mouse[1] <= button_continue_y+30:
        pygame.draw.rect(screen, color2, [button_continue_x, button_continue_y, button_continue_width, button_continue_height], border_radius=4)
    else:
        pygame.draw.rect(screen, color3, [button_continue_x, button_continue_y, button_continue_width, button_continue_height], border_radius=4)

    screen.blit(continue_text, (continue_text_x, continue_text_y))

def initial_pages(page_text):
    global visible_length, typing_speed, last_update
    current_time = pygame.time.get_ticks() / 1000

    if visible_length < len(page_text):
        if current_time - last_update > typing_speed:
            visible_length += 1
            last_update = current_time

    display_text = page_text[:visible_length]

    screen.fill(BACKGROUND)

    box = pygame.Rect(50, 200, 400, 60)
    pygame.draw.rect(screen, color2, box, border_radius=4)

    inner_box = box.inflate(-20, -20)

    draw_text_box(screen, display_text, text_font, color5, inner_box)

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

                        save_progress(current_page)

            elif button_back_x <= mouse[0] <= button_back_x+80 and button_back_x <= mouse[1] <= button_back_y+30:
                current_page -= 1
                visible_length = 0
                last_update = 0

                save_progress(current_page)
                    

    if 0 <= current_page <= 3:
        initial_pages(pages_text[current_page])
        if current_page > 0:
            button_back()

    if current_page == 4:
        screen.fill(BACKGROUND)

        screen.blit(idle_face, (WIDTH/4+28, HEIGHT/4))

        button_continue()
        button_back()

    if current_page == 5:
        screen.fill(test_color)



    pygame.display.update()
    clock.tick(60)

pygame.quit()