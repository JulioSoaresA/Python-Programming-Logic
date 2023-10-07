# Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2m².
# Difficult: Easy
# 1L = 2m²

width = float(input('Width of the wall in meters: '))
height = float(input('Height of the wall in meters: '))
mm = width * height
l = mm / 2

print(f'Your wall has the dimension of {width}m x {height}m and its area is {mm}m².')
print(f'To paint this wall, you will need {l}L of paint.')
