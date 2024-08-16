# FizzBuzz Problem
# Objective: In a range of numbers, for the multiples of 3 print Fizz and for multiple of 5 print Buzz, if the number is both a multiple of 3 and 5 print FizzBuzz
# Formula for multiples: multiple = K * num (K is a constent)
# For solve this we need to check if the number is dividable by the multiple with a modulus (%) of 0, which is the remainder of the division. 
# Examples: 
# 21/3=7 with a remainder of 0, this is Fizz
# 40/5=8 with a remainder of 0 this is Buzz
# 30/5=6 and 30/3=10 with a remainder of 0, this is a FizzBuzz

k3 = 3
k5 = 5
num = 0
num_range = 51

fizz = []
buzz = []
fizzbuzz=[]
out_numbers = []

# For loop, this will calculate the multiples of 2 in range of 100 numbers, starting in 0, add them to an array and print 
for num in range(1, num_range):
    if(num % k3 == 0 and num % k5 != 0):
        fizz.append(num)
    if(num % k5 == 0 and num % k3 != 0):
        buzz.append(num)
    if(num % k3 == 0 and num % k5 == 0):
        fizzbuzz.append(num)
    if(num % k3 != 0 and num % k5 != 0):
        out_numbers.append(num)

print("Fizz:", fizz)
print("Buzz:", buzz)
print("FizzBuzz:", fizzbuzz)
print("Out Numbers:", out_numbers)
