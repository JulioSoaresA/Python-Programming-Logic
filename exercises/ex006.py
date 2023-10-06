# Make a program that reads a number and shows its double, triple and square root.
# Difficult: Easy
from math import sqrt

n = int(input('Write a nunber: '))

n2 = n * 2
n3 = n * 3
nsqrt = sqrt(n)

print(f'The double of {n} is equal to {n2}')
print(f'The triple of {n} is equal to {n3}')
print(f'The square root of {n} is equal to {nsqrt:.2f}')
