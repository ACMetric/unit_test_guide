from pytest import MonkeyPatch
import main
#NOT import functions.cool_function !!

class TestMain():
    def test_if_fun(self, monkeypatch: MonkeyPatch)-> None:
        #Arrange
        input_number = 1
        
        #Use monkeypatch to mock functions.
        monkeypatch.setattr(main, "check_if_fun_number", lambda _: True)
        
        #Act
        result = main.run_main(input_number)

        #Assert
        expected_result = f"{input_number} is a fun number!"
        assert result == expected_result
        
        
    def test_if_not_fun(self, monkeypatch: MonkeyPatch)-> None:
        #Arrange
        input_number = 2
        
        #Use monkeypatch to mock functions.
        monkeypatch.setattr(main, "check_if_fun_number", lambda _: False)
        
        #Act
        result = main.run_main(input_number)
        
        #Assert
        expected_result = f"{input_number} is not a fun number :("
        assert result == expected_result