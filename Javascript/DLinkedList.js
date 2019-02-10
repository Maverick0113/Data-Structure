class Node{
    /* Double Linked List Node constructor */
    constructor(data){
        this.val = data
        this.left = null
        this.right = null
    }
}

class DLinkedList{
    /* Double Linked List constructor */
    constructor(){
        this.head = null;
        this.tail = null;
    }

    /* appendRight(x)
     * Add an item[x] to the right-end of the Linked List
     */
    appendRight(x){
        var new_Node = new Node(x);
        // if the Linked List is empty
        if (!this.head && !this.tail){
            this.head = new_Node;
            this.tail = new_Node;
            return;
        }

        this.tail.right = new_Node;
        new_Node.left = this.tail;
        this.tail = new_Node;
    }

    /* appendLeft(x)
     * Add an item[x] to the left-end of the Linked List
     */
    appendLeft(x){
        var new_Node = new Node(x);
        // if the Linked List is empty
        if (!this.head && !this.tail){
            this.head = new_Node;
            this.tail = new_Node;
            return;
        }

        new_Node.right = this.head;
        this.head.left = new_Node;
        this.head = new_Node;
    }

    /* extendRight(iterable)
     * Extend the Linked List by appending-right all the items in the array
     */
    extendRight(arr){
        // if the Linked List is empty
        if (!this.head && !this.tail){
            this.head = new Node(arr[0]);
            var cur = this.head;
            for (var i = 1; i < arr.length; i++){
                var new_Node = new Node(arr[i]);
                cur.right = new_Node;
                new_Node.left = cur;
                cur = cur.right;
            }
            this.tail = cur;
            return;
        }

        var cur = this.tail;
        for (var i = 0; i < arr.length; i++){
            var new_Node = new Node(arr[i]);
            cur.right = new_Node;
            new_Node.left = cur;
            cur = cur.right;
        }
        this.tail = cur;
    }

    /* extendLeft(iterable)
     * Extend the Linked List by appending-left all the items in the array
     */
    extendLeft(arr){
        // if the Linked List is empty
        if (!this.head && !this.tail){
            this.tail = new Node(arr[0]);
            var cur = this.tail; 
            for (var i = 0; i < arr.length; i++){
                var new_Node = new Node(arr[i]);
                cur.left = new_Node;
                new_Node.right = cur;
                cur = cur.left;
            }
            this.head = cur;
            return;
        }

        var cur = this.head;
        for (var i = 0; i < arr.length; i++){
            var new_Node = new Node(arr[i]);
            cur.left = new_Node;
            new_Node.right = cur;
            cur = cur.left;
        }
        this.head = cur;
    }

    /* insert(i, x)
     * Insert an item[x] at a given position
     */
    insert(i, x){
        var new_Node = new Node(x);
        // if the position[i] is negative
        if (i < 0){
            console.log("Out of bound index");
            return;
        }

        // if inserting at the first position
        if (i == 0){
            new_Node.right = this.head;
            this.head.left = new_Node;
            this.head = new_Node;
            return;
        }

        var index = 0;
        var cur = this.head;
        // Continue traversing as long as index is less than
        // position[i - 1] and current node's [next] exist
        while (index < i - 1 && cur.right){
            cur = cur.right;
            index++;
        }

        // if inserting at the last position
        if (!cur.right){
            this.tail.right = new_Node;
            new_Node.left = this.tail;
            this.tail = new_Node;
            return;
        }

        new_Node.right = cur.right;
        cur.right.left = new_Node;
        cur.right = new_Node;
        new_Node.left = cur;
    }

    /* remove(x)   
     * remove the first item from the list whose value is equal to [x]
     */
    remove(x){
        // if removed item is at first position
        if (this.head.val == x){
            this.head = this.head.right;
            this.head.left = null;
            return;
        }

        // if removed item is at last position
        if (this.tail.val == x){
            this.tail = this.tail.left;
            this.tail.right = null;
            return;
        }

        var cur_head = this.head;
        var cur_tail = this.tail;
        while (cur_head && cur_tail){
            if (cur_head.val == x){
                cur_head.left.right = cur_head.right;
                cur_head.right.left = cur_head.left;
                return;
            }
            if (cur_tail.val == x){
                cur_tail.left.right = cur_tail.right;
                cur_tail.right.left = cur_tail.left;
                return;
            }
            cur_head = cur_head.right;
            cur_tail = cur_tail.left;
        }

        print("Item not found");
    }

    /* pop([i])
     * remove the item at the given position in the list, and return it
     * if no index is specified, remove and
     * return the last item in the list
     */
    pop(i){
        // if the position[i] is negative
        if (i < 0){
            console.log("Out of bound index");
            return;
        }

        // if the popped item is at first position
        if (i == 0){
            data = this.head.val;
            this.head = this.head.right;
            this.head.left = null;
            return data;
        }

        var cur = this.head;
        var index = 0;
        // Continue traversing as long as inex is less than
        // position [i] and current node's [next] exist
        while (index < i && cur.right){
            cur = cur.right;
            index++;
        }

        // if the removed item is at last position
        if (!cur.right){
            var data = this.tail.data;
            this.tail = this.tail.left;
            this.tail.right = null;
            return data;
        }

        data = cur.val;
        cur.left.right = cur.right;
        cur.right.left = cur.left;
        return data;
    }

    /* clear()
     * remove all items from the list
     */
    clear(){
        this.head = null;
        this.tail = null;
    }

    /* index(x)
     * return zero-based index in the list of the first item
     * whose value is equal to [x]
     */
    index(x){
        var cur = this.head;
        var index = 0;
        while (cur){
            if (cur.val == x){
                return index;
            }
            cur = cur.right;
            index++;
        }
        return -1;
    }

    /* count(x)
     * return the number of times [x] appears in the list
     */
    count(x){
        var cnt = 0;
        var cur = this.head;
        while (cur){
            if (cur.val == x){
                cnt++;
            }
            cur = cur.right;
        }
        return cnt;
    }

    /* sort(reverse = False)
     * sort the items of the list in place
     */
    sort(flag){
        var arr = [];
        var cur = this.head;
        while (cur){
            arr.push(cur.val);
            cur = cur.right;
        }

        arr.sort();
        if (!flag){
            arr.reverse();
        }

        this.head = new Node(arr[0]);
        var cur = this.head;
        for (var i = 0; i < arr.length; i++){
            var new_Node = new Node(arr[i]);
            cur.right = new_Node;
            new_Node.left = cur;
            cur = cur.right;
        }
        this.tail = cur;
    }

    /* reverse()
     * reverse the elements of the list in place
     */
    reverse(){
        var cur = this.head;
        while (cur){
            var tmp = cur.left;
            cur.left = cur.right;
            cur.right = tmp;
            cur = cur.left;
        }
        var smp = this.head;
        this.head = this.tail;
        this.tail = smp;
    }
    /* copy()
     * return a shallow copy of the list
     */
    copy(){
        if (!this.head && !this.tail){
            print("Empty Linked List");
            return;
        }

        var new_list = new DLinkedList();
        var cur = this.head;
        while (cur){
            new_list.appendRight(cur.val);
            cur = cur.right;
        }
        return new_list;
    }

    /* print current linked list as a list */
    print(){
        if (!this.head && ! this.tail){
            console.log("Empty Linked List");
            return;
        }

        var cur_head = this.head;
        console.log("Going Right ->");
        while (cur_head){
            process.stdout.write(cur_head.val + " -> ");
            cur_head = cur_head.right;
        }
        console.log();

        var cur_tail = this.tail;
        console.log("Going Left ->");
        while (cur_tail){
            process.stdout.write(cur_tail.val + " -> ");
            cur_tail = cur_tail.left;
        }
        console.log();
    }
}

lis = new DLinkedList();
process.stdout.write("Current Linked List is: ");
lis.print();

lis.appendRight(30);
console.log("Append Right -> 30");
process.stdout.write("Current Linked List is: ");
lis.print();

lis.appendLeft(62);
console.log("Append Left -> 62");
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Extend Right -> [23, 15, 73, 77, 8, 38, 44]");
lis.extendRight([23, 15, 73, 77, 8, 38, 44]);
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Extend Left -> [90, 94, 78]");
lis.extendLeft([90, 94, 78]);
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Insert -> 13 at 3");
lis.insert(3, 13);
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Remove -> 8");
lis.remove(8);
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Pop -> 7");
lis.pop(7);
process.stdout.write("Current Linked List is: ");
lis.print();

lis.clear();
console.log("Clear ->")
process.stdout.write("Current Linked List is: ");
lis.print();

lis.extendRight([81, 78, 33, 21, 99, 14, 59]);
process.stdout.write("Current Linked List is: ");
lis.print();

process.stdout.write("21 is located at: ");
console.log(lis.index(21));

process.stdout.write("There are ");
process.stdout.write((lis.count(14).toString(10)));
console.log(" 14's in lis");

lis.sort(true);
process.stdout.write("Current Linked List is: ");
lis.print();

lis.reverse();
process.stdout.write("Current Linked List is: ");
lis.print();

copy = lis.copy()
console.log("Current Linked List is: ");
lis.print();
console.log("Copy Linked List is: ");
copy.print();