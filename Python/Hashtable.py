dictionary = {"Janurary" : 1, "February" : 2, "March" : 3,
              "April" : 4, "May" : 5, "June" : 6,
              "July" : 7, "August" : 8, "September" : 9,
              "October" : 10, "November" : 11, "December" : 12}
print("Current Hashtable: ", end = "")
print(dictionary)

# len(d)
# return the number of items in dictionary [d]
print("There are ", end = "")
print(len(dictionary), end = "")
print(" items in current hashtable")

# d[key]
# return the item of [d] with key [key]
print("The key -> ", end = "")
print("March", end = "")
print(" maps to value -> ", end = "")
print(dictionary["March"])

# d[key] = value
# set d[key] to [value]
print("d[Zero] -> 0")
dictionary["Zero"] = 0
print("Current Hashtable: ", end = "")
print(dictionary)

# del d[key]
# remove d[key] for [d]
print("del -> August")
del dictionary["August"]
print("Current Hashtable: ", end = "")
print(dictionary)

# key in d
# return True if [d] has a key [key], else False
print("December is in Current Hashtable: ", end = "")
print("December" in dictionary)

# key not in d
# return True if [d] not has a key [key], else False
print("Janurary not in Current Hashtable: ", end = "")
print("Janurary" not in dictionary)

# iter(d)
# return an iterator over the keys of the dictionary
it = iter(dictionary)
print("The iterator's next is: ", end = "")
print(next(iter(dictionary)))

# get(key, default)
# return the value for [key] if [key] is in the dictionary, else [default]
print("get -> November")
print("The key -> ", end = "")
print("November", end = "")
print(" maps to value -> ", end = "")
print(dictionary.get("November"))

# items()
# return a new view of the diciotnary's items, in pairs.
dic = dictionary.items()
print("items ->")
print("Current Dic: ", end = "")
print(dic)

# keys()
# return a new view of the dictionary's sorted
keys = dictionary.keys()
print("keys ->")
print("Current Keys: ", end = "")
print(keys)

# pop(key, default)
# if [key] is in dictionary, remove it and return its value, else return [default]
print("The popped key -> ", end = "")
print("September ", end = "")
print("returns -> ", end = "")
print(dictionary.pop("September"))
print("Current Hashtable: ", end = "")
print(dictionary)

# popitem()
# remove and return a (key, value) pair from the dictionary
# pairs are returned in LIFO open
print("popitem ->")
print("The popped pair is: ", end = "")
print(dictionary.popitem())
print("Current Hashtable: ", end = "")
print(dictionary)


# setdefault(key, default)
# if [key] is in the dictionary, return its value
# if not, insert [key] with a value of [default] and return [default]
dictionary.setdefault("Zero", 0)
print("setdefault -> (Zero, 0)")
print("Zero maps to -> ", end = "")
print(dictionary["Zero"])
print("Current Hashtable: ", end = "")
print(dictionary)

# update(other)
# update the dictionary with the key/value pairs from [other]
dictionary.update([("Zero", 1), ("Two", 2)])
print("update -> [(Zero, 0), (Two, 2)]")
print("Current Hashtable: ", end = "")
print(dictionary)

# values()
# return a new view of the dictionary's values
values = dictionary.values()
print("values ->")
print("Current Values: ", end = "")
print(values)

# copy()
# return a shallow copy of the dictionary
copy = dictionary.copy()
print("copy ->")
print("Current Hashtable: ", end = "")
print(dictionary)
print("Copy Hashtable: ", end = "")
print(copy)

# clear()
# remove all items from the dictionary
dictionary.clear()
print("clear ->")
print("Current Hashtable: ", end = "")
print(dictionary)