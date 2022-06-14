from random import shuffle

from InsertionSort import insertion_sort
from partition import partition


def median(a, i, j, k):
    l = [[a[i], i], [a[j], j], [a[k], k]]
    l.sort()
    return l[1][1]



def quick_sort(a, cutoff = 0):
    shuffle(a)
    if cutoff == 0:
        _quick_sort(a, 0, len(a) - 1)
    else:
        _quick_sort_insertion(a, 0, len(a)-1, cutoff)

def _quick_sort(a, low, high):
    if high <= low:
        return
    midElement = median(a, low, (low + high) // 2, high)
    a[low], a[midElement] = a[midElement], a[low]
    mid = partition(a, low, high) #o item no lugar certo
    _quick_sort(a, low, mid-1)
    _quick_sort(a, mid+1, high)

def _quick_sort_insertion(a, low, high, cutoff):
    if high <= low + cutoff-1:
        insertion_sort(a, low, high)
        return
    midElement = median(a, low, (low + high) // 2, high)
    a[low], a[midElement] = a[midElement], a[low]
    mid = partition(a, low, high)  # o item no lugar certo
    _quick_sort(a, low, mid - 1)
    _quick_sort(a, mid + 1, high)

