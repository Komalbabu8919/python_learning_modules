# Import required modules
import math
import random
import sys
import platform
import collections
import itertools
from datetime import datetime, date, timedelta

#Math module
# print('------------Math Module----------------')
# print('Square root of 25:', math.sqrt(25)) #5
# print('Power (2^3):', math.pow(2, 3)) #8
# print('Value of PI:', math.pi) #3.14
# print('Ceiling of 4.3:', math.ceil(4.3))  #5
# print('Ceiling of -4.3:', math.ceil(-4.3)) # 4
# print('Floor of 4.8:', math.floor(4.8))    #4
# print('Floor of -4.8:', math.floor(-4.8))   # -5
# print('Factorial of 5:', math.factorial(5))  # 120
# print('GCD of 12 and 18:', math.gcd(12, 18)) # 6
# print('LCM of 12 and 18:', math.lcm(12,18))   #36
# print('Sine of 45 radians:', math.sin(45))   #0.8509035245341184
# print('Cosine of 45 radians:', math.cos(45)) #0.5253219888177297
# print('Tangent of 45 radians:', math.tan(45)) # 1.6197751905438615
# print('Degrees of 45 radians:', math.degrees(45))#2578.3100780887044
# print('Radians of 45 degrees:', math.radians(45))#2578.3100780887044
# print()
# print()

# Random Module
# print('-------------Random Module--------------')
# # random float between 0.0 to 1.0 including
# print('Random float:', random.random())
# # random float between x to y including
# print('Random float from x to y:', random.uniform(1,10))
# # random does not take any arguments
# # print(random.random(1,10)) 
# # random int between x to y including
# print('Random integer:', random.randint(1, 100)) # 2
# # random int between x to y-1 in steps of z 
# print('Random integer from 1 to 20 insteps of 2:', random.randrange(1,21,2)) #13
# #random with list
# numbers = [10, 20, 30, 40, 50]
# print('Random choice:', random.choice(numbers))
# random.shuffle(numbers)
# print('Shuffled list:', numbers) # [40, 10 , 20, 30 ,50]
# print('Random sample:', random.sample(numbers, 3)) #[20, 10 50]
# print()
# print()


# Sys module
# print('----------------Sys Module----------------')
# print('Python version:', sys.version) #3.12.2
# print('Python executable:', sys.executable)# C:\Users\Komal Babu\AppData\Local\Programs\Python\Python311\python.exe
# print('Number of command-line arguments:', len(sys.argv))# 1
# print()
# print()

# Platform Module
# print('--------------Platform Module--------------')
# print('Operating system:', platform.system())   #Operating system: Windows
# print('Machine:', platform.machine())           #Machine: AMD64
# print('Processor:', platform.processor())       #Processor: Intel64 Family 6 Model 154 Stepping 4, GenuineIntel
# print('Python implementation:', platform.python_implementation())  #Python implementation: CPython
# print()
# print()

# # Collections Module
# print('---------------Collections Module----------------')
# Counter
# words = ['rakesh', 'adhithya', 'rakesh', 'charan', 'adhithya', 'rakesh']
# counter = collections.Counter(words)
# print('Word count:', counter) #Counter({'rakesh': 3, 'adhithya': 2, 'charan': 1})
# # Most common item
# print('Most common:', counter.most_common(1))#[('rakesh', 3)]
# print('Most common:', counter.most_common(2))#[('rakesh', 3), ('adhithya', 2)]
# print()

# # DefaultDict
# student_marks = collections.defaultdict(list)
# student_marks['Alice'].append(90)
# student_marks['Alice'].append(85)
# student_marks['Bob'].append(78)
# print('Student marks:', dict(student_marks))#: {'Alice': [90, 85], 'Bob': [78]}
# print()

# ## NamedTuple
# Student = collections.namedtuple('Student', ['name', 'age', 'course'])
# student = Student('John', 20, 'Python')
# print('Student tuple:', student)#Student(name='John', age=20, course='Python')
# print('Student name:', student.name)#John
# print('Student age:', student.age)#20
# print('Student course:', student.course)#python
# print()
# print()

# # Itertools module
# print('--------------Itertools Module--------------')
# items = ['A', 'B', 'C']
# # Permutations
# print('Permutations:')
# permutations = itertools.permutations(items)
# print(list(permutations))
# # Combinations
# print('Combinations:')
# combinations = itertools.combinations(items, 2)
# print(list(combinations))
# # Product
# print('Cartesian product:')
# cproduct = itertools.product([1, 2], ['A', 'B'])
# print(list(cproduct))
# print()
# print()

# # Datetime Module
# print('------------------Datetime Module-------------------')
# # Current date and time
now = datetime.now()
print('Current date and time:', now)
# Current date 
today = date.today()
print('Today\'s date:', today)
# Format date and time
print('Formatted date:', now.strftime('%d-%m-%Y'))
print('Formatted time:', now.strftime('%H:%M:%S'))
# Create a specific date time
birthday = datetime(2000, 5, 15, 19, 50, 50)
print('Example birthday:', birthday)
# Add days
future_date = today + timedelta(days=7)
print('Date after 7 days:', future_date)
# Subtract days
past_date = today - timedelta(days=7)
print('Date 7 days ago:', past_date)

