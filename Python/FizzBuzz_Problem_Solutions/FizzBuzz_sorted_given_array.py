# FizzBuzz Problem
# Objective: In a range of numbers, for the all multiples of 3 print Fizz and for all multiples of 5 print Buzz, if a number is both a multiple of 3 and 5 print FizzBuzz
# Formula for multiples: multiple = K * num (K is a constent)
# For solve this we need to check if the number is dividable by the multiple with a modulus (%) of 0, which is the remainder of the division. 
# Examples: 
# 21/3=7 with a remainder of 0, this is Fizz
# 40/5=8 with a remainder of 0 this is Buzz
# 30/5=6 and 30/3=10 with a remainder of 0, this is a FizzBuzz

k3 = 3
k5 = 5
num = 0
num_arr = [5,12,51,23,56,15,99,80,68,1,4,43,87,98,10,34,30,14,7,8,50,24,36,75,60]
#num_range = 51

fizz = []
buzz = []
fizzbuzz=[]
out_numbers = []

num_arr_sort = num_arr.copy()
num_arr_sort.sort()
for num in num_arr_sort:
    if(num % k3 == 0 and num % k5 != 0):
        fizz.append(num)
        print("Fizz")
    if(num % k5 == 0 and num % k3 != 0):
        buzz.append(num)
        print("Buzz")
    if(num % k3 == 0 and num % k5 == 0):
        fizzbuzz.append(num)
        print("FizzBuzz")
    if(num % k3 != 0 and num % k5 != 0):
        out_numbers.append(num)
        print(num)

print()
print("Fizz:", fizz)
print("Buzz:", buzz)
print("FizzBuzz:", fizzbuzz)
print("Out Numbers:", out_numbers)
print("Original Arry:", num_arr)
print("Sorted Array:", num_arr_sort)