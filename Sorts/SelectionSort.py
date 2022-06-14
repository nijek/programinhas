
def selection_sort(a):
    i = 0
    n = len(a)-1
    while i <= n:
        smallest = n
        for j in range(n, i-1, -1):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
        i += 1