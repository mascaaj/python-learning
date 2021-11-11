# FIFO implementation of queue using arrays

class Queue:

    def __init__(self, print=0, verbose=1):
        self.queue = []
        self.verbose = verbose
        self.print = print

    def dequeue(self):
        if self.is_empty():
            if self.print and self.verbose == 3:
                return print("dequeued :", -1)
            else:
                return -1
        else:
            deq_var = self.queue[0]
            del self.queue[0]
            if self.print and self.verbose == 3:
                return print("dequeued :", deq_var)
            else:
                return deq_var

    def enqueue(self, data):
        self.queue.append(data)
        if self.print and self.verbose == 3:
            print("enqueued :", data)

    def peek(self):
        if self.print and self.verbose < 3:
            print("peeked :", self.queue[0])
        return self.queue[0]

    def is_empty(self):
        if self.print and self.verbose >= 2:
            print("empty queue :", self.queue == [])
        return self.queue == []

    def size(self):
        if self.print and self.verbose == 1:
            return print("queue size :", len(self.queue))
        else:
            return len(self.queue)


if __name__ == "__main__":
    queue_test = Queue(print=0)
    queue_test.enqueue(1)
    queue_test.enqueue(2)
    queue_test.enqueue(3)
    queue_test.enqueue(4)
    queue_test.size()
    queue_test.dequeue()
    queue_test.size()
    queue_test.peek()
    queue_test.dequeue()
    queue_test.size()
    queue_test.is_empty()
    queue_test.dequeue()
    queue_test.dequeue()
    queue_test.is_empty()
    queue_test.dequeue()
