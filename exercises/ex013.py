# Make an algorithm that reads an employee's salary and shows his new salary, with a 15% increase.
# Difficult: Easy

salary = float(input('What is the employee salary? R$'))
increase = salary * 0.15
new_salary = salary + increase

print(f'The employee who earned R${salary:.2f}, with a 15% increase, will pass to earn R${new_salary:.2f}.')
