def partition (a, low, high):
    k = a[low]
    i = low
    j = high
    while True:
        while a[i] <= k:
            i += 1
            if i == high:
                break
        while a[j] >= k:
            j -= 1
            if j == low:
                break
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    return j