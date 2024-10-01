#!/usr/bin/python3
"""Defines the structure of a node in a singly linked list
"""


class Node:
    """Defines a node in a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initializes and instance with data and next_node

        Args:
            data: data element of the node
            next_node: reference to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Gets the value of self.__data

        Returns: value of self.__data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Sets the value of self.__data

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets the value of self.__next_node

        Returns: the value of self.__next_node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Sets the value of self.__next_node

        Args:
            value: value of self.__next_node
        Raises:
            TypeError: value is not a Node object
        """

        if not isinstance(value, Node) and value:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
Defines a singly linked list
"""


class SinglyLinkedList:
    """Defines a singly linked list
    """

    def __init__(self):
        """Initializes  a singly linked list
        """

        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node in the correct sorted position in the list

        Args:
            value: value for data section of the node
        """
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        insert = self.__head
        while insert.next_node and insert.next_node.data < value:
            insert = insert.next_node
        if insert.next_node:
            new_node.next_node = insert.next_node
        insert.next_node = new_node

    def __str__(self):
        """
        Prints the data section of all the nodes of a singly linked list

        Returns: all the data elements
        """
        node = self.__head
        print_nodes = ""

        while node:
            print_nodes += str(node.data) + "\n"
            node = node.next_node
        return (print_nodes[:-1])
