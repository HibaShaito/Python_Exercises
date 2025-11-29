# Mode:Easy, Exercise 2
"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?
Extras:

If the number is a multiple of 4, print out a different message. Ask the user for two numbers:
one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
if __name__=="__main__":
    while True:
        try:
            number=int(input("Enter a number: \n"))
            if(number%2==0):
                print("Your number is even")
                if(number%4==0):
                    print(f"{number} is a multiple of 4\n")

                    while True:
                        try:
                            num=int(input("Enter a number: \n"))
                            check=int(input(f"Enter a number to divide {num} by: \n"))
                            if num%check==0:
                                print(f"{num}/{check} divide evenly!(remainder of division is 0).")
                            else: 
                                print(f"{num}/{check} don't divide evenly!(remainder of division is not 0).") 

                            break
                    
                        except ValueError:
                            print("Please Enter valid numbers!")     

            elif (number%2==1):
                print("Your number is odd")

            break
        
        except ValueError:
                print("Please a valid number!")
