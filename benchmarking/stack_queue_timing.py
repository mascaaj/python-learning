import sys
import time
sys.path.append("../scripts/stacks_queues")
from queues import Queue
from queues_with_stacks import QueueTwoStacks, QueueOneStack
from stacks import Stack


if __name__ == "__main__":

    max_size = 500000

    st_test = Stack(print=1, verbose=1)
    qu_test = Queue(print=1, verbose=1)
    qu2s_test = QueueTwoStacks(print=1, verbose=1)
    qu1s_test = QueueOneStack(print=1, verbose=1)

    time_start = time.time()
    for i in range(max_size):
        st_test.push(i)
    time_stop = time.time()
    # st_test.size()
    delta_time = time_stop - time_start
    print("Delta time for stack push :", delta_time)

    time_start = time.time()
    for i in range(max_size):
        st_test.pop()
    time_stop = time.time()
    # st_test.size()
    delta_time = time_stop - time_start
    print("Delta time for stack pop :", delta_time)

    time_start = time.time()
    for i in range(max_size):
        qu_test.enqueue(i)
    time_stop = time.time()
    # qu_test.size()
    delta_time = time_stop - time_start
    print("Delta time for queue enqueue :", delta_time)

    time_start = time.time()
    for i in range(max_size):
        qu_test.dequeue()
    time_stop = time.time()
    # qu_test.size()
    delta_time = time_stop - time_start
    print("Delta time for queue dequeue :", delta_time)

    time_start = time.time()
    for i in range(max_size):
        qu2s_test.enqueue(i)
    time_stop = time.time()
    # qu2s_test.size()
    delta_time = time_stop - time_start
    print("Delta time for 2 stack queue enqueue :", delta_time)

    time_start = time.time()
    for i in range(max_size):
        qu2s_test.dequeue()
    time_stop = time.time()
    # qu2s_test.size()
    delta_time = time_stop - time_start
    print("Delta time for 2 stack queue dequeue :", delta_time)

    time_start = time.time()
    for i in range(max_size):
        qu1s_test.enqueue(i)
    time_stop = time.time()
    # qu1s_test.size()
    delta_time = time_stop - time_start
    print("Delta time for 1 stack queue enqueue :", delta_time)

    # time_start = time.time()
    # for i in range(max_size):
    #     qu1s_test.dequeue()
    # time_stop = time.time()
    # # qu1s_test.size()
    # delta_time = time_stop - time_start
    # print("Delta time for 1 stack queue dequeue :", delta_time)
