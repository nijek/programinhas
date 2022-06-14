def merge(a, aux, low, mid, high):
    for i in range(low, high+1):
        aux[i] = a[i]
    m = mid+1
    i = low
    while True:
        if low > mid:
            while m <= high:
                a[i] = aux[m]
                m += 1
                i += 1
            return
        if m > high:
            while low <= mid:
                a[i] = aux[low]
                i += 1
                low += 1
            return

        if aux[low] <= aux[m]:
            a[i] = aux[low]
            low += 1
        else:
            a[i] = aux[m]
            m += 1
        i += 1