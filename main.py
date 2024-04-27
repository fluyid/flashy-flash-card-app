from tkinter import Tk, Button, PhotoImage, Canvas
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
language_name_font = ("Ariel", 40, "italic")
translated_font = ("Ariel", 60, "bold")

data = pandas.read_csv("data/Top 100 German to English Words - Sheet1.csv")
to_learn = data.to_dict(orient="records")

# Functions


def next_card():
    current_card = random.choice(to_learn)
    print(current_card["German"])
    canvas.itemconfig(card_title, text="German")
    canvas.itemconfig(card_word, text=current_card["German"])


# Window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
card_title = name_of_language = canvas.create_text(400, 150, text="", font=language_name_font, fill="black")
card_word = translated_version = canvas.create_text(400, 263, text="", font=translated_font, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Button
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
