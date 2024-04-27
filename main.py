from tkinter import Tk, Label, Button, PhotoImage, Canvas

BACKGROUND_COLOR = "#B1DDC6"
language_name_font = ("Ariel", 40, "italic")
translated_font = ("Ariel", 60, "bold")

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
name_of_language = canvas.create_text(400, 150, text="German", font=language_name_font, fill="black")
translated_version = canvas.create_text(400, 263, text="ich", font=translated_font, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Button
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(row=1, column=0)

window.mainloop()
