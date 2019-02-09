class Node{
    /* Single Linked List Node constructor */
    constructor(data){
        this.val = data;
        this.next = null;
    }
}

class SLinkedList{
    /* Single Linked List constructor */
    constructor(){
        this.head = null;
    }

    /* append(x)
     * Add an item[x] to the end of the Linked List
     */
    append(x){
        // if the Linked List is empty
        if (!this.head){
            this.head = new Node(x);
            return;
        }

        var cur = this.head;
        while (cur.next){
            cur = cur.next;
        }
        cur.next = new Node(x);
    }

    /* extend(iterable)
     * Extend the Linked List by appending all the items in the array
     */
    extend(arr){
        // if the Linked List is empty
        if (!this.head){
            this.head = new Node(arr[0]);
            var cur = this.head;
            var i;
            for (i = 1; i < arr.length; i++){
                var new_node = new Node(arr[i]);
                cur.next = new_node;
                cur = cur.next;
            }
            return;
        }

        var cur = this.head;
        while (cur.next){
            cur = cur.next;
        }
        var i;
        for (i = 0; i < arr.length; i++){
            cur.next = new Node(arr[i]);
            cur = cur.next;
        }
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
            new_Node.next = this.head;
            this.head = new_Node;
            return;
        }

        var index = 0;
        var cur = this.head;
        // Continue traversing as long as index is less than
        // position[i - 1] and current node's [next] exist
        while (index < i - 1 && cur.next){
            cur = cur.next;
            index++;
        }

        // if inserting at the last position
        if (!cur.next){
            cur.next = new_Node;
            return;
        }

        new_Node.next = cur.next;
        cur.next = new_Node;
    }

    /* remove(x)   
     * remove the first item from the list whose value is equal to [x]
     */
    remove(x){
        // if the removed item is at first position
        if (this.head.val == x){
            this.head = this.head.next;
            return;
        }

        var cur = this.head;
        var prev = null;
        var found = false;
        while (cur){
            if (cur.val == x){
                found = true;
                break;
            }
            prev = cur;
            cur = cur.next;
        }

        // if item does not exist in Linked List
        if (!found){
            console.log("Item not found");
            return;
        }

        // if the removed item is at last position
        if (!cur.next){
            prev.next = null;
            return;
        }

        prev.next = cur.next;
    }

    /* pop([i])
     * remove the item at the given position in the list, and return it
     * if no index is specified, remove and
     * return the last item in the list
     */
    pop(i){
        // if the position [i] is negative
        if (i < 0){
            console.log("Out of bound index");
            return;
        }

        // if the popped item is at first position
        if (i == 0){
            var data = this.head.val;
            this.head = this.head.next;
            return data;
        }

        var cur = this.head;
        var prev = null;
        var index = 0;
        // Continue traversing as long as inex is less than
        // position [i] and current node's [next] exist
        while (index < i && cur.next){
            prev = cur;
            cur = cur.next;
            index++;
        }

        // if the removed item is at last position
        if (!cur.next){
            prev.next = null;
            return cur.val;
        }

        prev.next = cur.next;
        return cur.val;
    }

    /* clear()
     * remove all items from the list
     */
    clear(){
        this.head = null;
    }

    /* index(x)
     * return zero-based index in the list of the first item
     * whose value is equal to [x]
     */
    index(x){
        var i = 0;
        var cur = this.head;
        while (cur){
            if (cur.val == x){
                return i;
            }
            i++;
            cur = cur.next;
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
            cur = cur.next;
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
            cur = cur.next;
        }
        
        arr.sort();
        if (!flag){
            arr.reverse();
        }

        this.head = new Node(arr[0]);
        cur = this.head;
        var i;
        for (i = 1; i < arr.length; i++){
            cur.next = new Node(arr[i]);
            cur = cur.next;
        }
    }

    /* reverse()
     * reverse the elements of the list in place
     */
    reverse(){
        var cur = this.head;
        var prev = null;
        var nex = cur.next;
        while(nex){
            cur.next = prev;
            prev = cur;
            cur = nex;
            nex = nex.next;
        }
        cur.next = prev;
        this.head = cur;
    }

    /* copy()
     * return a shallow copy of the list
     */
    copy(){
        if (!this.head){
            return null;
        }
        var new_lis = new SLinkedList();
        var cur = this.head;
        while (cur){
            new_lis.append(cur.val);
            cur = cur.next;
        }
        return new_lis;
    }

    print(){
        if (!this.head){
            console.log("Empty Linked List");
            return;
        }

        var cur = this.head;
        while (cur){
            process.stdout.write(cur.val + " -> ");
            cur = cur.next;
        }
        console.log()
    }
}

lis = new SLinkedList();
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Append -> 30");
lis.append(30);
process.stdout.write("Current Linked List is: ");
lis.print();

console.log("Extend -> [62, 23, 15, 73, 77, 8, 38, 44]");
lis.extend([62, 23, 15, 73, 77, 8, 38, 44]);
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

lis.extend([81, 78, 33, 21, 99, 14, 59]);
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
process.stdout.write("Current Linked List is: ");
lis.print();
process.stdout.write("Copy Linked List is: ");
copy.print();