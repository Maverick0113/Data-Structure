s = {43, 95, 24, 21, 9, 19, 69, 94, 16}
print("Current Set: ", end = "")
print(s)

# len(s)
# return the number of elements in set [s]
print("The length of set is ", end = "")
print(len(s))

# x in s
# test [x] for membership in [s]
print("24 is in s, ", end = "")
print(24 in s)

# x not in s
# test [x] for non-membership in [s]
print("31 is not in s, ", end = "")
print(31 not in s)

# isdisjoint(other)
# return True if the set has no elements in common with [other]
o = {}
print("s is disjoint with o, ", end = "")
print(s.isdisjoint(o))

# issubset(other)
# set <= other
# test whether every element in the [set] is in the [other]
sub = {95, 9, 19}
print("sub is subset of s, ", end = "")
print(sub.issubset(s), end = ", ")
print(sub <= s)

# set > other
# test whether the [set] is a proper superset of [other]
print("set is proper superset of sub, ", end = "")
print(s > sub)

# union(*other)
# set | other | ...
# return a new set with elements from the set and all [others]
un1 = {95, 24, 1}
un2 = {94, 16, 3}
print("The union of s, un1, and un2 is: ", end = "")
print(s.union(un1, un2))
# print(s | un1 | un2)

# intersection(*other)
# set & other & ...
# return a new set with elements common to the set and all [others]
in1 = {43, 95, 24}
in2 = {24, 21, 9}
print("The intersection of s, in1, and in2 is: ", end = "")
print(s.intersection(in1, in2))
# print(s & in1 & in2)

# difference(*other)
# set - other - ...
# return a new set with elements in the set