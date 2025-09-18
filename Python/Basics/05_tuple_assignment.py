# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
# Your code here
a = tuple(range(0,11))
print(a)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
# Your code here
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(t))
10

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
# Your code here
t = ('a', 'b', 'c', 'd', 'e')
t[2]
'c'

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
# Your code here
t = (23, 45, 12, 67, 34, 89, 56)
max(t)
89

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
# Your code here
t = (1, 5, 2, 5, 3, 5, 4, 5, 6)
t.count(5)
4

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
# Your code here
mdt = (2,3.4,'Raghu',True)
print(mdt)
(2, 3.4, 'Raghu', True)

# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
# Your code here
t = ('java', 'python', 'c++', 'javascript')
t.index('python')
1

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
# Your code here
t = (10, 20, 30, 40, 50)
if (25 in (t)):
    print('True')
else:
    print('False')
False

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
# Your code here
t = tuple(range(2,12,2))
print(t)
(2, 4, 6, 8, 10)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
# Your code here 
num = (15, 23, 31, 42, 56, 78)
avg = sum(num)/len(num)
print('Average:' , avg)
Average: 40.833333333333336