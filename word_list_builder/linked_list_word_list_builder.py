# linked_list_word_list_builder.py
# Aidan Nachi
# 2024.04.18
# This file defines a function that takes words from an inputted file
# and puts them in a list sorted alphabetically.


from linked_list import Linked_list


def do_build_list_from_file():
    """ Build and print a list of words from a file. """

    print("\nWord List Builder")

    print("\nThe Word List Builder takes user inputted files and prints a list of")
    print("all the words in the file with the exception of the stop words, 'a', 'of',")
    print("'the', 'i', 'on', 'for', and 'from'. The number of occasions each word shows")
    print("up is also recorded as well as the total number of words and distinct words in the file.")

    # Give users the option to input files or exit.
    while True:
        user_input_option = input("\nWould you like to turn a file of words into a list? (y/n): ")
        print('')

        if user_input_option == "n":
            break

        else:

            # Keep track if the user's favorite word is included in the text
            # and keep track at the number of times it shows up.
            favorite_word = input("What is your favorite word? ")
            favorite_word_report = False
            favorite_word_count = 0

            user_file_input = input("\nInput file name: ")
            print('')
            a_list = Linked_list()

            # Insert words in the file into a linked list based on there alphabetical
            # order.
            with open(user_file_input) as f:
                for a_line in f:
                    for a_word in a_line.split():
                        if a_word == favorite_word:
                            favorite_word_report = True
                            favorite_word_count += 1

                        a_list.insert(a_word)

            if favorite_word_report is True:
                print(f"Your favorite word was included in the text of this"+
                       f" file on {favorite_word_count} seperate occasions.\n")

            else:
                print(f"Your favorite word was not included in the text of this file.\n")

            a_list.delete('a')
            a_list.delete('of')
            a_list.delete('the')
            a_list.delete('i')
            a_list.delete('on')
            a_list.delete('for')
            a_list.delete('from')

            a_list.list_print()


def main():
    """ Demonstrate the word list builder functionality. """

    do_build_list_from_file()


if __name__ == "__main__":
    main()




