"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 15-Mar-2020
File name: Ex_Sheet_1_Num_3.py

Description: This script calculates the area of a triangle, given its base and height.
"""

def triangleArea(b,h):
    """
    Function triangleArea(b,h) calculates and returns the area of a triangle 
    of base 'b' and height 'h' in input.
    
    Parameters:
        b (float): base of the triangle.
        h (float): height of the triangle.
    
    Returns:
        A (float): area of the circle.
    """
    
    A = 0.5 * b * h
    
    return A


def main():
    """
    Function main() defines two baraibles base and heigth and computes the area 
    of a triangle that base and height.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # base and height of the triangle. Choosing base = 1.0 and height = 2.0
    # we can test that the area is 1.0 
    base = 1.0
    height = 2.0
    
    # area of the triangle
    area = triangleArea(base, height)
    
    # Print section
    print("Base = {}, Height = {} - Area of the triangle = {}".format(base, height, area))
    

if __name__ == "__main__":
    main()