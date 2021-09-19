from my_array import Array

array = Array(capacity=10)

array.display()
for i in range(1, 10):
    array.append(i)
array.display()

array.reverse()
array.display()
array.remove_at(3)
array.display()
array.pop()
array.display()

print("index 0:", array.index(0))

print('size:', array.size())
