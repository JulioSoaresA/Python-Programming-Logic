# Make a program that asks how many km a rental car has traveled and how many days it has been rented.
# Difficult: Easy

rent_days = int(input('How many days did you rent the car? '))
km_traveled = float(input('How many kilometers did you travel? '))
total = (rent_days * 60) + (km_traveled * 0.15)

print(f'The total to pay is R${total:.2f}')
