class Deque:
    # Deque constructor
    def __init__(self):
        self.deque = []

    # appendLeft(x)
    # add [x] to the left side of the deque
    def appendLeft(self, x):
        self.deque = [x] + self.deque

    # appendRight(x)
    # add [x] to the right side of the Deque
    def appendRight(self, x):
        self.deque += [x]

    # extendLeft(iterable)
    # extend the left side of the deque by appending elements from [iterable]
    def extendLeft(self, arr):
        self.deque = arr[::-1] + self.deque

    # extendRight(iterable)
    # extend the right side of the deque by appending elements from [iterable]
    def extendRight(self, arr):
        self.deque += arr

    # index(x)
    # return the zero-based position of the first [x] in the deque
    def index(self, x):
        for i in range(len(self.deque)):
            if self.deque[i] == x:
                return i
        return -1

    # insert(i, x)
    # insert [x] into the deque at position [i]
    def insert(self, i, x):
        # if i is insert at first position
        if i == 0:
            self.deque = [x] + self.deque
            return
        
        # if i is insert at last position
        if i > len(self.deque):
            self.deque += [x]
            return
        
        self.deque = self.deque[:i - 1] + [x] + self.deque[i - 1:]
    
    # count(x)
    # return the number of [x] in deque
    def count(self, x):
        cnt = int(0)
        for i in self.deque:
            if i == x:
                cnt += 1
        return cnt
    
    # popLeft()
    # remove and return an element from the left side of the deque
    def popLeft(self):
        data = self.deque[0]
        self.deque = self.deque[1:]
        return data

    # popRight()
    # remove and return an element from the right side of the deque
    def popRight(self):
        data = self.deque[len(self.deque) - 1]
        self.deque = self.deque[:len(self.deque) - 1]
        return data

    # remove(x)
    # remove the first occurence of [x]
    def remove(self, x):
        for i in range(len(self.deque)):
            if self.deque[i] == x:
                self.deque = self.deque[:i] + self.deque[i + 1:]
                return
        print("Item does not exist")

    # reverse()
    # reverse the elements of the deque in-place
    def reverse(self):
        self.deque = self.deque[::-1]

    # rotate(x)
    # rotate the deque [x] steps to the right
    def rotate(self, x):
        self.deque = self.deque[len(self.deque) - x:] + self.deque[:len(self.deque) - x]
    
    # size()
    # return the size of the deque
    def size(self):
        return len(self.deque)

    # copy()
    # return a shallow copy of the Deque
    def copy(self):
        copy = Deque()
        copy.extendRight(self.deque)
        return copy

    # clear()
    # remove all elements from the deque
    def clear(self):
        self.deque = []

    # print current deque as a list
    def print(self):
        print(self.deque, end = " <- Tail")
        print()

deq = Deque()
print("Current Deque is: Head -> ", end = "")
deq.print()

print("appendLeft -> 45")
deq.appendLeft(45)
print("Current Deque is: Head -> ", end = "")
deq.print()

print("appendRight -> 40")
deq.appendRight(40)
print("Current Deque is: Head -> ", end = "")
deq.print()

print("extendLeft -> [87, 11, 85]")
deq.extendLeft([87, 11, 85])
print("Current Deque is: Head -> ", end = "")
deq.print()

print("extendRight -> [85, 78, 38, 34]")
deq.extendRight([85, 78, 38, 34])
print("Current Deque is: Head -> ", end = "")
deq.print()

print("85 is at position ", end = "")
print(deq.index(85))

print("Insert -> (3, 13)")
deq.insert(3, 13)
print("Current Deque is: Head -> ", end = "")
deq.print()

print("There are ", end = "")
print(deq.count(85), end = "")
print(" 85's in the deque")

print("The popped-left item from deque is ", end = "")
print(deq.popLeft())
print("Current Deque is: Head -> ", end = "")
deq.print()

print("The popped-right item from deque is ", end = "")
print(deq.popRight())
print("Current Deque is: Head -> ", end = "")
deq.print()

print("Remove -> 45")
deq.remove(45)
print("Current Deque is: Head -> ", end = "")
deq.print()

print("Reverse ->")
deq.reverse()
print("Current Deque is: Head -> ", end = "")
deq.print()

print("Rotate -> 3")
deq.rotate(3)
print("Current Deque is: Head -> ", end = "")
deq.print()

print("The size of the Current Deque is ", end = "")
print(deq.size())

print("Copy ->")
copy = deq.copy()
print("Current Deque is: Head -> ", end = "")
deq.print()
print("Copy Deque is: Head -> ", end = "")
copy.print()

print("Clear ->")
deq.clear()
print("Current Deque is: Head -> ", end = "")
deq.print()