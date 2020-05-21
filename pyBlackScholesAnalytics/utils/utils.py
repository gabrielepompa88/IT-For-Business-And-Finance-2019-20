"""
Author: Gabriele Pompa (gabriele.pompa@gmail.com)

Date: 20-May-2020
File name: utils.py
"""

# ----------------------- standard imports ---------------------------------- #
# for NumPy arrays
import numpy as np

# for date management
import datetime as dt

# for Matplotlib plotting
import matplotlib.pyplot as plt

# to identify iterable data-structures
from collections.abc import Iterable

#-----------------------------------------------------------------------------#

def datetime_obj_to_date_string(date):
    """
    Utility function to convert: from dt.datetime object --> to 'dd-mm-YYYY' String
    """
    return date.strftime("%d-%m-%Y") if isinstance(date, dt.datetime) else date

#-----------------------------------------------------------------------------#

def test_valid_format(date_string, date_format="%d-%m-%Y"):
    """
    Utility function to test whether a date_string String in input is conform to date_format (default: 'dd-mm-YYYY') date format.
    If not raises an error.
    """
    try:
        dt.datetime.strptime(date_string, date_format)
    except ValueError:
        print("String '{}' in input is not conform to 'dd-mm-YYYY' date format".format(date_string))
        raise
    else:
        return True
    
#-----------------------------------------------------------------------------#

def date_string_to_datetime_obj(date_string):
    """
    Utility function to convert: from 'dd-mm-YYYY' String object --> to dt.datetime.
    ValueError, due to wrong date format of the input String, is controlled.
    """
    
    return dt.datetime.strptime(date_string, "%d-%m-%Y") if (isinstance(date_string, str) and test_valid_format(date_string)) \
                                                         else date_string
                                                         
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
    
    if is_iterable_not_string(x):
        return isinstance(x[0], float) or isinstance(x[0], int)
    else:
        return isinstance(x, float) or isinstance(x, int)
    
#-----------------------------------------------------------------------------#

def is_date(x):
    """
    Utility function to check if input is/contains date-like data.
    The error due to invalid (non 'dd-mm-YYYY') date Strings is controlled thanks to test_valid_format() function.
    """
    
    if is_iterable_not_string(x):
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
