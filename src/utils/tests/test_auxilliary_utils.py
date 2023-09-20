import pytest
import utils.auxiliary_utils
from utils.auxiliary_utils import eq_zeros, get_critical_value


class TestEqZeroes:
    @pytest.mark.parametrize(
        "input_value, expected_result",
        [((1, 0.05), 8.415), ((2, 0.05), 2.379), ((3, 0.05), 0.226)],
    )
    def test_parametrized_for_5perc(self, input_value, expected_result) -> None:
        """Test that correct critical value for a given probability and x-value are retrieved"""

        # Act
        result = eq_zeros(input_value[0], input_value[1])

        # Assert
        assert round(result, 3) == expected_result


class TestGetCriticalValue:
    class FakeMinimizationResult:
        """Class used to mimic the result you would get from the minimization result"""
        def __init__(self, x, fun):
            self.x = x
            self.fun = fun

    def create_mock_minimization_result(
        self, return_value: float, function_value: float
    ):
        """Returns a fake minimization result and and keeps track with what inputs the function was called
        
        Args:
            return_value (float): the x attribure in the FakeMinimizationResult
            function_value (float): the fun attribute in the FakeMinimizationResult

        Returns:
            FakeMinimizationResult: Object used to mimic the result object of the minimization problem.
        """  

        def mock_minimization_result(opt_function, x0, method):
            # Make sure the attribute names are identical to the real attribute names of the minimization result, oterwise you get errors
            mock_minimization_result.called_with_function = opt_function
            mock_minimization_result.x0 = x0
            mock_minimization_result.method = method

            return self.FakeMinimizationResult(x=[return_value], fun=function_value)

        #Default is None
        mock_minimization_result.called_with_function = None
        mock_minimization_result.x0 = None
        mock_minimization_result.method = None
        return mock_minimization_result

    def test_below_minimization_tolerance(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test when you're optimization result is below the minimization tolerance
        """        
        # Arrange
        input_prob = 0.05
        #mock_func_value corresponds to the found minimization result (the .fun attribute)
        mock_func_value = 1e-8
        mock_return_value = 5
        mock_minimization_result = self.create_mock_minimization_result(
            return_value=mock_return_value, function_value=mock_func_value
        )

        monkeypatch.setattr(utils.auxiliary_utils, "minimize", mock_minimization_result)

        # Act
        result = get_critical_value(input_prob)

        # Assert
        assert result == mock_return_value
        assert mock_minimization_result.method == "BFGS"
        assert mock_minimization_result.x0 == 1
        #Unsure how to assert if it is called with the correct lambda function, so just check if it was called with a lambda function
        assert mock_minimization_result.called_with_function.__name__ == "<lambda>"


    def test_above_minimization_tolerance(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test if correctly throws error when you're above the minimization tolerance
        """   
        # Arrange
        input_prob = 0.05
        #mock_func_value corresponds to the found minimization result (the .fun attribute)
        mock_func_value = 1e-6
        mock_return_value = 5
        mock_minimization_result = self.create_mock_minimization_result(
            return_value=mock_return_value, function_value=mock_func_value
        )

        monkeypatch.setattr(utils.auxiliary_utils, "minimize", mock_minimization_result)

        #Act and Assert
        with pytest.raises(AssertionError):
            result = get_critical_value(input_prob)
