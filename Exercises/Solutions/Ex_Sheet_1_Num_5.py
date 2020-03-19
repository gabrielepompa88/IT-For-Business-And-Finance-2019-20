"""
Author: Gabriele Pompa
Identification Number: ABCXYZ [substitute with your Unisi Identification Number]

Date: 15-Mar-2020
File name: Ex_Sheet_1_Num_5.py

Description: This computes the sum the first n numbers 1,2,...,n and test three
methods of calculation.
"""

def listSum_1(l):
    """
    Function listSum_1(l) computes and returns the sum of the elements of list l
    using a for loop over the list.
    
    Parameters:
        l (List): input list.
    
    Returns:
        sum_res (float): result of the sum of the elements of list l.
    """
    
    # initialization for variable prod
    sum_res = 0.0
    
    for element in l:
        sum_res += element # a += b is equivalent to a = a + b
    
    return sum_res


def listSum_2(l):
    """
    Function listSum_2(l) computes and returns the sum of the elements of list l
    using sum() function.
    
    Parameters:
        l (List): input list.
    
    Returns:
        sum_res (float): result of the sum of the elements of list l.
    """
    
    # sum of elements in l
    sum_res = sum(l)
    
    return sum_res

def testRes(n):
    """
    Function testRes(n) tests listSum_1 and listSum_2 with each other and
    against the benchmark n*(n+1)/2.
    
    Parameters:
        n (int): number of elements.
    
    Returns:
        test_12_flag (bool): flag, True if comparison between using listSum_1 
                             and listSum_2 is successful, False otherwise.
                             
        test_1benchmark_flag (bool): flag, True if comparison between using 
                                     listSum_1 and n*(n+1)/2 is successful, 
                                     False otherwise.
                                     
        test_2benchmark_flag (bool): flag, True if comparison between using 
                                     listSum_2 and n*(n+1)/2 is successful, 
                                     False otherwise.
    """
    
    # 1,2,...,n list definition using list comprehension
    lis = range(1,n+1)

    # benchmark sum
    sum_benchmark = 0.5 *n*(n+1)
    
    # sum of lis elements using the two methods
    sum_1 = listSum_1(lis)
    sum_2 = listSum_2(lis)
    
    # test 1: listSum_1 and listSum2
    test_12_flag = (sum_1 == sum_2)
    
    # test 2: listSum_1 against benchmark
    test_1benchmark_flag = (sum_1 == sum_benchmark)

    # test 2: listSum_2 against benchmark
    test_2benchmark_flag = (sum_2 == sum_benchmark)
        
    return test_12_flag, test_1benchmark_flag, test_2benchmark_flag

def main():
    """
    Function main() set n, and test the three sum methods.
    
    Parameters:
        None
    
    Returns:
        None
        
    """
    
    # n to test
    n = 50
    
    # call of testRes(n)
    test_12, test_1benchmark, test_2benchmark = testRes(n)
    
    # Print section
    print("We test: n = {}".format(n))
    print("listSum_1 == listSum2? {}".format(test_12))
    print("listSum_1 == n*(n+1)/2? {}".format(test_1benchmark))    
    print("listSum_2 == n*(n+1)/2? {}".format(test_2benchmark))    

if __name__ == "__main__":
    main()