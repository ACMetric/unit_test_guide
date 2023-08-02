from custom_errors import NegativeNumberException
from numpy import sin


def check_if_fun_number(num: int)-> bool:
    """Checks if the given number is fun, returns true if number is fun

    Args:
        num (int): input number

    Returns:
        (bool, str): Result if it is a fun number, with explanation
    """    
    #Show that exception can also be tested
    if num< 0:
        raise NegativeNumberException(num)
    
    if (num % 2) == 0:
        return False
    
    #Add case we will not test to show code coverage
    if num == 17:
        return False
    
    return True

