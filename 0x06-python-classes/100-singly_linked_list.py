#!/usr/bin/python3

"""
    A module defining a node of a singly linked list
"""


class Node:
    """ A class representing a the node
    """

    def __init__(self, data, next_node=None):
        """
            Initializes a new instances of the Node class

            Args:
                data(int): The data value of the node
                next_node: The next node in the linked list.
        """
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Get and return the data value
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
            Sets the data value of the node

            Args:
                value(int): The new data value

            Raises:
                TypeError: If 'value' is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
            Gets and return next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
            Set the next node in the linked list

            Args:
                value (Node or none): The next node in the list.

            Raises:
                TypeError: If 'value' is not a Node object or None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ a class representing a singly linked list
    """

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
            Insert a new node into the correct sorted position in list

            Args:
                value (int): The value to be inserted
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ Returns a string representation of the linked list
        """
        if self.head is None:
            return ""
        current = self.head
        result = str(current.data)
        while current.next_node is not None:
            current = current.next_node
            result += "\n" + str(current.data)
        return result
