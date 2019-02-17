class Node:
    # Node constructor
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
class BinaryTree:
    # Binary Tree constructor
    def __init__(self):
        self.root = None
    
    # insert(x)
    # insert a new node [x] to the binary tree
    def insert(self, x):
        new = Node(x)
        # if tree is empty
        if not self.root:
            self.root = new
            return
        
        cur = self.root
        while cur:
            if new.val <= cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = new
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = new
                    break
    
    # extend(arr)
    # insert all items in the [arr]
    def extend(self, arr):
        for i in arr:
            self.insert(i)

    # find(x)
    # return the node whose value equals [x]
    def find(self, x):
        cur = self.root
        while cur:
            if x < cur.val:
                cur = cur.left
            elif x > cur.val:
                cur = cur.right
            else:
                return cur
    
    # height()
    # return the depth of the binary tree
    def height(self):
        def depth(cur):
            if not cur:
                return 0
            else:
                return 1 + max(depth(cur.left), depth(cur.right))
        return depth(self.root)
    
    # print()
    # print the inorder, preorder, and postorder traversal of the binary tree
    def traversal(self):
        def inorder(root):
            stk = []
            res = []
            while root:
                stk.append(root)
                root = root.left
            while stk:
                cur = stk.pop()
                res.append(cur.val)
                if cur.right:
                    cur = cur.right
                    while cur:
                        stk.append(cur)
                        cur = cur.left
            return res
        
        def preorder(root):
            stk = []
            res = []
            while root:
                stk.append(root)
                res.append(root.val)
                root = root.left
            while stk:
                cur = stk.pop()
                if cur.right:
                    cur = cur.right
                    while cur:
                        res.append(cur.val)
                        stk.append(cur)
                        cur = cur.left
            return res
        
        def postorder(root):
            if not root:
                return []
            stk = [root]
            res = []
            while stk:
                cur = stk.pop()
                res.append(cur.val)
                if cur.left:
                    stk.append(cur.left)
                if cur.right:
                    stk.append(cur.right)
            return res[::-1]

        print("Inorder Traversal -> ", end = "")
        print(inorder(self.root))
        print("Preorder Traversal -> ", end = "")
        print(preorder(self.root))
        print("Postorder Traversal -> ", end = "")
        print(postorder(self.root))

bt = BinaryTree()
print("Current Binary Tree:")
bt.traversal()

bt.insert(8)
print("Insert -> 8")
print("Current Binary Tree:")
bt.traversal()

bt.extend([3, 1, 6, 4, 7, 10, 14, 13])
print("Extend -> [3, 1, 6, 4, 7, 10, 14, 13]")
print("Current Binary Tree:")
bt.traversal()

print("Node 13 is here -> ", end = "")
print(bt.find(13).val)

print("The height of this tree is -> ", end = "")
print(bt.height())