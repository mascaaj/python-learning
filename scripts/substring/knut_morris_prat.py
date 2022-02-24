"""
Knut Morris Prat Algorithm Implementation
Uses Pi Table and counters
Not efficient with large alphabets
used for dna sequencing
O(N) average case running complexity
O(N+M) in worst case
22FEB22
"""


def construct_pi(pattern):
    pi_table = [0] * len(pattern)
    prefix_counter = 0
    # we ignore first element in table
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prefix_counter]:
            prefix_counter += 1
            pi_table[i] = prefix_counter
            i += 1
        else:
            if prefix_counter != 0:
                prefix_counter = pi_table[prefix_counter - 1]
            else:
                pi_table[i] = 0
                i += 1
    return pi_table


def search(text, pattern):
    """
    case 1 : text[i] = pattern[j] (letter match)
    case 2 : j = len(pattern) (pattern match)
    case 3 : text[i] != pattern[j], still more text to come
    case 3.1 : if j = 0 (at begining of pi table)
    case 3.2 : if j != 0
    """
    pi_table = construct_pi(pattern)
    i = 0  # tracks text
    j = 0  # tracks pattern

    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print("found match at index :", i - j)
            # back tracking
            j = pi_table[j - 1]  # search for more matches
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                # back tracking
                j = pi_table[j - 1]
            else:
                # no more to back track
                # accept defeat
                i += 1


if __name__ == "__main__":
    search("this is a test", "test")
