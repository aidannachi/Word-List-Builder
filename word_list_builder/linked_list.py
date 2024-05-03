# linked_list.py
# Aidan Nachi
# 2024.04.17
# This file defines a Linked List and a Linked List Node class
# with the usual behaviors of a each.
#
# The file defines a Linked List class with it's accompying Linked
# List Node class. Each class is built with the usual behaviors, these
# include inserting, deleting, and printing of the linked list. Behaviors
# of the linked list node class include printing of each individual node in
# the linked list. In our Node we are keeping track of data, the next node, and
# a count of each node. What makes this class special in contrast to others is
# that inserting is done in lexographic order automatically and a count is kept
# for values that get inserted more than once.
#
# Usage
# from linked_list import Linked_list


class Linked_list():
    """ Implement a Linked List object. """

    def __init__(self):
        """ Create a Linked List. """

        # Instance variables
        # head                  - the entry point into the linked list.
        # word_count            - the amount of words inserted into the list.
        # distinct_word_count   - the amount of new words inserted into the list.
        self.head = None
        self.word_count = 0
        self.distinct_word_count = 0


    def list_print(self):
        """ Print the Linked List. """

        # Start at the head so we can go through the values and print.
        p = self.head

        # Print the amount of items that were inserted into the linked list.
        print(f"File Word Count: {self.word_count}\n")

        # Print the amount of words inserted into the list that haven't been inserted before.
        print(f"There are {self.distinct_word_count} distinct words in this file.\n")

        print("Word List\n")

        print("Words in the file include...\n")

        while p is not None:
            p.node_print()
            p = p.next


    def insert(self, value):
        """ Insert a value into the Linked List. """

        # Start at the head and traverse through until we find where we
        # want to insert our value while keeping track of the previous node.
        p = self.head
        q = None

        # Keep track of the number of inserts done to the linked list over time.
        self.word_count += 1

        # Keep track if we have completed the insert or not.
        done = False

        # Make insertions based on numerical or alphabetical order.
        while not done:

            # We want to insert value into head if the linked list is empty.
            if self.head is None:
                temp = Linked_list_node(value)
                self.head = temp
                self.distinct_word_count += 1
                done = True

            # If value comes numerically or alphabetically after all values in
            # the linked list, insert it at the very end.
            elif p is None:
                temp = Linked_list_node(value)
                q.next = temp
                self.distinct_word_count += 1
                done = True

            # We don't want to add values more than one time into the list,
            # instead we just count the number of times it's been inserted.
            elif p.data == value:
                p.count += 1
                done = True

            # When the value we are inserting numerically or alphabetically
            # preceeds a value that's already in the list we insert before
            # the first value it preceeds.
            elif value < p.data:

                # Insert the value at the start if preceeds everything in the list.
                if self.head == p:
                    temp = Linked_list_node(value)
                    temp.next = self.head
                    self.head = temp
                    self.distinct_word_count += 1
                    done = True

                # Insert the value inbetween values but before the value it preceeds.
                else:
                    temp = Linked_list_node(value)
                    q.next = temp
                    temp.next = p
                    self.distinct_word_count += 1
                    done = True

            else:
                q = p
                p = p.next


    def delete(self, value):
        """ Delete a value from the linked list. """

        # Start at the head and traverse through until we find where we
        # want to delete our value while keeping track of the previous node.
        p = self.head
        q = None
        done = False

        # Search for the location of the value we want to delete.
        while p.next is not None and not done:
            if p.data == value:

                # Delete the value from the first position in the list.
                if q is None:
                    self.head = p.next
                    done = True

                # Delete value from the linked list that's anywhere but the first position.
                else:
                    q.next = p.next
                    done = True
            else:
                q = p
                p = p.next


class Linked_list_node():
    """ Implement a node object for the linked list. """

    def __init__(self, value):
        """ Create a linked list node object. """

        # Instance variables
        # data  -   holds the value in a node.
        # next  -   points to the next nodes location.
        # count -   keeps track of how many times a value is inserted.
        self.data = value
        self.next = None
        self.count = 1


    def node_print(self):
        """ Print the data and count of a node in a list. """

        print(f"'{self.data}' x{self.count}\n")



