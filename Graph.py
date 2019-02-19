class Graph:
    # Graph constructor
    def __init__(self):
        self.graph = {}
    
    # addEdge(x, y)
    # add an edge from [x] -> [y]
    def addEdge(self, x, y):
        if not x in self.graph:
            self.graph[x] = {y}
        else:
            self.graph[x].add(y)
    
    # bfs(x, y)
    # Breadth First Search from [x] -> [y]
    def bfs(self, x, y):
        que = [x]
        s = set()
        while que:
            cur = que.pop(0)
            s.add(cur)
            for i in self.graph[cur]:
                if i == y:
                    return s
                elif not i in s:
                    que.append(i)
        return None
    
    # dfs(x, y)
    # Depth First Search from [x] -> [y]
    def dfs(self, x, y):
        stk = [x]
        s = set()
        while stk:
            cur = stk.pop()
            s.add(cur)
            for i in self.graph[cur]:
                if i == y:
                    return s
                elif not i in s:
                    stk.append(i)
        return None

    # print()
    # print the dictionary containing all vertices and edges
    def print_graph(self):
        print(self.graph)

gph = Graph()
print("Current Graph:")
gph.print_graph()

print("Adding a -> c")
print("Adding b -> c")
print("Adding b -> e")
print("Adding c -> a")
print("Adding c -> b")
print("Adding c -> d")
print("Adding c -> e")
print("Adding d -> c")
print("Adding e -> c")
print("Adding e -> b")
gph.addEdge('a', 'c')
gph.addEdge('b', 'c')
gph.addEdge('b', 'e')
gph.addEdge('c', 'a')
gph.addEdge('c', 'b')
gph.addEdge('c', 'd')
gph.addEdge('c', 'e')
gph.addEdge('d', 'c')
gph.addEdge('e', 'c')
gph.addEdge('e', 'b')

print("Current Graph:")
gph.print_graph()

print("BFS from a -> e")
print(gph.bfs('a', 'e'))

print("DFS from a -> b")
print(gph.dfs('a', 'b'))
