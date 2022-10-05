'''
    THREADIND
    - #core = #taskSameTime (low-level)     => parallelism
    - Thread is a set of operations that needs to happen, and each thread is assigned to one core
        - threading => switching some a certain point in one thread to another point in other threads (i.e., one thread is waiting)
            - doesnt involve multiple cores
            - concurrent programming
'''

import threading
import time

ls = []

def count1(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.01)

def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.01)

x = threading.Thread(target=count1, args=(10,))
x.start()

y = threading.Thread(target=count2, args=(10,))
y.start()

# avoid executing later code when thread is still running
x.join()
y.join()

print(ls)