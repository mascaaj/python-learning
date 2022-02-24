"""
Implementations of various sorting algorithms
24FEB22
"""
import random
import time


class Sort():

    def __init__(self, data, ascending=True):
        self.data = data
        self.ascending = ascending
        self.time_elapsed = 0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]


class BogoSort(Sort):

    def __init__(self, data, ascending):
        super().__init__(data, ascending)
        self.count = 0

    def shuffle(self):
        # Fischer Yates Shuffle
        for i in range(len(self.data) - 2, -1, -1):
            j = random.randint(0, i + 1)
            self.swap(i, j)

    def is_sorted(self):
        for i in range(len(self.data) - 1):
            if self.ascending:
                if self.data[i] > self.data[i + 1]:
                    return False
            else:
                if self.data[i] < self.data[i + 1]:
                    return False
        return True

    def sort(self):
        time_start = time.time()
        while not self.is_sorted():
            self.count += 1
            # print("shuffling: iteration # : ", self.count)
            self.shuffle()
        time_stop = time.time()
        self.time_elapsed = time_stop - time_start
        print("Bogo Sort : Data Length : Time Taken : ",
              self.data, " : ", len(self.data), " : ",
              round(self.time_elapsed, 2))


class BubbleSort(Sort):

    def __init__(self, data, ascending):
        super().__init__(data, ascending)

    def sort(self):
        time_start = time.time()
        for i in range(len(self.data) - 1):
            # decrement by i to consider fewer elements
            # at every iteration
            for j in range(len(self.data) - i - 1):
                if self.ascending:
                    if self.data[j] > self.data[j + 1]:
                        self.swap(j, j + 1)
                else:
                    if self.data[j] < self.data[j + 1]:
                        self.swap(j, j + 1)
        time_stop = time.time()
        self.time_elapsed = time_stop - time_start
        if len(self.data) < 20:
            print("Bubble Sort : Data Length : Time Taken : ",
                  self.data, " : ", len(self.data), " : ",
                  round(self.time_elapsed, 2))
        else:
            print("Bubble Sort : Data Length : Time Taken : ",
                  len(self.data), " : ", round(self.time_elapsed, 2))


class SelectionSort(Sort):

    def __init__(self, data, ascending):
        super().__init__(data, ascending)

    def sort(self):
        time_start = time.time()
        for i in range(len(self.data) - 1):
            index = i
            for j in range(i, len(self.data)):
                if self.ascending:
                    # linear search
                    if self.data[j] < self.data[index]:
                        index = j
                else:
                    if self.data[j] > self.data[index]:
                        index = j
                if index != i:
                    self.swap(i, index)
        time_stop = time.time()
        self.time_elapsed = time_stop - time_start
        if len(self.data) < 20:
            print("Selection Sort : Data Length : Time Taken : ",
                  self.data, " : ", len(self.data), " : ",
                  round(self.time_elapsed, 2))
        else:
            print("Selection Sort : Data Length : Time Taken : ",
                  len(self.data), " : ", round(self.time_elapsed, 2))


class InsertionSort(Sort):
    """
    Iterate i and check with j in the reverse direction

    """
    def __init__(self, data, ascending):
        super().__init__(data, ascending)

    def sort(self):
        time_start = time.time()
        for i in range(len(self.data)):
            j = i
            if self.ascending:
                while j > 0 and self.data[j - 1] > self.data[j]:
                    self.swap(j - 1, j)
                    j -= 1
            else:
                while j > 0 and self.data[j - 1] < self.data[j]:
                    self.swap(j - 1, j)
                    j -= 1
        time_stop = time.time()
        self.time_elapsed = time_stop - time_start
        if len(self.data) < 20:
            print("Insertion Sort : Data Length : Time Taken : ",
                  self.data, " : ", len(self.data), " : ",
                  round(self.time_elapsed, 2))
        else:
            print("Insertion Sort : Data Length : Time Taken : ",
                  len(self.data), " : ", round(self.time_elapsed, 2))


class ShellSort(Sort):

    def __init__(self, data, ascending):
        super().__init__(data, ascending)
        self.gap = len(self.data) // 2

    def sort(self):
        time_start = time.time()
        while self.gap > 0:
            for i in range(self.gap, len(self.data)):
                j = i
                if self.ascending:
                    while j >= self.gap and self.data[j - self.gap] > self.data[j]:
                        self.swap(j - self.gap, j)
                        j -= 1
                else:
                    while j >= self.gap and self.data[j - self.gap] < self.data[j]:
                        self.swap(j - self.gap, j)
                        j -= 1
            self.update_gap()
        time_stop = time.time()
        self.time_elapsed = time_stop - time_start
        if len(self.data) < 20:
            print("Shell Sort : Data Length : Time Taken : ",
                  self.data, " : ", len(self.data), " : ",
                  round(self.time_elapsed, 2))
        else:
            print("Shell Sort : Data Length : Time Taken : ",
                  len(self.data), " : ", round(self.time_elapsed, 2))

    def update_gap(self):
        self.gap = self.gap // 2


class QuickSort(Sort):
    def __init__(self, data, ascending):
        super().__init__(data, ascending)

    def sort(self):
        time_start = time.time()
        self.quick_sort(0, len(self.data) - 1)
        time_stop = time.time()
        self.time_elapsed = time_stop - time_start
        if len(self.data) < 20:
            print("Quick Sort : Data Length : Time Taken : ",
                  self.data, " : ", len(self.data), " : ",
                  round(self.time_elapsed, 2))
        else:
            print("Quick Sort : Data Length : Time Taken : ",
                  len(self.data), " : ", round(self.time_elapsed, 2))

    def partition(self, low, high):
        pivot = (low + high) // 2
        self.swap(pivot, high)
        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.swap(low, j)
                low += 1
        self.swap(low, high)
        return low

    def quick_sort(self, low, high):
        if low >= high:
            return
        pivot = self.partition(low, high)
        self.quick_sort(low, pivot - 1)
        self.quick_sort(pivot + 1, high)
