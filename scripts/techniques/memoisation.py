# Factorial of number using memoisation

# last recent used cache
from functools import lru_cache


@lru_cache(maxsize=1000)
def factorial(input):
    if input < 2:
        return 1
    else:
        return input * factorial(input - 1)


def factorial_memo(input, factorial_dictionary):
    if input < 2:
        return 1
    elif input not in factorial_dictionary:
        factorial_dictionary[input] = input * factorial_memo(input - 1, factorial_dictionary)
    return factorial_dictionary[input]


if __name__ == "__main__":
    memo = 0
    factorial_dict = {}

    if memo == 0:
        # Results in a max recusion reached error
        for i in range(1, 5000):
            print(str(i) + "! = ", factorial(i))
    elif memo == 1:
        for i in range(1, 5000):
            print(str(i) + "! = ", factorial_memo(i, factorial_dict))
