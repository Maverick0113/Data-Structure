class Heap{
    /* Heap constructor */
    constructor(){
        this.heap = [];
    }

    // return a specified node parent node
    parent(i){
        if (i == 0){
            return 0;
        }
        return Math.floor((i - 1) / 2);
    }

    // return a specified node left node
    left(i){
        return (i * 2) + 1;
    }

    // return a specified node right node
    right(i){
        return (i * 2) + 1;
    }

    /* heappush(x)
     * push the value [x] onto the heap, maintaining the heap invariant
     */
    heappush(x){
        // if heap is empty
        if (this.heap.length == 0){
            this.heap.push(x);
            return;
        }

        this.heap.push(x);
        var cur = this.heap.length - 1;
        var par = this.parent(cur);
        while (this.heap[cur] > this.heap[par]){
            var tmp = this.heap[cur];
            this.heap[cur] = this.heap[par];
            this.heap[par] = tmp;
            cur = par;
            par = this.parent(cur);
        }
    }

    /* heappop()
     * pop and return the greatest item from the heap
     */
    heappop(){
        // if heap is empty
        if (this.heap.length == 0){
            return;
        }
        // if heap has only one item
        if (this.heap.length == 1){
            var data = this.heap[0];
            this.heap = [];
            return data;
        }

        var data = this.heap[0];
        var tmp = this.heap[0];
        this.heap[0] = this.heap[this.heap.length - 1];
        this.heap[this.heap.lenght - 1] = tmp;
        this.heap = this.heap.slice(0, -1);
        var cur = 0;
        while (cur < this.heap.length){
            var l = this.left(cur);
            var r = this.right(cur);
            if ((l > this.heap.length - 1) || (r > this.heap.length - 1)){
                break;
            }
            if ((this.heap[cur] > this.heap[l] && this.heap[cur] > this.heap[r])){
                break;
            }
            if ((this.heap[cur] < this.heap[l] && this.heap[cur] < this.heap[r])){
                if (this.heap[l] > this.heap[r]){
                    var a = this.heap[l];
                    this.heap[l] = this.heap[cur];
                    this.heap[cur] = a;
                    cur = l;
                }
                else{
                    var b = this.heap[r];
                    this.heap[r] = this.heap[cur];
                    this.heap[cur] = b;
                    cur = r;
                }
            }
            else if (this.heap[cur] < this.heap[l]){
                var c = this.heap[l];
                this.heap[l] = this.heap[cur];
                this.heap[cur] = c;
                cur = l;
            }
            else{
                var d = this.heap[r];
                this.heap[r] = this.heap[cur];
                this.heap[cur] = d;
                cur = r;
            }
        }
        return data;
    }

    /* heapreplace(x)
     * pop and return max item
     * push [x] on the heap, efficiently
     */
    heapreplace(x){
        // if heap is empty
        if (this.heap.length == 0){
            return;
        }
        // if heap has only one item
        if (this.heap.length == 1){
            var data = this.heap[0];
            this.heap = [];
            return data;
        }

        var data = this.heap[0];
        this.heap[0] = x; 
        var cur = 0;
        while (cur < this.heap.length){
            var l = this.left(cur);
            var r = this.right(cur);
            if ((l > this.heap.length - 1) || (r > this.heap.length - 1)){
                break;
            }
            if ((this.heap[cur] > this.heap[l] && this.heap[cur] > this.heap[r])){
                break;
            }
            if ((this.heap[cur] < this.heap[l] && this.heap[cur] < this.heap[r])){
                if (this.heap[l] > this.heap[r]){
                    var a = this.heap[l];
                    this.heap[l] = this.heap[cur];
                    this.heap[cur] = a;
                    cur = l;
                }
                else{
                    var b = this.heap[r];
                    this.heap[r] = this.heap[cur];
                    this.heap[cur] = b;
                    cur = r;
                }
            }
            else if (this.heap[cur] < this.heap[l]){
                var c = this.heap[l];
                this.heap[l] = this.heap[cur];
                this.heap[cur] = c;
                cur = l;
            }
            else{
                var d = this.heap[r];
                this.heap[r] = this.heap[cur];
                this.heap[cur] = d;
                cur = r;
            }
        }
        return data;
    }

    /* print current heap as a list */
    print(){
        if (this.heap.length == 0){
            console.log("Empty Heap");
        }
        process.stdout.write("Root -> ");
        console.log(this.heap);
    }
}

var hp = new Heap();
process.stdout.write("Current Heap: ");
hp.print();

console.log("Heappush -> 39");
console.log("Heappush -> 100");
console.log("Heappush -> 78");
console.log("Heappush -> 70");
console.log("Heappush -> 33");
console.log("Heappush -> 35");
console.log("Heappush -> 54");
console.log("Heappush -> 13");
console.log("Heappush -> 59");
hp.heappush(39);
hp.heappush(100);
hp.heappush(78);
hp.heappush(70);
hp.heappush(33);
hp.heappush(35);
hp.heappush(54);
hp.heappush(13);
hp.heappush(59);
process.stdout.write("Current Heap: ");
hp.print();

console.log("Heappop ->");
process.stdout.write("The greatest item is ");
console.log(hp.heappop());
process.stdout.write("Current Heap: ");
hp.print();

console.log("Heapreplace -> 43");
process.stdout.write("The greatest item is ");
console.log(hp.heapreplace());
process.stdout.write("Current Heap: ");
hp.print();