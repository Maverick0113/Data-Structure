var arr = [64, 13, 88, 48, 97, 74, 83, 96, 5, 52, 59, 79];
console.log("Current Array: " + '[' + arr + ']');

/* The [length] property of an object which is an instance
 * of type Array sets or returns the number of elements in
 * that array
 */
var length = arr.length;
console.log("The length of arr is " + length);

/* The [Array.from()] method creates a new, shallow-copied
 * Array instance from an array-like or iterable object
 */
var copy = Array.from(arr, x => x * -1);
console.log("Array.from(), x => x * -1");
console.log("Copy Array: " + "[" + copy + "]");

/* The [Array.isArray()] method determines whether the passed
 * value is an Array
 */
console.log("arr is an array: " + Array.isArray(arr));

/* The [Array.of()] method creates a new Array instance
 * with a variable number of arguments, regardless of number
 * or type of the arguments
 */
var ofArr = Array.of(7, 3, 13);
console.log("OfArr Array: " + "[" + ofArr + "]");

/* The [concat()] method is used to merge two or more arrays
 * This method does not change the existing arrays, but instead
 * returns a new array
 */
var con1 = [1, 2, 3];
var con2 = [4, 5, 6];
var con3 = con1.concat(con2);
console.log("Con3 Array: " + "[" + con3 + "]");

/* The [copyWithin()] method shallow copies part of an
 * array to another location in the same array and returns
 * it, without modify its size
 */
var copyWi = arr.copyWithin(1, 3);
console.log("CopyWi Array: " + "[" + copyWi + "]");

/* The [entries()] method returns a new Array Iterator object
 * that contains the key/value
 */
var it = arr.entries();
console.log("It Array Iterator is: " + "[" + it.next().value + "]");

/* The [every()] method tests whether all elements in the array pass
 * the test implemented by the provided function
 */
function positive(x) {
    return x > 0;
}
console.log("All elements in arr are positive: " + arr.every(positive));

/* The [fill()] method fills all the elements of an array from a start
 * index to an end index with a static value
 * The end index is not included
 */
var fiArr = arr.fill(1, 3, 5);
console.log("fiArr Array: " + "[" + fiArr + "]");

/* The [filter()] method creates a new array with all elemtns that
 * pass the test implemented by the provided function
 */
function lessThan13(x){
    return x < 13;
}
var filArr = arr.filter(lessThan13);
console.log("filArr Array: " + "[" + filArr + "]");

/* The [find()] method returns the value of the first element in the
 * array that satisfies the provided testing function
 * Otherwise undefined is returned
 */
function greaterThan80(x){
    return x > 80;
}
var found = arr.find(greaterThan80);
console.log("The first element greater than 80 is " + found);

/* The [findIndex()] method returns the index of the first element in the
 * array that satisfies the providing testing function
 * Otherwise, it returns -1, indicating no element passed the test
 */
function is1(x){
    return x == 1;
}
var index = arr.findIndex(is1);
console.log("1 is located at position " + index);

/* The [flat()] method creates a new array with all sub-array elements
 * concatenated into it recursively up to the specified depth
 */
var depth = [1, 2, [3, 4, [5, 6]]];
depth.flat();
console.log("Depth Array: " + "[" + depth + "]");

/* The [flatMap()] method fist maps each element using a mapping function,
 * then flattens the result into a new array
 */
function multiplyBy2(x){
    return x * 2;
}
depth.flatMap(multiplyBy2);
console.log("Depth Array: " + "[" + depth + "]");

/* The [forEach()] method executes a provided function once for each array element
 */
arr.forEach(function(element){
    console.log(element);
})

/* The [includes()] method determines whether an array includes a certain value
 * among its entries, returning true or false as appropriate
 */
console.log("59 is in arr: " + arr.includes(59));

/* The [indexOf()] method returns the first index at which a given element can
 * be found in the array, or -1 if it is not present
 */
console.log("5 is at position: " + arr.indexOf(5));

/* The [join()] method creates and returns a new string by concatenating all of
 * the elements in an array, separately by commas or a specified separator string
 * If the array has only one item, then that item will be returned without using
 * the separator
 */
var s = arr.join('');
console.log("String s: " + s);

/* The [keys()] method returns a new Array Iterator object that contains the
 * keys for each index in the array
 */
var k = arr.keys();
for (let i of k){
    console.log(i);
}

/* The [lastIndexOf] method returns the last index at which a given element can be found
 * in the array, or -1 if it is not present
 */
var index = arr.lastIndexOf(1);
console.log("1's last position is " + index);

/* The [map()] method creates a new array with the results of calling a provided
 * function on every element in the calling array
 */
function square(x){
    return Math.pow(x, 2);
}
var sqArr = arr.map(square);
console.log("sqArr Arrray: " + "[" + sqArr + "]");

/* The [pop()] method removes the last elemetn from an array and returns
 * that element
 */
var p = arr.pop();
console.log("p is : " + p);

/* The [push()] method adds one or more elemnts to the end of an array
 * and returns the new length of the array
 */
arr.push(13);
console.log("Current Array: " + '[' + arr + ']');

/* The [reduce()] method executes a reducer function on each member of
 * the array resulting in a single output value
 */
const reducer = (accumulator, cur) => accumulator + cur;
console.log("Arr sum: " + arr.reduce(reducer));

/* The [reduceRight()] method applies a function against an accumulator and
 * each value of the array (from right-to-left) to reduce it to a single value
 */
console.log("Arr sum: " + arr.reduceRight(reducer));

/* The [reverse()] method reverses an array in place
 */
arr.reverse();
console.log("Current Array: " + '[' + arr + ']');

/* The [shift()] method removes the first element from an array and returns
 * that removed element
 */
arr.shift();
console.log("Current Array: " + '[' + arr + ']');

/* The [slice()] method returns a shallow copy of a portion of an array into
 * a new array object selected from begin to end
 */
var slice = arr.slice(5, 9);
console.log("Slice Array: " + '[' + slice + ']');

/* The [some()] method tests whether at least one element in the array passes
 * the test implemented by the provided function
 */
function odd(x){
    return x % 2 == 1;
}
console.log("There at least exist one odd element in arr: " + arr.some(odd));

/* The [sort()] method sorts the elements of an array in place and returns the array
 */
arr.sort();
console.log("Current Array: " + '[' + arr + ']');

/* The [splice()] method changes the contents of an array by removing or replacing
 * existing elements and/or adding new elements
 */
arr.splice(3, 0, 3);
console.log("Current Array: " + '[' + arr + ']');

/* The [toString()] method returns a string representing the specified array
 * and its elements
 */
console.log("toString Array: " + arr.toString());

/* The [unshift()] method adds one or more elements to the beginning of an array
 * and returns the new length of the array
 */
arr.unshift(7, 9);
console.log("Current Array: " + '[' + arr + ']');

/* The [values()] method returns a new Array Iterator object that contains the values
 * for each index in the array
 */
var v = arr.values();
for (j of v){
    console.log(j);
}