# einstein.py

"""
https://cs50.harvard.edu/python/2022/psets/0/einstein/
Spec:
Using E = mc^2
Prompt the user for mass in kg (as integer) and then outputs
the equivalent number of Joules (E) (also as an int)

According to spec, we can safely assume the input will be an int.

Without accessing the math or sci libraries, here's my 1st (verbose) attempt.
"""


# E= mc^2
def mass_energy_equiv() -> int:

    # We're returning E, so our program has to define and solve mc^2
    # mass is our input variable
    # since user inputs are always Strings, we'll use `int()` to convert it
    m = int(input("Mass(kg) = "))

    # c = Speed of Light
    c = 300000000

    # We need c to the power of 2
    # We could do (c * c), but lets try using some of the functions available to us through Python's Standard Lib
    # pow(base, exponent)
    c_squared = pow(c, 2)

    # Now let's put it all together
    # Might as well do it phonetically
    E = (m * c_squared)
    print("E = ", E)
    return E

# We'll actually call the function down here, since it was defined above.
mass_energy_equiv()

"""
First attempt. Went a bit verbose so I could spell out my logic, but there's
definitely ways to 'clean' this up.
For instance, there's no need to save `c` to memory.
"""
