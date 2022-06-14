def insertion_sort(a, ini=0, fim=0):
    if fim == 0:
        fim = len(a) - 1
    i = 1 + ini
    while i <= fim:
        for j in range(i, ini, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
        i = i + 1