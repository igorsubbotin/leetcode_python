# Min Stack - https://leetcode.com/problems/min-stack/
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        self.stackToHeap = {}
        self.heapToStack = {}
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.heap.append(x)
        ix = len(self.heap) - 1
        self.stackToHeap[ix] = ix
        self.heapToStack[ix] = ix
        pix = self.getParentIndex(ix)
        while self.heap[ix] < self.heap[pix]:
            self.exchangeHeap(ix, pix)
            ix = pix
            pix = self.getParentIndex(ix)
        
    def pop(self):
        """
        :rtype: void
        """
        last_ix = len(self.stack) - 1
        ix = self.stackToHeap[last_ix]
        self.exchangeHeap(ix, last_ix)
        del self.stackToHeap[last_ix]
        del self.heapToStack[last_ix]
        self.heap.pop()
        item = self.stack.pop()
        if ix == last_ix:
            return item
        nix = None
        while nix != ix:
            nix = self.getMinValueIndex(ix)
            self.exchangeHeap(nix, ix)
            ix = nix
        return item
    
    def getMinValueIndex(self, pix):
        ix = pix
        v = self.heap[pix]
        lix = 2 * pix + 1
        lv = self.tryGetHeapValue(lix)
        if lv is not None and lv < v:
            v = lv
            ix = lix
        rix = 2 * pix + 2
        rv = self.tryGetHeapValue(rix)
        if rv is not None and rv < v:
            return rix
        return ix
    
    def tryGetHeapValue(self, ix):
        if ix >= len(self.heap):
            return None
        return self.heap[ix]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.heap[0]
        
    def exchangeHeap(self, i, j):
        self.exchange(self.heapToStack, i, j)
        self.exchange(self.heap, i, j)
        self.exchange(self.stackToHeap, self.heapToStack[i], self.heapToStack[j])
        
    def exchange(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t
        
    def getParentIndex(self, i):
        if i == 0:
            return 0
        return (i - 1) / 2