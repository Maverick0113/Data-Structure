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