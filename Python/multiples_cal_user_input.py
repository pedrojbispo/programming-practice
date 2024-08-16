# This program will calculate the multiples of specific number
# For multiples, it's requied the formula m=k*i
# m stands for multiple, it's the result
# k is a constant number
# n is a natural number

global k
global n

# User input with validation.
valid_k = False
valid_n = False
while(valid_k == False):
    try:
        k = int(input("Constant: "))
    except ValueError:
        print("Numbers only please!")
    else:
        valid_k = True
    finally:
        print()
while(valid_n == False):
    try:
        n = int(input("Max Range of numbers: "))
    except ValueError:
        print("Numbers only please!")
    else: 
        valid_n = True
    finally:
        print()

m = []
# For loop, this will calculate the multiples of 2 in range of 100 numbers, starting in 0, add them to an array and print 
for i in range(n+1):
    m.append(k * i)

print("Multiples of " + str(k) + ":", m)