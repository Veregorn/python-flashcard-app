from tkinter import *

# ------------------------------------ CONSTANTS ------------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------------------ UI SETUP ------------------------------------ #
# Create the App window
window = Tk()
window.title("Flashcard App")
window.geometry("890x750+500+300") # The last 2 values position the window App on the computer's screen
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

# Create a canvas for the flashcard and the 2 texts
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Create the card front image
card_front_img = PhotoImage(file="images/card_front.png")

# Put the image into the canvas
canvas.create_image(400, 263, image=card_front_img) # Position the image in the middle of the canvas (width / 2 and height / 2)

# Create a text for the language of the word displayed
canvas.create_text(400, 150, text="English", font=(FONT_NAME, 40, 'italic'))

# Create a text for the word to mem
canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, 'bold'))

# Position the canvas into the screen
canvas.grid(column=0, row=0, columnspan=2)

# Create the 'Wrong' button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, width=96, height=95, highlightthickness=0, border=0)
wrong_button.grid(column=0, row=1)

# Create the 'Right' button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, width=96, height=95, highlightthickness=0, border=0)
right_button.grid(column=1, row=1)





window.mainloop()