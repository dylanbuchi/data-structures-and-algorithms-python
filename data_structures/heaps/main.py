from heap import MinHeap

min_heap = MinHeap()

min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(5)
min_heap.insert(30)
min_heap.insert(20)

min_heap.insert(3)
print(min_heap.heap)

pop_item = min_heap.pop()

print(min_heap.heap, pop_item)
pop_item = min_heap.pop()

print(min_heap.heap, pop_item)
