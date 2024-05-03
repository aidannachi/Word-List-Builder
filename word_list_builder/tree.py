# cstree.py
# Aidan Nachi
# 2024.25.4
# This file defines a Binary Search Tree class with all the
# usual behaviors of a Binary Search Tree.
#
# This file defines a Binary Search Tree class as well as
# an accompying Tree Node class. The Tree class resembles the
# behaviors of a binary search tree, that contains two child
# subnodes for each parent node. The Tree class supports
# inserting and traversing of nodes. The insertions performed
# store nodes in a sorted order, this class specifically stores
# lexographically. The class keeps track of the total amound of
# words inserted and the amount of distinct words in the tree.
# Inserted items that have been inserted more than once will be
# added to a count and this data will be kept instead of having
# two nodes with the same data. The class also supports a print
# functionality that goes through every node in lexographic order
# and prints each nodes data and count.
#
# Usage
# from cstree import binary_search_tree


class Binary_search_tree():
    """ Implement a Binary Search Tree object.

    Instance variables
    root    the first node in the tree
    """

    # Instance Variables
    #
    # root                  Initial node in the tree
    #                       where we first refer
    #
    # total_word_count      The total amount of words
    #                       in a file
    #
    # distinct_word_count   The total amound of distinct
    #                       words in a file.

    def __init__(self):
        """ Create a binary search tree object.

        Usage
        binary_search_tree = Binary_search_tree()
        """

        self.root = None
        self.total_word_count = 0
        self.distinct_word_count = 0


    def inorder_traversal_print(self, ptr):
        """ Traverse and print each node in a tree rooted at ptr. """

        # Prints each node in a tree by performing an in order traversal
        # giving us a list of node values from a tree in order.
        if ptr:
            self.inorder_traversal_print(ptr.left)
            ptr.print_node()
            self.inorder_traversal_print(ptr.right)


    def list_builder_print(self):
        """ Traverse and print each node in the tree. """

        # Give access to in order traversal prints outside of the class.
        self.inorder_traversal_print(self.root)


    def word_count_traversal(self, ptr):
        """ Traverse and tally how many words got inserted into a tree. """

        # Perform an in order traversal and count how many times each
        # word was inserted into a tree.
        if ptr:
            self.word_count_traversal(ptr.left)
            self.total_word_count += ptr.count
            self.word_count_traversal(ptr.right)


    def word_counter(self):
        """ Traverse and tally how many words got inserted into a tree. """

        # Perform an in order traversal and count the number of inserts.
        self.word_count_traversal(self.root)


    def distinct_word_count_traversal(self, ptr):
        """ Traverse and tally each distinct word in a tree rooted at ptr. """

        # Perform an in order traversal and count each word in the tree.
        if ptr:
            self.distinct_word_count_traversal(ptr.left)
            self.distinct_word_count += 1
            self.distinct_word_count_traversal(ptr.right)


    def distinct_word_counter(self):
        """ Traverse and tally each node in a tree. """

        # Perform an in order traversal and count each word in the tree.
        self.distinct_word_count_traversal(self.root)


    def insert_tree_node(self, ptr, value):
        """ Insert a node in a tree rooted at ptr.

        Inserting occurs in lexographic fashion with values that coming first
        getting inserted in empty left child nodes, while greater values get
        inserted in empty right child nodes.

        Example, new_node = Tree_node('lime')

               mango
              /     \ 
           apple    pear
          /     \  /    \  Tree that new_node is getting inserted into.
        ______________________________________________________________________
               mango
              /     \  
           apple    pear
          /     \  /    \ 
                 \ 
                 lime      Tree node after new_node gets inserted into first empty
                           right child node of the left child node of the root.
        """

        # Covers case of inserting into an empty tree, where we
        # set the root to the node we are inserting.
        if self.root is None:
            new_node = Tree_node(value)
            self.root = new_node

        # Covers the case where we are trying to insert a node
        # that has been already inserted, where instead of inserting
        # the node we just add it to the count.
        elif value == ptr.data:
            ptr.count +=1

        # Covers the case the node we are inserting being less lexographically
        # than the node we are pointing at resulting us point to the left child node.
        elif value < ptr.data:
            if ptr.left is None:
                ptr.left = Tree_node(value)

            # We want to keep checking the value of the pointer until
            #  it's empty, then we can insert our new node.
            else:
                self.insert_tree_node(ptr.left, value)

        # Covers the case of the node we are inserting being greater lexographically
        # than the node we are currently pointing at resulting us to point to the
        # right child node.
        else:
            if ptr.right is None:
                ptr.right = Tree_node(value)

            # We want to keep checking the value of the pointer until
            #  it's empty, then we can insert our new node.
            else:
                self.insert_tree_node(ptr.right, value)


    def build_tree_from_file(self, filename):
        """ Insert data from a file into a tree ."""

        # Inserts items from a file into nodes of a tree based on
        # their lexographic order.
        with open(filename, 'r') as f:
            for a_line in f:
                for a_word in a_line.split():
                    self.insert_tree_node(self.root, a_word)


class Tree_node():
    """ Implement a Tree Node object.

        Instance variables
        data    holds the value being stored in the node
        count   holds the number of times a certain value has been inserted
        into a tree
        next    holds the location of the next node inside of a tree
        """

    def __init__(self, value):
        """ Create a Tree Node object.

        Parameter
        value   Data being stored in the node
        """

        self.data = value
        self.count = 1
        self.next = None
        self.left = None
        self.right = None



    def print_node(self):
        """ Print the data and count of a node in a tree. """

        print(f"{self.data:^20}{self.count:^10}\n")

