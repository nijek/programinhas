from Merge import merge


def _merge_sort(a, aux, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    _merge_sort(a, aux, low, mid)
    _merge_sort(a,aux, mid + 1, high)
    merge(a, aux, low, mid, high)

def merge_sort(a):
    aux = a.copy()
    _merge_sort(a, aux, 0, len(a) - 1)







