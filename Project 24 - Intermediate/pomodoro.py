from tkinter import *
import math
import pygame
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- SOUND SYSTEM ----------------------------#
pygame.mixer.init()
def play():
    file = resource_path("alarm.mp3")
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.01)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    global reps
    reps = 0
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        play()
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)
        window.config(padx=110)
    elif reps % 2 == 0:
        play()
        count_down(break_sec)
        timer_label.config(text="Break", fg=PINK)
        window.config(padx=110)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        window.config(padx=113)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.resizable(False, False)
window.config(padx=110, pady=20)
window.config(bg=YELLOW)

# Define the size and starting place of the window
window_height = 400
window_width = 500

screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Design the pomodoro logo
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill=GREEN, font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Create the labels and buttons
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", font=("arial", 10, "normal"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=("arial", 10, "normal"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=GREEN, font=(FONT_NAME, 15, "normal"))
check_label.grid(row=3, column=1)

window.mainloop()
