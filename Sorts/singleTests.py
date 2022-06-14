import sys
import time
from random import randint

from HeapSort import heap_sort

sys.setrecursionlimit(17500)
i = 1000000
a = [randint(-i,i) for _ in range(i+1)]
b = a.copy()
b.sort()
print('!')
t1 = time.perf_counter()
heap_sort(a)
t2 = time.perf_counter()
print(t2-t1)
assert (a.__eq__(b))
