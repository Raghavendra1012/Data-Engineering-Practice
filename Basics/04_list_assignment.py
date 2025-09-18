# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")
# Your code here
sqr = [i**2 for i in range(1,11)]
print(sqr)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = sum(i for i in a if i%2 == 0)
print(b)
30

# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
# Your code here
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
b = list(set(a))
print(b)
[1, 2, 3, 4, 5, 6, 7]

# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
# Your code here
a = [64, 34, 25, 12, 22, 11, 90] 
a.sort(reverse= True)
print(a)
[90, 64, 34, 25, 22, 12, 11]

# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
# Your code here
a = [15, 23, 31, 42, 56, 78, 91]
b = sum(a)/len(a)
48.0

# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here

# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here
a = [45, 67, 23, 89, 12, 34, 78]
a.sort(reverse=True)
b = a[1]
print(b)
78

# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.reverse()
print(a)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
# Your code here
a = [1, 5, 2, 5, 3, 5, 4, 5, 6]
b = a.count(5)
print(b)
4

# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
# Your code here
prime nos = []
for i in range(2,51):



# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
# Your code here
a,b = [1, 2, 3, 4, 5],[4, 5, 6, 7, 8]
c = list(set(a)&set(b))
print(c)
[4, 5]

# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
# Your code here
a = [[1, 2], [3, 4], [5, 6]]
print(a)
[[1, 2], [3, 4], [5, 6]]

# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
lol = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sums = [sum(sublist) for sublist in lol]
print(sums)
[6, 15, 24]

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here
lol = [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
max_value = [max(sublist) for sublist in lol]
print(max_value)
[5, 9, 8]

# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
three_d_list = [
    [[1, 2], [3, 4]],
      [[5, 6], [7, 8]]
      ]
print(three_d_list)
[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
n = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

total_sum = 0
for a in n:
    for b in a:
        for c in b:
            total_sum += c

print(total_sum)
36

# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = []
for sublist in n:
    for num in sublist:
        if num % 2 == 0:
            even_numbers.append(num)
print(even_numbers)
[2, 4, 6, 8]

# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here
a = [1, "hello", 3.14, True, [1, 2, 3]]
print(a)
[1, 'hello', 3.14, True, [1, 2, 3]]

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here
list = ["apple", "banana", "cherry", "date"]
length = [len(list) for list in list]
print(length)
[5, 6, 6, 4]

# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
a = [(1, 'a'), (2, 'b'), (3, 'c')]
print(a)
[(1, 'a'), (2, 'b'), (3, 'c')]

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
a = [(1, 'a'), (2, 'b'), (3, 'c')]
first_elements = []
for i in a:
    first_elements.append(i[0])
print(first_elements)
    
[1, 2, 3]

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here
a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print(a)
[{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here
dict = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
name = []
for i in dict:
    name.append(i['name'])
print(name)
['Alice', 'Bob']

# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here
dict = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
max_age = max(person['age'] for person in dict)
print(max_age)
30

# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here
four_d_list = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print(four_d_list)
[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]

# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here
four_d_list = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
max_num = max(num for b1 in four_d_list for b2 in b1 for b3 in b2 for num in b3)
print(max_num)
16

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(list_of_sets)
[{1, 2, 3}, {4, 5, 6}, {8, 9, 7}]

# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
union = set().union(*list_of_sets)
print(union)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here
list_of_complex = [1+2j, 3+4j, 5+6j]
print(list_of_complex)
[(1+2j), (3+4j), (5+6j)]

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here
list_of_complex = [1+2j, 3+4j, 5+6j]
magnitude = [abs(c) for c in list_of_complex]
print(magnitude)
[2.23606797749979, 5.0, 7.810249675906654]

# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
# Your code here

# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
# Your code here

# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
# Your code here
 functions = [len, str, int, float]
 print(functions)
[<built-in function len>, <class 'str'>, <class 'int'>, <class 'float'>]

# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
# Your code here
 functions = [len, str, int, float]
 string = '123'
 res = [func(string) for func in functions]
 print(res)
[3, '123', 123, 123.0]

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
# Your code here

# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
# Your code here

# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
# Your code here

# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
# Your code here

# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
# Your code here
 none_values = [None, None, None, None]
 print(none_values)
[None, None, None, None]

# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
# Your code here
none_values = [None, None, None, None]
for i in range(len(none_values)):
    if none_values[i] is None:
        none_values[i] = 0
print(none_values)
[0, 0, 0, 0]

# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
# Your code here
bool = [True, False, True, False,True]
print(bool)
[True, False, True, False, True]

# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
# Your code here
bool = [True, False, True, False, True]
true_count = bool.count(True)
print(true_count)
3

# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
# Your code here

# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
# Your code here

# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
# Your code here

# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here

# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
# Your code here

# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here 