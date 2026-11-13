# It checks how fast they completed a 5 km run.

name = input("What is your name? ")
time = input("How many minutes did you take to run 5 km? ")

if time.isdigit():
    time = int(time)
    if time <= 30:
        print(name, "finished 5 km in", time, "minutes. Great job!")
    else:
        print(name, "finished 5 km in", time, "minutes. Keep practicing!")
else:
    print("Please enter a valid number.")

# Example run 1
# Inputs: Alex, 25
# Output: Alex finished 5 km in 25 minutes. Great job!

# Example run 2
# Inputs: Sam, 35
# Output: Sam finished 5 km in 35 minutes. Keep practicing!

# Example run 3
# Inputs: Alex, abc
# Output: Please enter a valid number.
