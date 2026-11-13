# This program asks for the user's name and age.
# It checks the age and displays a message.

name = input("What is your name? ")
age = input("How old are you? ")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print(name, "is", age, "years old and is an adult.")
    else:
        print(name, "is", age, "years old and is a minor.")
else:
    print("Please enter a valid age.")

# Example run 1
# Inputs: Daniel, 20
# Output: Alex is 20 years old and is an adult.

# Example run 2
# Inputs: Sam, 12
# Output: Sam is 12 years old and is a minor.

# Example run 3
# Inputs: Lily, 35.5
# Output: Please enter a valid age.
