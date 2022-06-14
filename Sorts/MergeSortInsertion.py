from InsertionSort import insertion_sort

# merge [low:mid] com [mid+1, high]
from Merge import merge

cutoff = 7

def _merge_sort(a, aux, low, high):
    # if less than cutoff elements we use insertion sort
    if high <= low + cutoff:
        insertion_sort(a, low, high)
        return

    mid = (low + high) // 2
    _merge_sort(a, aux, low, mid)
    _merge_sort(a, aux, mid + 1, high)
    merge(a, aux, low, mid, high)


def merge_sort_insertion(a, cut=7):
    global cutoff
    cutoff = cut
    aux = a.copy()
    _merge_sort(a, aux, 0, len(a) - 1)
