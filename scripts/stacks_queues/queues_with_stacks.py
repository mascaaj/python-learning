# FIFO implementation of queue using stacks
import sys
sys.path.append(".")
from stacks import Stack


# Two stack method, no recursion
class QueueTwoStacks:

    def __init__(self, print=0, verbose=1):
        self.print = print
        self.verbose = verbose
        self.enqueue_stack = Stack(print=self.print, verbose=self.verbose)
        self.dequeue_stack = Stack(print=self.print, verbose=self.verbose)

    def dequeue(self):
        '''
        cases:
        0. check if dequeue stack is empty
            if empty
                1. check size of enqueue stack, if 1, pop return answer
                2. if not 1, pop till one, push into dequeue stack
            else
                3. pop from dequeue stack
        '''
        if self.dequeue_stack.is_empty():
            while self.enqueue_stack.size() > 1:
                self.dequeue_stack.push(self.enqueue_stack.pop())
            popvar = self.enqueue_stack.pop()
        else:
            popvar = self.dequeue_stack.pop()
        if self.print and self.verbose == 3:
            print("dequeued : ", popvar)
        return popvar

    def enqueue(self, data):
        self.enqueue_stack.push(data)
        if self.print and self.verbose == 3:
            print("enqueued :", data)

    def is_empty(self):
        if self.print and self.verbose <= 3:
            print("empty queue :", self.enqueue_stack == [] and self.dequeue_stack == [])
        return self.enqueue_stack == [] and self.dequeue_stack == []

    def size(self):
        if self.print:
            return print("queue size :", self.enqueue_stack.size() + self.dequeue_stack.size())
        else:
            return self.enqueue_stack.size() + self.dequeue_stack.size()


# One stack and recursion
class QueueOneStack:

    def __init__(self, print=0, verbose=1):
        self.print = print
        self.verbose = verbose
        self.stack = Stack(print=self.print, verbose=self.verbose)

    def dequeue(self):
        '''
        cases:
        0. check if dequeue stack is empty
            if empty
                1. check size of enqueue stack, if 1, pop return answer
                2. if not 1, pop till one, push into dequeue stack
            else
                3. pop from dequeue stack
        '''
        if self.stack.size() == 1:
            if self.print and self.verbose == 3:
                return print("dequeue item : ", self.stack.pop())
            else:
                return self.stack.pop()
        elif self.stack.is_empty():
            if self.print and self.verbose == 3:
                print("dequeue item : ", -1)
            return -1
        item = self.stack.pop()
        self.dequeue()
        self.stack.push(item)

    def enqueue(self, data):
        self.stack.push(data)
        if self.print and self.verbose == 3:
            print("enqueued :", data)

    # def is_empty(self):
    #     if self.print and self.verbose <= 3:
    #         print("empty queue :", self.enqueue_stack == [] and self.dequeue_stack == [])
    #     return self.enqueue_stack == [] and self.dequeue_stack == []

    def size(self):
        if self.print and self.verbose == 1:
            return print("queue size :", self.stack.size())
        else:
            return self.stack.size()


if __name__ == "__main__":
    queue_test = QueueOneStack(print=1, verbose=1)
    queue_test.enqueue(11)
    queue_test.enqueue(21)
    queue_test.enqueue(31)
    queue_test.enqueue(41)
    queue_test.enqueue(51)
    queue_test.enqueue(61)
    print("expect 11")
    queue_test.dequeue()
    print("expect 21")
    queue_test.dequeue()
    queue_test.enqueue(71)
    print("expect 31")
    queue_test.dequeue()
    print("expect 41")
    queue_test.dequeue()
    print("expect 51")
    queue_test.dequeue()
    print("expect 2")
    queue_test.size()
    print("expect 61")
    queue_test.dequeue()
    print("expect 71")
    queue_test.dequeue()
    print("expect -1")
    queue_test.dequeue()
