import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LGreen = "#8bc240"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


pomodoro = Tk()
pomodoro.title("Pomodoro by Ian \'Einstein\' Cultura")
pomodoro.config(width=300, height=300, bg=YELLOW)


def start_na():
    global reps
    reps += 1
    if reps % 8 == 0:
        say(3600)
        einstein.itemconfig(status, text = "Long Break")

    if reps % 2 == 0:
        say(300)
        einstein.itemconfig(status, text = "Short Break")

    else:
        say(1500)
        einstein.itemconfig(status, text = "Working Time")


def say(count):
    global timer
    mins = math.floor(count/60)
    secs = count%60
    if secs <= 9:
        secs = f"0{secs}"
    if mins <= 9:
        mins = f"0{mins}"

    einstein.itemconfig(gui_time, text=f"{mins}:{secs}")

    if count > 0:
        timer = pomodoro.after(1000, say, count - 1)

    else:
        start_na()




def reset_na():
    pomodoro.after_cancel(timer)
    einstein.itemconfig(gui_time, text="00:00")
    einstein.itemconfig(status, text="Timer")



einstein = Canvas(width=320, height=350, bg = YELLOW, highlightthickness=0)
image = PhotoImage(file= "tomato.png")
einstein.create_image(120, 140, image= image)
gui_time = einstein.create_text(130, 160, text="00:00", font=(FONT_NAME, 29, "bold"))
status = einstein.create_text(130, 10, text="Timer",fill = GREEN, font=(FONT_NAME, 29, "bold"))
start_button = Button(text = "start", highlightthickness=0,command = start_na)
start_button.place(x = 20, y = 250)
reset_button = Button(text = "reset", highlightthickness=0, command = reset_na)
reset_button.place(x = 215, y = 250)
einstein.create_text(120, 270, text="✓",fill = GREEN, font=(FONT_NAME, 30, "bold"))




einstein.place(x=30, y=15)



pomodoro.mainloop()



