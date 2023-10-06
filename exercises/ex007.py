# Make a program that reads two notes of a student, calculate and show your avarage.
# Difficult: Easy

n1 = float(input('Write the first note: '))
n2 = float(input('Write the second note: '))

avarage = (n1 + n2) / 2

print('The avarage between {:.1f} and {:.1f} is {:.1f}'.format(n1, n2, avarage))
