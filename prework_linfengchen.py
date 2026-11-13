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