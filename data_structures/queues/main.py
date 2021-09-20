from data_structures.queues.queue import Queue, QueueArray

queue = QueueArray()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(34)
queue.enqueue(25)

print(queue.size)
queue.display()