# Make a program that reads a number and shows its multiplication table.
# Difficult: Easy

n = int(input('Write a number to see its multiplication table: '))
i = int(input('Write the first number of the table: '))
j = int(input('Write the last number of the table: '))

print('-' * 12)
for x in range(i, j+1):
    print(f'{x:02} x {n} = {x * n:02}')
print('-' * 12)
