# File: Week11 - Cash Register.py
# Name: Adrian Rybinski
# Date: February 23, 2020
# Course: DSC 510 - Introduction to Programming
# Assignment: 11.1
# Desc: Allow user to add items to a cart and print a receipt with totals.

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class CashRegister:
    def __init__(self):
        self.total = 0.00
        self.count = 0
        print('Welcome to My First Convenience Store!!!')

    def add_item(self, price):
        self.count = self.count + 1
        self.total = self.total + price

    def getTotal(self):
        return self.total

    def getCount(self):
        return self.count

def print_receipt():
    print('\nFirst Convenience Store')
    print('123 Main Street')
    print('My Town, IL 60606')
    print('-------------------------')
    print('Shopping Receipt')
    print('-------------------------\n')
    print('Your purchase total is: {}'.format(locale.currency(shopping_cart.getTotal())))
    print('Total number of items in your cart: {}'.format(shopping_cart.getCount()))
    print('Thanks for shopping with us.  We hope to see you soon')


shopping_cart = CashRegister()

while True:
    more = input("Would you like to add an item to your cart? Y or N\n").upper()
    if more == 'Y':
        try:
            item_price = float(input('Enter the price of item: '))
        except ValueError:
            print('Invalid Entry.  Please enter a number')
        else:
            shopping_cart.add_item(item_price)
    elif more == 'N':
        print_receipt()
        break
    else:
        print('Invalid Entry.  Please enter Y or N.')
