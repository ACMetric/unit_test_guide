from functions import cool_function
from pytest import MonkeyPatch
from main import run_main

def test_if_fun(monkeypatch: MonkeyPatch)-> None:
    #Arrange
    input_number = 1
    
    #Use monkeypatch to mock functions.
    monkeypatch.setattr(cool_function, "check_if_fun_number", lambda _: True)
    
    #Act
    result = run_main(input_number)
    
    #Assert
    expected_result = f"{input_number} is a fun number!"
    assert result == expected_result
    
def test_if_not_fun(monkeypatch: MonkeyPatch)-> None:
    #Arrange
    input_number = 2
    
    #Use monkeypatch to mock functions.
    monkeypatch.setattr(cool_function, "check_if_fun_number", lambda _: False)
    
    #Act
    result = run_main(input_number)
    
    #Assert
    expected_result = f"{input_number} is not a fun number :("
    assert result == expected_result