from tkinter import *
import pandas as pd
import random

TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

#-----------------------------FUNCTIONALITY--------------------------------
try:
    # look for an existing file of words that need to be studied
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    # if that fails and there is no file, use the default and import into a dataframe
    original_data = pd.read_csv('data/french_words.csv')
    # convert dataframe into a list of dictionaries
    # orient the table to create a dictionary --> pairs the values by row into a list of dictionaries, keys are what the column headers were in the dataframe
    to_learn = original_data.to_dict(orient='records')
else:
    # but if there is a words to learn, use that as DF->list of dictionaries
    # orient the table to create a dictionary --> pairs the values by row into a list of dictionaries, keys are what the column headers were in the dataframe
    to_learn = data.to_dict(orient= 'records')

def next_card():
    global current_card, flip_timer # bring in globals
    window.after_cancel(flip_timer) # cancel the timer so that if shuffling between cards, timer starts again
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image = card_front)
    canvas.itemconfig(card_title, text = "French", fill = 'black')
    canvas.itemconfig(card_word, text = current_card['French'], fill = 'black')
    flip_timer = window.after(5000, func=flip_card) # reset timer

def flip_card():
    canvas.itemconfig(canvas_img, image = card_back)
    canvas.itemconfig(card_title, text = 'English', fill= 'white')
    canvas.itemconfig(card_word, text = current_card['English'], fill = 'white')

def is_known():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index = False) # false --> does not include the index numbers in new csv file
    next_card()

#----------------------------------UI--------------------------------------
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card) # set up an interval for the window to perform the flip card function, saved as a variable to then change/cancel in new card function

# canvas
canvas = Canvas(width = 800 , height = 526,  bg = BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file = 'images/card_front.png')
card_back = PhotoImage(file = 'images/card_back.png')
canvas_img = canvas.create_image(400,278, image = card_front)
card_title = canvas.create_text(400, 150, text = "French", fill = "black", font=(TITLE_FONT))
card_word = canvas.create_text(400, 263, text = "word", fill = "black", font=(WORD_FONT))
canvas.grid(column = 0, row = 0, columnspan = 2)

# buttons
right_img = PhotoImage(file= 'images/right.png')
right_button = Button(image= right_img, highlightthickness= 0, command=is_known)
right_button.grid(column = 1, row = 1)
wrong_img = PhotoImage(file = 'images/wrong.png')
wrong_button = Button(image= wrong_img, highlightthickness= 0, command=next_card)
wrong_button.grid(column = 0, row = 1)

next_card() # after UI is setup, the first card will be set up by calling this function before loop begins

window.mainloop()
