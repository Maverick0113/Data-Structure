class Stack{
    /* Stack constructor*/
    constructor(){
        this.stack = [];
        this.size = 0;
    }

    /* size()
     * return size of the stack
     */
    size(){
        return this.size;
    }

    /* empty()
     * return True if stack is empty, False otherwise
     */
    empty(){
        return this.size == 0;
    }

    /* push(x)
     * push [x] into stack
     */
    push(x){
        this.stack.push(x);
        this.size++;
    }

    /* pop()
     * remove and return top tiem from queue
     */
    pop(){
        var data = this.stack[this.size - 1];
        this.stack = this.stack.slice(0, -1);
        this.size--;
        return data;
    }

    /* print current queue as a list */
    print(){
        var rev = [];
        for (var i = this.stack.length - 1; i >= 0; i--){
            rev.push(this.stack[i]);
        }
        console.log(rev);
    }
}

var stk = new Stack();
process.stdout.write("Current Stack is: Top -> ");
stk.print();

console.log("Push -> 19");
console.log("Push -> 46");
console.log("Push -> 87");
console.log("Push -> 98");
console.log("Push -> 9");
console.log("Push -> 70");
console.log("Push -> 10");
stk.push(19);
stk.push(46);
stk.push(87);
stk.push(98);
stk.push(9);
stk.push(70);
stk.push(10);
process.stdout.write("Current Stack is: Top -> ");
stk.print();

process.stdout.write("The size of current stack is ");
console.log(stk.size());

process.stdout.write("Current Stack is empty: ");
console.log(stk.empty());

process.stdout.write("The popped item from stack is ");
console.log(stk.pop());
process.stdout.write("Current Stack is: Top -> ");
stk.print();