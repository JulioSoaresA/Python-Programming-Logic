# Make a program that reads the name of four studants and shows the order of the presentation
# Difficult: Easy

import random

first_studant = input('Type the name of the first studant: ')
second_studant = input('Type the name of the second studant: ')
third_studant = input('Type the name of the third studant: ')
fourth_studant = input('Type the name of the fourth studant: ')

list_of_studants = [first_studant, second_studant, third_studant, fourth_studant]

random.shuffle(list_of_studants)

print('The order of the studants is: {}'.format(list_of_studants))
