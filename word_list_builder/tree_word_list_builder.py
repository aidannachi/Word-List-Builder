# tree_word_list_builder.py
# Aidan Nachi
# 2024.4.25
# This file defines a function that takes words from an inputted file
# and puts them in a list sorted alphabetically.
#
# This file supports file input functionality that allows users to
# insert text files. The program then takes each word in the file and
# inserts them into a binary search tree. These words along with the
# number of times individual words were inserted, if inserted more than
# once are printed in lexographic order into a table and outputted for
# the user. The total number of words in the inputted file is also ouputted
# as well as the number of distinct words in the file.


from tree import Binary_search_tree

def do_build_list_from_file():
    """ Build a print a list from a file. """

    print('\nWord List Builder\n')
    print('The Word List Builder inputs words from'+
          ' a text file and inserts them\ninto'+
          ' a binary search tree based on their alphabetical'+
          ' order.\nThe words are then traversed and'+
          ' printed in order along with the\nnumber of'+
          ' occasions they were inserted into a'+
          ' lexographically ordered list.')



    # Give users the option to input files or exit.
    while True:
        user_input_option = input("\nWould you like to turn"+
                                  " a file of words into a list? (y/n): ")
        print('')

        if user_input_option == "n":
            break

        else:

            user_file_input = input("\nInput file name: ")
            print('')

            word_list_tree = Binary_search_tree()
            word_list_tree.build_tree_from_file(user_file_input)

            word_list_tree.word_counter()
            word_list_tree.distinct_word_counter()

            print("Number of words in this file: "+
                  f"{word_list_tree.total_word_count}\n")
            print("Number of distinct words in this file: "+
                  f"{word_list_tree.distinct_word_count}\n")

            # Insert words in the file into a tree based on there alphabetical
            # order.
            print(f"             WORD LIST\n")
            print(f"{'Word':^20}{'Count':^10}")
            print("     -------------------------\n")

            word_list_tree.list_builder_print()


def main():
    """ Demonstrate tree word list builder functionality. """

    do_build_list_from_file()


if __name__ == "__main__":
    main()
