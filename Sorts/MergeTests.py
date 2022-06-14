import sys
import time
from random import randint

import matplotlib.pyplot as plt

from BottomUpMergeSort import bottom_up_merge_sort
from MergeSortInsertion import merge_sort_insertion

sys.setrecursionlimit(17500)
x, ybu, y7, y70, y120= [], [], [], [], []
for i in range(1000, 50001, 1000):
    arr1 = [randint(-i, i) for _ in range(i)]
    # print(arr1)
    #arr = [i-j for j in range(i)]
    arr2, arr3, arr4, arr5, arr6 = arr1.copy(), arr1.copy(), arr1.copy(), arr1.copy(), arr1.copy()
    #assert (arr1.__eq__(arr2))
    #assert (arr1.__eq__(arr3))
    #assert (arr1.__eq__(arr4))

    x.append(i)

    a = time.perf_counter()
    bottom_up_merge_sort(arr1)
    b = time.perf_counter()
    ybu.append(b - a)

    a = time.perf_counter()
    merge_sort_insertion(arr2, 7)
    b = time.perf_counter()
    y7.append(b-a)

    a = time.perf_counter()
    merge_sort_insertion(arr3, 70)
    b = time.perf_counter()
    y70.append(b - a)

    # a = time.perf_counter()
    # merge_sort_insertion(arr4, 350)
    # b = time.perf_counter()
    # y350.append(b - a)
    #
    # a = time.perf_counter()
    # merge_sort_insertion(arr5, 700)
    # b = time.perf_counter()
    # y700.append(b - a)

    a = time.perf_counter()
    merge_sort_insertion(arr6, 120)
    b = time.perf_counter()
    y120.append(b - a)

    assert (arr3.__eq__(arr1))
    # if not arr3.__eq__(arr1):
    #     arr5.sort()
    #     print(arr5)
    #     print(arr3)
    #     print(arr1)
    # else:
    #     print('lol')
    #assert (arr1.__eq__(arr3))
    #assert (arr3.__eq__(arr4))

plt.plot(x, ybu, label="merge sort bottom up")
plt.plot(x, y7, label="merge sort cutoff 7")
plt.plot(x, y70, label="merge sort cutoff 70")
plt.plot(x, y120, label="merge sort cutoff 120")
# plt.plot(x, y350, label="merge sort cutoff 350")
# plt.plot(x, y700, label="merge sort cutoff 700")

plt.xlabel('tamanho da array')
# naming the y axis
plt.ylabel('tempo')
# giving a title to my graph
plt.title('merge sorts')
plt.legend()
# function to show the plot
plt.show()
