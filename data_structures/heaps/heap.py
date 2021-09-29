from abc import ABC, abstractclassmethod


class Heap(ABC):
    def __init__(self):
        super().__init__()
        self.heap = []

    def _get_left_index(self, index):
        return 2 * index + 1

    def _get_right_index(self, index):
        return 2 * index + 2

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    @abstractclassmethod
    def insert(self, value):
        ...

    @abstractclassmethod
    def pop(self):
        ...


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def pop(self):
        if not self.heap:
            return
        heap = self.heap
        min_value = heap[0]
        self.swap(0, len(heap) - 1)
        heap.pop()
        self._min_heapify(0)
        return min_value

    def _min_heapify(self, index):
        left = self._get_left_index(index)
        right = self._get_right_index(index)

        min_index = index

        heap = self.heap
        heap_size = len(heap)

        if left < heap_size and heap[left] < heap[min_index]:
            min_index = left

        if right < heap_size and heap[right] < heap[min_index]:
            min_index = right

        if min_index != index:
            self.swap(index, min_index)
            self._min_heapify(min_index)

    def insert(self, value):
        self._insert_interatively(value)

    def _insert_recursively(self, value):
        heap = self.heap
        heap.append(value)
        return self.bubble_up(len(self.heap) - 1)

    def _insert_interatively(self, value):
        heap = self.heap
        heap.append(value)
        index = len(heap) - 1
        parent_index = self._get_parent_index(index)

        while index and heap[parent_index] > heap[index]:

            self.swap(index, parent_index)

            index = parent_index
            parent_index = self._get_parent_index(index)

    def bubble_up(self, index):
        if index <= 0:
            return

        parent = self._get_parent_index(index)

        if self.heap[parent] > self.heap[index]:

            self.swap(parent, index)

        self.bubble_up(parent)