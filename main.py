import pygame
import sys
import os
import time
import json

pygame.init()

font_path = "assets/font/pixel.ttf"
idle = pygame.image.load("assets/faces/idle.png")
happy = pygame.image.load("assets/faces/happy.png")
sad = pygame.image.load("assets/faces/sad.png")
sleepy = pygame.image.load("assets/faces/sleepy.png")

current_face = ""

new_size = (200, 200)
idle_face = pygame.transform.scale(idle, new_size)
happy_face = pygame.transform.scale(happy, new_size)
sad_face = pygame.transform.scale(sad, new_size)
sleepy_face = pygame.transform.scale(sleepy, new_size)

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
page6 = ""

pages_text = [
    page0,
    page1,
    page2,
    page3,
    page4,
    page5
]

visible_length = 0
typing_speed = 0.02
last_update = 0

text_font = pygame.font.Font(font_path, 16)
button_font = pygame.font.Font(font_path, 8)

button_width = 100
button_height = 30

feed_text = text_font.render("Feed", True, white)
feed_button_x = 85
feed_button_y = 395

sleep_text = text_font.render("Sleep", True, white)
sleep_button_x = 85
sleep_button_y = 440

pet_text = text_font.render("Pet", True, white)
pet_button_x = 315
pet_button_y = 395

clean_text = text_font.render("Clean", True, white)
clean_button_x = 315
clean_button_y = 440

stats_text = text_font.render("Stats", True, white)
stats_button_x = 200
stats_button_y = 30

box_x = 30
box_y = 75
box_width = 440
box_height = 305

back_text = button_font.render("Back", True, white)
back_button_width = 50
back_button_height = 30
back_button_x = 30
back_button_y = 30

continue_text = button_font.render("Continue", True, white)

continue_button_width = 83
continue_button_height = 30
continue_button_x = WIDTH/2-43
continue_button_y = HEIGHT/2 + 150

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

def save_progress(page, pet):
    data = {
        "page": page,
        "pet": pet
    }

    with open("assets/memory.json", "w") as f:
        json.dump(data, f, indent=4)

def load_progress():
    default_pet = {
        "hunger": 50,
        "energy": 50,
        "happiness": 50,
        "cleanliness": 50
    }

    try:
        with open("assets/memory.json", "r") as f:
            data = json.load(f)
            page = data.get("page", 0)
            
        if page == 5:
            page = 4

        return page, data.get("pet", default_pet)
    except:
        return 0, default_pet
    
current_page, pet = load_progress()

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

def button(x, y, width, height, text_surface):
    if x <= mouse[0] <= x+width and y <= mouse[1] <= y+height:
        color = color2
    else:
        color = color3
    pygame.draw.rect(screen, color, [x, y, width, height], border_radius = 2)
    screen.blit(text_surface, (x+10, y+8))

def initial_pages(page_text):
    global current_page, visible_length, typing_speed, last_update
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
        button(continue_button_x, continue_button_y, continue_button_width, continue_button_height, continue_text)

while running:
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()

    if pygame.time.get_ticks() % 3000 < 20:
        save_progress(current_page, pet)

    if pet["hunger"] < 30:
        current_face = sad_face
    elif pet["energy"] < 30:
        current_face = sleepy_face
    elif pet["happiness"] > 80:
        current_face = happy_face
    else:
        current_face = idle_face

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if visible_length == len(pages_text[current_page]):
                if continue_button_x <= mouse[0] <= continue_button_x+80 and continue_button_y <= mouse[1] <= continue_button_y+30:
                    if current_page < len(pages_text) - 1:
                        current_page += 1
                        visible_length = 0
                        last_update = 0

                        save_progress(current_page, pet)
            if back_button_x <= mouse[0] <= back_button_x+80 and back_button_y <= mouse[1] <= back_button_y+30:
                if current_page > 0:
                    current_page -= 1
                    visible_length = 0
                    last_update = 0

                save_progress(current_page, pet)

        if current_page == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:

                if feed_button_x <= mouse[0] <= feed_button_x+button_width and feed_button_y <= mouse[1] <= feed_button_y+button_height:
                    pet["hunger"] += 10

                if sleep_button_x <= mouse[0] <= sleep_button_x+button_width and sleep_button_y <= mouse[1] <= sleep_button_y+button_height:
                    pet["energy"] += 10

                if pet_button_x <= mouse[0] <= pet_button_x+button_width and pet_button_y <= mouse[1] <= pet_button_y+button_height:
                    pet["happiness"] += 10

                if clean_button_x <= mouse[0] <= clean_button_x+button_width and clean_button_y <= mouse[1] <= clean_button_y+button_height:
                    pet["cleanliness"] += 10

                if stats_button_x <= mouse[0] <= stats_button_x+button_width and stats_button_y <= mouse[1] <= stats_button_y+button_height:
                    current_page = 5

            for key in pet:
                pet[key] = max(0, min(100, pet[key]))
                    

    if 0 <= current_page <= 3:
        initial_pages(pages_text[current_page])
        if current_page > 0:
            button(back_button_x, back_button_y, back_button_width, back_button_height, back_text)

    elif current_page == 4:
        screen.fill(BACKGROUND)

        pygame.draw.rect(screen, color3, (box_x, box_y, box_width, box_height), 4, border_radius = 2)

        screen.blit(current_face, (WIDTH/2 - 98, HEIGHT/4))
        button(feed_button_x, feed_button_y, button_width, button_height, feed_text)
        button(sleep_button_x, sleep_button_y, button_width, button_height, sleep_text)
        button(pet_button_x, pet_button_y, button_width, button_height, pet_text)
        button(clean_button_x, clean_button_y, button_width, button_height, clean_text)
        button(stats_button_x, stats_button_y, button_width, button_height, stats_text)

    elif current_page == 5:
        screen.fill(BACKGROUND)

        pygame.draw.rect(screen, color3, (box_x, box_y, box_width, box_height), 4, border_radius = 2)
        y = 170
        for key, value in pet.items():
            text = text_font.render(f"{key}: {value}", True, color5)
            screen.blit(text, (140, y))
            y += 30

        button(back_button_x, back_button_y, back_button_width, back_button_height, back_text)

    if pygame.time.get_ticks() % 2000 < 20:
        if pet["hunger"] > 0:
            pet["hunger"] -= 1
        if pet["energy"] > 0:
            pet["energy"] -= 1
        if pet["cleanliness"] > 0:
            pet["cleanliness"] -= 1
            

    pygame.display.update()
    clock.tick(60)

pygame.quit()