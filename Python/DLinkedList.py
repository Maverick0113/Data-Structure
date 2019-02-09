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