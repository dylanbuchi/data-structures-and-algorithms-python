from data_structures.trees.node import Node
from collections import deque


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def append(self, value):
        node = Node(value)

        if self.is_empty():
            self.root = node

        else:
            current = self.root

            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
                else:
                    return

        self.size += 1

    def search(self, value):
        if self.is_empty():
            return False
        curr = self.root

        while curr:
            if curr.value == value:
                return True

            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        return False

    def pre_order(self):
        output = []

        def helper(node):
            if node is None:
                return

            output.append(node.value)
            helper(node.left)
            helper(node.right)

        helper(self.root)
        return output

    def post_order(self):
        output = []

        def helper(node):
            if node is None:
                return

            helper(node.left)
            helper(node.right)
            output.append(node.value)

        helper(self.root)

        return output

    def in_order(self):
        output = []

        def helper(node):
            if node is None:
                return

            helper(node.left)
            output.append(node.value)
            helper(node.right)

        helper(self.root)
        return output

    def is_empty(self):
        return self.root is None

    def dfs(self):
        # this way it's like the pre-order
        stack = [self.root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.value)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return output

    def bfs(self):
        # level order
        queue = deque()
        queue.append(self.root)
        output = []

        while queue:
            node = queue.popleft()
            output.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return output
