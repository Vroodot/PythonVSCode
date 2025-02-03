# coke.py
"""
https://cs50.harvard.edu/python/2022/psets/2/coke/

Spec:
Create a machine that sells bottles of coke for 50 cents, but only accepts quarters, dimes, and nickels (25, 10, 5)

Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once we've hit 50 cents, output the change we owe.
We can assume that the use will only input intergers, and ignore any coins that don't fit the assignment.
"""

# Initialize the amount due
amount_due = 50


while amount_due > 0:
    print("Amount due: " + str(amount_due))
    coin_input = int(input("Insert Coin: "))

    # If our coin is of an acceptable denomination, we'll accept the input
    if coin_input == 5 or coin_input == 10 or coin_input == 25:
        amount_due -= coin_input # <- implicit breakpoint: if a_d >= 0, break
    # Otherwise we run the loop again

# At this point, we've broken out of the loop

# We call str(abs(... to return a positive value as a string
change = str(abs(amount_due))
print("Change Owed: " + change)
