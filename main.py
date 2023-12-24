import os
from tkinter import *
from time import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def star_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count >0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "tomato.png")

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas = Canvas(window, width=200, height=224, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)

# Title
title_label = Label(text=" Timer", fg= GREEN, bg= YELLOW, font=(FONT_NAME, 50))
title_label.grid(column =1, row=0)

# Tomate
canvas.create_image(100, 112, image=tomato_img)

# Clock
time_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row=1)

#button
start_button = Button(text="START", highlightthickness=0, command=star_timer)
start_button.grid(column =0, row=2)
reset_button = Button(text="RESET", highlightthickness=0)
reset_button.grid(column =2, row=2)

#Check_marks
check_marks = Label(text="V", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()