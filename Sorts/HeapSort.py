
class Heap:
    def __init__(self, max = 15):
        self.max = max
        self.n = 1
        self.pq = [None] * (self.max + 1)

    def insert(self, value):
        self.pq[self.n] = value
        self.swim(self.n)
        self.n += 1
        if self.n >= self.max // 2:
            self.duplicate()


    def duplicate(self):
        self.max *= 2
        self.pq += [None] * (self.max + 1)

    def delMax(self):
        if self.n <= 1:
            print("Sem elementos")
            return None
        else:
            max = self.pq[1]
            self.n -= 1
            self.pq[1] = self.pq[self.n]
            self.sink(1)
            self.pq[self.n+1] = None
            return max;

    def size(self):
        return self.n - 1
    def swim(self, indx):
        while indx > 1 and self.pq[indx] > self.pq[indx // 2]:
            self.swap(indx, indx//2)
            indx //= 2

    def sink(self, indx):
        while 2*indx <= self.n:
            j = 2 * indx
            if j < self.n and self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[indx] < self.pq[j]:
                self.swap(indx, j)
                indx = j
            else:
                return;

    def swap(self, indx1, indx2):
        self.pq[indx1], self.pq[indx2] = self.pq[indx2], self.pq[indx1]

def heap_sort(a):
    heap = Heap(len(a))
    for el in a:
        heap.insert(el)
    for i in range(len(a), 0, -1):
        a[i - 1] = heap.delMax()
