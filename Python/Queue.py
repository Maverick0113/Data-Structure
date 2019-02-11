class Queue:
    # Queue constructor
    def __init__(self):
        self.queue = []
        self.size = int(0)

    # size()
    # return size of the queue
    def size(self):
        return self.size

    # empty()
    # return True if queue is empty, False otherwise
    def empty(self):
        return self.size == 0

    # push(x)
    # Push [x] into queue
    def push(self, x):
        self.queue.append(x)
        self.size += 1

    # pop()
    # Remove and return top item from queue
    def pop(self):
        data = self.queue[0]
        self.queue = self.queue[1:]
        return data

    # print current queue as a list
    def print(self):
        print(self.queue)

que = Queue()
print("Current Queue is: Top -> ", end = "")
que.print()

print("Push -> 19")
print("Push -> 46")
print("Push -> 87")
print("Push -> 98")
print("Push -> 9")
print("Push -> 70")
print("Push -> 10")
que.push(19)
que.push(46)
que.push(87)
que.push(98)
que.push(9)
que.push(70)
que.push(10)
print("Current Queue is: Top -> ", end = "")
que.print()

print("The size of current queue is ", end = "")
print(que.size)

print("Current Queue is empty: ", end = "")
print(que.empty())

print("The popped item from queue is ", end = "")
print(que.pop())
print("Current Queue is: Top -> ", end = "")
que.print()