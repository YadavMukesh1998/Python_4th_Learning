
# Set Collection: Set is a collection which is unordered and unindexed. In python sets are written in {}.

# Example:01: How to create set?

# myset={"apple","banana","cherry", "Mukesh"}
# print(myset)  #{'apple', 'Mukesh', 'banana', 'cherry'}

# Example:02: Accessing items from set

# myset={"apple","banana","cherry", "Mukesh"}
#
# for i in myset:
#     print(i)


# Example:03: To check the value exists in set or not?
# myset={"apple","banana","cherry", "Mukesh"}
#
# print("Mukesh" in myset)
# print("Mukesh2" in myset)

# Examples:04: Add/Update items to set.
# add() - add single item to set,  update() - add multiple item to the set

# myset={"apple","banana","cherry", "Mukesh"}
# myset.add("Yadav")
# print(myset)

# myset={"apple","banana","cherry", "Mukesh"}
# myset.update(["Mango", "Grapes"])
# print(myset)

# Example;05: How to find the number of items in set?

# myset={"apple","banana","cherry", "Mukesh"}
# print(len(myset))


# Example:07: Remove item from set
# myset={"apple","banana","cherry", "Mukesh"}

# myset.remove("banana")
# myset.remove("Banana")   #>incorrect "B"
# print(myset)
# myset.discard("apple")
# print(myset)

# Example:07: Clear all values from set
# myset={"apple","banana","cherry", "Mukesh"}
# myset.clear()
# print(myset)

# Example:08: Joining 2 sets ::: Union()
# set1={1,2,3,4}
# set2={4,6,8,10}
# set3=set1.union(set2)
# print(set3)

#Another way to join 2 sets?
set1={1,2,3,4}
set2={"a","b","c"}
set1.update(set2)
print(set1)
print(set2)