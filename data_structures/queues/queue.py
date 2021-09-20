from data_structures.linkedlists.node import Node


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def peek(self):
        if self.is_empty():
            return
        return self.head.value

    def dequeue(self):
        if self.is_empty():
            return

        deleted = self.head.value

        if self.tail == self.head:
            self.tail = self.head = None

        else:
            self.head = self.head.next

        self.size -= 1
        return deleted

    def is_empty(self):
        return not self.size

    def display(self):
        curr = self.head

        while curr:
            print(curr.value, "->", end=' ')
            curr = curr.next


class QueueArray:
    def __init__(self) -> None:
        self.capacity = 10
        self.stack = [None] * self.capacity
        self.size = 0
        self.rear = -1
        self.first = 0

    def enqueue(self, value):
        if self.is_full():
            self.resize()

        self.rear += 1
        self.stack[self.rear] = value
        self.size += 1

    def peek(self):
        if self.is_empty():
            return
        return self.stack[self.first]

    def dequeue(self):
        if self.is_empty():
            return
        deleted = self.stack[self.first]
        self.size -= 1
        self.first += 1
        return deleted

    def is_empty(self):
        return not self.size

    def display(self):
        for i in range(self.first, self.rear + 1):
            print(self.stack[i])

    def is_full(self):
        return self.size == self.capacity

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity

        for i in range(self.size):
            temp[i] = self.stack[i]

        self.stack = temp
