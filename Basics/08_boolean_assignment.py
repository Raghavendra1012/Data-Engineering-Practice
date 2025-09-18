# BOOLEAN DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Check if a number is both even and greater than 10
print("SOLVED EXAMPLE:")
print("Check if a number is both even and greater than 10")
number = 16
is_even = number % 2 == 0
is_greater_than_10 = number > 10
result = is_even and is_greater_than_10
print(f"Number: {number}")
print(f"Is even: {is_even}")
print(f"Is greater than 10: {is_greater_than_10}")
print(f"Both conditions: {result}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Check if 25 is greater than 20 and less than 30
print("Question 1: Check if 25 is greater than 20 and less than 30")
# Your code here
a,b = 20,30
if 25>a & 25<b :
    print(True)
else:
    print(False)
True
# Question 2: Check if string "python" is equal to "Python" (case sensitive)
print("\nQuestion 2: Check if string 'python' is equal to 'Python' (case sensitive)")
# Your code here
str1 = 'python'
str2 = 'Python'
if str1 == str2 :
    print(True)
else:
    print(False)
False

# Question 3: Check if 15 is divisible by both 3 and 5
print("\nQuestion 3: Check if 15 is divisible by both 3 and 5")
# Your code here
a,b = 3,5
if 15%a & 15%b == 0:
    print(True)
else:
    print(False)
True

# Question 4: Check if 7 is not equal to 8
print("\nQuestion 4: Check if 7 is not equal to 8")
# Your code here
a = 8
if 7!= a:
    print(True)
else:
    print(False)
True
# Question 5: Check if 100 is greater than 50 or less than 25
print("\nQuestion 5: Check if 100 is greater than 50 or less than 25")
# Your code here
x,y = 50,25
z = 100
if z>x or z<y:
    print(True)
else:
    print(False)
True

# Question 6: Check if 0 is falsy in Python
print("\nQuestion 6: Check if 0 is falsy in Python")
# Your code here

# Question 7: Check if empty string "" is falsy in Python
print("\nQuestion 7: Check if empty string '' is falsy in Python")
# Your code here

# Question 8: Check if 42 is truthy in Python
print("\nQuestion 8: Check if 42 is truthy in Python")
# Your code here

# Question 9: Check if 10 is between 5 and 15 (inclusive)
print("\nQuestion 9: Check if 10 is between 5 and 15 (inclusive)")
# Your code here
a,b = 5,15
c = 10
if a<= c <=b:
    print(True)
else:
    print(False)
True

# Question 10: Check if 3.14 is greater than 3 and less than 4
print("\nQuestion 10: Check if 3.14 is greater than 3 and less than 4")
# Your code here 
a,b = 3,4
c= 3.14
if c>a and c<b:
    print(True)
else:
    print(False)
True