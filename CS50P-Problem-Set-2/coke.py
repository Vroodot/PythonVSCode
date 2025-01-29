# coke.py
"""
https://cs50.harvard.edu/python/2022/psets/2/coke/

Spec: 
Create a machine that sells bottles of coke for 50 cents, but only accepts quarters, dimes, and nickels (25, 10, 5)

Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once we've hit 50 cents, output the change we owe.
We can assume that the use will only input intergers, and ignore any coins that don't fit the assignment.
"""

# This will likely be using a while loop that's asserting a behavior

# In psuedo-code
# while amount_due < 50:
#    coin = int(input("Amount Due: "))
#    amount_due 
#