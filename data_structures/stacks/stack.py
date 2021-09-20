from data_structures.linkedlists.node import Node


class Stack():
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


class StackArray:
    def __init__(self) -> None:
        self.capacity = 10
        self.stack = [None] * self.capacity
        self.size = 0
        self.top = -1

    def push(self, value):
        if self.is_full():
            self.resize()

        self.top += 1
        self.stack[self.top] = value
        self.size += 1

    def peek(self):
        if self.is_empty():
            return self.stack[self.top]
        return

    def pop(self):
        if self.is_empty():
            return
        deleted = self.stack[self.top]
        self.size -= 1
        self.top -= 1
        return deleted

    def is_empty(self):
        return not self.size

    def display(self):
        for i in range(self.size):
            print(self.stack[i])

    def is_full(self):
        return self.size == self.capacity

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity

        for i in range(self.size):
            temp[i] = self.stack[i]

        self.stack = temp
