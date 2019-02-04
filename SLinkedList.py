class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    # Add an item to the end of the Linked List
    def append(self, x):
        # if the Linked List is empty
        if not self.head:
            self.head = Node(x)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(x)

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

    # Insert an item at a given position
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

l = SLinkedList()
l.extend([3, 4])
l.insert(4, 5)
print(l.head.next.next.val)