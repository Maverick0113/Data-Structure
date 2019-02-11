class Stack:
    # Stack constructor
    def __init(self):
        self.stack = []
        self.size = int(0)

    # size()
    # return size of the stack
    def size(self):
        return self.size

    # empty()
    # return True if stack is empty, False otherwise
    def empty(self):
        return self.size == 0

    # push(x)
    # push [x] into queue
    def push(self, x):
        self.stack.append(x)
        self.size += 1

    # pop()
    # remove and return top item from queue
    def pop(self):
        data = self.stack[-1]
        self.stack = self.stack[:-1]
        self.size -= 1
        return data

    # print current queue as a list
    def print(self):
        print(self.stack[::-1])

stk = Stack()
print("Current Stack is: Top -> ", end = "")
stk.print()

print("Push -> 19")
print("Push -> 46")
print("Push -> 87")
print("Push -> 98")
print("Push -> 9")
print("Push -> 70")
print("Push -> 10")
stk.push(19)
stk.push(46)
stk.push(87)
stk.push(98)
stk.push(9)
stk.push(70)
stk.push(10)
print("Current Stack is: Top -> ", end = "")
stk.print()

print("The size of current stack is ", end = "")
print(stk.size)

print("Current Stack is empty: ", end = "")
print(stk.empty())

print("The popped item from stack is ", end = "")
print(stk.pop())
print("Current Stack is: Top -> ", end = "")
stk.print()