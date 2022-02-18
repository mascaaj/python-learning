'''
Inversion of max heap to min heap
16FEB22
'''


class HeapTransformer:

    def __init__(self, heap):
        self.heap = heap

    def transform(self):
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self.fix_down(i)

    def fix_down(self, node_index):
        left_child_index = (2 * node_index) + 1
        right_child_index = (2 * node_index) + 2
        smallest_index = node_index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
            smallest_index = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
            smallest_index = right_child_index

        if smallest_index != node_index:
            self.heap[node_index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[node_index]
            self.fix_down(smallest_index)


if __name__ == "__main__":
    heap = [210, 100, 23, 2, 5]

    ht = HeapTransformer(heap)
    ht.transform()
    print(ht.heap)
