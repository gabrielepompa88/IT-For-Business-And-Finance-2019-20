"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 19-Mar-2020
File name: Ex_Sheet_1_Num_2.py

Description: This script scripts tests whether a number is even or odd.
"""

def isEven(n):
    """
    Function isEven(n) tests whether number 'n' is even or odd. 
    It returns True is n is even and False otherwise.
    
    Parameters:
        n (int): number to test.
    
    Returns:
        even_flag (bool): flag, True if n is even and False otherwise.
    """
    
    # `%` operator returns the remainder of an integer division. 
    # If the remainder of the division between `n` and `2` is 0, then n is even.
    # The result of the operation n % 2 == 0 is a boolean value that we store
    # into the variable even_flag
    even_flag = (n % 2 == 0)
    
    return even_flag


def main():
    """
    Function main() tests whether two numbers n1 and n2 are even or odd.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # numbers to test
    n1 = 10
    n2 = 17
    
    # test 
    is_n1_even = isEven(n1)
    is_n2_even = isEven(n2)
    
    # Print section
    if is_n1_even:
        print("n1 = {} is even".format(n1))
    else:
        print("n1 = {} is odd".format(n1))
        
    if is_n2_even:
        print("n2 = {} is even".format(n2))
    else:
        print("n2 = {} is odd".format(n2))
    

if __name__ == "__main__":
    main()