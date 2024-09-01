class DynamicArray:
    def __init__(self):
        self.array = []
        self.capacity = 1
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array.append(item)
        self.size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return str(self.array[:self.size])

# Example usage
dynamic_array = DynamicArray()
dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)
print(dynamic_array)  # Output: [10, 20, 30]
