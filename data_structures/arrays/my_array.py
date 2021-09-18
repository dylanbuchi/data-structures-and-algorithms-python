class Array:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__array = [None] * capacity
        self.__count = 0

    def __index_is_out_of_bounds(self, index):
        if index < 0 or index >= self.__count:
            print("Index out of bounds")
            return True
        return False

    def reverse(self):
        end = self.__count - 1

        for start in range(self.__count // 2):
            self.__array[start], self.__array[end] = self.__array[
                end], self.__array[start]
            end -= 1
        return True

    def insert_at(self, index, value):
        if self.__is_empty() or index < 0:
            return False
        if index >= self.__count:
            return self.append(value)

        self.append(0)

        for i in range(self.__count - 1, index, -1):
            self.__array[i] = self.__array[i - 1]

        self.__array[index] = value

        return True

    def index(self, index):
        if self.__is_empty() or self.__index_is_out_of_bounds(index):
            return False
        return self.__array[index]

    def pop(self):
        if self.__is_empty():
            return False

        self.__count -= 1
        return True

    def remove_at(self, index):
        if self.__is_empty() or self.__index_is_out_of_bounds(index):
            return False
        if index == self.__count - 1:
            return self.pop()

        for i in range(index, self.__count):
            if i + 1 < self.__count:
                self.__array[i] = self.__array[i + 1]

        self.__count -= 1
        return True

    def append(self, value):
        if self.__is_full():
            self.__resize()

        self.__array[self.__count] = value
        self.__count += 1
        return True

    def size(self):
        return self.__count

    def __is_full(self):
        return self.__count == self.__capacity

    def __is_empty(self):
        return not self.__count

    def display(self):
        if self.__is_empty():
            print("[]")

        for i in range(self.__count):
            print('[' if i == 0 else '', end='')
            print(f"{self.__array[i]}, "
                  if i != self.__count - 1 else self.__array[i],
                  end='' if i != self.__count - 1 else ']\n')

    def __resize(self):
        self.__capacity *= 2
        temp = [None] * self.__capacity
        for i in range(self.__count):
            temp[i] = self.__array[i]
        self.__array = temp

        return True
