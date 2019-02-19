class Graph{
    /* Graph constructor */
    constructor(){
        this.graph = new Map();
    }

    /* addEdge(x, y)
     * add an edge from [x] -> [y]
     */
    addEdge(x, y){
        if (!this.graph.has(x)){
            var s = new Set([y]);
            this.graph.set(x, s);
        }
        else{
            this.graph.get(x).add(y);
        }
    }

    /* bfs(x, y)
     * Breadth First Search from [x] -> [y]
     */
    bfs(x, y){
        var que = [x];
        var s = new Set();
        while (que.length > 0){
            var cur = que[0];
            s.add(cur);
            que = que.slice(1);
            var arr = Array.from(this.graph.get(cur));
            for (var i = 0; i < arr.length; i++){
                if (arr[i] == y){
                    return s;
                }
                else if (!s.has(arr[i])){
                    que.push(arr[i]);
                }
            }
        }
    }

    /* dfs(x, y)
     * Depth First Search from [x] -> [y]
     */
    dfs(x, y){
        var stk = [x];
        var s = new Set();
        while (stk.length > 0){
            var cur = stk.pop();
            s.add(cur);
            var arr = Array.from(this.graph.get(cur));
            for (var i = 0; i < arr.length; i++){
                if (arr[i] == y){
                    return s;
                }
                else if (!s.has(arr[i])){
                    stk.push(arr[i]);
                }
            }
        }
    }

    /* print()
     * print the dictionary containing all vertices and edges
     */
    print_graph(){
        console.log(this.graph);
    }
}

var gph = new Graph();
console.log("Current Graph:");
gph.print_graph();

console.log("Adding a -> c");
console.log("Adding b -> c");
console.log("Adding b -> e");
console.log("Adding c -> a");
console.log("Adding c -> b");
console.log("Adding c -> d");
console.log("Adding c -> e");
console.log("Adding d -> c");
console.log("Adding e -> c");
console.log("Adding e -> b");
gph.addEdge('a', 'c');
gph.addEdge('b', 'c')
gph.addEdge('b', 'e')
gph.addEdge('c', 'a')
gph.addEdge('c', 'b')
gph.addEdge('c', 'd')
gph.addEdge('c', 'e')
gph.addEdge('d', 'c')
gph.addEdge('e', 'c')
gph.addEdge('e', 'b')

console.log("Current Graph:");
gph.print_graph();

console.log("BFS from a -> e");
console.log(gph.bfs('a', 'e'));

console.log("DFS from a -> b");
console.log(gph.dfs('a', 'b'));