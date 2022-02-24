"""
Rabin Karb subsubstring search implementation
O(N*M) <- Worst case scenario
O(M+N) <- Best case scenario

Use Rabin Fingerprint Hash Function
Use Rolling Hash Function across the text
h("bbb") = h("abb") - h("a") + h("b")
22FEB22
"""


class RabinKarp:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        # size of alphabet for fingerprint function
        self.d = 26
        # Prime number for modulo operation
        self.q = 31

    def search(self):
        n = len(self.text)
        m = len(self.pattern)

        hash_text = 0
        hash_pattern = 0
        h = 1

        # Precalculate the largest term in the fingerprint
        for _ in range(m - 1):
            h = (h * self.d) % self.q

        # precalculate the hash of the pattern & text (initial combination only)
        for i in range(m):
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q

        for i in range(n - m + 1):

            # if match, naive search to confirm
            if hash_text == hash_pattern:
                j = 0
                while j < m:
                    if self.text[i + j] != self.pattern[j]:
                        break
                    j += 1

                if j == m:
                    print("Found the match at index", i)

            # rolling hash function, after initial combination
            if i < n - m:
                # h("bbb") = h("abb") - h("a") + h("b")
                # h("a") = ord(a) * 26^2
                # * self.d raises power of remaining bb terms
                # h("b") =  ord(b) % self.q
                hash_text = ((hash_text - ord(self.text[i]) * h) *
                             self.d + ord(self.text[i + m])) % self.q

                if hash_text < 0:
                    hash_text += self.q


if __name__ == "__main__":
    text = "this is a test of a test"
    pattern = "test"
    algorithm = RabinKarp(pattern, text)
    algorithm.search()
