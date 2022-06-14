def shellSort(a):
    n = len(a)
    k = n//2
    print(a)
    while k >= 1:
        print(k)
        for i in range(0, n-k):
            if a[i] > a[i+k]:
                a[i], a[i+k] = a[i+k], a[i]
        print(a)
        k //= 2



arr = [33,31,40,8,12,17,25,42]

shellSort(arr)
print(arr)

# This code is contributed by Mohit Kumra
