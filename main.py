from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

# UI CREATION
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

card_front = PhotoImage(file="images/card_front.png")
tick = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, anchor=CENTER, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=tick, highlightthickness=0)
right_button.config(highlightthickness=0)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=1, row=1)








window.mainloop()

