"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 04-Mar-2020
File name: template_example.py

Description:    This script is a template to be followed by any script that you define. 
                In this example we take two integer numbers, add them and then multiply them.
                Finally we print them on screen.
"""

def powNum(a,b):
    """
    Function powNum(a,b) exponentiates number 'a' to the power 'b' and returns the result as output 'c'.
    
    Parameters:
        a (int; float)
        b (int; float)
    
    Returns:
        c (int; float)
    """
    
    # calculation of a^b and assignment to variable c
    c = a**b
    
    # output c
    return c

def mulNum(a,b):
    """
    Function mulNum(a,b) multiplies number 'a' and 'b' and returns their product as output 'c'.
    
    Parameters:
        a (int; float)
        b (int; float)
    
    Returns:
        c (int; float)
    """
    
    # calculation of a*b and assignment to variable c
    c = a*b
    
    # output c
    return c

def addNum(a,b):
    """
    Function addNum(a,b) adds number 'a' and 'b' and returns their sum as output 'c'.
    
    Parameters:
        a (int; float)
        b (int; float)
    
    Returns:
        c (int; float)
    """
    
    # calculation of a+b and assignment to variable c
    c = a+b
    
    # output c
    return c

def main():
    """
    This is a docstring (DOCumentation STRing). 
    Always add documentation strings to the functions the you define.
    Documentation strings should explain what the function does, its inputs and its outputs.

    Input and output of each function should be described in details, 
    using the "Parameters" and "Returns" sections of the docstring, using the format:
        
        variableName (variableType)
        
    like:
        
        x (int)
    
    If more than one varible type is compatible with the function, separate all the possible variable types using a ';', like:
        
        x (int; float)
    
    If there are no inputs or if the functions doesn't return anything, just write "None", 
    as in the case of main() function.
    
    Function main() is the main function of the code and it is used to manage the high-level flow of the code, 
    in particular, it manages:
        - the definition of variables,
        - the access to data (when necessary), 
        - the calls to other more specific functions,

    Here below is how a possible docstring for function main() might be written:
        
    Function main() defines two variables 'x' and 'y' and computes their sum, product and exponentiation.
    Finally, it prints on screen the results.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # variable definition
    x = 17
    y = -1
    
    # addition x+y calling function addNum(a,b) and assignment to variable z
    z = addNum(x,y)
    
    # product x*y calling function mulNum(a,b) and assignment to variable w
    w = mulNum(x,y)
    
    # exponentiation x^y calling function powNum(a,b) and assignment to variable p
    p = powNum(x,y)
    
    # Print section
    print("Sum: x+y=({})+({})={}".format(x,y,z))
    print("Product: x*y=({})*({})={}".format(x,y,w))
    print("Exponentiation: x^y=({})^({})={}".format(x,y,p))
    
    
if __name__ == "__main__":
    # Python interpreter accesses your code from this block
    # Remember to document possibly each line of code, explaining what it does and why you decided to do that
    # To run code press "Run" in the "Run" section of Spyder's top panel.
    
    # call function main()
    main()

