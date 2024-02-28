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
# We have to test if 'words_to_learn.csv' exist (an updated list). In that case, read from it
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/en_es_words.csv')

# Create an English-Spanish dictionary from the DataFrame
# data_dict = {row.english:row.spanish for (index, row) in data.iterrows()} # This is a way viewed in the NATO Alphabet Project. Let's try another one here to create a list of dictionaries
to_learn = data.to_dict(orient="records")

# Create a variable with the language selected by the random choice of HEADS_OR_TAILS
selected_language = ""

# A variable for the timer of 3 seconds to flip the card
timer = None

# We need to keep the actual word in case it needs to be removed from the list. It's a dictionary {'english': 'english_word', 'spanish': 'spanish_word'}
current_word = {}

# ------------------------------------ FLIP CARD FUNCTION ------------------------------------ #
def flip_card():
    global selected_language
    global current_word

    # Change the language
    if selected_language == "English":
        selected_language = "Spanish"
        # Change the text in the canvas
        canvas.itemconfig(word_label_id, text=current_word['spanish'], fill=WHITE)
    else:
        selected_language = "English"
        # Change the text in the canvas
        canvas.itemconfig(word_label_id, text=current_word['english'], fill=WHITE)

    # Change the image in the canvas
    canvas.itemconfig(card_id, image=card_back_img)

    # Change the texts in the canvas
    canvas.itemconfig(language_label_id, text=selected_language, fill=WHITE)

# ------------------------------------ GENERATE RANDOM ENGLISH WORDS ------------------------------------ #
def generate_random_word():
    global selected_language
    global timer
    global current_word

    # Cancel the after loop if is set so we only have on timer running!!!
    if timer:
        window.after_cancel(timer)

    # Change the image in the canvas
    canvas.itemconfig(card_id, image=card_front_img)

    # Pick a random dict from our 'to_learn' list
    current_word = choice(to_learn)
    
    # Throw the coin to select a language
    selected_language = choice(HEADS_OR_TAILS)

    # Select a random word
    if selected_language == "English":
        # Change texts in canvas
        canvas.itemconfig(language_label_id, text=selected_language, fill=BLACK)
        canvas.itemconfig(word_label_id, text=current_word['english'], fill=BLACK)
        # After 3 seconds, call 'flip_card' function
        timer = window.after(3000, flip_card)
    else: # Spanish language selected
        # Change texts in canvas
        canvas.itemconfig(language_label_id, text=selected_language, fill=BLACK)
        canvas.itemconfig(word_label_id, text=current_word["spanish"], fill=BLACK)
        # After 3 seconds, call 'flip_card' function
        timer = window.after(3000, flip_card)

# ------------------------------------ UPDATE THE LIST AND SAVE IT TO A FILE ------------------------------------ #
def update_list():
    global current_word
    global to_learn

    # Remove this dict from out list
    to_learn.remove(current_word)
    print(f"Words to learn: {len(to_learn)}")

    # Create a new CSV file, we need to create a new DataFrame first
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    
    # Finally, we need to generate another word
    generate_random_word()

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
right_button = Button(image=right_image, width=96, height=95, highlightthickness=0, border=0, command=update_list)
right_button.grid(column=1, row=1)

# Call for a word one first time
generate_random_word()




window.mainloop()