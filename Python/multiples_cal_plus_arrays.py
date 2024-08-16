# This program will calculate the multiples of specific number
# For multiples, it's requied the formula m=k*i
# m stands for multiple, it's the result
# k is a constant number
# n is a natural number

k = 2
n = 100
m = []

# For loop, this will calculate the multiples of 2 in range of 100 numbers, starting in 0, add them to an array and print 
for i in range(n+1):
    m.append(k * i)

print("Multiples of 2:", m)
# Print an empty space
print()
# Print specifiy number of the array by it's postion index
print("In postion 50 the number is:", m[50])
# Print an empty space
print()
# Print the index of a specficy number in the array. Warning using index() method, the value must exist on the array.
print("The number 100 is at the postion:", m.index(100))
# Print an empty space
print()
# Extra array methods.
print("Array count repeated values:", m.count(2), "\nArray Length:", len(m), "\n")
# Print an empty space
print()
# Order Reversed
print("Reversed Array:", list(reversed(m)))
# Adding an extra values into the array
m_eddited = m.copy()
# Adding a number at the of the list
m_eddited.append(2)
# Combining arrays
p =[5,76,23,745,123,2,5,123,2,5,75,43,12,2]
m_eddited.extend(p)
print("Original Array:\n", m, "\nNew Edited Array:\n", m_eddited, "\n")
# Print an empty space
print()
print("Array count repeated values:", m_eddited.count(2), "\nArray Length:", len(m_eddited), "\n")
m_eddited_not_sorted = m_eddited.copy()
# Print an empty space
print()
# Sort the Array
m_eddited_sorted = m_eddited_not_sorted.copy()
m_eddited_sorted.sort()
print("Not Sorted Array:\n", m_eddited_not_sorted, "\nSorted Array:\n", m_eddited_sorted)