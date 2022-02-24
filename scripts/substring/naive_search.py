"""
Naive (Brute Force search) Search
O(N*M)
22FEB22
"""


def naive_search(text, pattern):

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            print("Found the match at index", i)


if __name__ == "__main__":
    text = "this is a test"
    pattern = "test"
    naive_search(text, pattern)
