# Jumping Statement:
# Break and Continue

for i in range(1,10):
    if i==5:
        break
    print(i)
print("Program Exited!")

for i in range(1,10):
    if i==3 or i==6 or i==7:  #jumping to next
        continue
    print(i)
print("Program Exit!!!!")

for i in range(3,7,2):

    print(i)


