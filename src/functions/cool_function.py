from custom_errors import NegativeNumberException
from numpy import sin
from fib_number_generator import FibNumberGenerator
from pathlib import Path
from pandas import DataFrame, read_csv

def check_if_fun_number(number: int)-> bool:
    """Checks if the given number is fun, returns true if number is fun

    Args:
        number (int): input number

    Returns:
        (bool): True if it is a fun number
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


def check_numbers_in_csv(path: Path) -> list[bool]:
    """Loop over a selection of numbers to check if fun

    Args:
        path (Path): The path to the numbers csv

    Returns:
        list[bool]: results of funness of numbers
    """    
    results = []
    df = read_csv(path=path)
    for number in df["Numbers"]:
        result = check_if_fun_number(number)
        results.append(result)
        
    return results
    


