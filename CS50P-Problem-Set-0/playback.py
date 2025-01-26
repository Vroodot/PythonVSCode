# playback.py

# Goal: Create a script that replaces all white space with a single elipses
# i.e " " = "..."

# Get the user input
print("User Input: ", end="")

# Get input, replace all " "(whitespace) with "..."(elipses)
x = input().replace(" ", "...")
print(x)

"""
Notes:
This one was relatively straightforward, 
its just a 1:1 replacement.

However, if you were to have multiple spaces, each instance
would get replaced exactly. So "  " would become "......"

https://docs.python.org/3/library/stdtypes.html#string-methods
"""