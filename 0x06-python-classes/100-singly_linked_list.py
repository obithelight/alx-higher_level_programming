#!/usr/bin/python3
''' A Module Representing a Node Class '''


class Node:
    ''' Defines a node of a singly linked list '''

    def __init__(self, data, next_node=None):
        '''
        Initializes the node class
        Args:
            data (integer) - data of the new Node
            next_node (Node) - next node of the new Node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' retrieves the data of the node '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' sets the data of the node '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        ''' retrieves the address of node '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' sets the address of the new Node '''
        if not isinstance(value, Node) and \
                value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' Defines a singly linked list '''

    def __init__(self):
        ''' Initializes the list '''
        self.__head = None

    def sorted_insert(self, value):
        '''
        Inserts a new Node into the singly linked list.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert

        '''
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        '''
        Prints the string representation of a
        singly linked list to the stdout
        '''
        elements = []
        temp = self.__head
        while (temp is not None):
            elements.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(elements))
