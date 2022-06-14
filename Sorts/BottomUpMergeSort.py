from Merge import merge


def bottom_up_merge_sort(a):
    N = len(a)
    j = 1
    aux=a.copy()
    while j < N:
        for low in range(0, N - j, 2*j):
            merge(a, aux, low, low + j - 1, min(low + 2*j - 1, N-1))
        j += j
