import tkinter as tk
from tkinter import *
import os 
import random


# root a canvas
root = tk.Tk()
root.title("Hangman Game")
root.geometry("1280x720")
# root.iconbitmap()

canvas = tk.Canvas(root, bg="#1e3346", width=800, height=700)
canvas.pack(fill="both", expand=True)

# frames
main_frame = tk.Frame(root, padx=5, pady=5, highlightbackground="black", highlightthickness=5)
main_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

heading_frame = tk.Frame(main_frame, padx=5, pady=5)
heading_frame.place(relwidth=0.8, height=120, relx=0.1, rely=0.025)

game_frame = tk.Frame(main_frame, padx=5, pady=5)
game_frame.place(relwidth=0.8, relx=0.1, rely=0.3)

button_frame = tk.Frame(main_frame, padx=5, pady=5)
button_frame.place(height=150, width=500, rely=0.3)

# headings
hangman_heading = tk.Label(heading_frame, text="Hangman Game", font=("Arial Black", 25), pady=10)
hangman_subheading = tk.Label(heading_frame, text="What mode do you wanna play ?", font=10, pady=10)

words = ["price","cook","committee","development","suit","canvas","volcano","wilderness","man","whistle","snakes","brother","approval","car","vessel","reward","fruit","smash","cable","curve","country","trail","island","elbow","loaf","toys","parent","boats","donkey","rate","bottle","view","ink","back","experience","air","voyage","education","bread","glass","gold","fish","flame","quarter","blade","birthday","agreement","metal","street","plough","flesh","babies","soap","lawyer","judge","sugar","motion","disgust","end","giant","glue","chairs","look","brake","cow","nut","discussion","cherries","jelly","north","town","cloud","control","grass","honey","trip","balls","break","fast","fall","company","suit","tax","canvas","donkey","music","church","skirt","stew","kiss"]

# funkce na hraní
def hadani():

    user_input = entry_letter.get()

    global attempts, hidden_word, word, guessed
    
    if not guessed == True and attempts > 0:

        if len(user_input) == 1 and (user_input.isalpha()) :
            if user_input in inputs:
                report_label.config(text=("You've already guessed this letter"))
            
            elif user_input in word:
                inputs.append(user_input)
                progress_word = list(hidden_word)
                chars = [i for i, char in enumerate(word) if char == user_input]

                for x in chars:
                    progress_word[x] = user_input

                hidden_word = "".join(progress_word)

                if not "_" in hidden_word:
                    guessed = True

                hidden_word_label.config(text=hidden_word)
                report_label.config(text=("")) 
                attempts_label.config(text=("Attempts left : " + str(attempts) + "\nUsed letters : " + str(inputs)))  
                
            else :
                report_label.config(text=("")) 
                inputs.append(user_input)
                attempts = attempts - 1  
                report_label.config(text=("The word does not contain this letter."))
                attempts_label.config(text=("Attempts left : " + str(attempts) + "\nUsed letters : " + str(inputs)))    

        elif len(user_input) == len(word) and user_input.isalpha():
            if user_input == word:
                guessed = True
            else:
                report_label.config(text=("That's not the word"))
                attempts = attempts - 1 
        else:
            report_label.config(text=("What are you doing? You can only enter ONE LETTER"))  

    
    if guessed == True :
        report_label.config(text=("YOU WON. Attempts left : " + str(attempts)))
        # konec()
    elif attempts == 0:
        report_label.config(text=("Too bad, you ran out of attempts. The word was : " + word))
        # konec()
            
# def konec():
#     konec_input = input("Chceš hrát znovu ? A/N\n").upper()
#     if len(konec_input) == 1 and konec_input.isalpha:
#         if konec_input == "A":
#             hadani()
#         elif konec_input == "N":
#             print("k kys")
#         else:
#             print("TY DEMENTE CO DĚLÁŠ PROSTĚ NAPIŠ A NEBO N DEMENTE!!!!!")
#     else:
#         print("TY DEMENTE CO DĚLÁŠ PROSTĚ NAPIŠ A NEBO N DEMENTE!!!!!")


# vygenerování random slova
def random_btn():
    random_word_button.pack_forget()
    set_word_button.pack_forget()
    hangman_subheading.pack_forget()

    set_vars()

    game_option.config(text="The game generated random word.")
    game_option.pack()

    global word, hidden_word
    word = random.choice(words)
    hidden_word = len(word) * "_"

    play_button.pack()

# kliknutí na btn pro zadání slova
def manual_btn():
    random_word_button.pack_forget()
    set_word_button.pack_forget()
    hangman_subheading.pack_forget()

    button_frame.config(bg="#1e3346")

    game_option.config(text="Type your word.")
    game_option.pack()

    entry_word.pack()
    set_button.pack()

def set_word():
    global word, hidden_word
    word = entry_word.get()

    if word.isalpha():
        error_label.pack_forget()
        entry_word.pack_forget()
        set_button.pack_forget()

        set_vars()
        hidden_word = (len(word) * "_")
    
        button_frame.config(height=50)
        game_option.config(text="Word successfuly set")

        play_button.pack()

    else:
        error_label.pack()

def play():
    game_option.pack_forget()
    play_button.pack_forget()
    button_frame.destroy()

    global hidden_word_label, attempts_label, letter_label

    hidden_word_label = tk.Label(game_frame, text=hidden_word)
    attempts_label = tk.Label(game_frame, text=("Attempts left : " + str(attempts)))
    letter_label = tk.Label(game_frame, text="Guess the letters OR the whole word (but only now, later you won't have the chance)\nThe word has " + str(len(word)) + " letters.")
    # image = tk.PhotoImage(game_frame, file=(str(attempts) + ".png"))

    letter_label.pack()
    hidden_word_label.pack()
    entry_letter.pack()
    report_label.pack()
    submit_letter_btn.pack()
    attempts_label.pack()

def set_vars():
    global inputs, attempts, guessed

    inputs = []
    attempts = 12
    guessed = False


#pro zadávání slova
entry_word = tk.Entry(button_frame)
set_button = tk.Button(button_frame, text="Enter", command=set_word)
error_label = tk.Label(button_frame, text="You can only enter words made out of letters, not numbers")
game_option = tk.Label(button_frame, text="Type your word", font=("Arial", 15), pady=5, padx=5 )

#  hra
submit_letter_btn = tk.Button(game_frame, text="Guess", command=hadani)
report_label = tk.Label(game_frame, text="")
entry_letter = tk.Entry(game_frame)

# buttony
random_word_button = tk.Button(button_frame, padx=5, pady=5, bg="#1e3346", text="Random word", fg="white", font=20, command=random_btn)
set_word_button = tk.Button(button_frame, padx=5, pady=5, bg="#1e3346", text="My own word", fg="white", font=20, command=manual_btn)
play_button = tk.Button(button_frame, padx=5, pady=5, bg="#1e3346", text="Play", fg="white", font=20, command=play)

# umístění main menu
hangman_heading.pack()
hangman_subheading.pack()
random_word_button.pack(fill="x")
set_word_button.pack(fill="x")

root.mainloop()