class Deque{
    /* Deque constructor */
    constructor(){
        this.deque = [];
    }

    /* appendLeft(x)
     * add [x] to the left side of the deque
     */
    appendLeft(x){
        this.deque = [x].concat(this.deque);
    }

    /* appendRight(x)
     * add [x] to the right side of the deque
     */
    appendRight(x){
        this.deque = this.deque.concat([x]);
    }

    /* extendLeft(iterable)
     * extend the left side of the deque by appending elements from [iterable]
     */
    extendLeft(arr){
        this.deque = arr.reverse().concat(this.deque);
    }

    /* extendRight(iterable)
     * extend the right side of the deque by appending elements from [iterable]
     */
    extendRight(arr){
        this.deque = this.deque.concat(arr);
    }

    /* index(x)
     * return the zero-based position of the first [x] in the deque
     */
    index(x){
        for (var i = 0; i < this.deque.length; i++){
            if (this.deque[i] == x){
                return i;
            }
        }
        return -1;
    }

    /* insert(i, x)
     * insert [x] into the deque at position [i]
     */
    insert(i, x){
        // if i is insert at first position
        if (i == 0){
            this.deque = [x].concat(this.deque);
            return;
        }

        // if i is insert at last position
        if (i > this.deque.length){
            this.deque = this.deque.concat([x])
            return;
        }

        this.deque = this.deque.slice(0, i).concat([x]).concat(this.deque.slice(i));
    }

    /* count(x)
     * return the number of [x] in deque
     */
    count(x){
        var cnt = 0;
        for (var i = 0; i < this.deque.length; i++){
            if (this.deque[i] == x){
                cnt++;
            }
        }
        return cnt;
    }

    /* popLeft()
     * remove and return an element from the left side of he deque
     */
    popLeft(){
        var data = this.deque[0];
        this.deque = this.deque.slice(1);
        return data;
    }

    /* popRight()
     * remove and return an element from the right side of he deque
     */
    popRight(){
        var data = this.deque[this.deque.length - 1];
        this.deque = this.deque.slice(0, -1);
        return data;
    }

    /* remove(x)
     * remove the first occurence of [x]
     */
    remove(x){
        for (var i = 0; i < this.deque.length; i++){
            if (this.deque[i] == x){
                this.deque = this.deque.slice(0, i).concat(this.deque.slice(i + 1));
                return;
            }
        }
        console.log("Item does not exist");
    }

    /* reverse()
     * reverse the elemnts of the deque in-place
     */
    reverse(){
        this.deque.reverse();
    }

    /* rotate(x)
     * rotate the deque [x] steps to the right
     */
    rotate(x){
        this.deque = this.deque.slice(this.deque.length - x).concat(this.deque.slice(0, this.deque.length - x));
    }

    /* size()
     * return the size of the deque
     */
    size(){
        return this.deque.length;
    }

    /* copy()
     * return a shallow copy of the Deque
     */
    copy(){
        var copy = new Deque();
        copy.extendRight(this.deque);
        return copy;
    }

    /* clear()
     * remove all elements from the deque
     */
    clear(){
        this.deque = [];
    }

    /* print current deque as a list */
    print(){
        console.log(this.deque + "] <- Tail");
    }
}

var deq = new Deque();
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("appendLeft -> 45");
deq.appendLeft(45);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("appendRight -> 40");
deq.appendRight(40);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("extendLeft -> [87, 11, 85]");
deq.extendLeft([87, 11, 85]);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("extendRight -> [85, 78, 38, 34]");
deq.extendRight([85, 78, 38, 34]);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

process.stdout.write("85 is at position ");
console.log(deq.index(85));

console.log("Insert -> (3, 13)");
deq.insert(3, 13);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("There are " + deq.count(85) + " 85's in the deque");

console.log("The popped-left item from deque is " + deq.popLeft());
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("The popped-right item from deque is " + deq.popRight());
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("Remove -> 45");
deq.remove(45);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("Reverse ->");
deq.reverse();
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("Rotate -> 3");
deq.rotate(3);
process.stdout.write("Current Deque is: Head -> [");
deq.print();

console.log("The size of the Current Deque is " + deq.size());

console.log("Copy ->");
var copy = deq.copy()
process.stdout.write("Current Deque is: Head -> [");
deq.print();
process.stdout.write("Copy Deque is: Head -> [");
copy.print();

console.log("Clear ->");
deq.clear();
process.stdout.write("Copy Deque is: Head -> [");
copy.print();