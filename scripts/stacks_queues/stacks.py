# LIFO implementation of stack using arrays

class Stack:

    def __init__(self, print=0, verbose=1):
        self.stack = []
        self.print = print
        self.verbose = verbose

    def pop(self):
        if self.is_empty():
            if self.print and self.verbose == 3:
                print("popped :", -1)
            return -1
        else:
            popvar = self.stack[-1]
            del self.stack[-1]
            if self.print and self.verbose == 2:
                print("popped :", popvar)
            return popvar

    def push(self, data):
        self.stack.append(data)
        if self.print and self.verbose == 3:
            print("pushed :", data)

    def peek(self):
        if self.print and self.verbose == 3:
            print("peeked :", self.stack[-1])
        return self.stack[-1]

    def is_empty(self):
        if self.print and self.verbose >= 2:
            print("empty stack :", self.stack == [])
        return self.stack == []

    def size(self):
        if self.print and self.verbose >= 2:
            print("stack size :", len(self.stack))
        return len(self.stack)


class GetMax:

    def __init__(self, print=0, verbose=1):
        self.print = print
        self.verbose = verbose
        self.main_stack = Stack(print=self.print, verbose=self.verbose)
        self.max_stack = Stack(print=self.print, verbose=self.verbose)
        self.min_stack = Stack(print=self.print, verbose=self.verbose)

    def push(self, data):
        """
        cases
        1. First element in the main stack
        2. Not first element in the main stack
        3. Compare , push and else duplicate in max stack
        """

        if self.main_stack.size() < 1:
            self.main_stack.push(data)
            self.max_stack.push(data)
            self.min_stack.push(data)
        else:
            self.main_stack.push(data)
            if data > self.max_stack.peek():
                self.max_stack.push(data)
                self.min_stack.push(self.min_stack.peek())
            elif data < self.min_stack.peek():
                self.min_stack.push(data)
                self.max_stack.push(self.max_stack.peek())
            else:
                self.max_stack.push(self.max_stack.peek())
                self.min_stack.push(self.min_stack.peek())

    def get_max(self):
        if self.print and self.verbose <= 2:
            print("max value : ", self.max_stack.peek())
        return self.max_stack.pop()

    def get_min(self):
        if self.print and self.verbose <= 2:
            print("min value : ", self.min_stack.peek())
        return self.min_stack.pop()


if __name__ == "__main__":
    stack_test = GetMax(print=1, verbose=3)
    stack_test.push(55)
    stack_test.push(18)
    stack_test.push(92)
    stack_test.push(105)
    stack_test.push(9)
    stack_test.push(75)
    stack_test.push(63)
    stack_test.get_max()
    stack_test.get_min()
