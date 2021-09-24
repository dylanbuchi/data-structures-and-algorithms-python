from data_structures.trees.binary_search_tree import BinarySearchTree

t = BinarySearchTree()

t.append(5)
t.append(3)
t.append(6)
t.append(2)
t.append(4)
t.append(7)

print(t.pre_order())
print(t.in_order())
print(t.post_order())

print(t.dfs())
print(t.bfs())

print(t.remove(5))
print(t.remove(2))
print(t.bfs())