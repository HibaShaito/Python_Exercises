# Mode: Easy, Exercise 4
"""
Exercise 4
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number.
 The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

-> Solution: https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
"""

def is_in_list(a:list,num:int):
    if num in a:
        return True
    return False


if __name__  == "__main__":
    a=[10,3,5,3,6,7,3,4]
    a.sort()
    while True:
        try:
            num=int(input("Enter a number: \n"))

            if is_in_list(a,num):
                print(f'{num} is in {a}')
            else:
                print(f'{num} is not in {a}')
            break
        except Exception:
            print("Please enter a number!")

