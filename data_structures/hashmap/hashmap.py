class HashMap():
    def __init__(self) -> None:
        self.capacity = 100
        self.bucket = [None] * self.capacity
        self.size = 0

    def calculate_hash(self, value):
        first_char_code = ord(str(value)[0])
        return (len(str(value)) * 2 * first_char_code) % self.capacity

    def insert(self, key, data):
        index = self.calculate_hash(key)
        bucket_list = self.bucket[index]

        if bucket_list is None:
            self.bucket[index] = []
            bucket_list = self.bucket[index]
            bucket_list.append([key, data])
        else:
            if len(bucket_list) == 1:
                stored_key, _ = bucket_list[0]
            if key == stored_key:
                bucket_list[0][1] = data
            else:
                bucket_list.append([key, data])

        self.size += 1

    def remove(self, key):
        if not self.bucket:
            return

        index = self.calculate_hash(key)
        bucket_list = self.bucket[index]

        if not bucket_list:
            return

        if len(bucket_list) == 1:
            bucket_list.clear()

        else:
            delete_index = None

            for i, key_data_tuple in enumerate(bucket_list):
                stored_key, _ = key_data_tuple
                if key == stored_key:
                    delete_index = i
                    break
            if delete_index:
                bucket_list.pop(delete_index)

        self.size -= 1

    def print_items(self):
        for item in self.bucket:
            if item:
                if len(item) == 1:
                    key, value = item[0]
                    print(f"{key}, {value}")
                else:
                    for t in item:
                        k, v = t
                        print(k, v)

    def get_value(self, key):
        index = self.calculate_hash(key)
        item = self.bucket[index]
        if item is None:
            return

        if len(item) == 1:
            return item[0][1]

        for lst in item:
            stored_key, stored_value = lst
            if stored_key == key:
                return stored_value
