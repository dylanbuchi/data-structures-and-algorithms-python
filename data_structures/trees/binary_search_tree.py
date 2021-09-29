from data_structures.trees.node import Node
from collections import deque


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def is_leaf(self, node):
        return node.left is node.right is None

    def remove(self, value):
        def remove_recursively(node, value=value):
            if node is None:
                return node

            if value == node.value:
                # check for one node leaf or one child
                if self.is_leaf(node):
                    return None

                if node.left is None:
                    return node.right

                if node.right is None:
                    return node.left

                successor_node_value = self.get_successor_value(node.right)
                node.value = successor_node_value
                node.right = remove_recursively(node.right,
                                                successor_node_value)

            elif value > node.value:
                node.right = remove_recursively(node.right)

            else:
                node.left = remove_recursively(node.left)

            return node

        remove_recursively(self.root)

    def _append_iterative(self, value):
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

    def append(self, value):
        self.size += 1
        if self.root is None:
            self.root = Node(value)
        else:
            return self._append_recursively(self.root, value)

    def _append_recursively(self, node, value):
        if node is None:
            return Node(value)

        if value > node.value:
            node.right = self._append_recursively(node.right, value)
        else:
            node.left = self._append_recursively(node.left, value)

        return node

    def get_successor_value(self, node, successor_value=None):
        if node is None:
            return successor_value
        if node:
            successor_value = node.value
        return self.get_successor_value(node.left, successor_value)

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
