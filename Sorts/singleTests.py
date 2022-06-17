import sys
import time
from random import randint

from BottomUpMergeSort import bottom_up_merge_sort
from HeapSort import heap_sort
from MergeSort import merge_sort
from MergeSortInsertion import merge_sort_insertion
from QuickSort import quick_sort

sys.setrecursionlimit(17500)
i = 100000000
a = [randint(-i,i) for _ in range(i+1)]
b = a.copy()
b.sort()
print('!')
t1 = time.perf_counter()
merge_sort_insertion(a, 10)
t2 = time.perf_counter()
print(t2-t1)
assert (a.__eq__(b))
