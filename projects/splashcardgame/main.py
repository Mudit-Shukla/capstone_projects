from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/word_to_learn.csv").to_dict(orient ="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_dict = {}

def choose_word():
    global current_dict, flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0,99)
    current_dict = data[index]
    canvas.itemconfig(french_title, text = "French" )
    canvas.itemconfig(french_text, text=data[index]["French"])
    canvas.itemconfig(image_background, image = image)
    flip_timer = window.after(3000, filp_card)

def filp_card():
    global image2
    canvas.itemconfig(french_title, text = "English")
    canvas.itemconfig(french_text, text = current_dict["English"])
    canvas.itemconfig(image_background, image = image2)

def is_known():
    data.remove(current_dict)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/word_to_learn.csv")
    choose_word()

window = Tk()
window.title("Flashy")
window.config(bg = BACKGROUND_COLOR, padx = 50, pady = 50)
image2 = PhotoImage(file ="images/card_front.png")


flip_timer = window.after(3000, filp_card)

canvas = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
image = PhotoImage(file ="images/card_back.png")
image_background = canvas.create_image((400,263), image = image )
french_title = canvas.create_text((400, 150), text = "Title", font = ("Arial", 40, "italic"))
french_text = canvas.create_text((400, 265), text = "bye-bye", font = ("Arial", 35, "bold"))
canvas.grid(row = 0,column = 0, columnspan = 2)


right_button_image = PhotoImage(file ="images/right.png", )
right_button = Button(image = right_button_image, highlightthickness = 0, bg = BACKGROUND_COLOR,command = is_known)
right_button.grid(row = 1,column = 0)
wrong_button_image = PhotoImage(file ="images/wrong.png")
wrong_button = Button(image = wrong_button_image, highlightthickness = 0, bg = BACKGROUND_COLOR, command = choose_word)
wrong_button.grid(row = 1, column = 1)

choose_word()



window.mainloop()