class Node:
    # Single Linked List Node constructor
    def __init__(self, data):
        self.val = data
        self.next = None

class SLinkedList:
    # Single Linked List constructor
    def __init__(self):
        self.head = None

    # append(x)
    # Add an item[x] to the end of the Linked List
    def append(self, x):
        # if the Linked List is empty
        if not self.head:
            self.head = Node(x)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(x)
    
    # extend(iterable)
    # Extend the Linked List by appending all the items in the array
    def extend(self, arr):
        # if the Linked List is empty
        if not self.head:
            self.head = Node(arr[0])
            cur = self.head
            for i in range(1, len(arr)):
                new = Node(arr[i])
                cur.next = new
                cur = cur.next
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        for i in arr:
            new = Node(i)
            cur.next = new
            cur = cur.next

    # insert(i, x)
    # Insert an item[x] at a given position
    def insert(self, i, x):
        new = Node(x)
        # if the position [i] is negative
        if i < 0:
            print("Out of bound index")
            return

        # if inserting at the first position
        if i == 0:
            new.next = self.head
            return

        index = int(0)
        cur = self.head
        # Continue traversing as long as index is less than
        # position [i - 1] and current node's [next] exist
        while index < i - 1 and cur.next:
            cur = cur.next
            index += 1

        # if the inserting at the last position
        if not cur.next:
            cur.next = new
            return

        new.next = cur.next.next
        cur.next = new

    # remove(x)   
    # remove the first item from the list whose value is equal to [x]
    def remove(self, x):
        # if the removed item is at first position
        if self.head.val == x:
            self.head = self.head.next
            return

        cur = self.head
        prev = None
        found = False
        while cur:
            if cur.val == x:
                found = True
                break
            prev = cur
            cur = cur.next

        # if item does not exist in Linked List
        if not found:
            print("Item not found")
            return

        # if the removed item is at last position
        if not cur.next:
            prev.next = None
            return

        prev.next = cur.next

    # pop([i])
    # remove the item at the given position in the list, and return it
    # if no index is specified, remove and
    # return the last item in the list
    def pop(self, i):

        # if the position [i] is negative
        if i < 0:
            print("Out of bound index")
            return

        # if the popped item is at first position
        if i == 0:
            self.head= self.head.next
            return self.head.val

        cur = self.head
        prev = None
        index = int(0)
        # Continue traversing as long as index is less than
        # position [i] and current node's [next] exist
        while index < i and cur.next:
            prev = cur
            cur = cur.next
            index += 1

        # if the removed item is at last position
        if not cur.next:
            prev.next = None
            return cur.val

        prev.next = cur.next
        return cur.val

    # clear()
    # remove all items from the list
    def clear(self):
        self.head = None

    # index(x)
    # return zero-based index in the list of the first item
    # whose value is equal to [x]
    def index(self, x):
        i = int(0)
        cur = self.head
        while cur:
            if cur.val == x:
                return i
            i += 1
            cur = cur.next
        return -1

    # count(x)
    # return the number of times [x] appears in the list
    def count(self, x):
        cnt = int(0)
        cur = self.head
        while cur:
            if cur.val == x:
                cnt += 1
            cur = cur.next
        return cnt

    # sort(reverse = False)
    # sort the items of the list in place
    def sort(self, flag):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr.sort(reverse = not flag)

        self.head = Node(arr[0])
        cur = self.head
        for i in range(1, len(arr)):
            cur.next = Node(arr[i])
            cur = cur.next

    # reverse()
    # reverse the elements of the list in place
    def reverse(self):
        cur = self.head
        prev = None
        nex = cur.next
        while nex:
            cur.next = prev
            prev = cur
            cur = nex
            nex = nex.next
        cur.next = prev
        self.head = cur
    
    # copy()
    # return a shallow copy of the list
    def copy(self):
        if not self.head:
            return None
        new = SLinkedList()
        cur = self.head
        while cur:
            new.append(cur.val)
            cur = cur.next
        return new

    # print current linked list as a list
    def print(self):
        if not self.head:
            print("Empty Linked List")
            return

        cur = self.head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
        

l = SLinkedList()
l.extend([2, 3, 1])
l.sort(True)
l.print()
