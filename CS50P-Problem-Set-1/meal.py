# meal.py

"""
Meal Time (https://cs50.harvard.edu/python/2022/psets/1/meal/)
Spec:
Input a time as '#:##' or '##.##' using a 24-hour clock
Output if its breakfast, lunch, or dinner time. If not, don't provide an output.
All meal times below are considered 'inclusive' As long as we are in the range, we should get the output
'breakfast time' = 7:00-8:00
'lunch time' = 12:00-13:00
'dinner time' = 18:00-19:00

From the assignment:
    'Structure your program per the below, wherein convert is a function (that can be called by main)
    that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
    For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).'
def main():
    ...
def convert(time):
    ...
# Note: This is necessary for the cs50 tester so it can test 'convert(time)' on its own.
# We'll omit it from out personal version
if __name__ == "__main__":
    main()
"""

def main():
    stime = input("What time is it? ")
    ftime = convert(stime)
    
    if 7.0 <= ftime <= 8.0:
        print("breakfast time")
    elif 12.0 <= ftime <= 13.0:
        print("lunch time")
    elif 18.0 <= ftime <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time:str) -> float:
    # First, let's convert the Input into hours and minutes
    hours, minutes = time.strip().split(":")
    
    # Convert str to floats
    # If minutes = 30, we'd like that to be 0.5, so we div by 60 as well
    m = float(minutes)/60
    h = float(hours)
    
    # Find result and return
    ftime = h + m
    return ftime

#if __name__ == "__main__":
    #main()

main()