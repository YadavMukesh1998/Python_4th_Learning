# 1_List:
# What is list collection?
# Ans. : List is a collection which is ordered and changeable. In python list are written with square brackets[].
# And list is mutable.
# in the list every item is representing by index  number and index start from 0.



# Example_01_How to create a list?

# mylist1=[10,20,30,40] #one single variable can hold multiple values.
# mylist2=["Apple","Banana", "Cherry"]
# mylist3=["Apple", 10, "Banana", 10.5]
# mylist=list()  #my list is empty.

# How to print the value from the list?
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

# How to access the item from list?

# mylist=["Apple","Banana", "Cherry"]  #index start from 0.
#
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])        #it will get the last one

# Range of indexes

# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# when you want to any selected element from the list
#
# print(mylist[2:5])
# print(mylist[-4:-1])


# How to change item values?
# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(mylist)

# How to change any item?
# mylist[0]="orange"
# print(mylist)

# How to raed items using loop statement?

# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# for i in mylist:
#     print(i)


# How to search a item is available in the list or not?

# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
#
# if "apple" in mylist:
#     print("yes, apple is present")
# else:
#     print("No, apple is not present")


# how to find the length of the list?

# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(len(mylist))


# How to add a new item in the list? >>for that 2 function are available>>> 1. append(), 2. insert().

# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
#
# mylist.append("orange")  #this will add the new item at the end.
# print(mylist)
#
# # what if we want a insert a new item in between?
#
# mylist.insert(2,"Mukesh")
# print(mylist)

# How to remove item form the list?

# 1. By using pop()
# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# mylist.pop(0)
# print(mylist)
#
# # 2. By using del()
# del mylist[2]
# print(mylist)
#
# # 3. By using clear()
# mylist.clear()
# print(mylist)


# How to copy this list to some other list?
# Ans_01: By using list()
# mylist1=["apple","banana","cherry","orange","kiwi","melon","mango"]
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)

# Ans_02: Copy()
# mylist1=["apple","banana","cherry"]
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)

# How to combine 2 lists?

# 01_Using "+" operator:

# list1=[1,2,3,4]
# list2=["M, A, N, K"]
# list3=list1+list2
# print(list1+list2)
# print(list3)


# 02_Using Looping staement;
list1=[1,2,3,4]
list2=["M, A, N, K"]

for i in list2:
    list1.append(i)
print(list1)

for i in list1:
    list2.append(i)
print(list2)


# 03_By using extend()
list1=[1,2,3,4]
list2=["M, A, N, K"]
list1.extend(list2)
print(list1)





