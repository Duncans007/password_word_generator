# Graphical User Interface (GUI) main run file for password word generator
# uses tkinter to get input and display output

import tkinter as tk
from src.functions import *

dict_file = "ext\dictionary.txt"


def main():

# ============================================================================================
# Variable Setup
# ============================================================================================

    # import dictionary words
    dictionary = import_dictionary(dict_file)


# ============================================================================================
# Function Declarations
# ============================================================================================

    # define function to take form input and generate password
    def generate_from_gui():
        # enable and wipe output field
        entry_generated_password.config(state='normal')
        entry_generated_password.delete(0, tk.END)

        try:
            # get text input from form
            count_w = int(entry_word_count.get())
            count_c = int(entry_char_count.get())

            # generate password from functions in functions.py
            gen_pass = generate_password(count_w, count_c, dictionary)

            # write generated password to output field
            entry_generated_password.insert(0, gen_pass)

        except ValueError:
            # if an error is thrown, set output to "Error: Invalid Input"
            entry_generated_password.insert(0, "Error: Invalid Input")

        # disable output field
        entry_generated_password.config(state='readonly')


# ============================================================================================
# Tkinter Setup
# ============================================================================================


    # create tkinter window
    window = tk.Tk()
    window.title("Password Word Generator")

    # add input field for word number
    label_word_count = tk.Label(window, text="Word Count: ")
    label_word_count.grid(row=0, column=0, pady=2, sticky=tk.W)
    entry_word_count = tk.Entry(window)
    entry_word_count.grid(row=0, column=1, pady=2, sticky=tk.W)

    # add input field for character count
    label_char_count = tk.Label(window, text="Total Length: ")
    label_char_count.grid(row=1, column=0, pady=2, sticky=tk.W)
    entry_char_count = tk.Entry(window)
    entry_char_count.grid(row=1, column=1, pady=2, sticky=tk.W)

    # add button to generate password
    button_generate = tk.Button(window, text="Generate", width=10, command=generate_from_gui)
    button_generate.grid(row=2, pady=2, columnspan=2)

    # add output field for generated password
    entry_generated_password = tk.Entry(window)
    entry_generated_password.grid(row=3, pady=2, columnspan=2, ipadx=50)
    entry_generated_password.config(state='readonly')


if __name__ == "__main__":
    main()
    tk.mainloop()