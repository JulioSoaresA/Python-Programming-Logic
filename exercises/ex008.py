# Make a program that reads a value in meters and displays it converted to kilometers, hectometers, decameters, decimeters, centimeters and millimeters.
# Difficult: Easy

m = float(input('Write a distance in meters: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'The distance of {m}m corresponds to:')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')
