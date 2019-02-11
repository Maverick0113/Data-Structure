class Queue{
    /* Queue constructor*/
    constructor(){
        this.queue = [];
        this.size = 0;
    }

    /* size()
     * return size of the queue
     */
    size(){
        return this.size;
    }

    /* empty()
     * return True if queue is empty, False otherwise
     */
    empty(){
        return this.size == 0;
    }

    /* push(x)
     * push [x] into queue
     */
    push(x){
        this.queue.push(x);
        this.size++;
    }

    /* pop()
     * remove and return top tiem from queue
     */
    pop(){
        var data = this.queue[0];
        this.queue = this.queue.slice(1);
        this.size--;
        return data;
    }

    /* print current queue as a list */
    print(){
        console.log(this.queue);
    }
}

var que = new Queue();
process.stdout.write("Current Queue is: Top -> ");
que.print();

console.log("Push -> 19");
console.log("Push -> 46");
console.log("Push -> 87");
console.log("Push -> 98");
console.log("Push -> 9");
console.log("Push -> 70");
console.log("Push -> 10");
que.push(19);
que.push(46);
que.push(87);
que.push(98);
que.push(9);
que.push(70);
que.push(10);
process.stdout.write("Current Queue is: Top -> ");
que.print();

process.stdout.write("The size of current queue is ");
console.log(que.size());

process.stdout.write("Current Queue is empty: ");
console.log(que.empty());

process.stdout.write("The popped item from queue is ");
console.log(que.pop());
process.stdout.write("Current Queue is: Top -> ");
que.print();