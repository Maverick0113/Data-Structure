class Heap:
    # Heap constructor
    def __init__(self):
        self.heap = []
    
    # return a specified node parent node
    def parent(self, i):
        if i == 0:
            return 0
        return (i - 1) // 2
    
    # return a specified node left node
    def left(self, i):
        return (2 * i) + 1
    
    # return a specified node right node
    def right(self, i):
        return (2 * i) + 2
    
    # heappush(x)
    # push the value [x] onto the heap, maintaining the heap invariant
    def heappush(self, x):
        # if heap is empty
        if len(self.heap) == 0:
            self.heap.append(x)
            return
        
        self.heap.append(x)
        cur = len(self.heap) - 1
        par = self.parent(cur)
        while self.heap[cur] > self.heap[par]:
            self.heap[cur], self.heap[par] = self.heap[par], self.heap[cur]
            cur = par
            par = self.parent(cur)
    
    # heappop()
    # pop and return the greatest item from the heap
    def heappop(self):
        # if heap is empty
        if len(self.heap) == 0:
            return
        # if heap has only one item
        if len(self.heap) == 1:
            data = self.heap[0]
            self.heap = []
            return data
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap[-1]
        self.heap = self.heap[:-1]
        cur = int(0)
        while cur < len(self.heap):
            l = self.left(cur)
            r = self.right(cur)
            if l > len(self.heap) - 1 or r > len(self.heap) - 1:
                break
            if self.heap[cur] > self.heap[l] and self.heap[cur] > self.heap[r]:
                break

            if self.heap[cur] < self.heap[l] and self.heap[cur] < self.heap[r]:
                if self.heap[l] > self.heap[r]:
                    self.heap[cur], self.heap[l] = self.heap[l], self.heap[cur]
                    cur = l
                else:
                    self.heap[cur], self.heap[r] = self.heap[r], self.heap[cur]
                    cur = r
            elif self.heap[cur] < self.heap[l]:
                self.heap[cur], self.heap[l] = self.heap[l], self.heap[cur]
                cur = l
            else:
                self.heap[cur], self.heap[r] = self.heap[r], self.heap[cur]
                cur = r
        return data
    
    # heapreplace(x)
    # pop and return max item
    # push [x] on the heap, efficiently
    def heapreplace(self, x):
        # if heap is empty
        if len(self.heap) == 0:
            return
        # if heap has only one item
        if len(self.heap) == 1:
            data = self.heap[0]
            self.heap = []
            return data
        
        data = self.heap[0]
        self.heap[0] = x
        cur = int(0)
        while cur < len(self.heap):
            l = self.left(cur)
            r = self.right(cur)
            if l > len(self.heap) - 1 or r > len(self.heap) - 1:
                break
            if self.heap[cur] > self.heap[l] and self.heap[cur] > self.heap[r]:
                break

            if self.heap[cur] < self.heap[l] and self.heap[cur] < self.heap[r]:
                if self.heap[l] > self.heap[r]:
                    self.heap[cur], self.heap[l] = self.heap[l], self.heap[cur]
                    cur = l
                else:
                    self.heap[cur], self.heap[r] = self.heap[r], self.heap[cur]
                    cur = r
            elif self.heap[cur] < self.heap[l]:
                self.heap[cur], self.heap[l] = self.heap[l], self.heap[cur]
                cur = l
            else:
                self.heap[cur], self.heap[r] = self.heap[r], self.heap[cur]
                cur = r
        return data


    # print current heap as a list
    def print(self):
        if len(self.heap) == 0:
            print("Empty Heap")
            return
        
        print("Root -> ", end = "")
        print(self.heap)


hp = Heap()
print("Current Heap: ", end = "")
hp.print()

print("Heappush -> 39")
print("Heappush -> 100")
print("Heappush -> 78")
print("Heappush -> 70")
print("Heappush -> 33")
print("Heappush -> 35")
print("Heappush -> 54")
print("Heappush -> 13")
print("Heappush -> 59")
hp.heappush(39)
hp.heappush(100)
hp.heappush(78)
hp.heappush(70)
hp.heappush(33)
hp.heappush(35)
hp.heappush(54)
hp.heappush(13)
hp.heappush(59)
print("Current Heap: ", end = "")
hp.print()

print("Heappop ->")
print("The greatest item is ", end = "")
print(hp.heappop())
print("Current Heap: ", end = "")
hp.print()

print("Heapreplace -> 43")
print("The greatest item is ", end = "")
print(hp.heapreplace(43))
print("Current Heap: ", end = "")
hp.print()
