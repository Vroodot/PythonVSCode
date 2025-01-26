# indoor_voice.py

# 1st attempt at the cs50p problem: [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/)
# Goal: Take an input String from the user and return one that isn't "yelling"



# 1st, get input from the user. We also stop the end param from making a new-line
print("Input: ", end="")

# Here, we store the user's input String, make sure only the first letter is capitalized, and we'll remove all the trailing white space just for fun.
i = input().capitalize().lstrip()
#desired solution for CS50 is something akin to: i = input().lower()

print(i)


"""
Scratch Paper:

Expected Behavoir
  1. Ask for input in the terminal
  2. Run the capitalize and lstrip methods on the input string
  3. Store that as `i`
  4. Print the inital input string with an "indoor voice"

Notes:
  After first test, it works!! Kind of.
  If the input contains multiple sentences, only the first one will be capitalized.
  It seems that capitalize() doesn't care about sentence structure or common society.
  If I wanted to get rid of leading whitespace as well, I could just use `strip().` The l/r prefix to picks side.

For the actual cs50p, they are likely wanting the use of `lower()` or `casefold()` since the goal is to only return an
LC-String. (Update: Yup, that hunch was correct!)

    Doc Pages Used To Answer CS50 Problem:
      [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

    Submitted Solution:
    # indoor.py

    # Goal: Take an input string and return a version of it that is in lowercase only
    print("YELL HERE: ", end="")
    print(input().lower())
"""
