# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
# Your code here
My_dict = {'Raghu':25 , 'Chiru':24}
print(My_dict)
{'Raghu': 25, 'Chiru': 24}

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
# Your code here
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4
print(my_dict)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
# Your code here
d = {'name': 'John', 'age': 25, 'city': 'New York'}
d.keys()
dict_keys(['name', 'age', 'city'])

# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
# Your code here
d = {'python': 3, 'java': 2, 'c++': 1}
d.values()
dict_values([3, 2, 1])

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
# Your code here
d = {'name': 'Alice', 'age': 30, 'city': 'London'}
if 'age' in d:
    print(True)
else:
    print(False)
True
# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
# Your code here
d = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
removed_key = d.pop('temp')
print(d)
{'a': 1, 'b': 2, 'c': 4}

# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
# Your code here
d = {'math': 85, 'science': 92, 'english': 78}
sum_of_d = sum(d.values())
print(sum_of_d)
255

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
# Your code here
sq = {x:x**2 for x in range(1,6)}
print(sq)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
# Your code here

# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
# Your code here
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d1.update(d2)
print(d1)
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
# Your code here
d = {'person': {'name': 'Raghu', 'age': 25}}
print(d)
{'person': {'name': 'Raghu', 'age': 25}}

# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
# Your code here
d = {'person': {'name': 'Raghu', 'age': 25}}
name = d['person']['name']
print(name)
Raghu

# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
# Your code here
list_dict = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print(list_dict)
{'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}

# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
# Your code here
dict1 = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
dict1['fruits'].append('orange')
print(dict1)
{'fruits': ['apple', 'banana', 'orange'], 'colors': ['red', 'blue']}

# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
# Your code here
d = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(d)
{'coordinates': (10, 20), 'rgb': (255, 0, 0)}

# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
# Your code here
d = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
e  =  d['coordinates'][0]
print(e)
10

# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
# Your code here
d = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print(d)
{'vowels': {'e', 'a', 'i'}, 'consonants': {'b', 'c', 'd'}}

# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
# Your code here
d = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
d['vowels'].add('o')
print(d)
{'vowels': {'e', 'o', 'a', 'i'}, 'consonants': {'b', 'c', 'd'}}

# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
# Your code here
 d = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(d)
{'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}

# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
# Your code here
d = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
name = d['company']['department']['employee']['name']
print(name)
john

# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
# Your code here
d = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print(d)
{'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}

# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
# Your code here
d = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
for key,value in d.items():
    print(f"{key}:{type(value)}")
int:<class 'int'>
float:<class 'float'>
str:<class 'str'>
bool:<class 'bool'>

# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
# Your code here
d = {'len': len, 'str': str, 'int': int}
print(d)
{'len': len, 'str': str, 'int': int}

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
# Your code here

# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
# Your code here
dict = {'double': lambda x: x*2, 'square': lambda x: x**2}
print(dict)
{'double': lambda x: x*2, 'square': lambda x: x**2}

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
# Your code here

# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
# Your code here
dict = {'list': list, 'dict': dict, 'set': set}
print(dict)
{'list': list, 'dict': dict, 'set': set}

# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")
# Your code here

# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
# Your code here
dict = {'a': None, 'b': None, 'c': None}
print(dict)
{'a': None, 'b': None, 'c': None}

# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
# Your code here
dict = {'a': None, 'b': None, 'c': None}
dict = {k:(0 if v is None else v) for k,v in dict.items()}
print(dict)
{'a': 0, 'b': 0, 'c': 0}

# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
# Your code here
dict = {'is_active': True, 'is_admin': False}
print(dict)
{'is_active': True, 'is_admin': False}

# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
# Your code here
dict = {'is_active': True, 'is_admin': False}
count = sum(v is True for v in dict.values())
print(count)
1

# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
# Your code here
dict = {'z1': 3+4j, 'z2': 1+2j}
print(dict)
{'z1': (3+4j), 'z2': (1+2j)}

# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
# Your code here
dict = {'z1': 3+4j, 'z2': 1+2j}
magnitude = {k:abs(v) for k ,v in dict.items()}
print(magnitude)
{'z1': 5.0, 'z2': 2.23606797749979}

# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
# Your code here
nest_dict = {'level1':{'level2':{'level3':{'level4':'deepvalue'}}}}
print(nest_dict)
{'level1': {'level2': {'level3': {'level4': 'deepvalue'}}}}


# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
# Your code here
nest_dict = {'level1':{'level2':{'level3':{'level4':'deepvalue'}}}}
nest_dict['level1']['level2']['level3']['level4']
'deepvalue'

# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
# Your code here
range_dict =  {'r1': range(3), 'r2': range(5)}
print(range_dict)
{'r1': range(3), 'r2': range(5)}

# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
# Your code here

# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
# Your code here

# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
# Your code here

# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
# Your code here

# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
# Your code here

# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
# Your code here
dict = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print(dict)
{'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}

# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
# Your code here

# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
# Your code here
nest_dict = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(nest-dict)
{'config': {'db': {'host': 'localhost', 'port': 5432}}}

# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
# Your code here
nest_dict = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
nest_dict['config']['db']['port']
5432

# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
# Your code here
tup_dict = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print(tup_dict)
{'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}

# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
# Your code here
tup_dict = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
tup_dict['points'][0]
(1, 2)

# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
# Your code here
set_dict = {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print(set_dict)
{'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}

# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
# Your code here 
set_dict = {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
