# Command Line Interface (CLI) main run file for password word generator
# Uses command line input to generate passwords
# Dictionary file is set

from src.functions import *
from time import sleep

if __name__ == "__main__":
    # import dictionary
    dict_file = "ext/dictionary.txt"
    dictionary = import_dictionary(dict_file)

    # screen clear
    print_screen_break = "".join(["\n"]*2)

    # open loop
    running = True
    while running:
        # clear screen
        print(print_screen_break)

        # ask for word/char count
        while True:
            try:
                word_count = int(input("How many words: "))
                break
            except ValueError:
                print("Not a valid input. Please try again.")

        while True:
            try:
                char_count = int(input("How many characters: "))
                break
            except ValueError:
                print("Not a valid input. Please try again.")


        # generate password, display result
        generated_password = generate_password(word_count, char_count, dictionary)
        print(generated_password)
        print(print_screen_break)

        # ask if want to generate another
        while True:
            running = input("Would you like to generate another? (y/n): ").lower()
            if running == "y":
                running = True
                break
            elif running == "n":
                running = False
                print("Thank you for using password_word_generator.")
                sleep(2)
                break
            else:
                print("\n\n")
                print(f"{running} is not a valid option. Please try again.")