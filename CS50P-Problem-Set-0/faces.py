#faces.py

"""
https://cs50.harvard.edu/python/2022/psets/0/faces/
Spec
Expected Input are strings that may contain the
emoticons ":)" or ":("


Expected Output will convert
:) -> 🙂
:( -> 🙁

Task requirements:
1. Implement a function named 'convert' that accepts a str as input
    and returns the expected output as seen above.
2. Implement a function called main that prompts the user for input,
    calls convert on that input, and then prints the result.
NOTE: Be sure to call `main` at the bottom of the file.
"""

# First let's define convert using `def`
# I'm assuming that return types and static typing works similarly to
# GDscript, we shall see!
def convert(text:str ) -> str:
    # Save converted text as a variable//
    # Chain replace functions on the text argument
    # "find and" replace(from: str, to: str)
    converted_text = text.replace(":)", "🙂").replace(":(", "🙁")
    # Then we give the string back
    return converted_text

# Now we can define main()
def main():
    # We need to call the input function, which returns a str
    # Which means we can just pass the 'input()'
    # As an argument for `convert`
    text = convert(input("Input emoticon: "))
    print(text)

# All of our functions have been defined
# Since convert() is being called within `main()`
# We only need to call main() here

# Python is read top to bottom, so functions must be defined above
# To be called below. Think of it as a "load order"
main()


"""
Expected Behavior:
If I were to input the string ':) :( :) :('
then main should output '🙂 🙁 🙂 🙁'


AND IT WORKS!!!
"""
