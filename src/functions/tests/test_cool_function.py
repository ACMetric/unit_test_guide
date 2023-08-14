from functions.cool_function import check_if_fun_number
import pytest
from custom_errors import NegativeNumberException

class TestCheckIfFunNumber():
    def test_number_equal_to_one(self)-> None:
        """Checks if 1 is a fun number
        """    
        
        #Arrange
        input_value = 1
        
        #Act
        result = check_if_fun_number(input_value)
        
        #Assert
        expected_result = True
        assert result == expected_result
        
    def test_number_equal_to_two(self)-> None:
        """Checks if 2 is not a fun number
        """   
        
        #Arrange
        input_value = 2
        
        #Act
        result = check_if_fun_number(input_value)
        
        #Assert
        expected_result = False
        assert result == expected_result
        
    @pytest.mark.parametrize("input_value, expected_result", [(1, True), (2, False), (42, False)])
    def test_parametrized_numbers(self, input_value, expected_result)-> None:
        """Use parametrization to check multiple inputs and outputs in the same test
        """   
        
        #Act
        result = check_if_fun_number(input_value)
        
        #Assert
        assert result == expected_result
        
    def test_invalid_number(self)-> None:
        """Test should trow error since invalid number
        """    
        
        #Arrange
        input_value = -2
        
        #Act and Assert
        with pytest.raises(NegativeNumberException):
            result = check_if_fun_number(input_value)
            
class TestCheckMultipleNumbers():
    def test_five_numbers(self) -> None:
        print()
        
    def test_empty_input(self) -> None:
        print()