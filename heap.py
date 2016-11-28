class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def insert(self, x):
        self.heaplist.append(x)
        self.size += 1
        self.bubble_up(self.size)

    def swap(self, i, j):
        tmp = self.heaplist[j]
        self.heaplist[j] = self.heaplist[i]
        self.heaplist[i] = tmp

    def bubble_up(self, i):
        while i // 2 > 0:
            # item at position i on the list is smaller than the item
            # at i // 2 (the parent of i). This violates the heap structure,
            # need to bubble up
            if self.heaplist[i] < self.heaplist[i // 2]:
                # Perform the swap
                self.swap(i, i // 2)
            i = i // 2

    def trickle_down(self, i):
        while (i * 2) <= self.size:
            minchild_idx = self.min_child(i)
            if self.heaplist[i] > self.heaplist[minchild_idx]:
                print(self.heaplist)
                self.swap(i, minchild_idx)
            i = minchild_idx

    def min_child(self, i):
        right = i * 2 + 1
        left = i * 2
        if right > self.size:
            return left
        if self.heaplist[left] < self.heaplist[right]:
            return left
        else:
            return right

    def build_heap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heaplist = [0] + alist
        while (i > 0):
            self.trickle_down(i)
            i = i - 1

def main():
    alist = [9, 7, 5, 3, 22, 4]
    h = BinaryHeap()
    print(alist)
    h.build_heap(alist)
    print(h.heaplist)

if __name__ == "__main__":
    main()
