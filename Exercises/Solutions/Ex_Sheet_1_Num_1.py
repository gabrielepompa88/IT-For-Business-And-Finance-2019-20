"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 19-Mar-2020
File name: Ex_Sheet_1_Num_1.py

Description: This script calculates the radius of a circle, given length of its circumference.
"""

# List here (one for each line) all import necessary for your code to run.
# here we need 'math' modulus to access pi constat (pi = 3.14...)
from math import pi

def circleRadius(c):
    """
    Function circleRadius(c) calculates and returns the radius of a circle
    given in input a circumference of length 'c.
    
    Parameters:
        c (float): length of the circumference.
    
    Returns:
        radius (float): radius of the circle.
    """
    
    r = c / (2.0 * pi)
    
    return r


def main():
    """
    Function main() defines a variable circumference and computes the radius 
    of a circle with that circumference.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # length of the circumference: we test using a length equal to 2 * pi
    # such that the radius should be 1.0
    circumference = 2*pi 
    
    # radius of the circle
    radius = circleRadius(circumference)
    
    # Print section
    print("Circumference = {} - Radius = {}".format(circumference, radius))
    

if __name__ == "__main__":
    main()