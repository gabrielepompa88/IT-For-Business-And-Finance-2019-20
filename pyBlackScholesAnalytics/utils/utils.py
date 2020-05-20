"""
Author: Gabriele Pompa (gabriele.pompa@gmail.com)

Date: 20-May-2020
File name: utils.py
"""

# ----------------------- standard imports ---------------------------------- #
# for date management
import datetime as dt

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
