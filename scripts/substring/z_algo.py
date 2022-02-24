"""
Z algorithm substring search
O(N+M) Worst case Running time
23FEB22
"""


class ZAlgorithm:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.S = pattern + text
        self.Z = [0 for _ in range(len(self.S))]

    def search(self):
        self.construct_z_table()

        for i in range(1, len(self.Z)):
            if self.Z[i] >= len(self.pattern):
                print("match found at index :", i - len(self.pattern))

    def construct_z_table(self):
        """
        case 1: not within z box k > right
            init n = 0, while letters match, increment
            once match stops, update z value
            create z box, left = k, right = k + n -1
        case 2: k within z box
            case 2.1 : z(p) < r-k+1, copy values
            case 2.2 : z(p) >= r-k+1, naive search
                introduce i term outside of zbox on the right
                check equality with i-k th term
                update l & r
        """
        self.Z[0] = len(self.S)
        left, right = 0, 0
        for k in range(1, len(self.S)):
            if k > right:
                n = 0
                while n + k < len(self.S) and self.S[n] == self.S[n + k]:
                    n += 1
                self.Z[k] = n
                if n > 0:
                    left = k
                    right = k + n - 1
            else:
                p = k - left
                if self.Z[p] < right - k + 1:
                    self.Z[k] = self.Z[p]
                else:
                    i = right + 1
                    while i < len(self.S) and self.S[i] == self.S[i - k]:
                        i = i + 1
                    # when i > len(S) while breaks, update Z
                    # update Z box limits
                    self.Z[k] = i - k
                    left = k
                    right = i - 1
        print(self.Z)


if __name__ == "__main__":
    algo = ZAlgorithm("aab", "baabcaabbcaab")
    algo.search()
