# Password generator that combines multiple short words to make easily memorable passwords

# Function generate_password() uses ceil() from the math library and shuffle(), randint() from the random library
# This file does not use any libraries not included with python install
from math import ceil
from random import shuffle, randint


def generate_password(word_count, character_count, dictionary):
    # figure out what is the necessary word length for each word
    # try to keep words as even as possible (ex for 14 char. 3 word, try [5,5,4])

    if word_count >= character_count:
        # if word count exceeds character count, use only single letters.
        # create ones array of length word_count to store lengths of each word

        word_length_store = [1] * word_count

    else:
        # if word count does not exceed character count:
        # find average word length, assuming most words longer with one word shorter
        average_word_length = ceil(character_count/word_count)
        word_length_store = [average_word_length]*(word_count-1)

        # add remaining word to the end. works regardless of if a different length word is needed or not
        word_length_store.append(character_count - sum(word_length_store))

        # shuffle list so short word isn't always last
        shuffle(word_length_store)

    # generate actual password by using required word lengths as keys
    password_list = []
    for length_key in word_length_store:
        # get random integer value within the length of the referenced list
        random_pick_value = randint(0, len(dictionary[length_key])-1)

        word = dictionary[length_key][random_pick_value]

        # capitalize first letter and add to list
        password_list.append(word.capitalize())

    return "".join(password_list)


def import_dictionary(dict_file):
    # read text file with dictionary words
    # check length of each word and store arrays of same-length words in a dictionary w/ key of length
    dict_words = {}

    words = open(dict_file, encoding='iso-8859-1').read().splitlines()
    for word in words:
        try:
            dict_words[len(word)].append(word.lower())
        except KeyError:
            dict_words[len(word)] = [word.lower()]

    return dict_words



if __name__ == "__main__":
    word_count = 3
    char_count = 14

    dictionary_file = "../ext/dictionary.txt"
    dictionary = import_dictionary(dictionary_file)

    passwd = generate_password(word_count, char_count, dictionary)

    print(passwd)