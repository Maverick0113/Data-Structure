class Node:
    # Double Linked List Node constructor
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class DLinkedList:
    # Double Linked List constructor
    def __init__(self):
        self.head = None
        self.tail = None
       
    # appendRight(x)
    # Add an item[x] to the right-end of the Linked List
    def appendRight(self, x):
        new = Node(x)
        # if the Linked List is empty
        if not self.head and not self.tail:
            self.head = new
            self.tail = new
            return

        self.tail.right = new
        new.left = self.tail
        self.tail = new

    # appendLeft(x)
    # Add an item[x] to the left-end of the Linked List
    def appendLeft(self, x):
        new = Node(x)
        # if the Linked List is empty
        if not self.head and not self.tail:
            self.head = new
            self.tail = new
            return

        new.right = self.head
        self.head.left = new
        self.head = new

    # extendRight(iterable)
    # Extend the Linked List by appending-right all the items in the array
    def extendRight(self, arr):
        # if the Linked List is empty
        if not self.head and not self.tail:
            self.head = Node(arr[0])
            cur = self.head
            for i in range(1, len(arr)):
                new = Node(arr[i])
                cur.right = new
                new.left = cur
                cur = cur.right
            self.tail = cur
            return

        cur = self.tail
        for i in range(len(arr)):
            new = Node(arr[i])
            cur.right = new
            new.left = cur
            cur = cur.right
        self.tail = cur

    # extendLeft(iterable)
    # Extend the Linked List by appending-left all the items in the array
    def extendLeft(self, arr):
        # if the Linked List is empty
        if not self.head and not self.tail:
            self.tail = Node(arr[0])
            cur = self.tail
            for i in range(1, len(arr)):
                new = Node(arr[i])
                new.right = cur
                cur.left = new
                cur = cur.left
            self.head = cur
            return

        cur = self.head
        for i in range(len(arr)):
            new = Node(arr[i])
            new.right = cur
            cur.left = new
            cur = cur.left
        self.head = cur

    # insert(i, x)
    # Insert an item[x] at a given position
    def insert(self, i, x):
        new = Node(x)
        # if the position[i] is negative
        if i < 0:
            print("Out of bound index")
            return

        # if inserting at the first position
        if i == 0:
            new.right = self.head
            self.head.left = new
            self.head = new
            return

        index = int(0)
        cur = self.head
        # Continue traversing as long as index is less than
        # position [i - 1] and current node's [right] exist
        while index < i - 1 and cur.right:
            cur = cur.right
            index += 1

        # if inserting at the last position
        if not cur.right:
            new.left = self.tail
            self.tail.right = new
            self.tail = new
            return

        new.right = cur.right
        cur.right.left = new
        cur.right = new
        new.left = cur

    # remove(x)   
    # remove the first item from the list whose value is equal to [x]
    def remove(self, x):
        # if removed item is at first position
        if self.head.val == x:
            self.head = self.head.right
            self.head.left = None
            return

        # if removed item is at last position
        if self.tail.val == x:
            self.tail = self.tail.left
            self.tail.right = None
            return

        cur_head = self.head
        cur_tail = self.tail
        while cur_head and cur_tail:
            if cur_head.val == x:
                print("H")
                cur_head.left.right = cur_head.right
                cur_head.right.left = cur_head.left
                return
            if cur_tail.val == x:
                print("T")
                cur_tail.left.right = cur_tail.right
                cur_tail.right.left = cur_tail.left
                return
            cur_head = cur_head.right
            cur_tail = cur_tail.left
        
        print("Item not found")

    # pop([i])
    # remove the item at the given position in the list, and return it
    # if no index is specified, remove and
    # return the last item in the list
    def pop(self, i):
        # if the position[i] is negative
        if i < 0:
            print("Out of bound index")
            return

        # if the popped item is at first position
        if i == 0:
            data = self.head.val
            self.head = self.head.right
            self.head.left = None
            return data

        cur = self.head
        index = int(0)
        # Continue traversing as long as index is less than
        # position [i] and current node's [right] exist
        while index < i and cur.right:
            cur = cur.right
            index += 1

        # if the removed item is at last position
        if not cur.right:
            data = self.tail.val
            self.tail =  self.tail.left
            self.tail.right = None
            return data

        data = cur.val
        cur.left.right = cur.right
        cur.right.left = cur.left
        return data

    # print current linked list as a list
    def print(self):
        if not self.head or not self.tail:
            print("Empty Linked List")
            return

        cur_head = self.head
        print("Going Right ->")
        while cur_head:
            print(cur_head.val, end = " -> ")
            cur_head = cur_head.right
        print()

        cur_tail = self.tail
        print("Going Left <-")
        while cur_tail:
            print(cur_tail.val, end = " -> ")
            cur_tail = cur_tail.left
        print()

lis = DLinkedList()
print("Current Linked List is: ", end = "")
lis.print()

lis.appendRight(30)
print("Append Right -> 30")
print("Current Linked List is: ")
lis.print()

lis.appendLeft(62)
print("Append Left -> 62")
print("Current Linked List is: ")
lis.print()

lis.extendRight([23, 15, 73, 77, 8, 38, 44])
print("Extend Right -> [23, 15, 73, 77, 8, 38, 44]")
print("Current Linked List is: ")
lis.print()

lis.extendLeft([90, 94, 78])
print("Extend Left -> [90, 94, 78]")
print("Current Linked List is: ")
lis.print()

lis.insert(3, 13)
print("Insert -> 13 at 3")
print("Current Linked List is: ")
lis.print()

lis.remove(8)
print("Remove -> 8")
print("Current Linked List is: ")
lis.print()

lis.pop(15)
print("Pop -> 7")
print("Current Linked List is: ")
lis.print()