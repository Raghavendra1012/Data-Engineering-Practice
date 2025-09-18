# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
# string1 = 'Python Programming'
string1[::-1]
'gnimmargorP nohtyP'

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
# Your code here
a = 'racecar'
if a == a:
    print('It is palindrome')
else:
    print("It is not palindrome")
It is palindrome


# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
# Your code here
a = 'Python is a great programming language'
word_count = len(a.split())
print("Number of words:",word_count)
Number of words: 6

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
# Your code here
str = 'hello world'
title_case_text = str.title()
print(title_case_text)
Hello World

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
# Your code here
string1 = 'Data Science'
len(string1)
12

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
# Your code here
text = 'Machine Learning'
text1 = text.replace(" ","_")
print(text1)
Machine_Learning

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
# Your code here
a = 'Python Programming Language'
a.startswith("python")
False

# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
# Your code here
str = 'Artificial Intelligence'
str[0:5]
'Artif'

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
# Your code here
a = "UPPERCASE"
a.lower()
'uppercase'

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
# Your code here
a = "Computer Science"
b = "aeiouAEIOU"
c = ""
for a in a:
    if a not in b:
        c += a
print(c)
Cmptr Scnc


# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
# Your code here

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
# Your code here
a = "listen"
b = "silent"
if sorted(a) == sorted(b):
    print("anagrams")
else:
    print("not anagrams")
anagrams

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
# Your code here
text = 'python programming language'
text1 = text.title()
print(text1)
Python Programming Language

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
# Your code here
a = "Hello World"
b = 'aeiouAEIOU'

c = ''.join(i for i in a if i not in b)
len(c)
8

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
# Your code here
a = "Python is a programming language"
b = a.split(' ')
max(b, key = len)
'programming'

# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
# Your code here
a = "Hello, World! How are you?"
b = ''.join(a for a in a if a not in string.punctuation)
b
'Hello World How are you'

# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
# Your code here
string = 'Python'
string.startswith('Python')
True

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
# Your code here
a = 'Hello World'
a.index('o')
4

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
# Your code here
string = 'apple,banana,orange'
string.split(",")
['apple', 'banana', 'orange']

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
# Your code here
list = ['Python', 'is', 'awesome']
a = " ".join(list)
print(a)
Python is awesome

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here
string = '12345'
print(string.isdigit())
True

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here
s = 'HelloWorld'
s.isalpha()
True

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here
a = "banana"
b = [a for a ,c in enumerate(a) if c == 'a']
print(b)
[1, 3, 5]


# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here
s = '  Hello World  '
s.strip()
'Hello World'

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here
s = 'programming'
s.endswith('ing')
True

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here
a = 'Hello World'
b = a.replace('o','0',1)
print(b)
Hell0 World

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here
a = 'Python is a programming language'
b = a.split(' ')
min(b,key = len)
a

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here
a = "Python programming is powerful"
count = sum(1 for word in a.split() if word.lower().startswith('p'))
print(count)
3

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
text = 'Hello World Python'
text[::-1]
'nohtyP dlroW olleH'

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here
mls = '''Hello 
Raghu
good 
morning'''
count = len(mls.splitlines(mls))
print(count)
4

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here
a = 'hello'
b = 'world'
common = set(a) & set(b)
print(common)
{'l', 'o'}

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here
import re

a = "abc123def456ghi789"
numbers = re.findall(r'\d+' , a)
print(numbers)
['123', '456', '789']

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here
a = 'A man a plan a canal Panama'
if 'A man a plan a canal Panama'== 'A man a plan a canal Panama':
    print('it is a palindrome')
else:
    print('it is not a palindrome')
    it is a palindrome
    
# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here
a = "((()))"
if a == a:
    print('balanced')
else:
    print('not balanced')
balanced

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 