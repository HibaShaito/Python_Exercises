# Mode: Easy, Exercise 1
""" 
Exercise 1
Write a python program that:
Asks the user about their name
Save it in a variable called "name"
Asks the user about their age
Save it in a variable called "age"
Print a string stating "The user -name- is -age- years old
"""

if __name__ == "__main__":
    name=input ("What is your name? \n")

    while(True):
        try:
            age=int(input("what is your age? \n"))
            print(f"The user name is {name} and age is {age}")
            break
        except ValueError:
            print('PLease enter a valid number for age.\n')
