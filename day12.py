#FOR LOOP PROBLEMS
#important problems
# 1. print numbers from 1 to 10 in one line

for n in range(1, 11):
    print(n, end=' ')
print()

#2. print even numbers from 5 to 30 in one line
for n in range(5, 31):
    if n % 2 == 0:
        print(n, end=' ')
print()

#3. print odd numbers from 5 to 30 in one line
for n in range(5,30):
    if n % 2 != 0:
        print(n, end=" ")
print()

#4. print numbers divisible by 5 from 1 to 30 in one line
for n in range(1, 30):
    if n % 5 == 0:
       print(n, end=" ")
print()

#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for n in range(1,101):
    if n % 5 == 0 and n % 7 == 0:
        print(n, end=" ")
print()

#6. sum of numbers from 10 to 25 
sum = 0 
for n in range(10, 26):
    sum += n 
print(f'Sum of numbers from 10 and 25 is {sum}')

#7. sum of numbers in list [4,3,2,5,6,7] 
numbers = [4,3,2,5,6,7]

sum = 0
for n in numbers:
    sum += n 
print(f'the sum of the list is {sum}')

#8. multiplication table of a number
# n = int(input("enter a number: "))

# for z in range(1,11):
#     print(n*z)


#9. factorial 
n = int(input())

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)

#9. fibonacci 
a = 0
b = 1 
n = 10 
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b 
print()

#10. reverse a string
        # 012345
string = 'rakesh'
rev = ''
for i in range(len(string)-1, -1, -1):
    rev = rev + string[i]
print(f'Revers of {string} is {rev}')

#11. count vowels in a string
s = input()

count = 0 

for n in s:
    if n in "aeiou":
        count += 1
print(count)

#12. count z's and y's in a string
s = input()

count = 0 

for n in s:
    if n == "z" or n == "y":
        count += 1
print(count)


#13. check whether a number is prime number or not 
n = int(input())

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")




#WHILE LOOP PROBLEMS
#print 1 to 10 with while loop
#print even numbers from 1 to 10
#print numbers divisible by both 5 and 7 from 1 to 500 
#count digits
#reverse a number
#palindrome number 
#palindrome string without slicing, without built in function
#armstrong number
