n = int(input("enter a number"))

for n in range(1,n+1):
    print(n*'*')
    print()


n = int(input("enter a number"))

for n in range(n,0,-1):
    print(n*'*')
    print()

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
    print()


for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)
    print()

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()