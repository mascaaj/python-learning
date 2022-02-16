'''
Implementation of heaps with arrays
16FEB22
'''

CAPACITY = 10


class Heap:

    def __init__(self):
        self.heap_size = 0
        self.heap = [0] * CAPACITY

    def insert(self, item):
        '''
        base case: heap is full
        else insert and heapify
        '''

        if self.heap_size == CAPACITY:
            print("max heap size reached")
            return

        self.heap[self.heap_size] = item
        self.heapify(self.heap_size, "up")
        self.heap_size += 1

    def heapify(self, node_index, direction="up"):

        if direction == "up":

            parent_index = (node_index - 1) // 2
            if node_index > 0 and self.heap[node_index] > self.heap[parent_index]:
                self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
                self.heapify(parent_index)

        elif direction == "down":

            left_child_index = (2 * node_index) + 1
            right_child_index = (2 * node_index) + 2
            largest_index = node_index

            if left_child_index < self.heap_size and self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index
            elif right_child_index < self.heap_size and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index

            if largest_index != node_index:
                self.heap[node_index], self.heap[largest_index] = self.heap[largest_index], self.heap[node_index]
                self.heapify(largest_index, "down")
        else:
            print("user has to specify direction as up or down")

    # peek function
    def peek(self):
        return self.heap[0]

    def poll(self):
        max_item = self.peek()
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1
        self.heapify(0, "down")
        return max_item

    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


if __name__ == "__main__":
    heap = Heap()

    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    print(heap.heap)
    heap.heap_sort()
