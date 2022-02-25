"""
Testing sorting algortithm implementations
24FEB22
"""

import random
import sys
sys.path.append(".")
from sorting import BogoSort, BubbleSort, SelectionSort, InsertionSort
from sorting import ShellSort, QuickSort, MergeSort


def input_data(count):
    return [random.randint(-count * 10, count * 10) for i in range(count)]


def test_bogo_sort(input, asc=True):
    algorithm = BogoSort(input, asc)
    algorithm.sort()


def test_bubble_sort(input, asc=True):
    algorithm = BubbleSort(input, asc)
    algorithm.sort()


def test_selection_sort(input, asc=True):
    algorithm = SelectionSort(input, asc)
    algorithm.sort()


def test_insertion_sort(input, asc=True):
    algorithm = InsertionSort(input, asc)
    algorithm.sort()


def test_shell_sort(input, asc=True):
    algorithm = ShellSort(input, asc)
    algorithm.sort()


def test_quick_sort(input, asc=True):
    algorithm = QuickSort(input, asc)
    algorithm.sort()


def test_merge_sort(input, asc=True):
    algorithm = MergeSort(input, asc)
    algorithm.sort()


if __name__ == "__main__":

    test_bogo_sort(input_data(10))

    test_bubble_sort(input_data(100))
    test_bubble_sort(input_data(1000))
    test_bubble_sort(input_data(10000))
    # test_bubble_sort(input_data(100000))

    test_selection_sort(input_data(100))
    test_selection_sort(input_data(1000))
    test_selection_sort(input_data(10000))
    test_selection_sort(input_data(100000))

    test_insertion_sort(input_data(100))
    test_insertion_sort(input_data(1000))
    test_insertion_sort(input_data(10000))
    test_insertion_sort(input_data(100000))

    test_shell_sort(input_data(100))
    test_shell_sort(input_data(1000))
    test_shell_sort(input_data(10000))
    test_shell_sort(input_data(100000))

    test_quick_sort(input_data(100))
    test_quick_sort(input_data(1000))
    test_quick_sort(input_data(10000))
    test_quick_sort(input_data(100000))

    test_merge_sort(input_data(100))
    test_merge_sort(input_data(1000))
    test_merge_sort(input_data(10000))
    test_merge_sort(input_data(100000))
