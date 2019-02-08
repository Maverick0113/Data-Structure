arr = [64, 13, 88, 48, 97, 74, 83, 96, 5, 52, 59, 79]
print("Current Array: ", end = "")
print(arr)

# append(x)
# add an item[x] to the end of the list
arr.append(16)
print("Append -> 16")
print("Current Array: ", end = "")
print(arr)

# extend(iterable)
# extend the list by appending all the items from
# the iterable[iterable]
arr.extend([55, 77, 20])
print("Extend -> [55, 77, 20]")
print("Current Array: ", end = "")
print(arr)

# insert(i, x)
# Insert an item[x] at a given position[i]
arr.insert(2, 18)
print("Insert -> 18 at 2")
print("Current Array: ", end = "")
print(arr)

# remove(x)
# remove the first item from the list whose value is
# equal to [x]
arr.remove(74)
print("Remove -> 74")
print("Current Array: ", end = "")
print(arr)

# pop([i])
# remove the item at the given position[i] in the list,
# and return it. if no index is specified, remove and
# return the last item in the list
arr.pop()
print("Pop ->")
print("Current Array: ", end = "")
print(arr)

# clear()
# remove all items from the list
arr.clear()
print("Clear ->")
print("Current Array: ", end = "")
print(arr)

arr = [52, 90, 18, 68, 41, 82, 34, 61, 52, 62, 14, 10, 22]
print("Current Array: ", end = "")
print(arr)

# index(x, [start], [end])
# return zero-based index in the list of the first item
# whose vlue is equal to [x]
print("41 is located at: ", end = "")
print(arr.index(41))

# count(x)
# return the number of times [x] appears in the list
print("There are ", end = "")
print(arr.count(52), end = "")
print(" 52's in arr")

# sort(key = None, reverse = False)
# sort the items of the list in place
arr.sort()
print("Current Array: ", end = "")
print(arr)

# reverse()
# reverse the elements of the list in place
arr.reverse()
print("Current Array: ", end = "")
print(arr)

# copy()
# return a shallow copy fo the list
copy = arr.copy()
print("Current Array: ", end = "")
print(arr)
print("Current Copy: ", end = "")
print(copy)

# Copy Slice
# arr[:]
# return all elements in array
print("Copy Slice: ", end = "")
print(arr[:])

# Front Slice
# arr[x:]
# return all elements at and after position [x]
print("Front Slice: ", end = "")
print(arr[7:])

# Back Slice
# arr[:y]
# return all elements before position [y]
print("End Slice: ", end = "")
print(arr[:5])

# Interval Slice
# arr[x:y]
# return all elements at and after position [x] and 
# before positon [y]
print("Interval Slice: ", end = "")
print(arr[3:9])

# Reverse Slice
# arr[::-1]
# return all elements in arr in reverse
print("Reverse Slice: ", end = "")
print(arr[::-1])