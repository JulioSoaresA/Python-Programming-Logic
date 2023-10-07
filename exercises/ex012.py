# Make an algorithm that reads the price of a product and shows its new price, with 5% discount.
# Difficult: Easy

product = float(input('Enter the price of the product: '))
discount = product * 0.05
new_price = product - discount

print(f'The product that cost R${product:.2f}, with 5% discount, will cost R${new_price:.2f}.')
