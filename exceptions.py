from .better_ac import *

class ACCarStateError(Exception):
    """Exception raised for errors in the ACCarState class."""

def raise_car_state_error(func):
    """
    Raise an ACCarStateError with the given message if a method returns -1.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == -1:
            raise ACCarStateError("Something went wrong when trying to call {}".format(func.__name__))
        return result
    return wrapper
