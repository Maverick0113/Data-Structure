class Node:
    # Trie Node constructor
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    # Trie constructor
    def __init__(self):
        self.root = self.getNode()
    
    # return a new trie node
    def getNode(self):
        return Node()
    
    # char to int
    def charToIndex(self, ch):
        return ord(ch) - ord('a')
    
    # insert(x)
    # add a new word[x] to the trie
    def insert(self, x):
        cur = self.root
        for level in range(len(x)):
            index = self.charToIndex(x[level])

            # if current char is not present
            if not cur.children[index]:
                cur.children[index] = self.getNode()
            cur = cur.children[index]
        
        # indicate last node as leaf
        cur.end = True
    
    # search(x)
    # return true if word [x] exists in trie
    def search(self, x):
        cur = self.root
        for level in range(len(x)):
            index = self.charToIndex(x[level])
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur != None and cur.end

words = ["animal", "lion", "zebra", "penguin", "bird"]

trie = Trie()

print("Inserting -> [animal, lion, zebra, penguin, bird]")
for i in words:
    trie.insert(i)

if trie.search("zebra"):
    print("Found Zebra!")

if trie.search("bird"):
    print("Found Bird!")

if trie.search("alligator"):
    print("Found alligator!")
