# How to create a string variable

# Example: ways of creating string variables
# s="Mukesh"
# s='Mukesh'
# s=str("Mukesh")
# s=str('Mukesh')

#Example: creating empty string variables
# name=""
# name=''
# name=str()

# mutable:  cannot change the value of variable
# immutable: can change the value of the variable any time

# string is muatble or immutable????? >>> immutable

# str1="welcome"
# print(id(str1))
#
# str1=str1+ "to python"
# print(id(str1))

# if the value is changed after updation then it is immutable


# Example:3 : + and * with strings

# str="welcome"
# print(str+"Programming")

# print(str*10)  #>>> welcomewelcomewelcomewelcomewelcomewelcomewelcomewelcomewelcomewelcome

# ========================================================================================================

# Slicing: We can extract some portion of the string, find the n.um of char in the string, we can get the string, we can reverse the string

# Example:04: Slicing
#starting index always starts with 0 position
#ending index come from 1st position.

# str="welcome"
# print(str[1:3])
# print(str[:6]) #welcom here starting index is 0 by default.
# print(str[3:])
#
# print(str[1:-1]) #elcom: last one char removed
# print(str[1:-2]) #elco last two char removed

# Example: ord() and chr()

# print(ord("A")) #65: returns the ASCII code for the character
#
# print(chr(65)) #A : character represented by ASCII number.


# Example: 6 : max(), min() & len()

# print(max("abc"))
# print(min("abc"))
# print(len("abc"))


# Example: 07 ; in and not in operators -- return true/false
#
# s="welcome"
# print("come" in s) #true
# print("lome" in s) #false
#
# print("come" not in s)
# print("lome" not in s)

# Example: 08 : String Comparison

#Example8: String comparison with relational operators

# print("tim" == "tie")         # False
# print("free" != "freedom")    # True
# print("arrow" > "aron")       # True
# print("right" >= "left")      # True
# print("teeth" < "tee")        # False
# print("yellow" <= "fellow")   # False
# print("abc" > "1")            # True


# Example: 09 : Testing Strings  True/ False

# s = "welcome to python"
# print(s.isalnum())                    # False
#
# print("Welcome".isalpha())           # True
# print("first Number".identifier()) # False
# print("2012".isdigit())              # True
# print(s.islower())                   # True
# print("WELCOME".isupper())           # True
# print(" ".isspace())                 # True


# Example :10 : Searching for substring

# Example10: Searching for substrings
# s = "welcome to python"

# print(s.endswith("thon"))      # True
# print(s.startswith("good"))    # False
# print(s.find("come"))          # 3
# print(s.find("become"))        # -1  (not found)
# print(s.count("o"))            # 3  (Returns number of occurrences of substring in the string)


# Example: 11: Converting String in different format

# s = "String in PYTHON"
#
# s1 = s.capitalize()
# print(s1)   # String in python
#
# s2 = s.title()
# print(s2)   # String In Python
#
# s3 = s.lower()
# print(s3)   # string in python
#
# s4 = s.upper()
# print(s4)   # STRING IN PYTHON
#
# s5 = s.swapcase()
# print(s5)   # sTRING IN python
#
# s6 = s.replace("in", "on")
# print(s6)   # Strong on PYTHON


# Example:12 Reverse a String

#Method-1

s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reversed string is", rev_str)