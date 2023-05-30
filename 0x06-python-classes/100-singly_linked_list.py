#!/usr/bin/python3
"""Define a singly linked list data structure."""


class Node:
    """A node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node instance.

        Args:
            data: The data to be stored in the node.
            next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data stored in the node.

        Args:
            value: The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node in the linked list.

        Args:
            value: The next node.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list."""

    def __init__(self):
        """Initialize the linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a value in sorted order.

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        current = self.__head
        result = ""
        while current is not None:
            result += "{}".format(current.data)
            current = current.next_node
            if current is not None:
                result += "\n"
        return result
