#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#create same list with comprehension

# #for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)    # [2, 4, 6, 8, 10]
# #create same list with comprehension

# #for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a) #[(2, 3), (4, 1)]
#create same list with comprehension
a = [(x, y) for x in range(1, 5) if x % 2 == 0 for y in range(1, 4) if x + y == 5]

print(a)



# #set comprehension
# l = [3,4,3,5,6,7,6]
#create list, set, dict comrehension with above list
#list
# l = [3, 4, 3, 5, 6, 7, 6]

# a = [x * x for x in l]

# print(a)

# # set
# l = [3, 4, 3, 5, 6, 7, 6]

# a = {x * x for x in l}

# print(a)


# # Dictionary
# l = [3, 4, 3, 5, 6, 7, 6]

# a = {x: x * x for x in l}

# print(a)



# #function
# def numbers():
#     return 1 
#     return 2 
# n = numbers()
# print(n)  #1
# print(type(n)) #<class 'int'>

# #generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)
# print(type(n))        <class 'generator'>
print(next(n))    #1
print(next(n))     #2
print(n.__next__())  #3
print(n.__next__())  #4
# print(next(n))    # error

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))  #2
print(n.__next__())  #4
for x in n:      #6        The for loop automatically calls next() repeatedly.
    print(x)     #8

#write generator to generate odd numbers
def oddnumbers():
    for x in range(1,10):
        if x % 2 != 0:
            yield x
n = oddnumbers()

for x in n:
    print(x)    # 1 3 5 7 9 

#write generator to generate even numbers
def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x

n = evennumbers()

for x in n:
    print(x)   # 2 4 6 8 

#write generator to generate prime numbers

def primenumbers():
    for x in range(2, 20):
        count = 0

        for y in range(1, x + 1):
            if x % y == 0:
                count += 1

        if count == 2:
            yield x

n = primenumbers()

for x in n:
    print(x) 
