import sys
import time
from random import randint

import matplotlib.pyplot as plt

from HeapSort import heap_sort
from MergeSortInsertion import merge_sort_insertion
from QuickSort import quick_sort

sys.setrecursionlimit(17500)

x, ymerge_insertion, yquick,yheap = [], [], [], []
i = 100000
k = 0
while i <= 1000000:
    i += 100000
    k += 1
    arr1 = [randint(-i, i) for _ in range(i)]
    #arr = [i-j for j in range(i)]
    arr2 = arr1.copy()
    arr3 = arr1.copy()
    assert (arr1.__eq__(arr2))
    assert (arr1.__eq__(arr3))

    x.append(i)

    print("Iteração ", k, ":")
    a = time.perf_counter()
    heap_sort(arr3)
    b = time.perf_counter()
    yheap.append(b - a)

    print('H: ', (b - a))

    a = time.perf_counter()
    merge_sort_insertion(arr1, 10)
    b = time.perf_counter()
    ymerge_insertion.append(b-a)
    print('M: ', (b-a))

    a = time.perf_counter()
    quick_sort(arr2, 10)
    b = time.perf_counter()
    yquick.append(b - a)
    print('Q: ', (b-a))

assert (arr2.__eq__(arr1))
assert (arr3.__eq__(arr1))

plt.plot(x, yquick, label="quicksort method")
plt.plot(x, yheap, label="heap sort")
plt.plot(x, ymerge_insertion, label="mergesort with insertion on N=7")



plt.xlabel('tamanho da array')
plt.ylabel('tempo')
plt.title('sorts')
plt.legend()
plt.show()
