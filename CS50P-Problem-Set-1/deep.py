# deep.py

"""
https://cs50.harvard.edu/python/2022/psets/1/deep/
Based on Douglas Adams' Hitchhiker's Guide

Spec:
Prompt the user for the anwser to 'The Great Question of Life, the Universe and Everything'
Output Yes if the user inputs "42", (case-insensitively!) "forty-two", or "forty two"
"""

# Just in case someone answsers with "Forty-Two", we don't want them to not get credit. So let's call `lower()` to prevent that from happening
answer: str = input("What is the Answer to the Great Question of Life, the Universe, and Everything?!?! ").lower().strip()


match answer:
    case "forty-two" | "42" | "forty two":
        print("Yes")
    case _:
        print("No")


"""
Expected Behavior:
The program should first look if the user typed 42 .
If not, then it will check to see if the answer is either forty-two or forty two regardless of case.

If I enter anything else, Deep Thought should politely but firmly tell me to shove it.

Running 1st test now!?
Hey it worked! I could even input things such as FOrtY TWo

I'm sure there are more explicit methods that I could use to see if the user answer was 'close enough.' Worth exploring later, but this fits spec.

Had a couple of minor syntax errors, just unlearning Godot specific stuff and learning the Python Docs, but it is working as intended and ready to submit!

After re-reading my lecture notes, I decided I probably ought to do a match statement just to get them into my toolbelt.
"""