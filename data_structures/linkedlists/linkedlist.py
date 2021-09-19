from data_structures.linkedlists.node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def insert_at_tail(self, value):
        node = Node(value)

        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_at_index(self, index: int, val: int) -> None:
        if index == 0:
            return self.insert_at_head(val)
        if index == self.size:
            return self.insert_at_tail(val)
        if index < 0 or index > self.size:
            return

        curr = self.head
        node = Node(val)

        while curr.next and index:
            curr = curr.next
            index -= 1

        prev_node = self.get_previous_node_of(curr)

        node.next = curr
        prev_node.next = node
        self.size += 1

    def get_previous_node_of(self, node):
        curr = self.head

        while curr.next != node:
            curr = curr.next
        return curr

    def insert_at_head(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def is_empty(self):
        return not self.size

    def display(self):
        if self.is_empty():
            print("[]")
        curr = self.head

        while curr:
            print(f"({curr.value}) -> ", end='')
            curr = curr.next
        print()

    def delete_at_tail(self):
        if self.is_empty():
            return

        if self.head == self.tail:
            self.head = self.tail = None

        else:

            prev_node = self.get_previous_node_of(self.tail)
            prev_node.next = None
            self.tail = prev_node

        self.size -= 1

    def delete_at_head(self):
        if self.is_empty():
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            next_node = self.head.next
            self.head.next = None
            self.head = next_node

        self.size -= 1

    def delete_at_index(self, index):
        if self.is_empty():
            return
        if index == self.size - 1:
            return self.delete_at_tail()
        if index == 0:
            return self.delete_at_head()

        if index < 0 or index >= self.size:
            return

        curr = self.head

        while curr.next and index:
            curr = curr.next
            index -= 1

        prev_node = self.get_previous_node_of(curr)

        prev_node.next = prev_node.next.next
        curr.next = None
        self.size -= 1
