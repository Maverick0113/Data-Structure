var arr = [43, 95, 24, 21, 9, 19, 69, 94, 16];
var s = new Set(arr);
console.log(s);

/* The [size] accessor property returns the number of elements
 * in a Set object
 */
console.log("The size of s is " + s.size);

/* The [add()] method appends a new element with a specified
 * value to the end of a Set object
 */
s.add(13);
console.log(s);

/* The [clear()] method removes all elements from a Set object
 */
s.clear();
console.log(s);

arr = [79, 37, 62, 11, 17];
var s = new Set(arr);
console.log(s);

/* The [delete()] method removes the specified element from a
 * Set object
 */
s.delete(37);
console.log(s);

/* The [entries()] method returns a new Iterator object that contains
 * an array of [value, value] for each element in the Set object,
 * in insertion order
 */
var it = s.entries();
for (let i of it){
    console.log(i);
}

/* The [forEach()] method executes a provided function once for each
 * value in the Set object, in insertion order
 */
function logSetElements(v1, v2, s){
    console.log('s[' + v1 + '] = ' + v2);
}
s.forEach(logSetElements);

/* The [has()] method returns a boolean indicating whether an element
 * with the specified value exists in a Set object or not
 */
console.log('17 is in s: ' + s.has(17));

/* The [values()] method returns a new Iterator object that contains
 * the values for each element in the Set object in insertion order
 */
var vl = s.values();
console.log("The first element in s is " + vl.next().value);