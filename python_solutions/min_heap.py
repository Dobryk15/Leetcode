import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*self.maxsize
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 0 # there are also implementations where it is equal to 1

    def parent(self, pos):
        return (pos-1) // 2

    def leftChild(self, pos):
        return (2 * pos) + 1

    def rightChild(self, pos):
        return (2 * pos) + 2

    def isLeaf(self, pos):
        return pos*2 + 1 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
            self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    if (self.rightChild(pos) < self.size): # to avoid the case of propagating right-tail 0's into the tree
                        self.swap(pos, self.rightChild(pos))
                        self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.Heap[self.size] = element
        current = self.size
        
        self.size += 1
        
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print_heap(self):
        for i in range((self.size//2)):
            print(" PARENT: " + str(self.Heap[i])+" left_child: "+
                                 str(self.Heap[2 * i + 1])+" right_child: "+
                                 str(self.Heap[2 * i + 2]))

    def minHeap(self):
        for pos in range(self.size//2 - 1, -1, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped

if __name__ == "__main__":
	# Test
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(4)
    minHeap.insert(10)
    minHeap.insert(1)
    minHeap.insert(19)
    minHeap.insert(20)
    minHeap.insert(13)
    minHeap.insert(7)
    minHeap.insert(17)
    minHeap.insert(18)
    minHeap.insert(2)

    print(minHeap.Heap)
    
    minHeap.minHeap()
    print(minHeap.Heap)
    print(minHeap.size)

    print('--- The minHeap ---')
    minHeap.print_heap()
    print("The min value in the heap: " + str(minHeap.remove()))

