# LoopingStatement: 1. while loop, 2. for loop

#while loop: where you have to start initialization:is required,
#                                    condition: when you have to stop
#                                    increment: how much value increment,
#

# example: print 1_______________10 numbers.
#
a = 1 #initialization

while a<=10:  #condition
    print(a)
    a=a+1 #increment
    print("Done!!!")   #this time print is part of loop, indentation.
print("Done!!!")

# example: print 10 to 1.

i=10
while i>=1:
    print(i)
    i=i-1
print("Done!!!")