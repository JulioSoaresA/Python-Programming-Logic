# Make a program that reads something from the keyboard and shows its primitive type and all possible information about it on the screen.
# Difficult: Easy

anything = input('Write anything: ')

print(f'Primitive value: {type(anything)}')
print(f'Only spaces: {anything.isspace()}')
print(f'Its a number: {anything.isnumeric()}')
print(f'Its alpha: {anything.isalpha()}')
print(f'Its alphanum: {anything.isalnum()}')
print(f'Its in upper: {anything.isupper()}')
print(f'Its in lower: {anything.islower()}')
print(f'Its in caps: {anything.istitle()}')
