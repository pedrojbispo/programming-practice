# Fibonacci sequence is a mathematical problem
# Definition: F0 = 0 ; F1 = 1 and Fn = Fn-1 + Fn-2 for n>1
# Calculate the first 100 Fibonacci sequence numbers

fib = []
fib_num = 0
n=100

for i in range (n+1):
    if i == 0:
        fib.append(0)
    if i == 1:
        fib.append(1)
    if i>=2:
        fib_num = fib[i-1] + fib[i-2]
        fib.append(fib_num)
print(fib)