# interpreter.py

"""
(https://cs50.harvard.edu/python/2022/psets/1/interpreter/)
Spec:
Get user input as a str formatted as 'x y z'
x = int
y is '+' '-' '*' or '/'
z = int

We want to output the answer, rounded to a single decimal place

According to Spec we can make the following assumptions:
1. The user won't be dividing by 0
2. The user will use correct formatting


"""

# using .split(" ") we can divide each into x y z as defined by spec
# juuuust in case there is an external whitespace error, I also called .strip()
x, y, z = input("Expression: ").strip().split(" ")
# Now we can cast x and z as integers
x = int(x)
z = int(z)
# There may be a more clever way to cast y to the proper symbol, but if you only have a hammer?
match y:
    # a will act as the variable for our result in this match
    case "+":
        a = x + z
        a = round(float(a), 1)
    case "-":
        a = x - z
        a = round(float(a), 1)
    case "*":
        a = x * z
        a = round(float(a), 1)
    case "/":

        a = x / z
        a = round(float(a), 1)
    case _:
        pass
print(a)
