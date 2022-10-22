# File: Week5 - Calculator.py
# Name: Adrian Rybinski
# Date: January 12, 2020
# Course: DSC 510 - Introduction to Programming
# Assignment: 5.1
# Desc: Provide a method to perform various calculations for user

def calculateAverage(): # defines the function for the average calculation
    for i in range(0, n_times):
        number = int(input('Enter Number:\n'))
        n.append(number)
        avg = sum(n) / n_times
    print("The average of the numbers is", round(avg, 2))

def performCalculation(math_op): # defines the function for the remaining calculation options
            if math_op == '+':
                print('The result of your calculation is: ' + "{:0.2f}".format(add))
            elif math_op == '-':
                print('The result of your calculation is: ' + "{:0.2f}".format(dif))
            elif math_op == '*':
                print('The result of your calculation is: ' + "{:0.2f}".format(multi))
            elif math_op == '/':
                print('The result of your calculation is: ' + "{:0.2f}".format(div))
            else:
                print('Error in calculation. Please review your entries and try again.')

print('Hello and welcome to our Super Calculator!!!')
try_again = 'Y'
while try_again == 'Y':
    math_op = input('Which math operation would you like to perform? Select +, -, *, /, or avg.\n').lower()
    if math_op == 'avg':
        n_times = int(input('How many numbers would you like to average?\n'))
        n = []
        calculateAverage()
    elif math_op == '+' or math_op == '-' or math_op == '*' or math_op == '/':
        number_1 = input('Please enter the first number for this calculation:\n')
        number_2 = input('Please enter the second number for this calculation:\n')
        add = float(number_1) + float(number_2)
        dif = float(number_1) - float(number_2)
        multi = float(number_1) * float(number_2)
        div = float(number_1) / float(number_2)
        performCalculation(math_op)
    else:
        print('Invalid Entry. The only valid operations are +, -, *, /, and avg.')
    try_again = input('Would you Like to perform another calculation? Y or N:\n').upper()
    if try_again == 'N':
        print('Thanks for using our calculator.  Hope to see you soon!!')
    elif try_again == 'Y':
        print()
    else:
        print('Invalid Entry.  Please enter Y or N.')
        try_again = input('Would you Like to perform another calculation? Y or N:\n').upper()
