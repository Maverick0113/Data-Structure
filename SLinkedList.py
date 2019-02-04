class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        if not self.head:
            self.head = Node(x)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(x)

    def extend(self, arr):
        if not self.head:
            self.head = Node(arr[0])
            cur = self.head
            for i in range(1, len(arr)):
                new = Node(arr[i])
                cur.next = new
                cur = cur.next
        cur = self.head
        while cur.next:
            cur = cur.next
        for i in arr:
            new = Node(i)
            cur.next = new
            cur = cur.next

l = SLinkedList()
l.extend([3, 4])
print(l.head.next.val)