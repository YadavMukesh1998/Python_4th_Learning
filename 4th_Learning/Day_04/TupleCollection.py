# Tuple: It is a collection which is ordered and unchangeable. In Python tuple are written with round brackets().
# Tuple is immutable, it means the below mentioned are not possible.
# 1. we can not modify existing value
# 2. we can not append new value
# 3. we can not insert new value.
# 4. we can not remove a value.
#***==================================================================***

# How to create tuple?
# Ans.:
# mytuple=("apple", "Banana","Orange")
# print(mytuple)

# How to access tuple?
# mytuple=("apple", "Banana","Orange")
# print(mytuple[1])
# print(mytuple[-1])

# How to identify range of tuple?

# mytuple=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(mytuple[2:4])
# print(mytuple[-4:-1])


#Changing tuple Values:
# Note: by default tuple do not allow to change the value bcoz it is immutable.but there is work around.
# Change the tuple to list the do modification and again change it to tuple.

# Example:01
# mytuple=["apple","banana","cherry","orange","kiwi","melon","mango"]
# mylist=list(mytuple)
# mylist[0]="MUKESH"
# print(mylist)

# mytuple=tuple(mylist)
# print(mytuple)

# Example:02 : reading tuple items using loop.

# mytuple=["apple","banana","cherry","orange","kiwi","melon","mango"]
# for i in mytuple:
#     print(i)

# How to search a item is available in the tuple or not?
# mytuple=["apple","banana","cherry","orange","kiwi","melon","mango"]
# if "apple" in mytuple:
#     print("Yes! Apple is present")
# else:
#     print("No!Apple is not present")

# how to find the length of the list?
mytuple=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(len(mytuple))