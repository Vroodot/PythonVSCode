# camel.py


"""
(https://cs50.harvard.edu/python/2022/psets/2/camel/)
Spec:
Create a function that inputs a camelCase str and output a snake_case str
According to the assignment, we can assume the input will always be in camelCase


Notes as I went through this problem:
    - We first need to find the hump in the camel 'C'
    - We can use Python for loops can iterate through characters in a string
        ```
        for cha in camelCase:
            print(cha)
        ```
"""

def main() -> None:
    camel = input("camelCase: ").strip()
    camel_to_snake(camel)

def camel_to_snake(camel: str) -> str:
    snake = ""
    for c in camel:
        # c = the individual character we are iterating on

        # now we can find the hump in the camel 'C'
        if c.isupper():
            # to convert to snake, we have to convert to lower, then add-front an `_`
            c = "_"+ c.lower()
        # We can compose the new string by adding each character back to snake as we iterate
        s = c
        snake += s
    print(snake)
# Expected Result: iterate through each character and construct the string back letter-by-letter


main()
