# There are 3 type of Control Statements.
from selectors import SelectSelector

#1. Conditional Statements:
#       if, if else, elif

# 2. Looping Statement
#       while, for

# 3. Jumping Statement
#         break, continue

# =======================================================================================

#1. Conditional Statements:
#       if, if else, elif

# Example:1
# A person is eligible to vote or not
# age>=18

# age = 25
# if age>=18:
#     print("Eligible for Vote")
# else:
#     print("Not eligible for Vote")

# ------------------------------------------------------
# Example:2

# if True:
#     print("True Condition")
# else:
#     print("false Condition")

# Example:3

# RRC_Active_State=1
#
# if RRC_Active_State:
#     print("Idle Mode")
# else:
#     print("Inactive Mode")

# signal_strength = 1
#
# if signal_strength:
#     print("Signal present")
# else:
#     print("No signal")

# Example:4 Find a number is even or odd number

# num=13
# if num%2==0:
#     print("Given number is Even")
# else:
#     print("Given Num is Odd")


# How to combine whole statement in a single line (Ternary Operator)
# Example:5

# num=11
# print("Even Number") if num%2==0 else print("Odd Number")

# Example:6 : if else - Multiple statement in single line

# a=5
#
# {print("hello"),print("python")} if a>=10 else {print("hi"),print("java")}


# Example:7: Multiple condition using elif

# Using Elif

weekno=12
if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tuesday")
elif weekno==4:
    print("Wednesday")
elif weekno==5:
    print("Thursday")
elif weekno==6:
    print("Friday")
elif weekno==7:
    print("Saturday")      
elif weekno==0:
    print("None")
else:
    print("Invalid Number")

# ============================================================================Practice Work
Mukesh="Blue"
if Mukesh=="Red" or Mukesh=="Blue":
    print("Good Man")
else:
    print("Bad Man")


