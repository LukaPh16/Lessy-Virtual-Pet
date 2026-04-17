# Lessy Virtual Pet

A small pixel-style virtual pet game built with Pygame, where you take care of a dog named Lessy.
Feed, clean, play, and keep Lessy happy — or watch her get sad and sleepy.

---

## Features

*  Interactive pet (Lessy)
*  Feed, Sleep, Pet, Clean actions
*  Dynamic emotions (happy, sad, sleepy, idle)
*  Status messages based on pet condition
*  Save system (progress stored in JSON)
*  Stats screen (hunger, energy, happiness, cleanliness)
*  Button click animations
*  Simple UI with pixel-style design

---

## How It Works

Lessy has 4 main stats:

* Hunger
* Energy
* Happiness
* Cleanliness

These values:

* Increase when you interact with her
* Decrease over time

Your goal is to keep all stats balanced.

---

##  How to Run

### 1. Install requirements

pip install pygame

### 2. Run the game

python main.py

---

## Project Structure

project/
│
├── main.py
├── assets/
│   ├── faces/
│   │   ├── idle.png
│   │   ├── happy.png
│   │   ├── sad.png
│   │   ├── sleepy.png
│   │
│   ├── font/
│   │   └── pixel.ttf
│   │
│   └── memory.json

---

## Save System

* Game progress is saved in:

  assets/memory.json

* Stores:

  * Current page
  * Pet stats

---

## Controls

* Mouse click to interact
* Buttons:

  * Feed → increases hunger
  * Sleep → restores energy
  * Pet → increases happiness
  * Clean → improves cleanliness
  * Stats → view pet stats

---

## Future Improvements

* Visual stat bars
* Speech bubbles
* Sound effects
* Animations
* More pets or customization

---

## About

This project was made as a small interactive game to bring a virtual version of a real dog (*Lessy*) closer to someone special.

---

## Built With

* Python
* Pygame
* JSON (for saving data)

---
