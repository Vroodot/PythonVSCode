# tip.py

"""
Below, we can see that most of the calculator is complete.
We just have to finish out the TODO list
https://cs50.harvard.edu/python/2022/psets/0/tip/
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
def dollars_to_float(d):
    # TODO
def percent_to_float(p):
    # TODO
main()

Spec:
`dollars_to_float(d)` is expecting a String (formatted as $##.##)
    I need convert that value to a float without the dollar sign
`percent_to_float(p)` is expecting a String (formatted as ##%)
    I need to remove the trailing percent sign and convert from percent to float
    For example: 15% -> 0.15

According to the Spec, we can safely assume that the user will input cooperate and input values in the expected formats
"""
# So, I don't need to touch this
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    # I'm pretty sure that lstrip("$") would also work
    # But this one feels straight forward given the static input format
    dollars = float(d.removeprefix("$"))
    return dollars

def percent_to_float(p: str) -> float:
    # Same as above, but with rstrip("%")
    # We divide by 100 to move the decimal left two places
    percent = float(p.removesuffix("%"))/100
    return percent

main()

# This one was mostly fill-in the blank
# We just had to use the proper String methods, then convert to floats
# Since we were converting from percentage to float, we divided by 100
