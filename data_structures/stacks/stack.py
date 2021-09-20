from data_structures.linkedlists.node import Node


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head

        self.head = node
        self.size += 1

    def peek(self):
        if self.is_empty():
            return
        return self.head.value

    def pop(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.size -= 1

    def is_empty(self):
        return self.head is None

    def display(self):
        curr = self.head

        while curr:
            print(curr.value, "->", end=' ')
            curr = curr.next
