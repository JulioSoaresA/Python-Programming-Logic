# Make a program that reads any angle and shows on the screen the value of the sine, cosine and tangent of that angle.
# Difficult: Easy

from math import sin, cos, tan, radians

angle = float(input('Enter the angle: '))
sine_angle = sin(radians(angle))
cosine_angle = cos(radians(angle))
tangent_angle = tan(radians(angle))

print(f'The sine of {angle} is {sine_angle:.2f}')
print(f'The cosine of {angle} is {cosine_angle:.2f}')
print(f'The tangent of {angle} is {tangent_angle:.2f}')
