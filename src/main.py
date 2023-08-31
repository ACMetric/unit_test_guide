#from functions import cool_function
from functions.cool_function import check_if_fun_number

def run_main(num: int)-> str:
    """Returns a message depending on if the given number is fun

    Args:
        num (int): Number that will be tested for funness

    Returns:
        str: Return message about the number
    """    
    is_fun = check_if_fun_number(num)
    if is_fun:
        return f"{num} is a fun number!"
    else:
        return f"{num} is not a fun number :("


if __name__ == "__main__":
    run_main(2)