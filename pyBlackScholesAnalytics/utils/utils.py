"""
Author: Gabriele Pompa (gabriele.pompa@gmail.com)

Date: 20-May-2020
File name: utils.py
"""

# ----------------------- standard imports ---------------------------------- #
# for NumPy arrays
import numpy as np

# for Pandas Series and DataFrame
import pandas as pd

# for date management
import datetime as dt

# for Matplotlib plotting
import matplotlib.pyplot as plt

# to identify iterable data-structures
from collections.abc import Iterable

#-----------------------------------------------------------------------------#

def scalarize(x):
    """
    Reduce array x to scalar, if possible.
    """
    
    if is_iterable_not_string(x) and x.size == 1:
        return x.item()
    else:
        return x
    
#-----------------------------------------------------------------------------#

def iterable_to_numpy_array(x, sort=True, sort_func=None):
    """
    Create a 1-dim NumPy Array from a 1-dim Iterable with elements of the same type.
    If the iterable has elements of different data-type, it raises an error.
    
    If sort is True (default), returns a sorted array. Optionally uses a custom 
    function sort_funct to sort the iterable (default: ascending order).
    """
    
    if is_iterable_not_string(x) and test_same_type(x):
        if not isinstance(x, np.ndarray):
            x = np.array([xi for xi in x])
        return np.array(sorted(x, key=sort_func)) if sort else x
    else:
        return x
    
def homogenize(x, *args, **kwargs):
    """
    Utility function to homogenize variable x, calling:
        - function iterable_to_numpy_array()
        - fucntion scalarize()
    sequentially.
    """

    # convert x into a NumPy array if it is an Iterable of same data-type
    x = iterable_to_numpy_array(x, *args, **kwargs)
    
    # reduce x to a scalar, if possible
    x = scalarize(x)
    
    return x
    
#-----------------------------------------------------------------------------#

def coordinate(x, y, col_labels, ind_labels):
    """
    Utility function to coordinate the two scalar/np.ndarray variables x and y. 
    The following cases are considered:
        
        1) if x has length n and y has length m, then:
            x, y ---> [m rows x n cols] pd.DataFrame defining a mesh-grid
            of coordinates (see np.meshgrid documentation)
            
        2) if x has length n and y is a scalar, then:
            x ---> [1 row x n cols] pd.DataFrame with x as values
            y ---> [1 row x n cols] pd.DataFrame with y value repeated n-times along the row

        3) if x is a scalar and y has length m, then:
            x ---> [m rows x 1 col] pd.DataFrames with x value repeated m-times along the column
            y ---> [m rows x 1 col] pd.DataFrame with y as values
        
        4) if both x and y are scalar, then:
            y, x ---> [1 row x 1 col] pd.DataFrame with x and y value, respectively
    
    Scalar/Iterables col_labels and ind_labels are used to set the columns and indexes
    of the returned dataframes.
    
    Parameters:
        
        x (scalar; np.ndarray): x variable
        y (scalar; np.ndarray): y variable
        col_labels (scalar or Iterable): defines the column labels
        ind_labels (scalar or Iterable): defines the indexes
        

    Results:
        
        x_df (pd.DataFrame): homogenized x variable
        y_df (pd.DataFrame): homogenized y variable
    """
    
    if is_iterable(x) and is_iterable(y):
        # case 1    
                
        # creating a mesh-grid combining x and y
        x, y = np.meshgrid(x, y)
                
    elif is_iterable(x) and (not is_iterable(y)):
        # case 2
        
        # length of x
        n = len(x)

        # make y look like x
        y = np.repeat(y, repeats=n)

        # reshape x and y to shape (1,n)
        x = x.reshape((1,n))
        y = y.reshape((1,n))
        
    elif (not is_iterable(x)) and is_iterable(y):
        # case 3
        
        # length of y
        m = len(y)

        # make x look like y
        x = np.repeat(x, repeats=m)
        
    else:
        # case 4 
        
        # make x and y length-1 arrays
        x = np.array([x])
        y = np.array([y])
        
    # set labels for columns and indexes
    cols = col_labels if is_iterable_not_string(col_labels) else np.array([col_labels]) 
    inds = ind_labels if is_iterable_not_string(ind_labels) else np.array([ind_labels]) 
        
    x_df = pd.DataFrame(data=x, 
                        index=inds,
                        columns=cols)
    
    y_df = pd.DataFrame(data=y, 
                        index=inds,
                        columns=cols)
    
    return x_df, y_df

#-----------------------------------------------------------------------------#

def simple_output(x, do_simplify=True):
    """
    Utility function to simplify to NumPy array or scalar a variable x
    that is a Pandas DataFrame or Series.
    """
    
    if do_simplify:
        x = x.squeeze()
        return x.values if is_iterable(x) else x
    else:
        return x
       
#-----------------------------------------------------------------------------#

def test_same_type(iterable_obj):
    """
    Utility function to test whether all elements of aniterable_obj are of the 
    same type. If not it raises a TypeError.
    """
    # by set definition, the set of types of the elements in iterable_obj
    # includes all and only the different types of the elements in iterable_obj.
    # If its length is 1, then all the elements of iterable_obj are of the 
    # same data-type
    if len(set([type(x) for x in iterable_obj])) == 1:
        # all element are of the same type: test successfull!
        return True
    else:
        raise TypeError("Iterable '{}' in input has elements of heterogenous types: {}"\
                        .format(iterable_obj, [type(x) for x in iterable_obj]))

#-----------------------------------------------------------------------------#

def test_valid_format(date_string, date_format="%d-%m-%Y"):
    """
    Utility function to test whether:
        
        1-dim case:
            a date_string String is  
            
        Multi-dim case:
            a (non-String) Iterable has elements
        
    conform to the date_format (default: 'dd-mm-YYYY') date format. 
    If not, it raises a ValueError.
    
    If date_string in input is neither an Iterable, nor a String, it raises a TypeError.
    """
    
    try:    
        if isinstance(date_string, str):
            # 1-dim case
            dt.datetime.strptime(date_string, date_format)
        elif is_iterable_not_string(date_string):
            # Multi-dim case
            pd.to_datetime(date_string, format=date_format, errors='raise')
        else:
            # neither an Iterable, nor a String: raise TypeError
            raise TypeError("Type {} of date_string {} not recognized".format(type(date_string), date_string))    
            
    except ValueError:
        # not conform to date_format: raise ValueError
        raise ValueError("date_string {} in input is not conform to 'dd-mm-YYYY' date format".format(date_string))
    else:
        # conform to date_format: test successfull!
        return True
    
#-----------------------------------------------------------------------------#

def datetime_obj_to_date_string(date):
    """
    Utility function to convert: 
        
        1-dim case:
            from dt.datetime object --> to 'dd-mm-YYYY' String
        
        Multi-dim case:
        
            from pd.DatetimeIndex --> to pd.Index of 'dd-mm-YYYY' String
            from Iterable --> to List of 'dd-mm-YYYY' String
    """
    
    if isinstance(date, dt.datetime) or isinstance(date, pd.DatetimeIndex):
        # .strftime() is a polymorphic method, implemented by both 
        # datetime objects of datetime (1-dim) and DatetimeIndex (Multi-dim) objects of Pandas 
        # so there is no need to differentiate between the two case when calling it
        return date.strftime("%d-%m-%Y")
    elif is_iterable_not_string(date):
        # all other kind of iterables (Lists, np.ndarray, etc..) are mapped to Lists
        return [d.strftime("%d-%m-%Y") for d in date]
    else:
        return date

#-----------------------------------------------------------------------------#

def date_string_to_datetime_obj(date_string):
    """
    Utility function to convert: 
        
        1-dim case:
            from String object conform to 'dd-mm-YYYY' date foramt --> to dt.datetime.
        
        Multi-dim case:
            from (non-String) Iterable objects of elements conform to 'dd-mm-YYYY' date format --> to pd.DatetimeIndex
            
    The 'dd-mm-YYYY' date format is controlled throught test_valid_format() utility function.
    """
    
    if isinstance(date_string, str) and test_valid_format(date_string):
        # 1-dim case
        return dt.datetime.strptime(date_string, "%d-%m-%Y")
    elif is_iterable_not_string(date_string) and test_valid_format(date_string):
        # Multi-dim case
        return pd.DatetimeIndex(date_string)     
    else: 
        return date_string
                                                         
#-----------------------------------------------------------------------------#

def is_iterable(x):
    """
    Utility function to check if input can be iterated over (that is, if input is a List, np.array, pd.date_range, etc.).
    """    
    return isinstance(x, Iterable)

#-----------------------------------------------------------------------------#

def is_iterable_not_string(x):
    """
    Utility function to check if input can be iterated over (that is, if input is a List, np.array, pd.date_range, etc.)
    but it is not a String
    """
    return is_iterable(x) and not isinstance(x, str)

#-----------------------------------------------------------------------------#

def is_numeric(x):
    """
    Utility function to check if input is/contains numeric data.
    """
    
    if is_iterable_not_string(x) and test_same_type(x):
        # since all elements are of the same type, 
        # it's enought to check the first element
        return isinstance(x[0], float) or isinstance(x[0], int)
    else:
        return isinstance(x, float) or isinstance(x, int)
    
#-----------------------------------------------------------------------------#

def is_date(x):
    """
    Utility function to check if input is/contains date-like data.
    The error due to invalid (non 'dd-mm-YYYY') date Strings is controlled thanks to test_valid_format() function.
    """
    
    if is_iterable_not_string(x) and test_same_type(x):
        # since all elements are of the same type, 
        # it's enought to check the first element
        return isinstance(x[0], dt.datetime) or (isinstance(x[0], str) and test_valid_format(x[0]))
    else:
        return isinstance(x, dt.datetime) or (isinstance(x, str) and test_valid_format(x))

#-----------------------------------------------------------------------------#

def plot_compare(x, f, f_ref, **kwargs):
    """
    Plotting function to compare a function f(x) with another reference function
    f_ref(x). It makes 6 plots:
        
        [Top-Left]     f(x) Vs x    
        [Top-Right]    f_ref(x) Vs x
        [Mid-Left]     f(x) - f_ref(x) Vs x
        [Mid-Right]    (f(x) - f_ref(x)) / f_ref(x) Vs x
        [Bottom-Left]  |f(x) - f_ref(x)| Vs x
        [Bottom-Right] |(f(x) - f_ref(x)) / f_ref(x)| Vs x
    """
   
    # parsing optional parameters
    f_label = kwargs['f_label'] if 'f_label' in kwargs else "f"
    f_ref_label = kwargs['f_ref_label'] if 'f_ref_label' in kwargs else "f_ref"
    title = kwargs['title'] if 'title' in kwargs else "f Vs f_ref comparison"    
    
    # define the figure
    fig, axs = plt.subplots(figsize=(15, 8), nrows=3, ncols=2)
    
    # [Top-Left] f(x) Vs x
    axs[0,0].plot(x, f, 'b-', lw=1.5)
    axs[0,0].set_ylabel(r"$" + f_label + r"$", fontsize=12)
    axs[0,0].set_xlabel(r"$x$", fontsize=12) 
    axs[0,0].set_title("Test function", fontsize=12)
    axs[0,0].grid(True)

    # [Top-Right] f_ref(x) Vs x
    axs[0,1].plot(x, f_ref, 'b-', lw=1.5)
    axs[0,1].set_ylabel(r"$" + f_ref_label + r"$", fontsize=12)
    axs[0,1].set_xlabel(r"$x$", fontsize=12) 
    axs[0,1].set_title("Reference function", fontsize=12)
    axs[0,1].grid(True)

    # [Mid-Left] f(x) - f_ref(x) Vs x
    axs[1,0].plot(x, f-f_ref, 'r-')
    axs[1,0].plot(x, np.zeros(len(x)), 'k--', lw=0.5)
    axs[1,0].set_ylabel(r"$" + f_label + r" - " + f_ref_label + r"$", fontsize=12)
    axs[1,0].set_xlabel(r"$x$", fontsize=12) 
    axs[1,0].set_title("Differences", fontsize=12)
    axs[1,0].grid(True)
    
    # [Mid-Right] (f(x) - f_ref(x)) / f_ref(x) Vs x
    axs[1,1].plot(x, (f-f_ref)/f_ref, 'r-', lw=1.5)
    axs[1,1].plot(x, np.zeros(len(x)), 'k--', lw=0.5)
    axs[1,1].set_ylabel(r"$ \frac{" + f_label + r" - " + f_ref_label + r"}{" + f_ref_label + r"}$", fontsize=12)
    axs[1,1].set_xlabel(r"$x$", fontsize=12) 
    axs[1,1].set_title("Relative Differences", fontsize=12)
    axs[1,1].grid(True)

    # [Bottom-Left] |f(x) - f_ref(x)| Vs x
    axs[2,0].plot(x, np.abs(f-f_ref), 'r-')
    axs[2,0].plot(x, np.zeros(len(x)), 'k--', lw=0.5)
    axs[2,0].set_ylabel(r"$|" + f_label + r" - " + f_ref_label + r"|$", fontsize=12)
    axs[2,0].set_xlabel(r"$x$", fontsize=12) 
    axs[2,0].set_title("Differences (absolute value)", fontsize=12)
    axs[2,0].grid(True)
    
    # [Bottom-Right] |(f(x) - f_ref(x)) / f_ref(x)| Vs x
    axs[2,1].plot(x, np.abs((f-f_ref)/f_ref), 'r-', lw=1.5)
    axs[2,1].plot(x, np.zeros(len(x)), 'k--', lw=0.5)
    axs[2,1].set_ylabel(r"$ \left| \frac{" + f_label + r" - " + f_ref_label + r"}{" + f_ref_label + r"} \right|$", fontsize=12)
    axs[2,1].set_xlabel(r"$x$", fontsize=12) 
    axs[2,1].set_title("Relative Differences (absolute value)", fontsize=12)
    axs[2,1].grid(True)

    # make the main title
    fig.suptitle(title, fontsize=15) 
    
    # show the plot
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    plt.show()
    
#-----------------------------------------------------------------------------#

def plot(x, f, **kwargs):
    """
    Basic plotting function a bit customized
    """
   
    # parsing optional parameters
    x_label = kwargs['x_label'] if 'x_label' in kwargs else r"$x$"
    f_label = kwargs['f_label'] if 'f_label' in kwargs else "f"
    title = kwargs['title'] if 'title' in kwargs else "f(x) Vs x"
    f_up = kwargs['f_up'] if 'f_up' in kwargs else None
    f_up_label = kwargs['f_up_label'] if 'f_up_label' in kwargs else 'f_up_label'
    f_down = kwargs['f_down'] if 'f_down' in kwargs else None
    f_down_label = kwargs['f_down_label'] if 'f_down_label' in kwargs else 'f_down_label'
    
    # define the figure
    fig, ax = plt.subplots(figsize=(10,6))
    
    # f(x) Vs x
    ax.plot(x, f, 'b-', lw=1.5)
    ax.set_ylabel(f_label, fontsize=12)
    ax.set_xlabel(x_label, fontsize=12) 
    ax.set_title(title, fontsize=15)
    ax.grid(True)
    
    if f_up is not None:
        ax.plot(x, f_up, 'r--', lw=0.5, label=f_up_label)
    
    if f_down is not None:
        ax.plot(x, f_down, 'g--', lw=0.5, label=f_down_label)

    # add legend
    if (f_up is not None) or (f_down is not None):
        ax.legend(loc='best', ncol=1)

    # show the plot
    fig.tight_layout()
    plt.show()
