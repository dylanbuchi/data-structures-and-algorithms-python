from data_structures.linkedlists.linkedlist import LinkedList

nums = LinkedList()

nums.insert_at_index(0, 45)
nums.insert_at_index(1, 4546)
nums.insert_at_index(1, 4)
nums.display()

nums.delete_at_index(1)
nums.delete_at_index(1)

print(nums.size)
print(nums.tail.value)
print(nums.head.value)
nums.display()