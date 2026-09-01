# 1. Display Python keywords
import keyword

print(keyword.kwlist)


# 2. Count the number of Python keywords
import keyword

print(len(keyword.kwlist))


# 3. Create variables with underscore
name = "Komal"
user_name = "Komal"

print(name)
print(user_name)


# In Python, variable names cannot normally contain
# special symbols like @, #, $, %, -, etc.
# We can use letters, numbers, and underscore _.


# 4. Variable starting with a number
# 9name = "Komal"
# SyntaxError: invalid decimal literal


name1 = "Komal"
student2 = "Komal"
_1name = "Komal"

print(name1)
print(student2)
print(_1name)


# 5. Assign multiple variables with multiple values
name, age, city = "Komal", 23, "Hyd"

print(name)
print(age)
print(city)


# 6. Assign multiple variables to a single value
x = y = z = 10

print(x)
print(y)
print(z)


# 7. Reassign a variable to a different value
name = "Komal"
print(name)

name = "Babu"
print(name)


# 8. Swap variables using a third variable
a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)


# 9. Swap variables using Python's multiple assignment
a = 10
b = 20

a, b = b, a

print(a)
print(b)


# 10. Swap variables using arithmetic
a = 10
b = 20

a = a * b
b = a / b
a = a / b

print(a)
print(b)


# 11. Create variables
name = "Komal"
age = 23

print(name)
print(age)


# 12. Delete a variable
name = "Komal"
print(name)

del name

# print(name)
# NameError: name 'name' is not defined


# 13. Single-line comment

name = "Komal"
print(name)


# 14. Multi-line comment
# We are learning Python
# This comment has multiple lines

name = "Komal"
print(name)