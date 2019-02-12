var map = new Map([["Janurary", 1], ["February", 2], ["March", 3], ["April", 4], ["May", 5], ["June", 6], ["July", 7], ["August", 8], ["September", 9], ["October", 10], ["November", 11], ["December", 12]]);
process.stdout.write("Current Hashtable: ");
console.log(map);

/* size
 * returns the number of key/pairs in the Map object
 */
console.log("size ->");
process.stdout.write("There are ");
console.log(map.size + " items in Current Hashtable");

/* delete(key)
 * returns true if [key] in the Map object existed and has been removed, else false
 */
console.log("delete -> August");
map.delete("August");
process.stdout.write("Current Hashtable: ");
console.log(map);

/* entries()
 * returns a new Iterator object that contains an array of [key, value] for 
 * each element in the Map object in insertion order
 */
console.log("entries ->");
process.stdout.write("Current Entries: ");
console.log(map.entries());

/* forEach(callback)
 * executes a provided function[callback] once
 * per each key/value pair in the Map object, in
 * insertion order
 */
function log(value, key, map){
    console.log(`m[${key}] = ${value}`);
}
console.log("forEach -> log");
map.forEach(log);

/* get(key)
 * returns a specified [key] from a Map object
 */
console.log("get -> November");
process.stdout.write("The key -> November maps to -> ");
console.log(map.get("November"));

/* has(key)
 * returns a boolean indicating whether an element 
 * with the specified [key] exists or not
 */
process.stdout.write("December is in Current Hashtable: ");
console.log(map.has("December"));

/* keys()
 * return a new Iterator object that contains
 * the keys for each element in the Map object
 * in insertion order
 */
console.log("keys ->");
process.stdout.write("Current Keys: ");
console.log(map.keys());

/* set(key, value)
 * adds or updates an element with a specified [key] and [value] to a Map object
 */
console.log("set -> (December, 13)");
map.set("December", 13);
process.stdout.write("Current Hashtable: ");
console.log(map);

/* values()
 * returns a new Iterator object that contain the
 * values for each element in the Map object in insertion order
 */
console.log("values ->");
process.stdout.write("Current Value: ");
console.log(map.values());