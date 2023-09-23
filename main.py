import pyautogui
import math
import random
import threading
import time
import keyboard
from tkinter import *

# Function to move mouse in a figure-8
def move_mouse():
    while running:
        for t in range(0, 628, 5):  # Goes from 0 to 2π in steps of 5
            if not running or random.uniform(0, 100) > movement_uptime:
                time.sleep(0.5)  # Don't move for 0.5 seconds
                continue

            x = 10 * math.sin(t / 100)
            y = 5 * math.cos(2 * t / 100)
            pyautogui.moveRel(x, y, duration=0.01)
            time.sleep(0.05)  # Tiny sleep to allow time for interruption

# Function to handle clicks
def handle_clicks():
    while running:
        time_to_next_click = random.uniform(5, 15)
        time.sleep(time_to_next_click)

        if running:
            hold_duration = random.uniform(2, 3)
            pyautogui.mouseDown()
            time.sleep(hold_duration)
            pyautogui.mouseUp()

# Function to start moving mouse and clicking
def start_move():
    global running
    running = True
    move_thread = threading.Thread(target=move_mouse)
    click_thread = threading.Thread(target=handle_clicks)
    move_thread.start()
    click_thread.start()

# Function to stop moving mouse and clicking
def stop_move():
    global running
    running = False

# Function to set movement uptime
def set_movement_uptime(val):
    global movement_uptime
    movement_uptime = float(val)

# Initialize variables
running = False
movement_uptime = 50.0

# Create Tkinter window
root = Tk()
root.title("Soothing Coding Music Player")

# Create and place buttons and slider
start_button = Button(root, text="Play", command=start_move)
start_button.pack(side=LEFT)
stop_button = Button(root, text="Pause", command=stop_move)
stop_button.pack(side=RIGHT)

movement_uptime_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Track #", command=set_movement_uptime)
movement_uptime_slider.set(50)
movement_uptime_slider.pack()

# Add hotkeys
keyboard.add_hotkey('F2', start_move)
keyboard.add_hotkey('F4', stop_move)

# Start Tkinter main loop
root.mainloop()
