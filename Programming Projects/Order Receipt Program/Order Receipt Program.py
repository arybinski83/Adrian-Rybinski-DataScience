# File: Week4-Receipt with function.py
# Name: Adrian Rybinski
# Date: December 22, 2019
# Course: DSC 510 - Introduction to Programming
# Assignment: 4.1
# Desc: Calculate the installation cost of fiber optic wire and display a receipt to client.

print('Welcome to the Fiber Optic Store\n')
buyer = input('Please enter your company name:\n')
length = float(input('Please specify the needed length of fiber optic cable in feet:\n'))
if length > 500:
    cost = 0.50  # cost of fiber optic wire per foot if order over 500 feet
elif 250 < length <= 500:
    cost = 0.70  # cost of fiber optic wire per foot if order over 250 and less or equal to 500
elif 100 < length <= 250:
    cost = 0.80  # cost of fiber optic wire per foot if order over 100 and less or equal to 250
else:
    cost = 0.87  # cost of fiber optic wire per foot if order 100 or less (default rate)


def order_amt(length, cost):  # Total calculated cost of fiber optic wire
    total = length * cost
    return 'Order Total: $'+"{:0.2f}".format(total) # Order total displayed to 2 decimal places with additional text


print('Thank you for your order. All order(s) will be processed within 3 to 5 business days.')
print('Below is your detailed order receipt.\n')
print('Ordered by: ' + buyer)
print('Quantity Ordered: ' + "{:0.2f}".format(length) + ' feet')  # Formatted order quantity to display 2 decimal places
print('Cost per foot: $' + "{:0.2f}".format(cost))  # Formatted cost per foot to display 2 decimal places
print(order_amt(length, cost))  # Total order amount called up from function
print('Please remit payment within 30 days from the order date.')
