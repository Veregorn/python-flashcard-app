from tkinter import *
import pandas
from random import choice

# ------------------------------------ CONSTANTS ------------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
HEADS_OR_TAILS = ["English", "Spanish"]
BLACK = "#000000"

# ------------------------------------ GLOBAL VARIABLES ------------------------------------ #
# Read the words file and save therm in a variable (DataFrame)
data = pandas.read_csv('data/en_es_words.csv')

# Create an English-Spanish dictionary from the DataFrame
data_dict = {row.english:row.spanish for (index, row) in data.iterrows()}

# We need to separate keys from values too
english_words_list = list(data_dict.keys())

# Create a variable with the language selected by the random choice of HEADS_OR_TAILS
selected_language = ""

# ------------------------------------ GENERATE RANDOM ENGLISH WORDS ------------------------------------ #
def generate_random_word():
    global selected_language
    
    # Throw the coin to select a language
    selected_language = choice(HEADS_OR_TAILS)

    # Select a random word
    if selected_language == "English":
        # Select a random english word to be our key
        random_english_word = choice(english_words_list)
        # So our value is...
        equivalent_spanish_word = data_dict[random_english_word]
        # Change texts in canvas
        canvas.itemconfig(language_label_id, text=selected_language)
        canvas.itemconfig(word_label_id, text=random_english_word)
    else: # Spanish language selected
        # Select a random english word to be our value
        random_english_word = choice(english_words_list)
        # So our value is...
        equivalent_spanish_word = data_dict[random_english_word]
        # Change texts in canvas
        canvas.itemconfig(language_label_id, text=selected_language)
        canvas.itemconfig(word_label_id, text=equivalent_spanish_word)

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
card_id = canvas.create_image(400, 263, image=card_front_img) # Position the image in the middle of the canvas (width / 2 and height / 2)

# Create a text for the language of the word displayed
language_label_id = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, 'italic'), fill=BLACK)

# Create a text for the word to mem
word_label_id = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, 'bold'), fill=BLACK)

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






window.mainloop()