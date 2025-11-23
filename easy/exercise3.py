# Mode: Easy, Exercise 3
"""
Exercise 3
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""
def extract_first_last (l :list):
    if  len(l) ==0:
        return "The list is empty"
    return [l[0],l[-1]]

if __name__ == "__main__":
    result= extract_first_last([5, 10, 15, 20, 25])
    print(result)