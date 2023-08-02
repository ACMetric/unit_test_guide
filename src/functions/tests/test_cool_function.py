from functions.cool_function import check_if_fun_number
import pytest
from custom_errors import NegativeNumberException


def test_number_equal_to_one()-> None:
    """Checks if 1 is a fun number
    """    
    
    #Arrange
    input_value = 1
    
    #Act
    result = check_if_fun_number(input_value)
    
    #Assert
    expected_result = True
    assert result == expected_result
    
def test_number_equal_to_two()-> None:
    """Checks if 2 is not a fun number
    """   
     
    #Arrange
    input_value = 2
    
    #Act
    result = check_if_fun_number(input_value)
    
    #Assert
    expected_result = False
    assert result == expected_result
    
def test_invalid_number()-> None:
    """Test should trow error since invalid number
    """    
    
    #Arrange
    input_value = -2
    
    #Act and Assert
    with pytest.raises(NegativeNumberException):
        result = check_if_fun_number(input_value)