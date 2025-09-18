# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
# Your code here
a = 5+3j
print(a)
(5+3j)

# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
# Your code here
z = 7 - 2j
print(z.real)
7.0

# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
# Your code here
z = 4+6j
print(z.imag)
6.0

# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
# Your code here
a = (3 + 2j)
b = (1 + 4j)
print(a+b)
(4+6j)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
# Your code here
a = (2 + 3j)
b = (1 + 2j)
print(a*b)
(-4+7j)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
# Your code here
a = (6 + 8j)
Magnitude = abs(a)
print(Magnitude)
10.0

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
# Your code here
a = (5 - 7j)
b = a.conjugate()
print(b)
(5+7j)
# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
# Your code here
a,b = (10 + 5j) , (3 + 2j)
print(a-b)
(7+3j)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
# Your code here
a,b = (8 + 6j) , (2 + 1j)
res = a/b
print(res)
(4.4+0.8j)
# Question 10: Find the phase angle of complex number 1 + 1j
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
# Your code here 
import cmath
z = 1 + 1j
ang = cmath.phase(z)
print(ang)
0.7853981633974483