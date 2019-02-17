class Node{
    /* Node constructor */
    constructor(data){
        this.val = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree{
    /* Binary Tree constructor */
    constructor(){
        this.root = null;
    }

    /* insert(x)
     *insert a new node [x] to the binary tree
     */
    insert(x){
        new_Node = new Node();
        // if tree is empty
        if (!this.root){
            this.root = new_Node;
            return;
        }

        var cur = this.root;
        while (cur){
            if (x <= cur.val){
                if (cur.left){
                    cur = cur.left;
                }
                else{
                    cur.left = new_Node;
                    break;
                }
            }
            else{
                if (cur.right){
                    cur = cur.right;
                }
                else{
                    cur.right = new_Node;
                    break;
                }
            }
        }
    }

    /* extend(arr)
     * insert all items in the [arr]
     */
    extend(arr){
        for (var i = 0; i < arr.length; i++){
            this.insert(arr[i]);
        }
    }

    /* find(x)
     * return the node whose value equals [x]
     */
    find(x){
        var cur = this.root
        while (cur){
            if (x < cur.val){
                cur = cur.left;
            }
            else if (x > cur.val){
                cur = cur.right;
            }
            else{
                return cur;
            }
        }
        return null;
    }

    /* height()
     * return the depth of the binary tree
     */
    height(){
        function max(x, y){
            if (x > y){
                return x;
            }
            else{
                return y;
            }
        }
        
        function depth(cur){
            if (!cur){
                return 0;
            }
            else{
                return 1 + max(depth(cur.left), depth(cur.right));
            }
        }
        return depth(this.root);
    }

    /* traversal()
     * print the inorder, preorder, and postorder traversal of the binary tree
     */
    traversal(){
        function inorder(root){
            var stk = [];
            var res = [];
            while (root){
                stk.push(root);
                root = root.left;
            }
            
            var cur;
            while (stk.length > 0){
                cur = stk.pop();
                res.push(cur.val);
                if (cur.right){
                    cur = cur.right;
                    while (cur){
                        stk.push(cur);
                        cur = cur.left;
                    }
                }
            }
            return res;
        }

        function preorder(root){
            var stk = [];
            var res = [];
            while (root){
                stk.push(root);
                res.push(root.val);
                root = root.left;
            }
            
            var cur;
            while (stk.length > 0){
                cur = stk.pop();
                if (cur.right){
                    cur = cur.right;
                    while (cur){
                        stk.push(cur);
                        res.push(cur.val);
                        cur = cur.left;
                    }
                }
            }
            return res;
        }

        function postorder(root){
            if (!root){
                return [];
            }
            var stk = [root];
            var res = [];
            var cur;
            while (stk.length > 0){
                cur = stk.pop();
                res.push(cur.val);
                if (cur.left){
                    stk.push(cur.left);
                }
                else{
                    stk.push(cur.right);
                }
            }
            return res.reverse();
        }

        process.stdout.write("Inorder Traversal -> ");
        console.log(inorder(this.root));
        process.stdout.write("Preorder Traversal -> ");
        console.log(preorder(this.root));
        process.stdout.write("Postorder Traversal -> ");
        console.log(postorder(this.root));
    }
}

var bt = new BinaryTree();
console.log("Current Binary Tree:")
bt.traversal();

bt.insert(8);
console.log("Insert -> 8");
console.log("Current Binary Tree:");
bt.traversal();

bt.extend([3, 1, 6, 4, 7, 10, 14, 13]);
console.log("Extend -> [3, 1, 6, 4, 7, 10, 14, 13]");
console.log("Current Binary Tree:");
bt.traversal();

process.stdout.write("Node 13 is here -> ");
console.log(bt.find(13).val);

process.stdout.write("The height of this tree is -> ");
console.log(bt.height());