from custom_errors import NegativeNumberException
from numpy import sin


def check_if_fun_number(number: int)-> bool:
    """Checks if the given number is fun, returns true if number is fun

    Args:
        number (int): input number

    Returns:
        (bool, str): Result if it is a fun number, with explanation
    """    
    #Show that exception can also be tested
    if number< 0:
        raise NegativeNumberException(number)
    
    if (number % 2) == 0:
        return False
    
    #Add case we will not test to show code coverage
    if number == 17:
        return False
    
    return True


def check_multiple_numbers(numbers: list[int]) -> list[bool]:
    """Loop over a selection of numbers to check if fun

    Args:
        numbers (list[int]): Numbers to check

    Returns:
        list[bool]: results of funness of numbers
    """    
    results = []
    for index, number in enumerate(numbers):
        result = check_if_fun_number(number)
        results.append(result)
        
    return results
    
