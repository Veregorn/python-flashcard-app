from tkinter import *
import pandas
from random import choice

# ------------------------------------ CONSTANTS ------------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
HEADS_OR_TAILS = ["English", "Spanish"]
BLACK = "#000000"
WHITE = "#FFFFFF"

# ------------------------------------ GLOBAL VARIABLES ------------------------------------ #
# Read the words file and save therm in a variable (DataFrame)
data = pandas.read_csv('data/en_es_words.csv')

# Create an English-Spanish dictionary from the DataFrame
# data_dict = {row.english:row.spanish for (index, row) in data.iterrows()} # This is a way viewed in the NATO Alphabet Project. Let's try another one here to create a list of dictionaries
to_learn = data.to_dict(orient="records")

# Create a variable with the language selected by the random choice of HEADS_OR_TAILS
selected_language = ""

# A variable for the timer of 3 seconds to flip the card
timer = None

# ------------------------------------ FLIP CARD FUNCTION ------------------------------------ #
def flip_card(word):
    global selected_language

    # Change the language
    if selected_language == "English":
        selected_language = "Spanish"
    else:
        selected_language = "English"

    # Change the image in the canvas
    canvas.itemconfig(card_id, image=card_back_img)

    # Change the texts in the canvas
    canvas.itemconfig(language_label_id, text=selected_language, fill=WHITE)
    canvas.itemconfig(word_label_id, text=word, fill=WHITE)

# ------------------------------------ GENERATE RANDOM ENGLISH WORDS ------------------------------------ #
def generate_random_word():
    global selected_language
    global timer

    # Cancel the after loop if is set
    if timer:
        window.after_cancel(timer)

    # Change the image in the canvas
    canvas.itemconfig(card_id, image=card_front_img)

    # Pick a random dict from our 'to_learn' list
    random_word = choice(to_learn)

    # Extract both words (English and Spanish)
    english_word = random_word['english']
    spanish_word = random_word['spanish']
    
    # Throw the coin to select a language
    selected_language = choice(HEADS_OR_TAILS)

    # Select a random word
    if selected_language == "English":
        # Change texts in canvas
        canvas.itemconfig(language_label_id, text=selected_language, fill=BLACK)
        canvas.itemconfig(word_label_id, text=english_word, fill=BLACK)
        # After 3 seconds, call 'flip_card' function
        window.after(3000, flip_card, spanish_word)
    else: # Spanish language selected
        # Change texts in canvas
        canvas.itemconfig(language_label_id, text=selected_language, fill=BLACK)
        canvas.itemconfig(word_label_id, text=spanish_word, fill=BLACK)
        # After 3 seconds, call 'flip_card' function
        timer = window.after(3000, flip_card, english_word)

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

# Create the card back image
card_back_img = PhotoImage(file="images/card_back.png")

# Put the image into the canvas
card_id = canvas.create_image(400, 263, image=card_front_img) # Position the image in the middle of the canvas (width / 2 and height / 2)

# Create a text for the language of the word displayed
language_label_id = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, 'italic'), fill=BLACK)

# Create a text for the word to mem
word_label_id = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, 'bold'), fill=BLACK)

# Position the canvas into the screen
canvas.grid(column=0, row=0, columnspan=2)

# Create the 'Wrong' button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, width=96, height=95, highlightthickness=0, border=0, command=generate_random_word)
wrong_button.grid(column=0, row=1)

# Create the 'Right' button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, width=96, height=95, highlightthickness=0, border=0, command=generate_random_word)
right_button.grid(column=1, row=1)

# Call for a word one first time
generate_random_word()




window.mainloop()