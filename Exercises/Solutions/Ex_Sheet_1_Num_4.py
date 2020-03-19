"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 15-Mar-2020
File name: Ex_Sheet_1_Num_4.py

Description: This computes the product of elements in a list.
"""

def listMul(l):
    """
    Function listMul(l) computes and returns the product of elements in list l.
    
    Parameters:
        l (List): input list.
    
    Returns:
        prod (float): product of the elements of list l.
    """
    
    # initialization for variable prod
    prod = 1.0
    
    for element in l:
        prod *= element # a *= b is equivalent to a = a * b
    
    return prod


def main():
    """
    Function main() defines a list and computes the product of its elements.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # test list
    lis = [10, 20, 30]
    
    # product of the elements in the list
    product = listMul(lis)
    
    # Print section
    print("List = {} - Product of its elements = {}".format(lis, product))
    

if __name__ == "__main__":
    main()