class Node{
    /* Trie Node constructor */
    constructor(){
        this.children = [null] * 26;
        this.end = false;
    }
}

class Trie{
    /* Trie constructor */
    constructor(){
        this.root = this.getNode();
    }

    /* return a new trie node */
    getNode(){
        return new Node();
    }

    /* char to int */
    charToIndex(ch){
        return ch.charCodeAt(0) - 'a'.charCodeAt(0);
    }

    /* insert(x)
     * add a new word[x] to the trie
     */
    insert(x){
        var cur = this.root;
        for (var level = 0; level < x.length; level++){
            var index = this.charToIndex(x[level]);
            if (!cur.children[index]){
                cur.children[index] = this.getNode();
            }
            cur = cur.children[index];
        }
        cur.end = true;
    }

    /* search(x)
     * return true if word [x] exists in trie
     */
    search(x){
        var cur = this.root;
        for (var level = 0; level < x.length; level++){
            var index = this.charToIndex(x[level]);
            if (!cur.children[index]){
                return false;
            }
            cur = cur.children[index];
        }
        return cur != null && cur.end;
    }
}

var words = ["animal", "lion", "zebra", "penguin", "bird"];

var trie = new Trie();
console.log("Inserting -> [animal, lion, zebra, penguin, bird]");

for (var i = 0; i < words.length; i++){
    trie.insert(words[i]);
}

if (trie.search("zebra")){
    console.log("Found zebra!");
}

if (trie.search("bird")){
    console.log("Found bird!");
}

if (trie.search("alligator")){
    console.log("Found alligator!");
}