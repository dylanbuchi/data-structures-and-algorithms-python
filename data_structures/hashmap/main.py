from hashmap import HashMap

hm = HashMap()

hm.insert("one", 1)
hm.insert("two", 2)
hm.remove("two")
print(hm.get_value("one"))

hm.print_items()