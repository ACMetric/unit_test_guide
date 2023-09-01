from functions.cool_function import check_if_fun_number, check_numbers_in_csv
import pytest
from pytest import MonkeyPatch
from custom_errors import NegativeNumberException
from fib_number_generator import FibNumberGenerator
import functions.cool_function 
from pandas import DataFrame


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
        
    def test_invalid_number(self)-> None:
        """Test should trow error since invalid number
        """    
        
        #Arrange
        input_value = -2
        
        #Act and Assert
        with pytest.raises(NegativeNumberException):
            result = check_if_fun_number(input_value)
        
    @pytest.mark.parametrize("input_value, expected_result", [(1, True), (2, False), (42, False)])
    def test_parametrized_numbers(self, input_value, expected_result)-> None:
        """Use parametrization to check multiple inputs and outputs in the same test
        """   
        
        #Act
        result = check_if_fun_number(input_value)
        
        #Assert
        assert result == expected_result  
     
    @pytest.fixture
    def fifth_fib_number(self)-> FibNumberGenerator:
        """Returns the fibonacci number generator on its 5th number,
        resets afterwards

        Yields:
            FibNumberGenerator: Teh number generator 
        """        
        number_generator = FibNumberGenerator()
        number_generator.get_next_number()
        number_generator.get_next_number()
        number_generator.get_next_number()
        number_generator.get_next_number()
        
        yield number_generator
        
        number_generator.current = 0
        
        
    def test_fifth_fib_number(self, fifth_fib_number:FibNumberGenerator)-> None:
        """Test the 5th fibonacci number using a fixture
        """   
        
        #Act
        result = check_if_fun_number(fifth_fib_number.current)
        
        #Assert
        expected_result = True
        assert result == expected_result
        
    def test_sixth_fib_number(self, fifth_fib_number: FibNumberGenerator)-> None:
        """Test the 6th fibonacci number using a fixture
        """   
        #Arrange
        fifth_fib_number.get_next_number()
        
        #Act
        result = check_if_fun_number(fifth_fib_number.current)
        
        #Assert
        expected_result = False
        assert result == expected_result
        
        
class TestCheckMultipleNumbers():
    def mock_dataframe(self) -> DataFrame:
        """Return a fake df
        """        
        data = {'Numbers': [1, 2, 3, 4, 5]}
        return DataFrame(data)
    
    
    def test_multiple_numbers_from_csv(self,  monkeypatch: MonkeyPatch) -> None:
        """Checks if numbers in the number.csv are fun, but we mock the result of the read_csv function.
        """    
        
        #Arrange
        #We mock read_csv from functions.cool_function, NOT from pandas
        monkeypatch.setattr(functions.cool_function , "read_csv", lambda _: self.mock_dataframe())
        fake_path = "home/acmetric/number.csv"
        
        #Act
        result = check_numbers_in_csv(fake_path)
        
        #Assert
        expected_result = [True, False, True, False, True]
        assert result == expected_result
        
        
        
    def create_mock_dataframe(self)-> DataFrame:
        """Returns a fake df and keeps track with what inputs the function was called"""
        def mock_dataframe(path):
            # Store the path for later validation
            mock_dataframe.called_with_path = path
            data = {'Numbers': [1, 2, 3, 4, 5]}
            return DataFrame(data)

        # Setting default attribute for called_with_path
        mock_dataframe.called_with_path = None
        return mock_dataframe
    
    
    def test_multiple_numbers_from_csv(self,  monkeypatch: MonkeyPatch) -> None:
        """Checks if numbers in the number.csv are fun, but we mock the result of the read_csv function
        And we also keep track with which input the read_csv was called
        """    
        
        #Arrange
        fake_path = "home/acmetric/number.csv"
        mock_df = self.create_mock_dataframe()
        
        monkeypatch.setattr(functions.cool_function, "read_csv", mock_df)
        
        #Act
        result = check_numbers_in_csv(fake_path)
        
        #Assert
        expected_result = [True, False, True, False, True]
        assert result == expected_result
        assert mock_df.called_with_path == fake_path
        
    

        
   