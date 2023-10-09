# Make a program that reads the name of three students and shows the name of one of them.
# Difficulty: Easy

from random import choice

first_student = input('First student: ')
second_student = input('Second student: ')
third_student = input('Third student: ')

choiced_student = choice([first_student, second_student, third_student])

print(f'The choiced student was {choiced_student}')
