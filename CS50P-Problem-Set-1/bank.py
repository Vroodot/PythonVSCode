# bank.gd

"""
Spec:
Recreate the rules of S7E24 of Seinfeld.
Implement a program that prompts the user for a greeting. If the greeting starts with 'hello', output '$0'
If the greeting starts with an 'h' but isn't 'hello', output '$20'
If neither of those happen, output '$100'
We should also ignore any leading whitespace and not worry about case
"""

greeting:str = input("Greeting: ").lstrip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
