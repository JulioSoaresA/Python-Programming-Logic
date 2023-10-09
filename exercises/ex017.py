# Make a program that reads the length of the cathetus opposite and adjacent of a right triangle, calculate and show the length of the hypotenuse.
# Difficult: Easy

co = float(input('Length of the cathetus opposite: '))
ca = float(input('Length of the adjacent cathetus: '))
hipotenuse = (co ** 2 + ca ** 2) ** (1/2)

print(f'The hypotenuse will measure {hipotenuse:.2f}')
