#ctrl+/=(make everything a comment)

# name = "Mukesh"
# age = 26
# sal = 200000.50

name,age,sal="Mukesh",27,2000000

# approach: 1

# print(name)
# print(age)
# print(sal)
# print(name,age,sal)

# Approach:2

# print("Name is",name)
# print('Age is',age)
# print('Salary is',sal)

# Approach:3

print('Name is %s Age is %d Salary is %g' %(name,age,sal))

# Approach: 4

print('Name is {} age is {} Salary is {}' .format(name,age,sal))
print('Age is {} name is {} Salary is {}' .format(name,age,sal))


