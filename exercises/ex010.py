# Make a program that reads how much money a person has in their wallet and shows how much money they can buy.
# Consider US$1.00 = R$5.17
# Dificult: Easy

rs = float(input('How much money do you have in your wallet? R$'))
us = rs / 5.17

print(f'With R${rs:.2f} you can buy US${us:.2f}')
