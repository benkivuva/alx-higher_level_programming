#!/usr/bin/python3

class Node:
    """Node class for a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node instance.

        Args:
            data (int): Data value of the node.
            next_node (Node, optional): Next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data value of the node.

        Returns:
            int: Data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): Data value to set.

        Raises:
            TypeError: If the data value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: Next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): Next node to set.

        Raises:
            TypeError: If the next node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class representing a singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (in increasing order).

        Args:
            value (int): Value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: String representation of the linked list.
        """
        output = ""
        current = self.head
        while current:
            output += str(current.data) + "\n"
            current = current.next_node
        return output.strip()
